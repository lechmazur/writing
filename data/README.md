# Public Benchmark Data

Snapshot `2026-08-23` covers the canonical `comparator_v2_eval_v2_v3_combined_public` leaderboard scope.

## Repository Tables

- [Leaderboard](leaderboard.csv)
- [Direct head-to-head results](head_to_head.csv)
- [Pair-story aggregates](pair_story_aggregates.csv)
- [Judgment index](judgments_index.csv)
- [Evaluator diagnostics](evaluator_diagnostics.csv)
- [Evaluator agreement](evaluator_agreement.csv)
- [Rating diagnostics](rating_diagnostics.csv)
- [Tie sensitivity](tie_sensitivity.csv)
- [Side-bias corrections](side_bias_corrections.csv)
- [Scope compatibility](scope_compatibility.csv)
- [Judgment JSON Schema](judgments_schema.json)
- [Browsable judgment sample](judgments_sample.jsonl)
- [Comparison prompt](methodology/comparison_prompt.txt)
- [Comparison rubric](methodology/comparison_rubric.txt)

The index contains 67,178 accepted ordered judgments and
163 excluded or superseded response records. Both `ab`
and `ba` presentations are preserved. Numeric leaderboard aggregation collapses them only
at analysis time.

## Full Prose and Source Texts

- [judgments-accepted-part-0001.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0001.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 10,367,529 compressed bytes
- [judgments-accepted-part-0002.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0002.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 10,249,172 compressed bytes
- [judgments-accepted-part-0003.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0003.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 9,533,002 compressed bytes
- [judgments-accepted-part-0004.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0004.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 9,714,585 compressed bytes
- [judgments-accepted-part-0005.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0005.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 9,831,231 compressed bytes
- [judgments-accepted-part-0006.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0006.jsonl.zst) — accepted evaluator prose and parsed judgments; 10,000 records; 9,649,230 compressed bytes
- [judgments-accepted-part-0007.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-accepted-part-0007.jsonl.zst) — accepted evaluator prose and parsed judgments; 7,178 records; 6,960,235 compressed bytes
- [judgments-excluded-part-0001.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/judgments-excluded-part-0001.jsonl.zst) — excluded, malformed, or superseded evaluator responses; 163 records; 117,280 compressed bytes
- [stories-part-0001.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/stories-part-0001.jsonl.zst) — referenced story texts; 12,255 records; 17,981,591 compressed bytes
- [writing-prompts-part-0001.jsonl.zst](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/writing-prompts-part-0001.jsonl.zst) — writing prompts; 400 records; 63,298 compressed bytes
- [SHA256SUMS](https://github.com/lechmazur/writing/releases/download/benchmark-data-2026-08-23/SHA256SUMS) — SHA-256 checksums for release data assets; 0 records; 1,036 compressed bytes

`judgments-accepted` assets contain the exact evaluator prose used by the public fit.
`judgments-excluded` contains indexed parse failures and preserved superseded router
attempts. The story and writing-prompt assets make the release self-contained even when a
historical model is not shown in the repository's current-model story browser.

Evaluator commentary is evidence about a judgment, not ground truth. It can contain
mistakes, subjective claims, or inaccurate quotations. Provider response envelopes,
request identifiers, account metadata, HTTP traces, and internal filesystem paths are not
published.
