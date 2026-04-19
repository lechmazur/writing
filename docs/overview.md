# Creative Writing Benchmark — Overview

This repository benchmarks LLMs on creative writing across generation, comparison, and analysis phases. The canonical public rating is now the pairwise-comparison Thurstone rating, not an absolute 0-10 rubric mean. Pipelines generate stories, compare matched stories written to the same required elements, and produce ranked reports and charts from those head-to-head outcomes.

Key docs:
- Project details: `PROJECT_DOCUMENTATION.md`
- End‑to‑end flows: `PIPELINES.md`

## Core Phases (High Level)
- Story generation → `/mnt/r/writing2-data/stories_wc/<llm>/story_wc_*.txt`
  - `run_wc_prompts.py` supports `--models` to override its current in-file default model pool for one run
- Story lexical diagnostics (optional) → `data/proper_names_by_llm.csv`
- Legacy absolute grading and comments → `/mnt/r/writing2-data/graded/`, `/mnt/r/writing2-data/grader_eval_raw/` (diagnostic/archive path, no longer the public leaderboard)
- Optional simple grading + combined overall metric → `/mnt/r/writing2-data/for_grading_simple_wc/`, `/mnt/r/writing2-data/graded_simple/`, `data/*_simple.csv`, `data/*_combined.csv` (diagnostic/archive path)
- Sentence-length diagnostics in grading pipeline → `data/sentence_length_*.csv`, `reports/sentence_length_report.md`, `images/sentence_length_*.png`
- Style and similarity analyses → `style_fingerprint_*`, `story_similarity_*`
- Inter-LLM A-vs-B quality comparisons → `data/inter_llm_comparison_*.csv`, `reports/inter_llm_comparison_score_leaderboard.md`, `images/inter_llm_comparison_*`
- Reports and charts → `reports/`, `images/`, `data/*.csv`
- The previous absolute-rating README surface and its old README-linked chart PNGs are archived under `archive/absolute_ratings_v4_2026_04_19/`.
- Reporting/chart stages assume complete model metadata and complete weighted-report inputs; shared display names, categories, and chart colors now come from the server-backed `model_info.py` adapter via `/mnt/r/benchmark_utils` and `/mnt/r/connections`, and missing presentation or question-level SEMs are treated as errors rather than silently defaulted.
- New router-backed `.txt` outputs also emit adjacent `.json` sidecars with request metadata, usage summaries, outcome classification, and request-trace excerpts for invalid or failed calls.

## Inter-LLM Comparison Maintenance
- Canonical intake for newly generated models is pairwise comparison, not independent rubric grading. `prepare_grading.py` and `vis_word_counts_script.py` remain useful as pre-comparison QC.
- Public quality rankings should use the Thurstone comparison rating from `reports/inter_llm_comparison_score_leaderboard.md`. Absolute rubric means are archived diagnostics and should not be revived as the main leaderboard.
- Active comparison roster is explicit: `data/inter_llm_active_models.txt`.
- Full-run policy files are versioned at repository root:
  - `inter_llm_comparison_full_evaluators.txt`
  - `inter_llm_comparison_story_excluded_models.txt`
- New story directories do not automatically enter canonical comparison. Refresh the active roster from `/mnt/r/writing2-data/stories_wc/*` before `--run-all`; the exclusion file prevents models from being re-added on the next roster rebuild, while the active roster controls the current run scope.
- Word-count readiness is not just “no outliers”: check both `vis_word_counts_script.py` output and `data/word_count_issues_wc.txt` for formatting anomalies before scheduling comparison runs.
- Incomplete models can still be compared if overlap supports the chosen `--n`, but that should be an explicit policy exception and later called out in reporting.
- Recommended new-model intake order is: QC, roster refresh, anchor pilot, optional new-vs-new pilot, then broader/canonical expansion.
- Pairwise comparison runner supports both single and multi-evaluator execution:
  - with no evaluator flags, comparison scripts default to the versioned roster in `inter_llm_comparison_full_evaluators.txt`
  - `run_inter_llm_comparisons.py --evaluator <model>`
  - `run_inter_llm_comparisons.py --evaluators "<m1,m2,...>"`
  - `run_inter_llm_comparisons.py --evaluators-per-pair <N>` deterministically keeps only `N` eligible evaluators per `(llm_a, llm_b, template_id)` after self-eval filtering
  - default comparison temperature is `1.0` (`--temperature` to override)
  - default self-eval guard is `--self-eval-policy family` (same-family + exact self-eval exclusion)
  - override with `--self-eval-policy exact` or `--self-eval-policy off` when needed
