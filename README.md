# Founder Signal

Reusable AI skills for founders building a LinkedIn presence through a clear profile and useful content.

Founder Signal turns your audience, goals, notes and experience into profile improvements, content plans and post drafts. Use the four skills independently or together. Each founder's facts, proof and voice stay separate.

## Choose a skill

| Skill | When to use it | What you get |
|---|---|---|
| [Profile audit](skills/linkedin-profile-audit/SKILL.md) | Review your profile or check completed edits | A weighted readiness score, prioritised fixes, headline, About, banner and Experience drafts, plus Featured recommendations |
| [Content planner](skills/linkedin-content-planner/SKILL.md) | Plan a week or another period | A calendar and post briefs filtered by topic, content pillar, funnel stage or source section |
| [Post creator](skills/linkedin-post-creator/SKILL.md) | Create one post within a selected section | Ideas, a CPIO summary, complete content and a caption suited to the format |
| [Post writer](skills/linkedin-post-writer/SKILL.md) | Draft from a brief or edit existing copy | A complete post that preserves your facts, meaning and voice |

The creator supports text posts, carousel copy, video scripts and image briefs. Scripts and visual briefs are drafts. Finished media requires the appropriate tools and a separate request.

## Get started

1. Download or clone this repository.
2. Copy the selected folders from `skills/` into your AI assistant's skill directory. Keep each folder's references, scripts and metadata together. Back up an existing skill with the same name before replacing it.
3. Ask your assistant to use the skill and supply your founder context.

For Codex, personal skills belong in `~/.agents/skills/`. Project skills belong in `.agents/skills/` inside the project. Codex also supports symlinked skill folders. See [OpenAI's installation guidance](https://learn.chatgpt.com/docs/build-skills) for details.

Other assistants have their own installation and invocation conventions. Skill loading, script execution and computer-use support depend on the platform.

### Requirements

| Task | What the assistant needs |
|---|---|
| Planning and writing | Access to the skill files and your supplied context |
| Live profile inspection | Approved computer-use tools and access to the target LinkedIn profile |
| Numeric audit scoring | Python 3 or a verified executable equivalent |

The bundled calculator uses only the Python standard library. The skills require no particular browser provider or LinkedIn integration. When live access is unavailable, the audit can use supplied text, screenshots or an export and mark unseen checks unassessed. Without a verified calculator, it returns a qualitative audit with the numeric score unavailable.

## Example prompts

These examples use Codex's `$skill-name` syntax. Replace the example context with your own facts and supply the referenced notes or drafts.

### Audit your profile

```text
Use $linkedin-profile-audit to audit this profile: [profile URL].
My goal is to attract clients from small accounting firms.
My offer is invoice administration workflows.
Use the founder facts and approved proof below.
```

If your profile goal is missing, the skill asks one question and waits. It reuses a goal you've already supplied. Customers, testimonials and revenue figures are not prerequisites for an audit.

### Plan next week

```text
Use $linkedin-content-planner to plan next week around reducing
repetitive admin, with three consideration-stage posts.
Use the audience, offer and source notes below.
```

Topic and funnel stage are separate filters. You can request one stage for the whole week. Without a specified cadence, the planner proposes three posts for the next full week. Dates are suggestions, not scheduled posts.

### Create one post

```text
Use $linkedin-post-creator to create one carousel about invoice
handoffs for small accounting firms, at the consideration stage.
Include ideas, slide copy and a companion caption.
Use these notes: [paste your notes].
```

A section can be a topic, content pillar, funnel stage or source-document passage. If no specific section has been selected, the creator asks for clarification before generating ideas or copy.

### Rewrite a draft

```text
Use $linkedin-post-writer to edit the draft below using my voice samples.
Preserve the facts, meaning and consideration-stage purpose.
Change only the wording. Return clean post copy.
```

The writer removes generic AI phrasing while preserving the founder's actual language and level of certainty. It does not invent anecdotes, opinions or results to simulate a personal voice.

## Write with CPIO

The creator and writer use four steps:

- **Convey:** decide the one point the reader should understand.
- **Package:** choose the angle, opening and format.
- **Information:** select the facts and examples that support the point.
- **Order:** arrange them so a new reader can follow the explanation.

CPIO guides the writing process. It does not guarantee reach or sales. The creator can show a short summary, while the writer usually keeps the process internal and returns the copy.

## Understand the profile score

The Profile Readiness Score uses 20 criteria across six sections:

| Section | Maximum points |
|---|---:|
| Headline | 25 |
| About | 25 |
| Featured | 20 |
| Banner | 15 |
| Experience | 10 |
| Photo | 5 |
| Total | 100 |

Each criterion earns 5 points for pass, 2.5 for partial and 0 for fail. Missing evidence remains unassessed. Incomplete audits show a provisional range and assessed coverage, without a grade. With no assessed criteria, the assessment is unavailable.

The calculator generates the score block and checks the delivered report against the saved criterion statuses. It verifies arithmetic, not the fairness of an evidence judgement. Qualitative judgements can vary and need review.

This is a custom readiness rubric, not LinkedIn's ranking system. Read the [full criteria and scoring rules](skills/linkedin-profile-audit/references/scoring.md).

## Review before publishing

The skills use supplied or inspected evidence and flag missing facts. They preserve attribution, approximate figures and uncertainty. Private client details need publication permission before appearing in public copy.

Profile audits are read-only. Plans and drafts require your review. They do not update LinkedIn, publish posts, send messages or schedule content.

The bundle covers profile review, planning and writing inspired by a 90-day founder guide. It does not run a complete 90-day programme or provide automated analytics.

## Contribute and test

From the repository root:

```sh
python3 -B -m unittest discover -s tests
```

The automated tests cover arithmetic, grade boundaries, unknown evidence, invalid inputs, goal requirements and generated-report verification. They need no external packages, credentials or private test files. The GitHub Actions workflow runs the same command on pushes and pull requests.

For behavioural testing, follow the [stress-test procedure](stress-tests/README.md). Use fresh contexts and inspect the actual output. Keep examples fictional or approved for sharing. The `audits/`, `drafts/` and dated `stress-tests/` folders are ignored by Git. Keep raw founder evidence local.

## Acknowledgements

- [How To Build A LinkedIn Presence As A Founder (90-days)](https://docs.google.com/document/d/1FWY73HV-ZpTUOVDEAKv1LxwtGQC55tN93akZBL6_I0A/edit) informed the planning and CPIO references.
- [FAT Agent](https://github.com/spruikco/fat-agent-skill) informed the weighted audit and re-audit approach.
- User-supplied editing guidance informed the human-voice references.

The readiness rubric and calculator are custom to Founder Signal. Detailed attribution and adaptation notes appear in the relevant references.

## Licence

No repository licence has been assigned. Upstream provenance and redistribution permissions for the founder guide and supplied writing rules remain unconfirmed.
