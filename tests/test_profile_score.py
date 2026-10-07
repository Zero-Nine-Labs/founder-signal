import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'skills/linkedin-profile-audit/scripts/score_profile.py'
IDS = [f'{prefix}{i}' for prefix, count in [('H', 5), ('A', 5), ('F', 4), ('B', 3), ('E', 2), ('P', 1)] for i in range(1, count + 1)]


class ProfileScoreTest(unittest.TestCase):
    def calculate(self, statuses):
        result = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(statuses), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_observed_arithmetic_errors(self):
        statuses = dict.fromkeys(IDS, 'unassessed')
        statuses.update(dict.fromkeys(['H1', 'H2', 'H4', 'H5', 'A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B3'], 'pass'))
        statuses['H3'] = 'partial'
        result = self.calculate(statuses)
        self.assertEqual((result['earned'], result['upper'], result['coverage'], result['grade']), (57.5, 97.5, 60, None))
        statuses['H5'] = statuses['A2'] = 'partial'
        statuses['B1'] = statuses['B3'] = 'unassessed'
        result = self.calculate(statuses)
        self.assertEqual((result['earned'], result['upper'], result['coverage']), (42.5, 92.5, 50))
        self.assertEqual(sum(section['earned'] for section in result['sections']), result['earned'])
        self.assertEqual(sum(section['maximum'] for section in result['sections']), 100)

    def test_complete_grade_boundary_and_unknowns(self):
        statuses = dict.fromkeys(IDS, 'pass')
        statuses.update(dict.fromkeys(['H3', 'A2', 'F3'], 'partial'))
        statuses['B3'] = 'fail'
        result = self.calculate(statuses)
        self.assertEqual((result['earned'], result['coverage'], result['grade']), (87.5, 100, 'B'))
        statuses['B3'] = 'partial'
        result = self.calculate(statuses)
        self.assertEqual((result['earned'], result['grade']), (90, 'A'))
        result = self.calculate(dict.fromkeys(IDS, 'unassessed'))
        self.assertEqual((result['earned'], result['upper'], result['coverage'], result['grade']), (0, 100, 0, None))

    def test_generates_the_score_block_from_current_statuses(self):
        statuses = dict.fromkeys(IDS, 'unassessed')
        statuses.update(dict.fromkeys(['H1', 'H2', 'H4', 'A1', 'A3', 'A4', 'A5'], 'pass'))
        statuses.update(dict.fromkeys(['H3', 'H5', 'A2'], 'partial'))
        result = subprocess.run([sys.executable, str(SCRIPT), '--markdown', '--goal', 'Attract client enquiries'], input=json.dumps(statuses), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('42.5 to 92.5/100', result.stdout)
        self.assertIn('Coverage: 50%', result.stdout)
        self.assertIn('| Total | 42.5 | 100 | 50 |', result.stdout)
        self.assertIn('<!-- profile-score:start -->', result.stdout)
        self.assertNotIn('97.5', result.stdout)

    def test_markdown_requires_a_goal_and_handles_no_evidence(self):
        statuses = dict.fromkeys(IDS, 'unassessed')
        missing = subprocess.run([sys.executable, str(SCRIPT), '--markdown'], input=json.dumps(statuses), text=True, capture_output=True)
        self.assertNotEqual(missing.returncode, 0)
        rendered = subprocess.run([sys.executable, str(SCRIPT), '--markdown', '--goal', 'Recruit engineers'], input=json.dumps(statuses), text=True, capture_output=True)
        self.assertEqual(rendered.returncode, 0, rendered.stderr)
        self.assertIn('Assessment unavailable', rendered.stdout)
        self.assertNotIn('0 to 100', rendered.stdout)

    def test_verifies_the_delivered_score_block_and_rejects_drift(self):
        statuses = dict.fromkeys(IDS, 'pass')
        rendered = subprocess.run([sys.executable, str(SCRIPT), '--markdown', '--goal', 'Client enquiries'], input=json.dumps(statuses), text=True, capture_output=True, check=True).stdout
        with tempfile.TemporaryDirectory() as folder:
            report = Path(folder) / 'audit.md'
            variants = [('Founder context\n\n' + rendered + '\nEvidence notes.', statuses, True), (rendered.replace('Grade: A', 'Grade: B'), statuses, False), (rendered + rendered, statuses, False), (rendered, {**statuses, 'H1': 'fail'}, False), ('No score block', statuses, False)]
            for content, inputs, valid in variants:
                with self.subTest(content=content, inputs=inputs):
                    report.write_text(content)
                    result = subprocess.run([sys.executable, str(SCRIPT), '--verify-report', str(report), '--goal', 'Client enquiries'], input=json.dumps(inputs), text=True, capture_output=True)
                    self.assertEqual(result.returncode == 0, valid, result.stderr)

    def test_rejects_missing_extra_or_invalid_statuses(self):
        valid = dict.fromkeys(IDS, 'pass')
        invalid = [{key: value for key, value in valid.items() if key != 'H1'}, {**valid, 'H6': 'pass'}, {**valid, 'H1': 'almost'}, []]
        for statuses in invalid:
            with self.subTest(statuses=statuses):
                result = subprocess.run([sys.executable, str(SCRIPT)], input=json.dumps(statuses), text=True, capture_output=True)
                self.assertNotEqual(result.returncode, 0)


if __name__ == '__main__':
    unittest.main()