- One-command pipeline mirrors this with `--pair-evaluator`, `--pair-evaluators`, and `--pair-evaluators-per-pair`.
- Batch manager also supports both single and multi-evaluator execution:
  - `run_inter_llm_comparison_batch.py --evaluator <model>`
  - `run_inter_llm_comparison_batch.py --evaluators "<m1,m2,...>"` or `--evaluators-file <path>`
  - `run_inter_llm_comparison_batch.py --evaluators-per-pair <N>` applies the same deterministic per-pair cap before scheduling evaluator subprocesses
  - `--pairs-file <path>` schedules exact unordered pairs from a file without expanding a roster
  - `--added-models` schedules `new_model x active_model` only; it does not create comparisons among the added models in that same invocation
  - `--compare-only` to skip build and resume against existing tasks only
  - `--compare-shard-root` + `--defer-shard-merge` to isolate writes for multi-process runs
  - `--merge-shards-from <dir1,dir2,...>` to merge shard outputs into canonical CSVs in a single safe step
- The preferred cost-control pattern is to keep the full evaluator roster and use `--evaluators-per-pair` / `--pair-evaluators-per-pair` instead of freezing one small global judge panel.
- Comparison prompt-template experiments are supported with:
  - `--template-id` (isolation key across prompts/raw/index/scores/summaries)
  - `--template-path` (alternate pairwise comparison template file)
  - non-default template outputs are stored under template-scoped subdirectories.
- If the evaluator roster changes materially, such as replacing `gpt-5.2-low` with `gpt-5.4-low`, start a new versioned evaluator file and a new `template_id` rather than mixing judge eras inside one scope.
- Incremental comparison coverage should prioritize leaderboard-relevant uncertainty near the top of the ranking. When budget is limited, prefer missing or inconclusive direct comparisons among high-ranked models over evenly completing lower-table pair coverage.
- Use `--pairs-file` for manually selected high-value gaps so the runner executes exactly those direct comparisons rather than every combination in a temporary roster.
- Non-batch comparison runs default to port `8006`; batch maintenance uses port `8040` unless overridden.
- Expect higher latency on batch router `8040`; progress output may pause for long intervals under load.
- Operational port policy:
  - `8006` is the regular/fast router and should be the default for smoke checks, quick validation, small batches (roughly under 200 calls), and Gemini runs.
  - `8040` is the batch router. It is typically lower-cost in our setup, but it is slower and only some providers support true batch processing there.
  - `8040` is fine for larger production runs where there are many calls and latency matters less than batch pricing.
  - Metadata-aware clients should attach `metadata.router_request_id`; on invalid or failed responses they should inspect the adjacent sidecar first and `/request_trace/<id>` second.
  - In practice, true `8040` batch support is limited to Gemini, OpenAI, and Anthropic. Other models are forwarded to the regular `8006` path, so `8040` does not improve turnaround for them.
  - Gemini is especially slow on `8040` and can take many hours. Prefer a separate Gemini-only invocation on `8006` unless you are intentionally trading latency for lower batch cost.
  - `run_inter_llm_comparison_batch.py` uses one port per invocation for all evaluators, so split Gemini into its own invocation when you want fast results.
  - Port choice does not set concurrency by itself; total in-flight requests come from the effective `pair-workers * workers` combination.
