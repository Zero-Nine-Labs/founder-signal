"""Calculate rubric 1.0 scores from a JSON map of all 20 criterion statuses."""
import argparse
import json
from pathlib import Path
import sys


SECTIONS = {'Headline': ('H', 5), 'About': ('A', 5), 'Featured': ('F', 4), 'Banner': ('B', 3), 'Experience': ('E', 2), 'Photo': ('P', 1)}
POINTS = {'pass': 5, 'partial': 2.5, 'fail': 0, 'unassessed': None}
IDS = [f'{prefix}{i}' for prefix, count in SECTIONS.values() for i in range(1, count + 1)]


def score(statuses):
    if not isinstance(statuses, dict) or set(statuses) != set(IDS):
        raise ValueError('Provide exactly the 20 criterion IDs H1-H5, A1-A5, F1-F4, B1-B3, E1-E2 and P1.')
    if any(not isinstance(value, str) or value not in POINTS for value in statuses.values()):
        raise ValueError('Statuses must be pass, partial, fail or unassessed.')
    awards = {key: POINTS[value] for key, value in statuses.items()}
    sections = []
    for name, (prefix, count) in SECTIONS.items():
        values = [awards[f'{prefix}{i}'] for i in range(1, count + 1)]
        sections.append({'section': name, 'earned': sum(value for value in values if value is not None), 'maximum': count * 5, 'unassessed': values.count(None) * 5})
    earned = sum(section['earned'] for section in sections)
    unknown = sum(section['unassessed'] for section in sections)
    grade = None if unknown else next(label for threshold, label in [(90, 'A'), (80, 'B'), (70, 'C'), (60, 'D'), (0, 'F')] if earned >= threshold)
    return {'awards': awards, 'sections': sections, 'earned': earned, 'maximum': 100, 'unassessed': unknown, 'upper': earned + unknown, 'coverage': 100 - unknown, 'grade': grade}


def render(result):
    if not result['coverage']:
        summary = '**Assessment unavailable.** No criteria have been assessed.'
    elif result['unassessed']:
        summary = f"**Provisional score: {result['earned']:g} to {result['upper']:g}/100. Coverage: {result['coverage']:g}%. No grade.**"
    else:
        summary = f"**Score: {result['earned']:g}/100. Coverage: 100%. Grade: {result['grade']}.**"
    lines = ['<!-- profile-score:start -->', '## Profile Readiness Score', '', summary, '', '| Section | Earned | Maximum | Unassessed |', '|---|---:|---:|---:|']
    for section in result['sections']:
        lines.append(f"| {section['section']} | {section['earned']:g} | {section['maximum']:g} | {section['unassessed']:g} |")
    lines.extend([f"| Total | {result['earned']:g} | 100 | {result['unassessed']:g} |", '<!-- profile-score:end -->'])
    return '\n'.join(lines)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    output = parser.add_mutually_exclusive_group()
    output.add_argument('--markdown', action='store_true', help='Generate the score summary and table.')
    output.add_argument('--verify-report', type=Path, help='Check a saved report against its criterion statuses.')
    parser.add_argument('--goal', help='The founder goal already supplied by the user.')
    args = parser.parse_args()
    try:
        if (args.markdown or args.verify_report) and not (args.goal and args.goal.strip()):
            raise ValueError('A supplied profile goal is required before generating an audit score block.')
        result = score(json.load(sys.stdin))
        if args.verify_report:
            report = args.verify_report.read_text(encoding='utf-8')
            if report.count('<!-- profile-score:start -->') != 1 or report.count('<!-- profile-score:end -->') != 1 or render(result) not in report:
                raise ValueError('Report score block is missing, duplicated or differs from the supplied criterion statuses. Regenerate it.')
            print('Verified: report score block matches the supplied criterion statuses.')
        else:
            print(render(result) if args.markdown else json.dumps(result, indent=2))
    except (ValueError, TypeError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
