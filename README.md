# LinkedIn founder skills

Four reusable skills for founders who want a clearer LinkedIn profile and useful content. Each works independently with the founder's own audience, goal, evidence and voice.

| Skill | Use it for | Output |
|---|---|---|
| [Profile audit](skills/linkedin-profile-audit/SKILL.md) | Reviewing a profile or checking completed edits | Weighted readiness score, prioritised fixes, headline, About, banner and Experience drafts |
| [Content planner](skills/linkedin-content-planner/SKILL.md) | Planning a week or another requested period | Calendar and supported briefs, filtered by topic, pillar, funnel stage or source section |
| [Post creator](skills/linkedin-post-creator/SKILL.md) | Creating one post within a selected section | Ideas, CPIO summary, content and a caption suited to the format |
| [Post writer](skills/linkedin-post-writer/SKILL.md) | Drafting from a brief or revising existing copy | Complete post copy edited for factual support and the founder's voice |

CPIO means Convey, Package, Information and Order. These skills cover profile review, planning and writing inspired by a 90-day founder guide. They do not run a complete 90-day programme or publish posts.

## Install

Download or clone this repository. Copy each selected folder under `skills/` into your AI platform's skill directory, preserving its `references/`, `scripts/` and metadata. Install only the skills you need. Check for an existing folder with the same name before copying, and back it up before replacing it.

For current Codex installations, use `~/.agents/skills/` for personal skills or `.agents/skills/` inside a project for project-scoped skills. These locations and symlink support are documented in [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills). Existing installations may use different configured locations. Other platforms have their own installation and invocation conventions.

The skills do not install browser tools or require a particular provider. A live profile audit needs the platform's approved computer-use tools and access to the target profile. Supplied text, screenshots or an export can support a partial audit when browser access is unavailable.

Numeric scoring needs Python 3 or a verified executable equivalent. The bundled Python helper uses only the standard library. Without a calculator, the audit returns qualitative findings and marks the numeric score unavailable.

## Use

In Codex, invoke the selected skill by name. Replace the example context with the founder's own facts.

```text
Use $linkedin-profile-audit to audit this profile: [URL].
Goal: attract clients. Audience: small accounting firms.
Offer: invoice administration workflows. Use only the proof I supply.

Use $linkedin-content-planner to plan next week around reducing
repetitive admin, with three consideration posts.

Use $linkedin-post-creator to create one carousel about invoice
handoffs, using the notes below. Include slide copy and a caption.

Use $linkedin-post-writer to revise this draft for my supplied voice.
Preserve its facts, meaning and consideration-stage purpose.
```

The audit asks and stops when the profile goal is missing. The creator asks and stops when no specific section has been selected. Both reuse information already supplied. Essential missing proof stays pending rather than becoming invented content.

Keep private client details out of public copy unless publication is permitted. Audits, plans and drafts do not authorise LinkedIn edits, publishing, messages or scheduling.

## Check the bundle

From the repository root:

```sh
python3 -B -m unittest discover -s tests
```

The six automated tests cover score arithmetic, grade boundaries, unknown evidence, invalid inputs, generated reports, goal requirements and report drift. They need no packages, credentials or private test files. GitHub Actions runs the same command on pushes and pull requests.

The [stress-test procedure](stress-tests/README.md) covers behavioural and browser checks. Raw founder evidence and dated agent runs remain local and are ignored by Git. Never force-add them without reviewing their contents.

Earlier fresh-context tests verified the missing-goal stop and final numeric report blocks three times each. One About judgement still varied by 2.5 points. Arithmetic verification cannot establish whether a qualitative judgement is fair. A narrow browser check covers mobile web, not a mobile app or physical device. These are recorded limitations, not new verification of a changed profile.

## Sources and licence

The planning and CPIO references adapt [How To Build A LinkedIn Presence As A Founder (90-days)](https://docs.google.com/document/d/1FWY73HV-ZpTUOVDEAKv1LxwtGQC55tN93akZBL6_I0A/edit). [FAT Agent](https://github.com/spruikco/fat-agent-skill) informed the scoring and re-audit approach. The readiness rubric and Python calculator are custom to this bundle, not measured LinkedIn ranking factors. Detailed source notes are in the relevant references.

The creator and writer include writing rules supplied by the user. Their upstream provenance and the guide's redistribution permissions have not been established. A repository licence has not been selected. Resolve those source questions before assigning a public redistribution licence.