- Comparison scripts now emit step/progress tracking and before/after row deltas for prompt/index/score hygiene checks.
- Aggregation is margin-primary (Thurstone-style on signed margins) with BT as reference, plus evaluator diagnostics:
  - `data/inter_llm_comparison_rating_diagnostics.csv`
  - `data/inter_llm_comparison_tie_sensitivity.csv`
  - `data/inter_llm_comparison_evaluator_diagnostics.csv`
  - `data/inter_llm_comparison_evaluator_agreement.csv`
  - `data/inter_llm_comparison_side_bias_corrections.csv`
- Rating diagnostics include BT-vs-Thurstone rank agreement, sigma stability, and transitivity cycle-rate checks.
- Bootstrap uncertainty in comparison aggregation is hierarchical by default (stories + evaluators), with a story-only fallback flag.
- Evaluator side-A bias correction on signed margins is enabled by default during aggregation (toggleable).
- `plot_inter_llm_comparison_charts.py` renders large Plotly comparison charts, including shaded uncertainty rectangles for rating CIs, shared model-brand logos on rating charts where `/mnt/r/benchmark_utils` has assets, and a pairwise margin heatmap.
- Use `run_inter_llm_comparison_batch.py` for:
  - roster initialization from `/mnt/r/writing2-data/stories_wc/*`
  - roster initialization with exclusions via `--exclude-models` / `--exclude-models-file`
  - all-pairs runs from active roster
  - pair-parallel compare runs (`--pair-workers`) with safe shard-to-canonical merge behavior
  - compare-only resume runs (`--compare-only`) without adding new tasks
  - deferred-merge shard workflows for parallel evaluator invocations
  - total evaluator concurrency caps during pair-parallel runs (`--max-workers-per-llm`)
  - adaptive expansion of inconclusive pairs (`--adaptive-inconclusive`)
  - disagreement-focused adaptive expansion (`--adaptive-disagreement`)
  - added-model incremental runs (`new_model x active_model`)
  - dropped-model filtering across tasks/index/scores with optional re-aggregation
  - stale-state repair (`--repair-stale-paths`) after path-root migrations
- For guaranteed net-new matchup expansion, combine builder flags:
  - `--only-new` and `--require-exact-n`
- For similarity landscape coverage, `run_inter_llm_similarity_sweep.py` supports:
  - `--target <model>` (hub-and-spoke)
  - `--all-pairs` (full matrix coverage)

## Poor‑Writing Analysis (Where this fits)
Purpose: For each story, have an analyzer LLM surface up to three concrete, quoted examples of very poor writing and rate each 1–10 (10 = worst). Results are later parsed into structured CSVs.

Steps:
1) Build prompts (one per story):
   ```bash
   python build_poor_writing_prompts.py --llms ""   # empty → all LLMs
   # → /mnt/r/writing2-data/for_poor_writing/<llm>/analyze_story_wc_*.txt
   ```
2) Run analyzer (parallel, resumable):
   ```bash
   python run_poor_writing_analysis.py -p 8040 --analyzer gpt-5-low --workers 24 --skip-existing
   # → /mnt/r/writing2-data/poor_writing_raw/<analyzer>/<llm>/story_wc_*.txt
   # → data/poor_writing_run_log.csv
   ```
3) Aggregate parsed results:
   ```bash
   python aggregate_poor_writing.py
   # → data/poor_writing_examples.csv, data/poor_writing_story_summary.csv,
   #   data/poor_writing_parse_errors.csv
   ```

`run_poor_writing_analysis.py` uses an OpenAI‑compatible proxy at `http://localhost:<port>/v1/` (default port `8040`). The SDK requires an API key value, but many proxies ignore it. The runner prints pending task counts, progress updates, and a start/end/duration summary with tracked output paths; it appends a CSV log with `OK`/`ERROR <exc>` statuses.

See `PIPELINES.md` for flags and operational details.

Optional utility:
```bash
python build_proper_names_by_llm.py
# → data/proper_names_by_llm.csv
#   Uses sentence-aware capitalization checks to reduce false positives
#   from sentence starters such as "After".

python compare_proper_name_similarity.py --focus-llm pony-alpha
# → data/proper_name_pair_similarity.csv
# → data/proper_name_similarity_matrix.csv
# → reports/proper_name_similarity_leaderboard.md
```
