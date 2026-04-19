# Creative Writing Benchmark — Project Documentation

Last updated: 2026-04-19

## Table of Contents
1. [Purpose](#purpose)
2. [Who This Document Is For](#who-this-document-is-for)
3. [Benchmark Philosophy](#benchmark-philosophy)
4. [System Overview](#system-overview)
5. [Repository Map](#repository-map)
6. [Data Model and Path Conventions](#data-model-and-path-conventions)
7. [End-to-End Pipeline Narrative](#end-to-end-pipeline-narrative)
8. [Scoring Methodology](#scoring-methodology)
9. [Reliability, Normalization, and Agreement](#reliability-normalization-and-agreement)
10. [Analysis and Reporting Outputs](#analysis-and-reporting-outputs)
11. [Poor-Writing Analysis Stack](#poor-writing-analysis-stack)
12. [Similarity and Diversity Stacks](#similarity-and-diversity-stacks)
13. [Inter-LLM Comparison Stack](#inter-llm-comparison-stack)
14. [Operational Guidance](#operational-guidance)
15. [Testing Strategy](#testing-strategy)
16. [Error Handling and Failure Policy](#error-handling-and-failure-policy)
17. [Configuration and Extensibility](#configuration-and-extensibility)
18. [Troubleshooting](#troubleshooting)
19. [Maintenance Checklist](#maintenance-checklist)
20. [Script-Verified Defaults Snapshot](#script-verified-defaults-snapshot)
21. [Detailed Script Contracts](#detailed-script-contracts)
22. [Data Contracts and CSV Schemas](#data-contracts-and-csv-schemas)
23. [Current Hardcoded Model Pools](#current-hardcoded-model-pools)
24. [Verification Log](#verification-log)
25. [Related Documents](#related-documents)

## Purpose

This repository implements a full benchmark system for measuring creative writing performance across many LLMs. It is not just a plotting repo and not just an evaluation script. It is a multi-stage production workflow that starts with prompt construction, runs large generations, performs pairwise story comparisons, computes robust aggregates, and finally produces ranked reports with diagnostics.

In practice, this benchmark should be thought of as an operations pipeline as much as an evaluation framework. The quality of the final rankings depends on repeatable prompt construction, stable file naming, consistent parsing, and explicit handling of partial failures. A result table is only meaningful when the pipeline that produced it is inspectable and reproducible.

The central question is straightforward: when models are asked to write constrained fiction with the same required-element brief, which ones consistently produce stronger stories in direct head-to-head comparison?

The answer requires disciplined process control. Consistent prompt design, deterministic file conventions, explicit quality gates, multi-evaluator pairwise judgments, and transparent statistical summaries are all required to avoid measuring noise instead of writing ability.

This document explains how that process is designed today, what assumptions it makes, and how to extend it safely.

## Who This Document Is For

Use this document if you are running the benchmark end-to-end, modifying one stage in the pipeline, validating whether reported rankings are trustworthy, onboarding a new writer or grader model, or debugging result drift between runs.

The goal is to make the repository legible at two levels at once: high-level architecture for orientation, and script-level behavior for implementation details. If you need to understand both what the system is trying to do and what the current code actually does, this is the right reference.

If you only need command snippets, use [PIPELINES.md](PIPELINES.md). If you only need a short project summary, use [docs/overview.md](docs/overview.md).

## Benchmark Philosophy

The benchmark intentionally avoids the easiest failure mode in creative-writing evals: scoring “vibes” without controlled constraints. Each story prompt is built around ten required element categories. The writer must satisfy those constraints while still producing coherent and engaging fiction.

This structure gives the benchmark two useful lenses at once:
1. Craft quality: plot, characterization, prose, thematic cohesion, and overall impact.
2. Constraint integration quality: whether each required element appears naturally and functionally.

That split is why the rubric is partitioned into Q1–Q8 and Q9A–Q9J, and why aggregation uses explicit weights.

The benchmark also assumes that single-evaluator outputs are noisy. Instead of trusting one evaluator, it uses multiple evaluator LLMs and analyzes agreement patterns as first-class outputs.

The canonical public leaderboard is now the inter-LLM comparison Thurstone rating. Legacy absolute 0-10 rubric means remain useful for diagnostics and historical audit, but they are archived and should not be used as the main quality ranking going forward.

## System Overview

At a high level, the system has five layers:

1. Prompt and element-set construction.
2. Story generation for each writer model.
3. Pairwise comparison prompt preparation and evaluator-model scoring.
4. Thurstone-style aggregation, diagnostics, and ranking.
5. Secondary analysis products (comments, summaries, poor-writing profiles, style/diversity, inter-LLM similarity).

The dominant workflow is batch-oriented and file-backed. Most scripts communicate through explicit files rather than in-memory orchestration. This is intentional: resumability and post-hoc auditability matter more here than minimal I/O.

This design also keeps failure isolation clear. If one stage fails or is interrupted, operators can inspect intermediate files, repair the issue, and resume from a known boundary instead of rerunning the entire benchmark. The cost is heavier I/O and more path discipline, but that tradeoff is deliberate.

## Repository Map

Major top-level areas:

- `prompts/`:
  Prompt templates for generation, grading, analysis, and synthesis tasks.
- `tests/`:
  Integration-heavy test suite covering orchestration behavior and data contracts.
- `data/`:
  Canonical processed outputs, metrics CSVs, and run logs.
- `images/`:
  Generated charts and heatmaps.
- `reports/`:
  Markdown leaderboards and narrative report outputs.
- `docs/`:
  High-level orientation docs.
- `temp/`:
  Generated API/dependency artifacts (`API.md`, `dependencies.dot`).

Core code is mostly at repository root, with helper packages for complex modules:
- `prepare_grading_pkg/`
- `collect_grades_pkg/`
- `charts_bars_pkg/`
- `grader_agreement_pkg/`
- `style_fingerprint/`
- `best_worst/`

Operationally, the easiest way to navigate this repository is to treat it as a set of script families. Prompt construction scripts feed generation scripts; generation scripts feed grading-prep scripts; grading scripts feed collection and analysis scripts. Once this mental model is established, most path and schema decisions become predictable.

## Data Model and Path Conventions

The system uses a split between repository-local outputs and external story/grade corpora. This split keeps heavy raw artifacts outside the repo while preserving lightweight, versioned analysis products inside the repo.

Primary external storage roots:
- `/mnt/r/writing2-data/stories_wc/`
- `/mnt/r/writing2-data/for_grading_wc/`
- `/mnt/r/writing2-data/for_grading_simple_wc/`
- `/mnt/r/writing2-data/graded/`
- `/mnt/r/writing2-data/graded_simple/`
- `/mnt/r/writing2-data/grader_eval_raw/`

Primary repository-local output roots:
- `data/`
- `images/`
- `reports/`

Router-backed text-generation/evaluation scripts now also emit adjacent `.json` sidecars for new calls. The sidecar contract is operational rather than analytic: it captures the output path, prompt path when available, request port, `router_request_id`, provider finish reason, refusal signal, provider model/response id, usage summary, final outcome classification, and any fetched `/request_trace/<id>` excerpt. This is the main audit trail for router-visible failures such as HTTP-200 refusals, reasoning-only outputs, incomplete responses, and transport errors.

Important conventions:
- Story files typically use `story_wc_####.txt` style naming.
- Grade files mirror story index naming for deterministic joins.
- CSV files in `data/` are treated as canonical analysis inputs.
- Scripts should avoid hard-coded ad hoc paths and should resolve paths once.

Filename determinism is not cosmetic here; it is the join key across almost every downstream table. When names drift, rankings drift, and debugging becomes expensive. The safest default is to preserve naming contracts and add explicit conversion helpers when new formats are introduced.

## End-to-End Pipeline Narrative

### Phase A: Category-set construction and rating

The project first creates candidate required-element sets, has proposer models select coherent combinations, then has independent rater models score those sets. The highest-rated normalized set per seed is chosen for downstream writing prompts.

Conceptually, this phase is where task difficulty is shaped. If required elements are too random, the benchmark measures prompt awkwardness instead of writing skill. If required elements are too easy, the benchmark loses discriminatory power. The proposer-and-rater loop is the mechanism used to keep that balance explicit.

Primary scripts:
- `create_prompts.py`
- `choose_cats.py`
- `create_rate_prompts.py`
- `run_rate_prompts.py`
- `collect_ratings.py`
- `create_wc_prompts.py`

Outputs from this phase become the story-generation prompt source of truth.

### Phase B: Story generation

Writers generate stories from the WC prompts. The expected target is a constrained length band (600–800 words), and stories are stored by model under `/mnt/r/writing2-data/stories_wc/<llm>/`.

This phase is usually the longest wall-clock segment, so resumability and clear run logs matter more than minimal script complexity. Generation is intentionally designed so operators can rerun specific models without invalidating unrelated outputs.

Primary script:
- `run_wc_prompts.py`

This script is long-run oriented, parallelized, resumable, and heavily logged.

### Phase C: Pre-grading preparation and word-count diagnostics

Generated stories are cleaned and converted into grading-ready prompts. In parallel, word-count diagnostics are produced to identify out-of-range outputs and data quality anomalies.

This stage turns free-form model outputs into parser-friendly grading packets. It is also where malformed `<story>` wrapping and word-count marker artifacts are normalized, which prevents later grading and aggregation scripts from silently dropping rows.

Primary scripts:
- `prepare_grading.py`
- `vis_word_counts_script.py`

Modes:
- Full rubric prompt generation (default).
- Simple overall-only grading prompt generation (`--simple`).

### Phase D: Optional gating and cleanup

This stage detects rubric-level mismatches that can contaminate downstream grading quality. Examples include POV mismatches and closure failures. Operators may remove affected grades through explicit plan/apply flows.

The intent is to remove known-invalid grading evidence before it influences aggregate metrics. It is deliberately explicit and auditable: plan the exclusions, inspect them, then apply them.

Primary scripts:
- `check_single_pov.py`
- `remove_grades_for_mismatches.py`
- `remove_suspicious_grades.py`

This phase exists to fix root-quality issues rather than masking them in aggregation.

### Phase E: Grading

Teacher models score story files using the rubric prompts. The grading runner includes block-list support for known problematic grader-story combinations.

At this point the benchmark shifts from generation variance to evaluator variance. The script behavior around skip/overwrite, teacher pools, and blocked combinations has direct impact on the shape of the final dataset, so these defaults should be treated as part of the experimental protocol.

Primary script:
- `create_grades.py`

Notable behavior:
- Supports full and simple modes.
- Can skip or overwrite existing outputs.
- Enforces `BLOCKED_STORIES_BY_TEACHER` exclusions and reports withheld task counts.

### Phase F: Grade aggregation and scoring exports

Raw grade text files are parsed and transformed into canonical CSVs. The parser validates ranges, coverage, and parse integrity, then produces per-question and per-story aggregates.

This phase is the main contract boundary for downstream analytics. Once outputs are written here, most later scripts assume schemas and naming are stable, so contract changes should be made cautiously and with test coverage.

Primary script:
- `collect_grades.py`

Outputs include:
- `data/teacher_student_file_questions.csv`
- `data/teacher_student_filemeans.csv`
- `data/teacher_student_filemeans_numbered.csv`
- `data/teacher_student_stats.csv`
- `data/student_overall_stats*.csv`

Optional simple + combined outputs are generated when simple-grade data exists, unless disabled with `--no-simple`.

### Phase G: Core analysis and report generation

This stage builds model-level statistics, normalized views, chart packs, and leaderboard markdown artifacts.

The reporting layer intentionally emits both machine-oriented tables and reader-oriented artifacts. CSV outputs remain the audit trail, while markdown and images provide communication artifacts for interpretation and discussion.

Primary scripts:
- `analysisb.py`
- `analysis_basic.py`
- `analysis_extra.py`
- `leaderboard.py`
- `charts_bars.py`
- `charts_heatmaps.py`
- `charts_scatter.py`
- `charts_strip.py`

### Phase H: Comments and summary synthesis

Per-question comments are extracted, summarized, and fused into higher-level model summaries.

These outputs complement quantitative rankings with qualitative evidence. They are useful for diagnosing why a model performs as it does, especially when two models are close numerically but fail in different ways.

Primary scripts:
- `collect_comments_1to6.py`
- `create_summary_prompts.py`
- `generate_summary_responses.py`
- `create_general_summary_prompts.py`
- `generate_general_summary_responses.py`

These outputs are intended for qualitative interpretability and editorial insight, not numeric ranking.

## Scoring Methodology

Scoring is designed to preserve per-dimension signal while still producing a stable overall ranking number. The system avoids collapsing directly to one score too early; instead it keeps question-level and story-level structure available for diagnostics and sensitivity checks.

### Rubric partition

The benchmark rubric has 18 scored components:
- Q1–Q8: major narrative/craft dimensions.
- Q9A–Q9J: required-element integration dimensions.

If an element category is intentionally set to `None` in prompt construction, the corresponding 9-series item is treated as not applicable and removed from weighted aggregation for that story; remaining weights are re-normalized.

### Per-story score

Each grader produces per-question scores in `[0.0, 10.0]`.

For one `(story, grader)` pair, aggregate with a weighted power mean (`p = 0.5`) using a 60/40 group split:
- total weight on Q1–Q8 = 0.60
- total weight on Q9A–Q9J = 0.40

`p = 0.5` intentionally behaves like a soft-minimum relative to arithmetic mean, so weak dimensions pull the aggregate down more aggressively than they would under a plain average.

This matters because creative-writing quality is not additive in a simple way. A story with one or two major breakdowns should not rank equivalently to a story that is consistently solid across dimensions. The chosen power-mean behavior makes that tradeoff explicit.

The final story score is the mean across graders.

### Per-model score

Model-level summaries are computed from story-level aggregates:
- mean score,
- SEM,
- confidence intervals,
- and optional normalized variants.

The ranking table and bar charts are generated from these model-level values.

The repository keeps intermediate tables so that each step of this reduction can be audited. You can trace a model-level number back to story-level and question-level evidence instead of treating the leaderboard as opaque.

### Combined overall metric (optional)

When simple grading is available, the combined metric is:

`combined = 0.7 * original_weighted_power_mean + 0.3 * simple_overall_score`

This is exported as separate combined CSVs/charts so the baseline and combined views remain separable.

## Reliability, Normalization, and Agreement

### Why normalization exists

Different grader models have different severity scales. A raw 8.0 from one grader may not carry the same meaning as 8.0 from another. To reduce this scale bias, normalized views (typically z-score style transformations) are generated per grader before cross-grader consolidation in specific analyses.

### Agreement diagnostics

`grader_agreement.py` and `grader_agreement_pkg/` compute multiple agreement lenses:
- story-level pairwise agreement,
- question-level pairwise agreement,
- profile-shape agreement (relative score vector structure),
- and grader-level agreement diagnostics.

These checks are critical because they validate that benchmark conclusions are not driven by one grader’s idiosyncrasies.

In operational terms, agreement diagnostics are the guardrails against evaluator drift. If agreement collapses, ranking confidence should be treated as degraded even when raw coverage is high.

### Stability checks

The project includes robustness routines and reports such as leave-one-grader-out tables and exclusion-based rank sensitivity checks. These are used to answer practical questions like: “If one grader is removed, does the top tier collapse or stay stable?”

## Analysis and Reporting Outputs

Typical outputs consumed by readers:
- leaderboard markdown: `reports/leaderboard.md`, `reports/normalized_leaderboard.md`
- auxiliary leaderboard/report artifacts in `reports/`
- chart suite in `images/` including raw and normalized comparisons
- tabular metrics in `data/` for reproducible downstream analysis

The reporting layer is intentionally split between machine-friendly CSVs and human-friendly Markdown/PNG outputs.

That split supports two workflows. Analysts can re-run statistical slices directly from CSV contracts, while stakeholders can consume stable leaderboard/report artifacts without re-parsing raw grader text.

## Poor-Writing Analysis Stack

This stack exists to capture concrete failure modes, not just aggregate low scores.

The key idea is to preserve example-level evidence for severe issues. Aggregate scores can reveal that a model underperforms, but this stack explains how it underperforms by extracting concrete problematic passages and synthesizing repeat patterns.

Primary scripts:
- `build_poor_writing_prompts.py`
- `run_poor_writing_analysis.py`
- `aggregate_poor_writing.py`
- `build_poor_writing_theme_prompts.py`
- `run_poor_writing_thematic_analysis.py`
- `run_poor_writing_theme_synthesis.py`
- `run_poor_writing_easy20.py`

Workflow summary:
1. Build one analyzer prompt per story.
2. Run analyzer model over all prompts with resumable execution.
3. Parse and aggregate up to three severe examples per story.
4. Build per-LLM thematic prompts from high-severity examples.
5. Produce thematic diagnostics and reader-friendly synthesized summaries.

Expected outputs include:
- `data/poor_writing_examples.csv`
- `data/poor_writing_story_summary.csv`
- `data/poor_writing_parse_errors.csv`
- run logs in `data/poor_writing*_log.csv`

## Similarity and Diversity Stacks

### Intra-LLM story similarity and diversity

This stack estimates diversity within each writer’s story portfolio by sampling story pairs and evaluating similarity.

Unlike rubric scoring, this track focuses on intra-model spread. It asks whether a model repeatedly writes in near-identical structures or can sustain variety under shared prompt constraints.

Primary scripts:
- `build_similarity_tasks.py`
- `run_similarity_evals.py`
- `aggregate_similarity.py`

Core metric:
- diversity is mapped as `10 - similarity` after aggregation.

Primary outputs:
- `data/story_similarity_tasks.csv`
- `data/story_similarity_scores.csv`
- `data/llm_diversity_stats.csv`
- `reports/diversity_leaderboard.md`

### Style fingerprint diversity

A separate style-focused track computes lexical/style fingerprints, then derives diversity-like scores from feature geometry.

This parallel track is intentionally independent of semantic pairwise judgments. It offers a second perspective on variety that can catch stylistic collapse even when semantic plots appear different.

Primary scripts/modules:
- `build_style_fingerprints.py`
- `compute_style_diversity.py`
- `style_fingerprint/`
- `style_fingerprint_charts.py`
- `style_diversity_leaderboard.py`
- `style_diversity_leaderboard_altmarks.py`

This complements semantic similarity by measuring stylistic spread.

## Inter-LLM Comparison Stack

This stack compares different writer models directly on matched prompt indices.

Direct A-vs-B comparison exists because aggregate leaderboard gaps do not always explain pairwise matchups. Matched-index comparisons provide targeted evidence for whether one model tends to beat another on identical story seeds.

Primary scripts:
- `build_inter_llm_similarity_prompts.py`
- `run_inter_llm_similarity.py`
- `run_inter_llm_similarity_sweep.py`
- `aggregate_inter_llm_similarity.py`

Related broader comparison pipeline:
- `build_inter_llm_comparison_prompts.py`
- `run_inter_llm_comparisons.py`
- `aggregate_inter_llm_comparison_scores.py`
- `create_inter_llm_comparison_summary_prompts.py`
- `generate_inter_llm_comparison_summary_responses.py`
- `run_inter_llm_comparison_pipeline.py`
- `run_inter_llm_comparison_batch.py`

These scripts are used when you need explicit A-vs-B closeness and interpretable side-by-side outputs.

## Operational Guidance

### Baseline run order

For a clean full run, use this sequence:
1. category-set build/rate/select
2. story generation
3. prepare grading + WC diagnostics
4. grading
5. collect grades
6. core analysis + leaderboard
7. optional qualitative/auxiliary stacks

Exact command recipes are maintained in [PIPELINES.md](PIPELINES.md).

In day-to-day operations, most reproducibility issues come from partial reruns and mixed snapshots rather than algorithmic bugs. Keeping strict run order and clear input/output boundaries is the fastest way to avoid hard-to-debug drift.

### Runtime assumptions

- Linux/WSL environment.
- Local OpenAI-compatible proxy (default `localhost:8040`).
- Moderate to high parallelism (`--workers`) tuned to machine + proxy capacity.
- Frequent use of `--skip-existing` for resumable long runs.

### Logging and run summaries

CLI runs emit standardized start/summary blocks through `sitecustomize.py` and `script_logging.py` instrumentation. This gives consistent visibility into:
- start/end timestamps,
- runtime,
- output paths, including files written through `Path.write_text()`, `Path.open(...)`, plain `open(...)`, and pandas `to_csv()`,
- and summary context.

When adding a new writer path, prefer one of the tracked write helpers above. If a custom writer bypasses those hooks, call `current_run().add_output(path)` explicitly and verify the file appears under `[SUMMARY] outputs:`.

`stdout_lines` is now opt-in noise control:
- set `SCRIPT_LOGGING_STDOUT_LINES=1` to include stdout line counts in summaries,
- set `SCRIPT_LOGGING_DEBUG=1` to include internal debug plumbing lines,
- or set `SCRIPT_LOGGING_DISABLE=1` to disable automatic instrumentation.

For longer jobs, scripts should continue reporting progress counters and explicit error totals.

## Testing Strategy

The project favors integration tests over brittle micro-unit tests. Most failure modes in this repo appear at boundaries between scripts, files, and parsers rather than in tiny helper logic.

That said, shared router-call plumbing is a deliberate exception. The repo now has one shared router-aware chat helper, and it is tested directly because its classification and sidecar behavior are benchmark-critical across many scripts at once.

For this codebase, test value comes from exercising real contracts and realistic data flows. A passing unit test on a helper function is less informative than an integration test that proves a full stage can read the prior stage output and emit valid downstream artifacts.

Current testing shape:
- extensive integration tests under `tests/`
- selected unit tests for parsing/utilities where precision matters
- boundary-value coverage for dataset contracts and CLI-driven orchestration

Execution standard:
- `pytest -n auto`

Supplementary static checks:
- `ruff --select B,F`

Testing principles used in this repository:
- prioritize behavior and contracts,
- avoid coupling tests to incidental float artifacts,
- include edge-path and no-data branches,
- and assert explicit failure when required keys or types are wrong.

## Error Handling and Failure Policy

The repository prefers fail-fast behavior when inputs are malformed. Missing keys, invalid numeric ranges, parse contract mismatches, and impossible states should raise explicit exceptions rather than degrade silently.

For LLM-calling scripts, fail-fast now also includes metadata-aware response validation before raw text is persisted. Empty content, reasoning-only/incomplete outputs, refusals, and request-layer failures are classified explicitly; invalid outcomes are recorded in sidecars instead of being silently written as if they were normal text.

This policy is especially important for benchmark credibility. Silent fallbacks hide data loss and can produce clean-looking but invalid rankings. Explicit failures are operationally noisier, but they preserve trust in published results.

Important conventions:
- guard denominators before division,
- validate sample sizes before statistics operations,
- treat index bounds as contracts,
- clamp values after transformations,
- keep default args immutable,
- do not use broad exception swallowing,
- and avoid leaking sentinel values (`None`, `NaN`, empty string) into arithmetic.

A reproducible benchmark requires explicit breakage over quiet corruption.

## Configuration and Extensibility

### Model inventories and metadata

Benchmark rosters and shared model presentation are now split on purpose:
- `model_info.py`
  - thin compatibility adapter for this repo
  - keeps only local roster/highlight/suppression policy
  - reads shared display names, category buckets, and chart colors through `/mnt/r/benchmark_utils`
  - preserves the legacy pandas-compatible map surfaces through shared adapters
  - keeps roster filtering/order, benchmark alias compatibility, and `new_palette` derivation local to this repo
- `model_metadata_client.py`
  - is a thin wrapper over `benchmark_utils.model_metadata_client`
  - sends the benchmark-local `writing2:model_metadata` router identity
  - falls back to `/mnt/r/connections` via the shared in-process metadata module backend
  - keeps the benchmark's non-404-only fallback policy local instead of depending on shared predicate hooks
- `evaluators_list.txt`

When adding models:
- keep naming stable across generation, grading, and analysis stages,
- ensure directory names and report names remain join-compatible,
- add or update local roster/highlight/suppression policy only when this client specifically needs it,
- and do not reintroduce a copied factual display/category/color catalog in-repo.

### Public scoring policy

Public model quality ratings should be based on the inter-LLM comparison stack:
- primary score: Thurstone-style rating from signed pairwise comparison margins,
- uncertainty: hierarchical bootstrap over stories and evaluators,
- direct evidence: pair-stat rows and pairwise margin heatmap,
- reference only: Bradley-Terry columns and charts.

Absolute 0-10 rubric means, normalized absolute-score leaderboards, question-breakdown charts, and old grader-vs-model heatmaps are archived diagnostics. The previous absolute-rating README surface and its old README-linked chart PNGs are archived under `archive/absolute_ratings_v4_2026_04_19/`.

### Question and weight adjustments

If rubric structure changes:
- update question definitions and parsing logic,
- update weights in `question_weights.py`,
- verify collection scripts and downstream charts,
- and add integration coverage for new question ids.

### Path/config hygiene

Keep configuration runtime-driven and centralized. Avoid scattered constants and hidden assumptions. Prefer `pathlib.Path` throughout and resolve path roots once per script.

## Troubleshooting

### Symptom: missing rows in aggregated CSVs

Likely causes:
- missing raw files for one or more graders,
- parse failures in grade format,
- mixed naming conventions that break joins.

Actions:
- inspect script run logs in `data/`.
- inspect `data/suspicious_records.csv` and parse-error outputs.
- verify story and grade filename alignment.

### Symptom: rankings changed unexpectedly between runs

Likely causes:
- changed model/grader pools,
- partial rerun without consistent input snapshot,
- differences in exclusion/gating application,
- or changes in normalization inputs.

Actions:
- verify run order and run scope against [PIPELINES.md](PIPELINES.md).
- compare source CSV timestamps and row counts.
- confirm whether simple/combined metrics were enabled.

### Symptom: slow or unstable long jobs

Likely causes:
- worker count too high for proxy throughput,
- timeout mismatch,
- rerunning without `--skip-existing`.

Actions:
- lower worker count.
- keep resumable mode enabled.
- run in smaller model subsets and aggregate incrementally.

## Maintenance Checklist

When making substantial benchmark changes:

1. Update this file: [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md).
2. Update command runbook: [PIPELINES.md](PIPELINES.md).
3. Update overview if behavior changed materially: [docs/overview.md](docs/overview.md).
4. Add/adjust integration tests in `tests/`.
5. Rebuild affected reports/charts and verify key outputs in `data/`, `images/`, and `reports/`.
6. Confirm no stale legacy branches remain in docs or scripts.

## Script-Verified Defaults Snapshot

This section records behavior verified directly from the current scripts in this repository (not inferred from older docs). It is intended as a practical reality check when runbooks drift.

### Global path roots

From [project_paths.py](project_paths.py):
- `REPO_ROOT = /mnt/r/writing2`
- `DATA_ROOT = /mnt/r/writing2-data`

Most modern scripts use these constants. A few legacy scripts still hard-code absolute paths directly. Operationally this means the project currently assumes this exact filesystem layout unless those scripts are edited.

### Key default ports and concurrency

Across most runners:
- default proxy port is `8040`
- OpenAI-compatible client is used against `http://localhost:<port>/v1/`
- API key is typically placeholder `"xx"` (required by SDK, often ignored by proxy)
- long timeouts are configured to tolerate slow generations

Inter-LLM comparison non-batch exceptions:
- `run_inter_llm_comparisons.py` defaults to `port=8006`
- `run_inter_llm_comparison_pipeline.py` defaults to `port=8006`
- `run_inter_llm_comparison_batch.py` remains `port=8040` (batch router default)
- `run_inter_llm_comparison_batch.py` uses one port per invocation for all selected evaluators
- self-eval exclusion defaults to `family` policy in comparison runner + pipeline + batch
- Operational latency expectation:
  - Batch router traffic on `8040` is often high-latency and bursty; long silent intervals between progress lines are expected and not by themselves a failure signal.
  - Prefer `8006` for smoke tests, quick validation, small batches (roughly under 200 calls), and Gemini runs.
  - In this environment, `8040` is typically lower-cost (about half-price) relative to `8006`, but it is the batch router and only some providers support true batching there.
  - `8040` is fine for larger production runs where there are many calls and latency matters less than batch pricing.
  - In practice, true `8040` batch support is limited to Gemini, OpenAI, and Anthropic. Other models are forwarded to the regular `8006` path, so using `8040` for them mainly changes routing, not throughput.
  - Gemini is especially slow on `8040` and can take many hours. When turnaround matters, run Gemini in its own `8006` invocation and aggregate once all evaluator passes finish.

Current default worker counts vary by script and are not globally centralized. Examples:
- `create_grades.py`: internal `DEFAULT_WORKERS = 220`
- `run_wc_prompts.py`: `DEFAULT_WORKERS = 100`
- `run_rate_prompts.py`: `DEFAULT_WORKERS = 90`
- `run_similarity_evals.py`: `DEFAULT_WORKERS = 2`
- `run_inter_llm_similarity.py`: `DEFAULT_WORKERS = 50`
- `run_inter_llm_comparisons.py`: `DEFAULT_WORKERS = 20`
- `build_style_fingerprints.py`: `DEFAULT_WORKERS = 300`
- `run_grader_evals.py`: `--workers` default `40`

### Scoring defaults

Current aggregation stack uses:
- power-mean exponent `p = 0.5` for rubric aggregation (`collect_grades_pkg/worker.py`)
- question weights from [question_weights.py](question_weights.py)
- category split effectively 60/40 via per-question weights
- optional combined metric: `0.7 * rubric_score + 0.3 * simple_score`

### Logging and resumability defaults

Most heavy runners support resumability through existing-output checks (`--skip-existing` or skip-by-default behavior). Many scripts emit explicit progress and summary lines, including counts and runtime. `sitecustomize.py` + `script_logging.py` are used broadly for standardized run blocks.

For inter-LLM comparison runs specifically, operators should expect occasional long waits (especially on batch port `8040`) before progress lines are emitted. Health checks should use end-of-run summaries and file-row deltas rather than assuming continuous output cadence.

## Detailed Script Contracts

This section gives script-level contracts by phase: what each script expects, what it writes, and non-obvious behavior that matters for reproducibility.

### Phase A: Category-set construction and rating

This phase converts broad element pools into concrete writing constraints that can be reused across all writer models. The objective is not only to generate many candidate sets, but to ensure the selected sets are coherent enough to be fair and challenging. Reproducibility here depends heavily on deterministic sampling, deduplication rules, and stable mapping between prompt ids and chosen sets.

#### `create_prompts.py`

Purpose: build category-selection prompts from element pools.

Current verified behavior:
- Reads template: `prompts/prompt_select_categories.txt`
- Reads element lists from `elements/*.txt`
- Filters out literal `"None"` during pool loading
- Samples 10 options per category
- Uses deterministic seed `42`
- Default prompt count is `400` (`--count` overrides)
- Writes `prompts_select_categories/prompt_cat_<N>.txt`

#### `choose_cats.py`

Purpose: run chooser models on selection prompts and save chosen sets.

Current verified behavior:
- Input prompt dir: `prompts_select_categories/`
- Output dir: `/mnt/r/writing2-data/chosen_cats/<model>/`
- Default workers: `50`
- Model list is hardcoded in script, with no `--models` flag
- Skips outputs that already exist

#### `create_rate_prompts.py`

Purpose: turn chosen sets into rating prompts plus index mapping.

Current verified behavior:
- Scans `/mnt/r/writing2-data/chosen_cats/<model>/prompt_cat_*.txt`
- Validates each set has exactly 10 expected categories
- Logs invalid sets to `prompts_rate_required_sets/broken_sets.txt`
- Deduplicates by set text per source prompt (keeps first proposer)
- Writes:
  - `prompts_rate_required_sets/prompt_rate_cat_<N>.txt`
  - `prompts_rate_required_sets/prompt_rate_cat_<N>.json`
- Mapping JSON stores both set text and proposer model

#### `run_rate_prompts.py`

Purpose: run rating prompts through rater models.

Current verified behavior:
- Input: `prompts_rate_required_sets/prompt_rate_cat_*.txt`
- Output: `rated_sets/<model>/rating_cat_*.txt`
- Defaults: `port=8040`, `workers=90`
- Optional `--models` overrides hardcoded model list
- Skips existing outputs

#### `collect_ratings.py`

Purpose: aggregate set-level ratings and proposer-level stats.

Current verified behavior:
- Reads mappings from `prompts_rate_required_sets/*.json`
- Reads ratings from `rated_sets/<model>/rating_cat_*.txt`
- Parses lines using index+numeric regex
- Computes:
  - raw mean/std per set
  - z-normalized mean/std per set (per-rater normalization)
  - best raw and best normalized set flags
- Writes:
  - `ratings_summary/sets_ratings.csv`
  - `ratings_summary/proposer_stats.csv`

#### `create_wc_prompts.py`

Purpose: choose winning set per prompt and render writing prompts.

Current verified behavior:
- Input:
  - `ratings_summary/sets_ratings.csv`
  - `prompts/prompt_create_wc.txt`
- Selection logic:
  1. highest `norm_avg`
  2. tie-break by highest `raw_avg`
  3. remaining tie-break by seeded RNG (`seed=42`)
- Writes:
  - `prompts_wc/prompt_wc_<N>.txt`
  - `prompts_wc/selected_sets.json`
  - `prompts_wc/selected_proposer_stats.csv`

### Phase B: Story generation

Story generation is the throughput-critical stage and the main producer of long-lived raw artifacts. Contract clarity here is mostly about path layout and resumability semantics. Operators should be able to restart from partial outputs without introducing duplicate or mislabeled stories.

#### `run_wc_prompts.py`

Purpose: generate stories from WC prompts with per-model word-count injection.

Current verified behavior:
- Inputs:
  - `prompts_wc/prompt_wc_*.txt`
  - optional `data/special_word_counts.csv` for per-model min/max
- Outputs:
  - `/mnt/r/writing2-data/stories_wc/<model>/story_wc_*.txt`
  - `/mnt/r/writing2-data/stories_wc/run_log.csv`
- Defaults:
  - `port=8040`, `workers=100`, temperature `1.0`
  - optional `--models` overrides the in-file `MODELS` list for one invocation
- Non-obvious behavior:
  - Flushes router queues (`openai`, `claude`, `gemini`) before run
  - Falls back to default word range `(600, 800)` if model has no custom row
  - Uses hardcoded `MODELS` list in-script, and current file currently resolves to the final assignment:
    - `MODELS = ['minimax-m2.7']`

### Phase C: Pre-grading and WC diagnostics

This phase is where generation outputs are transformed into evaluator-facing packets. The scripts have to absorb noisy story formatting while preserving canonical identifiers, because downstream graders and parsers assume filename stability. Word-count diagnostics are produced here so quality issues are visible before expensive grading runs.
For new-model onboarding, this phase is also the readiness gate for pairwise comparison: use it to confirm length compliance and formatting cleanliness before spending comparison budget.

#### `prepare_grading.py` and `prepare_grading_pkg/*`

Purpose: convert stories into grading prompt packets and emit word-count diagnostics.

Current verified behavior:
- Modes:
  - default full rubric prompt template
  - `--simple` uses simple single-score template
- Input roots (repo-default mode):
  - stories: `/mnt/r/writing2-data/stories_wc`
  - prompts: `prompts_wc`
- Output roots:
  - full: `/mnt/r/writing2-data/for_grading_wc/<model>/grade_story_*.txt`
  - simple: `/mnt/r/writing2-data/for_grading_simple_wc/<model>/grade_story_*.txt`
- Diagnostic outputs in `data/`:
  - `word_count_details_wc.csv`
  - `model_word_count_summary_wc.csv`
  - `largest_word_count_deviations_wc.csv`
  - `word_count_issues_wc.txt`
  - `unused_stories_for_grading.txt`
- Comparison intake guidance:
  - this phase is QC/prep even when comparison grading is the canonical next step
  - “no outliers” is not sufficient by itself; operators should still inspect `word_count_issues_wc.txt`
- Story extraction behavior:
  - handles malformed or partial `<story>` tags
  - removes inline word-count markers
  - uses model-specific chooser for `llama4-maverick` (first vs last candidate by distance to range)
  - otherwise picks last valid candidate

#### `vis_word_counts_script.py`

Purpose: standalone visualization/QC for word-count outputs.

Current verified behavior:
- Reads CSVs in `data/` with robust parser to tolerate unquoted commas in trailing text fields
- Produces charts in `images/` including distribution, histogram, summary, CI, and outlier visualizations

### Phase D: Grading

Grading scripts materialize the teacher-model view of each story. The most important operational contracts are teacher pool definition, skip/overwrite behavior, and blocked combinations. These choices directly define dataset coverage and therefore must be interpreted as experimental settings, not incidental implementation details.

#### `create_grades.py`

Purpose: run teacher models on prepared grading prompt packets.

Current verified behavior:
- Full mode paths:
  - input: `/mnt/r/writing2-data/for_grading_wc`
  - output: `/mnt/r/writing2-data/graded`
- Simple mode paths:
  - input: `/mnt/r/writing2-data/for_grading_simple_wc`
  - output: `/mnt/r/writing2-data/graded_simple`
- Default workers: `220` (internal constant)
- CLI:
  - `--overwrite`
  - `--students` subset filter
  - `--simple`
- Current hardcoded teacher pool:
  - `gpt-5.1-low`
  - `gemini-3-pro-preview`
  - `qwen3-max`
  - `deepseek-v32-exp`
  - `grok-4-1-fast-reasoning`
  - `kimi-k2-0905`
  - `claude-sonnet-4-5-20250929-0K`
- Current blocklist (`BLOCKED_STORIES_BY_TEACHER`):
  - for `claude-sonnet-4-5-20250929-0K`: `story_wc_240.txt`, `story_wc_124.txt`, `story_wc_317.txt`, `story_wc_0.txt`

### Phase E: Grade aggregation and derived metrics

Aggregation is the canonicalization boundary where loosely formatted grader text becomes strict tables consumed by nearly every later stage. The parser must therefore be defensive about malformed tags while remaining strict enough to surface contract breaks. This phase also handles NA logic and combined-score derivations that materially affect final rankings.

#### `collect_grades.py` + `collect_grades_pkg/*`

Purpose: parse graded outputs and write canonical analysis CSVs.

Current verified behavior:
- Full parse root: `/mnt/r/writing2-data/graded`
- Optional simple parse root: `/mnt/r/writing2-data/graded_simple`
- Full parse:
  - parses per-question tags/comments
  - handles malformed tag variants
  - tracks suspicious and malformed patterns
  - computes per-file power-mean aggregate with `p=0.5`
  - applies per-question weighting from `question_weights.py`
  - rebalances category weights when some questions are missing/NA
- Q9 NA enforcement:
  - cross-checks prompt-required elements
  - force-sets Q9 to NA when required element is `None`
- Simple parse:
  - expects `<overall_simple>...</overall_simple>`
- Combined path:
  - only for overlapping keys
  - formula `0.7*original + 0.3*simple`
- `--no-simple` disables simple+combined.

Major outputs (non-exhaustive):
- `data/teacher_student_file_questions.csv`
- `data/teacher_student_filemeans.csv`
- `data/teacher_student_filemeans_numbered.csv`
- `data/teacher_student_stats.csv`
- `data/student_overall_stats.csv`
- `data/normalized_avg_per_student.csv`
- sentence-length artifacts:
  - `data/sentence_length_story_stats.csv`
  - `data/sentence_length_llm_stats.csv`
  - `data/sentence_length_score_correlation.csv`
  - `reports/sentence_length_report.md`
- optional simple/combined CSV set
- diagnostics: suspicious, malformed, all-tens, disagreement, distributions, per-category/per-question tables

### Phase F: Analysis and leaderboard generation

Once grade tables are canonicalized, analysis scripts build stakeholder-facing outputs. The core requirement in this phase is consistency between tables and rendered artifacts, especially when normalized or weighted variants are available. Scripts here prefer rebuilding derived views when source freshness checks indicate stale intermediates.

#### `analysisb.py`

Purpose: orchestrate broad chart/report generation from collected data.

Current verified behavior:
- CLI flag:
  - `--include-weighted-ranking` (otherwise weighted ranking paths are skipped)
- Generates multiple outputs by calling chart and report modules
- Attempts combined and question-weighted chart variants when prerequisites exist
- Also regenerates sentence-length charts:
  - `images/sentence_length_mean_by_llm.png`
  - `images/sentence_length_vs_score.png`

#### `leaderboard.py`

Purpose: standard and normalized leaderboards.

Current verified behavior:
- `--mode standard`:
  - input default: `data/student_overall_stats.csv`
  - output markdown: `reports/leaderboard.md`
- default normalized mode:
  - input default: `data/normalized_avg_per_student.csv`
  - output markdown: `reports/normalized_leaderboard.md`
  - output png: `images/normalized_leaderboard.png`
- If normalized CSV is missing or older than `teacher_student_filemeans_numbered.csv`, it is rebuilt.
- Suppressed models are removed from chart rendering but still included in markdown tables.

### Phase G: Comment and summary synthesis

This phase extracts qualitative evidence from grader comments and condenses it into structured narratives per model. It is intentionally separated from numeric ranking so interpretability workflows can evolve without destabilizing score computation. Filename normalization is a key concern because comments and summaries are merged across multiple model naming conventions.

#### `collect_comments_1to6.py`

Purpose: extract Q1–Q8 comment evidence from grader outputs.

Current verified behavior:
- Scans `/mnt/r/writing2-data/graded/<grader>/<llm>/grade_story_*.txt`
- Emits `comments_by_llm_1to8/q1..q8/<short-model>.txt`
- Parses `<question>/<grade>/<comment>` blocks for questions `1..8`

#### `create_summary_prompts.py`

Purpose: build per-question summarization prompts.

Current verified behavior:
- Input: `comments_by_llm_1to8/q1..q8/*.txt`
- Output: `/mnt/r/writing2-data/for_summarizing/q1..q8/<short-model>.txt`
- Embeds verbatim rubric section for each question from `prompts/prompt_grading.txt`
- Normalizes model filename mapping using multiple fallbacks (hyphen variants, decimal underscore conversion)

#### `generate_summary_responses.py`

Purpose: execute per-question summarization prompts.

Current verified behavior:
- Input root: `/mnt/r/writing2-data/for_summarizing`
- Output root: `summaries/`
- Uses process pool with per-process client
- Current script main hardcodes:
  - model: `gemini-3-pro-preview`
  - workers: `100`
- This script currently has no CLI for model/worker override

#### `create_general_summary_prompts.py`

Purpose: fuse eight per-question summaries into one per-model general-summary prompt.

Current verified behavior:
- Input: `summaries/q1..q8/*.txt`
- Output: `for_general_summary/<short-model>.txt`
- Requires all eight question summaries for a model; skips incomplete sets

#### `generate_general_summary_responses.py`

Purpose: generate final per-model general summaries.

Current verified behavior:
- Input: `for_general_summary/*.txt`
- Output: `general_summaries/*.txt`
- CLI:
  - `-m/--model` (default `gpt-5.1-low`)
  - `-p/--port` (default `8040`)
  - `-w/--workers` (default `60`)
  - `--overwrite`

### Phase H: Pairwise similarity and diversity

Pairwise similarity scripts estimate intra-model variation by comparing story pairs sampled within each LLM. The resulting diversity statistics are complementary to rubric scores: they answer whether a model can vary outputs, not whether any single output is high quality. Task sampling parameters therefore function as methodological settings and should be treated as part of the contract.

#### `build_similarity_tasks.py`

Purpose: build within-LLM story-pair evaluation tasks.

Current verified behavior:
- Input stories: `/mnt/r/writing2-data/stories_wc/<llm>/story_*.txt`
- Prompt context: `prompts_wc/prompt_*.txt`
- Output: `data/story_similarity_tasks.csv`
- Defaults:
  - `K_PAIRS = 50`
  - `SEED = 20250829`
  - `MAX_PER_STORY = 2`
- Adds `overlap_frac` covariate based on exact required-element overlap.

#### `run_similarity_evals.py`

Purpose: run similarity evaluators on within-LLM story pairs.

Current verified behavior:
- Inputs:
  - `data/story_similarity_tasks.csv`
  - template: `prompts/prompt_similarity.txt`
- Outputs:
  - raw: `story_similarity_raw/<evaluator>/<llm>/<story_a>__<story_b>.txt`
  - parsed rows: `data/story_similarity_scores.csv`
- Defaults:
  - evaluators: `gpt-5-medium,qwen3-235b-a22b-thinking-2507`
  - workers: `2`
- Requires at least two evaluators.

#### `aggregate_similarity.py`

Purpose: convert pairwise similarity into LLM-level diversity stats and charts.

Current verified behavior:
- Input: `data/story_similarity_scores.csv`
- Outputs:
  - `data/llm_diversity_stats.csv`
  - `reports/diversity_leaderboard.md`
  - `images/llm_diversity_bar_start0.png`
  - `images/llm_diversity_bar_zoomed.png`
- Formula: `diversity = 10 - mean(similarity_overall)` after evaluator-averaging per pair.

### Phase I: Cross-LLM similarity (A vs B)

Cross-LLM similarity extends pairwise analysis from within-model variation to between-model closeness. The workflow depends on matched indexing and append-safe task logs so repeated sweeps can be resumed and deduplicated. Aggregation outputs are designed to support both global matrices and focused slices.

#### `build_inter_llm_similarity_prompts.py`

Purpose: build matched-index cross-LLM similarity prompts.

Current verified behavior:
- Input stories from two LLM directories under `/mnt/r/writing2-data/stories_wc`
- Input template: `prompts/prompt_similarity.txt`
- Output prompts: `/mnt/r/writing2-data/inter_llm_similarity_prompts/<A>__vs__<B>/pair_####.txt`
- Appends tasks to `data/inter_llm_similarity_tasks.csv`
- Supports `--n`, `--sample`, `--seed`

#### `run_inter_llm_similarity.py`

Purpose: evaluate cross-LLM similarity prompt packets.

Current verified behavior:
- Defaults:
  - evaluator: `gpt-5.2-low`
  - workers: `50`
- Input tasks: `data/inter_llm_similarity_tasks.csv`
- Raw output: `/mnt/r/writing2-data/inter_llm_similarity_raw/<evaluator>/<A>__vs__<B>/pair_####.txt`
- Parsed append output: `data/inter_llm_similarity_scores.csv`
- Supports `--skip-existing`

#### `run_inter_llm_similarity_sweep.py`

Purpose: automate `target vs everyone` and full all-pairs cross-LLM similarity runs.

Current verified behavior:
- Discovers candidate LLMs from `/mnt/r/writing2-data/stories_wc`
- Supports `--all-pairs`, `--only`, `--exclude`, `--limit`
- Runs prompt builder + evaluator pair runner per comparison
- Deduplicates `data/inter_llm_similarity_tasks.csv`
- Optional `--skip-aggregate` to skip final aggregate rebuild

#### `aggregate_inter_llm_similarity.py`

Purpose: aggregate cross-LLM similarity scores into pair stats, matrix, and leaderboard.

Current verified behavior:
- Input: `data/inter_llm_similarity_scores.csv`
- Outputs:
  - `data/inter_llm_pair_stats.csv`
  - `data/inter_llm_similarity_matrix.csv`
  - `reports/inter_llm_similarity_leaderboard.md`
  - `images/inter_llm_similarity_heatmap.png`
- Supports `--focus-llms` for filtered leaderboard/heatmap views while still writing full CSV stats.

### Phase J: Cross-LLM comparison (A vs B quality judgments)

This phase performs explicit head-to-head quality judgments instead of pure similarity scoring. Deterministic side randomization and strict machine tags are required so evaluator responses can be parsed without ambiguity. Because these comparisons feed margin-primary global ratings (with BT as reference), parser strictness and index integrity are critical.

#### `build_inter_llm_comparison_prompts.py`

Purpose: build A-vs-B comparison prompts with rubric context and deterministic side randomization.

Current verified behavior:
- Inputs:
  - stories: `/mnt/r/writing2-data/stories_wc/<llm>/story_wc_####.txt`
  - prompt template: `prompts/prompt_inter_llm_comparison.txt`
  - rubric summary: `prompts/prompt_rubric_summary.txt`
- Outputs:
  - prompts (default template): `/mnt/r/writing2-data/inter_llm_comparison_prompts/<A>__vs__<B>/pair_####.txt`
  - prompts (non-default template): `/mnt/r/writing2-data/inter_llm_comparison_prompts/<template_id>/<A>__vs__<B>/pair_####.txt`
  - tasks index: `data/inter_llm_comparison_tasks.csv`
- Includes side mapping columns:
  - `side_a_llm`, `side_b_llm`, `side_swapped`
- Records `template_id` per task row.
- Deduplicates tasks CSV by `(llm_a, llm_b, template_id, story_idx)` keeping newest row.
- Prints explicit build summary with before/after prompt counts, before/after task rows (global and pair-level), dedup-removed row count, and runtime.
- Supports guaranteed net-new selection:
  - `--only-new` excludes indices already present for that `(llm_a, llm_b, template_id)` in `data/inter_llm_comparison_tasks.csv`
  - `--require-exact-n` fails fast when fewer than `--n` eligible indices exist
- Supports prompt-template experiments:
  - `--template-path` to choose an alternate comparison template file
  - `--template-id` to isolate outputs and task rows for that template

#### `run_inter_llm_comparisons.py`

Purpose: run evaluator on A-vs-B comparison prompts and parse strict machine tags.

Current verified behavior:
- Defaults:
  - evaluators: versioned roster from `inter_llm_comparison_full_evaluators.txt` (when neither `--evaluator` nor `--evaluators` is provided)
  - port: `8006` (non-batch default; pass `-p 8040` for batch router)
  - temperature: `1.0`
  - workers: `20`
  - self-eval policy: `family` (blocks exact self-eval and same-family evaluator/writer matchups)
- Evaluator selection:
  - `--evaluator <model>` runs one evaluator
  - `--evaluators <m1,m2,...>` runs each prompt once per evaluator in one invocation
  - `--evaluators-per-pair <N>` deterministically selects up to `N` eligible evaluators per `(llm_a, llm_b, template_id)` after self-eval filtering
  - `--evaluator-selection-seed <int>` changes that stable per-pair evaluator subset
  - preferred screening/cost-control mode is “full evaluator roster + `--evaluators-per-pair`” rather than a frozen small global evaluator list
- Self-eval policy control:
  - `--self-eval-policy family|exact|off`
  - `family` uses the server-backed `model_info.category_map` when available, with prefix fallback heuristics
- Outputs:
  - raw (default template): `/mnt/r/writing2-data/inter_llm_comparison_raw/<evaluator>/<A>__vs__<B>/pair_####.txt`
  - raw (non-default template): `/mnt/r/writing2-data/inter_llm_comparison_raw/<evaluator>/<template_id>/<A>__vs__<B>/pair_####.txt`
  - index CSV: `data/inter_llm_comparison_index.csv`
  - strict score CSV: `data/inter_llm_comparison_scores.csv`
- Skip behavior:
  - skips existing raw outputs by default
  - `--overwrite` forces rerun
- Template behavior:
  - `--template-id` filters tasks for one template and tags emitted index/score rows with that ID
  - legacy rows without `template_id` are treated as `default`
- Prints periodic progress (`[PROGRESS] done/total (%)`) and final pair-level before/after row deltas for index and score CSVs.
- Requires machine tags:
  - `<winner>`, `<margin>`
- Preferred continuous tag:
  - `<signed_margin>` (`-10.0..10.0`, positive = Story A better, negative = Story B better)
- Optional machine tag:
  - `<confidence>` (defaults to `0.0` when absent)
- Optional diagnostics tag:
  - `<flags>` (when present, parser validates known keys)
- Also validates analysis tags for downstream summary quality checks.

#### `aggregate_inter_llm_comparison_scores.py`

Purpose: aggregate strict A-vs-B score outputs, compute margin-primary global ratings, and emit evaluator diagnostics.

Current verified behavior:
- Input: `data/inter_llm_comparison_scores.csv`
- Template scope:
  - default aggregation scope is `--template-id default`
  - `--all-templates` aggregates all template IDs together
- Outputs:
  - `data/inter_llm_comparison_pair_story.csv`
  - `data/inter_llm_comparison_pair_stats.csv`
  - `data/inter_llm_comparison_bt_ratings.csv`
  - `data/inter_llm_comparison_rating_diagnostics.csv`
  - `data/inter_llm_comparison_tie_sensitivity.csv`
  - `data/inter_llm_comparison_evaluator_diagnostics.csv`
  - `data/inter_llm_comparison_evaluator_agreement.csv`
  - `data/inter_llm_comparison_side_bias_corrections.csv`
  - `reports/inter_llm_comparison_score_leaderboard.md`
- Defaults:
  - bootstrap samples: `300`
  - bootstrap seed: `12345`
  - evaluator resampling in bootstrap: enabled by default (`--bootstrap-resample-evaluators`)
  - side-bias correction: enabled by default (`--side-bias-correction`)
- Rating behavior:
  - primary ranking is Thurstone-style (least-squares on signed margins)
  - this Thurstone ranking is the canonical public quality rating
  - BT columns are retained as reference, with tie-aware outcomes derived from signed margins
  - tie threshold is configurable via `--tie-epsilon` (default `0.5`)
  - bootstrap uncertainty is hierarchical by default (story resampling + evaluator resampling within story)
  - legacy story-only bootstrap is available via `--no-bootstrap-resample-evaluators`
  - evaluator side-A bias correction on signed margins is applied by default; disable via `--no-side-bias-correction`
  - tie sensitivity grid is configurable via `--tie-sensitivity-epsilons` (default `0.25,0.5,1.0`)
  - rating diagnostics include Thurstone-vs-BT rank correlation, sigma bootstrap stability, and triad-cycle transitivity metrics
  - pair-stat SEM/CI calculations use sample variance (`n-1`) for uncertainty estimation

#### `plot_inter_llm_comparison_charts.py`

Purpose: render large visual artifacts from aggregated pairwise-comparison ratings/stats.

Current verified behavior:
- Inputs:
  - `data/inter_llm_comparison_bt_ratings.csv`
  - `data/inter_llm_comparison_pair_stats.csv`
  - optional diagnostics subtitle source: `data/inter_llm_comparison_rating_diagnostics.csv`
- Outputs:
  - `images/inter_llm_comparison_thurstone_ratings.png`
  - `images/inter_llm_comparison_bt_ratings.png`
  - `images/inter_llm_comparison_pair_margin_heatmap.png`
- Chart behavior:
  - rating charts use per-model shaded CI rectangles (95% CI) behind bars
  - model display names and family colors follow the server-backed `model_info.py` adapter
  - rating charts embed small model-brand logos from `/mnt/r/benchmark_utils` when the shared brand registry resolves a logo for the plotted model/category
  - emits large Plotly exports suitable for report/inspection workflows
  - supports `--include-suppressed` to include models otherwise hidden by chart suppression policy

#### `run_inter_llm_comparison_pipeline.py`

Purpose: one-command orchestrator for build → compare → aggregate → summarize flow.

Current verified behavior:
- Supports:
  - `--pair-evaluator` (single evaluator)
  - `--pair-evaluators` (comma-separated evaluator list)
  - `--pair-evaluators-per-pair <N>` (deterministically cap each pair to `N` eligible evaluators after self-eval filtering)
  - `--evaluator-selection-seed <int>` (changes the stable per-pair evaluator subset used by the cap)
  - `--temperature` (forwarded to pairwise runner; default `1.0`)
  - `--self-eval-policy family|exact|off` (default `family`, forwarded to pairwise runner)
  - `--template-id` (comparison-template isolation key)
  - `--template-path` (alternate pairwise comparison template file)
  - default port `8006` (non-batch), configurable via `-p/--port`
  - `--only-new`, `--require-exact-n` (forwarded to prompt builder)
  - `--bootstrap-resample-evaluators` / `--no-bootstrap-resample-evaluators` (forwarded to aggregate step)
  - `--side-bias-correction` / `--no-side-bias-correction` (forwarded to aggregate step)
  - `--skip-score-aggregate`
  - `--overwrite-compare`
  - `--overwrite-summary`
  - `--dry-run`
- Prints explicit `[STEP x/4]` stage markers and a final before/after delta block for prompt/raw/task/index/score counts plus summary existence checks.
- Protocol rule:
  - when evaluator roster or other benchmark-critical comparison policy changes materially, use a new `template_id` rather than mixing runs into an existing scope

#### `run_inter_llm_comparison_batch.py`

Purpose: simple no-subcommand manager for roster-driven inter-LLM maintenance.

Current verified behavior:
- Uses explicit active roster file: `data/inter_llm_active_models.txt`
- Full-run policy files can be stored and versioned at repository root:
  - evaluator set: `inter_llm_comparison_full_evaluators.txt`
  - story-model exclusions: `inter_llm_comparison_story_excluded_models.txt`
- Canonical intake for newly generated models is comparison-first: QC the stories, refresh the active roster, run a pilot, then expand coverage.
- Supports action flags:
  - `--init-roster-from-stories` (create roster from `/mnt/r/writing2-data/stories_wc/*`)
  - `--exclude-models` / `--exclude-models-file` (filter models from roster/run scope)
  - `--run-all` (all unordered active pairs)
  - `--pairs-file <path>` (exact unordered pair list; one comma- or whitespace-separated pair per non-comment line)
  - `--added-models` (run `new_model x active_model` only)
  - `--drop-models` (remove model rows from tasks/index/scores)
  - `--repair-stale-paths` (rewrite legacy comparison CSV paths, backfill task side columns, drop missing-path rows)
- Roster/exclusion policy:
  - new story directories are not automatically included in `--run-all`; rerun `--init-roster-from-stories` after new generations land
  - keep long-term story-model policy in `inter_llm_comparison_story_excluded_models.txt`
  - keep current run scope aligned by updating the active roster file too
- Partial-coverage policy:
  - incomplete models may still be compared when overlap supports the requested `--n`
  - treat this as an explicit policy exception and note the incompleteness later in reporting
- Recommended expansion policy:
  - anchor pilot first
  - optional new-vs-new pass second
  - broader/canonical expansion after the pilot identifies which models are worth deeper coverage
- Supports incremental net-new expansions by passing through builder controls:
  - `--only-new`, `--require-exact-n`
- Supports compare-only resume mode:
  - `--compare-only` skips build stage and runs compare against existing tasks only
  - filters selected pairs to those with tasks for `--template-id`
  - `--n 0` is accepted only with `--compare-only`
- Supports pair-parallel compare execution with safe CSV isolation/merge:
  - `--pair-workers` (parallel pairs)
  - compare stage writes per-(pair,evaluator) `index/scores` shard CSVs and merges back into canonical CSVs
  - prevents shared-write races on `data/inter_llm_comparison_index.csv` and `data/inter_llm_comparison_scores.csv`
  - `--compare-shard-root` overrides shard output directory
  - `--defer-shard-merge` keeps shard outputs without canonical merge in that invocation
  - `--merge-shards-from <dir1,dir2,...>` performs explicit shard-to-canonical merge (for safe multi-process runs)
- Supports evaluator set selection:
  - `--evaluator <model>` for single-evaluator mode
  - `--evaluators <m1,m2,...>` for multi-evaluator mode in one invocation
  - `--evaluators-file <path>` for file-based evaluator lists (one per line or comma-separated lines)
  - `--evaluators-per-pair <N>` to deterministically cap each pair to `N` eligible evaluators after self-eval filtering
  - `--evaluator-selection-seed <int>` to change that stable per-pair evaluator subset
- `--added-models` does not compare the added models against each other in one invocation; it only schedules `added x active`.
- Comparison evaluation temperature is configurable with `--temperature` (default `1.0`).
- Supports global evaluator concurrency caps for parallel pair runs:
  - `--max-workers-per-llm`
  - batch runner auto-adjusts effective pair concurrency and per-pair workers to keep total evaluator workers at or below the cap
  - effective in-flight request fan-out is driven by the effective `pair-workers * workers` combination, not by port choice alone
- Supports aggregate bootstrap mode control:
  - `--bootstrap-resample-evaluators` / `--no-bootstrap-resample-evaluators`
- Supports aggregate side-bias correction control:
  - `--side-bias-correction` / `--no-side-bias-correction`
- Forwards self-eval filtering policy to pairwise runner:
  - `--self-eval-policy family|exact|off` (default `family`)
- Supports adaptive coverage expansion:
  - `--adaptive-inconclusive` selects pairs where CI around mean signed margin crosses zero
  - prioritization uses `priority = ci95_signed_margin_left - abs(mean_signed_margin_left)`
  - pair limits via `--adaptive-top-k` and `--adaptive-max-story-pairs`
  - `--adaptive-disagreement` selects pairs with high cross-evaluator disagreement
  - disagreement prioritization uses `priority = mean_pairwise_abs_margin_diff * sqrt(overlap_story_pairs)`
  - disagreement limits via `--adaptive-disagreement-top-k`, `--adaptive-disagreement-min-priority`,
    `--adaptive-disagreement-min-overlap-story-pairs`, and `--adaptive-disagreement-max-story-pairs`
  - adaptive mode enforces net-new pair expansion behavior (`--only-new`)
- Adaptive and manual incremental pair selection should weight leaderboard impact toward the top of the ranking. Under a constrained call budget, prefer missing direct comparisons and inconclusive pairs involving high-ranked models over uniformly completing every remaining lower-table pair. Use `--pairs-file` for exact high-value manual selections so temporary rosters do not create unintended extra comparisons.
- After runs and/or drops, can rebuild rating artifacts via aggregate step (default on, `--no-aggregate` to skip).
- When compatible legacy rows are intentionally promoted into a current canonical template scope, keep their original prompt/raw paths as provenance. The aggregate leaderboard emits a scope note when score rows for a template point outside that template's prompt/raw directory.
- Optional cleanup with `--prune-dropped-artifacts` removes dropped pair prompt/raw/summary files.
- Template behavior:
  - supports `--template-id` and `--template-path` for isolated prompt-template experiments
  - repair mode backfills missing `template_id` as `default` in existing comparison tables
  - evaluator-roster changes such as replacing `gpt-5.2-low` with `gpt-5.4-low` should use a new versioned evaluator file and a new `template_id`

### Phase K: Poor-writing diagnostics

Poor-writing diagnostics intentionally focus on negative evidence density rather than average score behavior. The stack moves from per-story extraction to per-model thematic synthesis, preserving traceability from summaries back to concrete examples. Mixed repo-local and data-root output paths are part of the current contract and must be handled carefully in runbooks.

#### `build_poor_writing_prompts.py`

Purpose: build one analyzer prompt per story for poor-writing extraction.

Current verified behavior:
- Inputs:
  - stories: `/mnt/r/writing2-data/stories_wc/<llm>/story_*.txt`
  - template: `prompt_poor_writing_analysis.txt` (root or `prompts/`)
- Outputs:
  - `/mnt/r/writing2-data/for_poor_writing/<llm>/analyze_story_*.txt`
- Supports:
  - `--llms`
  - `--limit`
- Skips existing prompt outputs.

#### `run_poor_writing_analysis.py`

Purpose: run analyzer model over poor-writing prompt packets.

Current verified behavior:
- Default analyzer: `gpt-5-low`
- Output raw: `/mnt/r/writing2-data/poor_writing_raw/<analyzer>/<student>/<story>.txt`
- Log CSV: `data/poor_writing_run_log.csv`
- Supports `--students`, `--workers`, `--skip-existing`

#### `aggregate_poor_writing.py`

Purpose: parse poor-writing analyzer outputs and emit structured CSVs.

Current verified behavior:
- Input raw root: `/mnt/r/writing2-data/poor_writing_raw`
- Outputs:
  - `data/poor_writing_examples.csv` (sorted severe-first)
  - `data/poor_writing_examples__<llm>.csv`
  - `data/poor_writing_story_summary.csv`
  - `data/poor_writing_parse_errors.csv`

#### `build_poor_writing_theme_prompts.py`

Purpose: create per-LLM thematic-analysis prompts from high-severity examples.

Current verified behavior:
- Input: `data/poor_writing_examples__<llm>.csv`
- Output: `/mnt/r/writing2-data/for_poor_writing_themes/<llm>.txt`
- Defaults:
  - `--min-severity 7.0`
  - `--max-examples 400`

#### `run_poor_writing_thematic_analysis.py`

Purpose: run thematic profiling on per-LLM theme prompts.

Current verified behavior:
- Input prompts: `/mnt/r/writing2-data/for_poor_writing_themes/<llm>.txt`
- Raw outputs: `poor_writing_themes_raw/<evaluator>/<llm>.txt` (repo-local)
- Log CSV: `data/poor_writing_theme_run_log.csv`
- Defaults:
  - evaluator `gpt-5-medium`
  - workers `16`

#### `run_poor_writing_theme_synthesis.py`

Purpose: produce natural-language synthesis from theme profile + examples.

Current verified behavior:
- Inputs:
  - `poor_writing_themes_raw/<evaluator>/<llm>.txt`
  - `data/poor_writing_examples__<llm>.csv`
- Outputs:
  - `poor_writing_theme_summaries/<evaluator>/<llm>.txt`
  - `data/poor_writing_theme_synthesis_log.csv`
- Defaults:
  - evaluator `gpt-5-medium`
  - min severity `7.0`
  - max examples `120`

#### `run_poor_writing_easy20.py`

Purpose: produce easy-to-understand top-N showcase with concise explanations.

Current verified behavior:
- Input: `data/poor_writing_examples__<llm>.csv`
- Outputs:
  - `poor_writing_easy20/<evaluator>/<llm>.txt`
  - `data/poor_writing_easy20_log.csv`
- Defaults:
  - evaluator `gpt-5-medium`
  - `--n-items 30`
  - min severity `7.0`
  - max examples `300`

### Phase L: Style fingerprint and diversity

Style-fingerprint scripts model writing variation as a mixed-type feature geometry problem. They generate axis-level features first, then compute diversity metrics from those features, allowing richer diagnostics than raw pairwise similarity alone. Version-pinned outputs are included so metric interpretations remain tied to a specific axis configuration.

#### `build_style_fingerprints.py`

Purpose: generate mixed-type style fingerprints per story using axis spec JSON.

Current verified behavior:
- Inputs:
  - stories from `/mnt/r/writing2-data/stories_wc`
  - prompts from `prompts_wc`
  - template `prompts/prompt_style_fingerprint.txt`
  - axis config `style_axes.json`
- Outputs:
  - raw: `style_fingerprint_raw/<evaluator>/<llm>/<story>.txt`
  - canonical csv: `data/style_fingerprints.csv`
  - version-pinned csv: `data/style_fingerprints_v<axes_version>.csv`
- Defaults:
  - evaluator list: `gpt-5.1-low`
  - workers: `300`
- Tolerant parsing behavior:
  - fills sentinels on parse mismatch
  - marks `format_error` when parsing is incomplete/invalid

#### `compute_style_diversity.py`

Purpose: compute per-LLM diversity metrics from style fingerprints.

Current verified behavior:
- Input:
  - `data/style_fingerprints.csv`
  - `style_axes.json`
- Outputs:
  - `data/story_diversity_metrics_by_evaluator.csv`
  - `data/story_diversity_metrics.csv`
  - `data/style_knn.csv`
- Includes both:
  - legacy Euclidean/z-score metrics
  - weighted Gower mixed-type metrics
- `diversity_score` is currently weighted Gower mean pairwise distance in `[0,1]`.

#### `style_diversity_leaderboard.py`

Purpose: render style-diversity markdown leaderboard and chart.

Current verified behavior:
- Input: `data/story_diversity_metrics.csv` (`diversity_score` required)
- Outputs:
  - `reports/diversity_leaderboard.md`
  - `images/diversity_leaderboard.png`

### Phase M: Grader evaluation and weighted reporting

This phase evaluates the evaluators. It estimates grader reliability, converts those signals into weights, and then recomputes weighted student summaries. The contracts here matter because weighted outputs are often compared against unweighted baselines; schema mismatches or partial data can easily invalidate that comparison.

#### `grader_eval_select_stories.py`

Purpose: choose evaluation subset graded by all graders.

Current verified behavior:
- Inputs:
  - `data/teacher_student_stats.csv`
  - `data/teacher_student_file_questions.csv`
- Eligibility:
  - requires each grader has >=18 questions for `(student, file)`
  - requires file graded by all graders
- Samples up to `k=60` with seed `20250829`
- Output: `data/grader_eval_story_set.csv`

#### `build_grader_eval_tasks.py`

Purpose: build cross product of selected stories × graders × evaluators.

Current verified behavior:
- Input:
  - `data/grader_eval_story_set.csv`
  - `data/teacher_student_stats.csv`
- Optional `--evaluators-file`; otherwise evaluators default to grader list (`E=G`)
- Output: `data/grader_evaluation_tasks.csv`

#### `run_grader_evals.py`

Purpose: run evaluator models to assess grader quality.

Current verified behavior:
- Input:
  - `data/grader_evaluation_tasks.csv`
  - templates `prompt_evaluate_grader.txt`, `prompt_grading.txt`
  - stories and graded files from `/mnt/r/writing2-data`
- Outputs:
  - raw: `/mnt/r/writing2-data/grader_eval_raw/<evaluator>/<grader>/<student>__<graded_file>.txt`
  - parsed rows: `data/grader_evaluations_raw.csv`
- Defaults:
  - workers: `40`
  - temperature: `1.0`
- Parses expanded expert metric set plus gate flags and lens/closure tags.

#### `aggregate_grader_evals.py`

Purpose: convert grader-eval rows into grader weights and weighted student means.

Current verified behavior:
- Inputs:
  - `data/grader_evaluations_raw.csv`
  - `data/teacher_student_stats.csv`
- Outputs:
  - `data/grader_weights.csv`
  - `data/student_overall_stats_weighted.csv`
- Supports both BASIC and RICH schemas.
- Uses robust CSV reader for partially written lines and trailing-comma issues.

#### `weighted_reports.py`

Purpose: produce weighted-vs-unweighted comparison CSV artifacts.

Current verified behavior:
- Requires:
  - `data/grader_weights.csv`
  - `data/student_overall_stats.csv`
  - `data/student_overall_stats_weighted.csv`
  - `data/teacher_student_category_stats.csv`
  - `data/question_by_student.csv` with explicit `sem` values for question-weighted rollups
- Writes:
  - `data/student_overall_weighted_vs_unweighted.csv`
  - `data/question_by_student_weighted.csv`
  - `data/student_overall_stats_qweighted.csv`
- Failure mode is strict: missing question weights, missing `sem` columns, unknown question IDs, or malformed numeric fields now raise immediately instead of silently substituting placeholder values.

## Data Contracts and CSV Schemas

This section highlights files that act as cross-stage contracts. These should be treated as interface surfaces; changing schemas here requires coordinated changes across multiple scripts and tests.

In practice, these CSVs function like API boundaries for the repository. Most downstream scripts assume column presence and semantic meaning, not just file existence. A small producer-side schema tweak can propagate into chart errors, leaderboard drift, or silent row drops if consumers are not updated in lockstep.

### Primary contracts

- `data/teacher_student_file_questions.csv`
  - canonical per-question score/comment table
  - consumed by multiple analytics and QC scripts
- `data/teacher_student_filemeans_numbered.csv`
  - canonical per-file aggregate with story index
  - used for normalized leaderboard regeneration and downstream scoring
- `data/student_overall_stats.csv`
  - raw overall summary by student model
- `data/normalized_avg_per_student.csv`
  - normalized counterpart rebuilt from filemeans when stale/missing
- `data/story_similarity_scores.csv`
  - per-pair evaluator outputs for within-LLM diversity pipeline
- `data/inter_llm_similarity_scores.csv`
  - per-pair evaluator outputs for cross-LLM similarity pipeline
- `data/inter_llm_comparison_scores.csv`
  - strict machine-tag output for A-vs-B comparison aggregation
- `data/style_fingerprints.csv`
  - canonical style-fingerprint table used by style diversity computation

### Rule of thumb for schema updates

When changing one of these files:
1. update producer script
2. update all known consumers
3. add or refresh integration tests in `tests/`
4. document the change in [PIPELINES.md](PIPELINES.md) and this file

## Current Hardcoded Model Pools

Several scripts still use in-file hardcoded model lists, while others accept CLI overrides. This matters for reproducibility and for explaining why a run processed fewer models than expected.

When debugging coverage differences between runs, check hardcoded pools before assuming data loss. In this repository, run scope is sometimes constrained intentionally in-script for operational batches, so what looks like a missing-model issue may actually be current code behavior.

### Scripts with hardcoded pools (current code)

- `choose_cats.py`
- `run_rate_prompts.py` (can override with `--models`)
- `run_wc_prompts.py` (can override with `--models`; final in-file assignment currently sets `MODELS = ['minimax-m2.7']`)
- `create_grades.py` (teacher pool hardcoded)
- `generate_summary_responses.py` (main currently hardcoded to `gemini-3-pro-preview`)

### Scripts with strong CLI control

- `run_similarity_evals.py` (`--evaluators`, `--workers`, `--skip-existing`)
- `run_inter_llm_similarity.py` (`--evaluator`, `--workers`, `--skip-existing`)
- `run_inter_llm_similarity_sweep.py` (`--target` or `--all-pairs`, plus `--only`, `--exclude`, `--limit`, and evaluator settings)
- `run_inter_llm_comparisons.py` (`--evaluator` or `--evaluators`, `--workers`, `--self-eval-policy`, `--overwrite`)
- `run_inter_llm_comparison_pipeline.py` (full pipeline parameterization)
- `generate_general_summary_responses.py` (`--model`, `--workers`, `--overwrite`)

## Verification Log

Verification timestamp: `2026-03-02` (local workspace pass).

Checked directly against script sources:
- generation path scripts
- grading and aggregation scripts
- similarity/diversity stacks
- inter-LLM similarity and comparison stacks
- poor-writing analysis stack
- style-fingerprint stack
- grader-evaluation and weighted-report stack
- leaderboard and analysis orchestrators

Practical implication:
- This document now intentionally reflects current implementation details, including non-obvious defaults and hardcoded pools, rather than only intended architecture.
- If scripts are edited later, this section should be treated as stale until re-verified.

Verification in this document is snapshot-based. It captures what the scripts do at the recorded date, not what they were intended to do historically. Treat it as an implementation contract tied to this code revision.

## Related Documents

- [README.md](README.md): narrative results and benchmark interpretation.
- [PIPELINES.md](PIPELINES.md): runnable command cookbook.
- [docs/overview.md](docs/overview.md): short orientation.
- [temp/API.md](temp/API.md): generated API-level script documentation.

This document is the high-level technical source of truth for architecture and operational intent. The runbook remains the source of truth for exact commands.
