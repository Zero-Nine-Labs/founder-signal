# Testing the LinkedIn skills

Use a fresh agent context for each fixture. Give it the current skill path and raw request only. Do not show expected answers, other case outputs or evaluator notes. Keep founder context inside the fixture so earlier cases cannot supply a missing goal, section or proof. Use the requested test model and record it. Record the skill commit or file hashes before each round.

Save each exact response and its actual tool actions in separate files. For an audit, retain the 20 criterion statuses, generated score block and delivered report. Prefix all files with the case and run number. If the response asks for clarification, end that case without inventing an answer.

Evaluate the response independently against the acceptance criteria. For scores, rerun the helper on the saved statuses and verify the delivered report. Check evidence judgements separately: correct arithmetic does not prove a fair score. Confirm a missing goal or selected section produces one question only, while a supplied goal or selection is reused.

Repeat fragile cases at least three times with independent contexts after the final instruction change. Keep earlier failures as historical evidence. Do not count a corrected response as a new independent run or combine results from different skill versions into one pass rate. Repeat changed cases and relevant adjacent cases, rather than every unchanged case.

For live profile validation, use the environment's preferred computer-use workflow. Verify target name and URL, then inspect the actual page pixels. Check the default desktop layout and a narrow web viewport when supported, record dimensions and limitations, and restore temporary settings. Check lazy-loaded sections and the full Experience list before treating missing extraction as absence. Report mobile web and mobile app validation separately.

Validate all skill metadata, relative references and installed links after edits. Run the focused score-helper tests for code changes and check the diff for whitespace errors. Keep dates, skill version notes, raw responses, evaluation and live evidence together in a dated test folder.

Dated run folders are ignored by Git because they may contain founder profile evidence, private context and local paths. Preserve those files locally. Publish only deliberately reviewed, sanitised fixtures and results. The automated score-helper tests must run without these local folders.
