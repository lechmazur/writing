# LLM Creative Writing Benchmark — Pipelines Runbook

This runbook captures all major pipelines in this repo with concise descriptions and exact commands to run. Commands assume Linux (WSL) and a local OpenAI‑compatible proxy at `http://localhost:8040` unless noted.

> Paths are relative to `/mnt/r/writing2`. Run everything from the repo root and export the repo to `PYTHONPATH` first.
> For architecture/rationale and data-contract context, see `PROJECT_DOCUMENTATION.md` (refreshed 2026-03-02).

```bash
cd /mnt/r/writing2
export PYTHONPATH="$PWD:$PYTHONPATH"
```

Compatibility note
- All generated data files are written under `data/` (and images under `images/`). Root-level mirroring has been removed to keep the repo root clean and avoid ambiguity.
- Router-backed scripts that write `.txt` artifacts now also write adjacent `.json` sidecars for new calls. Those sidecars carry the `router_request_id`, provider metadata, usage summary, final outcome classification, and any fetched request-trace excerpt.
- The public quality leaderboard is now the inter-LLM comparison Thurstone rating. Absolute 0-10 rubric ratings and their old README-linked charts are archived under `archive/absolute_ratings_v4_2026_04_19/` and should not be used as the main ranking going forward.

---

## Environment
- Proxy: OpenAI-compatible router on `localhost:8040`
- Tuning: Many scripts accept `--workers`; set based on CPU and proxy capacity
- Resuming: Prefer `--skip-existing` flags to resume large jobs safely
- Diagnosis: use port `8006` for smoke/debug runs where fast feedback and `/request_trace/<id>` inspection matter most; keep `8040` for larger production runs once the client is metadata-aware.
- Latency expectations:
  - Non-batch/smoke runs should typically use port `8006` for faster feedback.
  - Batch router runs on port `8040` can be much slower and bursty; quiet periods of 30-120s (or more) between progress lines are normal under load.
  - In our setup, batch `8040` is usually cheaper (about half price) than `8006`, but only some providers support true batch execution there.
  - Use `8006` by default for smaller batches, roughly under 200 calls, where turnaround matters more than batch pricing.
  - Use `8040` for larger production runs where there are many calls and slower batch execution is acceptable.
  - In practice, true `8040` batch support is limited to Gemini, OpenAI, and Anthropic. Other models are forwarded to the regular `8006` path.
  - Gemini is especially slow on `8040` and can take many hours; prefer `8006` for Gemini unless you are deliberately optimizing for batch pricing over turnaround.
  - `run_inter_llm_comparison_batch.py` uses one port per invocation for all evaluators; to keep Gemini on `8006`, run it in a separate invocation.
  - Do not assume a hang just because output pauses; rely on final summary and before/after row deltas.
- Charts emit paired `_highlighted` PNGs with bolded focus models and thicker bar borders; keep these local (not published). Rating charts also embed small model-brand logos from `/mnt/r/benchmark_utils` when the shared brand registry has an asset for the plotted model.
- All CLI runs emit `[START]`/`[SUMMARY]` blocks via `sitecustomize.py` (`script_logging.ScriptRun`). Summaries automatically list IO paths, including files written through `Path.write_text()`, `Path.open(...)`, plain `open(...)`, and pandas `to_csv()`; if a custom writer bypasses those hooks, call `current_run().add_output(path)` explicitly and verify the file appears under `[SUMMARY] outputs:`. Set `SCRIPT_LOGGING_STDOUT_LINES=1` to also include stdout line counts, `SCRIPT_LOGGING_DEBUG=1` to include debug plumbing lines, or `SCRIPT_LOGGING_DISABLE=1` to disable instrumentation entirely.

---

## A) Category‑Set Selection & Rating
Purpose: Build prompts; have LLMs choose element sets; have other LLMs rate sets; pick the best; produce WC (word‑count) story prompts.

1) Create selection prompts (category choices)
```bash
python create_prompts.py --count 400
# → prompts_select_categories/prompt_cat_*.txt
```

2) Run selection prompts through multiple LLMs (edit hard‑coded models inside the script or use its defaults)
```bash
python choose_cats.py -p 8040 --workers 50
# → chosen_cats/<model>/prompt_cat_*.txt
```

3) Build “rate required sets” prompts + index→{set,model} mapping
```bash
python create_rate_prompts.py
# → prompts_rate_required_sets/prompt_rate_cat_*.txt + .json
```

4) Run rating prompts (override models via --models)
```bash
python run_rate_prompts.py -p 8040 --workers 90 \
  --models "gpt-5-low,claude-opus-4-1-20250805-0K,gemini-2.5-pro,qwen3-235b-a22b-thinking-2507"
# → rated_sets/<model>/rating_cat_*.txt
```

5) Aggregate ratings and proposer stats
```bash
python collect_ratings.py
# → ratings_summary/sets_ratings.csv, ratings_summary/proposer_stats.csv
```

6) Create final WC story prompts from best sets
```bash
python create_wc_prompts.py
# → prompts_wc/prompt_wc_*.txt, prompts_wc/selected_sets.json
```

---

## B) Story Generation (WC prompts → stories)
Purpose: Generate 600–800 word stories for each model.

```bash
python run_wc_prompts.py -p 8040 --workers 30
# or override the in-file default pool for one run:
python run_wc_prompts.py -p 8040 --workers 30 --models "model-a,model-b"
# → /mnt/r/writing2-data/stories_wc/<model>/story_wc_*.txt  +  /mnt/r/writing2-data/stories_wc/run_log.csv
```

Optional: extract per-LLM proper-name frequency tables from generated stories.
```bash
python build_proper_names_by_llm.py
# → data/proper_names_by_llm.csv   (columns: llm, proper_name, count)
#   Uses sentence-aware capitalization filtering to reduce false positives
#   from sentence starters (for example "After").
```

Compare LLMs by proper-name usage (pair scores + matrix + leaderboard):
```bash
python compare_proper_name_similarity.py
# → data/proper_name_pair_similarity.csv
# → data/proper_name_similarity_matrix.csv
# → reports/proper_name_similarity_leaderboard.md
#
# Focus on one LLM:
# python compare_proper_name_similarity.py --focus-llm pony-alpha
```

---

## C) Pre‑Grading + Word Count Diagnostics
Purpose: Extract clean story text, enforce 600–800, build grading prompts, and write word‑count diagnostics.

```bash
# Full rubric prompts (default)
python prepare_grading.py
# → /mnt/r/writing2-data/for_grading_wc/<model>/grade_story_wc_*.txt

# Optional simple overall-only prompts
python prepare_grading.py --simple
# → /mnt/r/writing2-data/for_grading_simple_wc/<model>/grade_story_wc_*.txt

# → data/word_count_details_wc.csv, data/model_word_count_summary_wc.csv,
#   data/largest_word_count_deviations_wc.csv, data/word_count_issues_wc.txt,
#   data/unused_stories_for_grading.txt
```
Notes:
- For new-model comparison intake, this stage is QC, not the canonical scoring path. If the next step is pairwise comparison, you usually do not need to run independent grading just because these files were prepared.
- “No outliers” only means no stories fell outside the strict `<600` / `>800` bounds. Still inspect `data/word_count_issues_wc.txt` before scheduling expensive comparison runs.
- New models are not comparison-ready until you refresh the active comparison roster from `stories_wc`.

---

## D) Gating Checks & Cleanup (optional, recommended)
Purpose: LLM scan for rubric‑level mismatches that depress grades; optionally remove those prompts/results.

Run checks:
```bash
python check_single_pov.py --analyzer-model gpt-4-1 --max-workers 120 -p 8040
# → data/gating_summary.csv, data/pov_summary.csv, data/gating_summary.jsonl
```

Optionally remove mismatched items (dry‑run vs apply):
```bash
python remove_grades_for_mismatches.py --only "POV_FAIL|SCENE_SCOPE_FAIL|CLOSURE_ABSENT" \
  --plan-csv deletion_plan.csv
# Apply deletions
python remove_grades_for_mismatches.py --only "POV_FAIL|SCENE_SCOPE_FAIL|CLOSURE_ABSENT" \
  --plan-csv deletion_plan.csv --apply
```

---

## E) Grading
Purpose: Grade stories with multiple teacher LLMs.

Grade (edit teacher list inside the script if needed):
```bash
# Full rubric grading (default)
python create_grades.py -p 8040            # add --overwrite to force regrade
# → /mnt/r/writing2-data/graded/<teacher>/<student>/grade_story_wc_*.txt

# Optional simple overall-only grading
python create_grades.py -p 8040 --simple   # add --overwrite to force regrade
# → /mnt/r/writing2-data/graded_simple/<teacher>/<student>/grade_story_wc_*.txt
```
Block listed combos are skipped automatically: `create_grades.BLOCKED_STORIES_BY_TEACHER`
currently prevents `claude-sonnet-4-5-20250929-0K` from grading `story_wc_240.txt`,
`story_wc_124.txt`, `story_wc_317.txt`, and `story_wc_0.txt` for every student. Edit that constant to
add/remove exclusions; the run summary prints how many tasks were withheld.

Aggregate grades to CSVs and diagnostics:
```bash
# Includes simple/combined outputs by default when graded_simple exists
python collect_grades.py
# → data/teacher_student_stats.csv, data/teacher_student_matrix.csv,
#   data/teacher_student_filemeans.csv, data/teacher_student_filemeans_numbered.csv,
#   data/teacher_student_file_questions.csv, distribution CSVs, correlations,
#   data/suspicious_records.csv, data/normalized_avg_per_student.csv
#   sentence-length analysis outputs:
#   data/sentence_length_story_stats.csv, data/sentence_length_llm_stats.csv,
#   data/sentence_length_score_correlation.csv, reports/sentence_length_report.md
#   plus optional simple/combined outputs:
#   data/teacher_student_stats_simple.csv, data/student_overall_stats_simple.csv,
#   data/teacher_student_stats_combined.csv, data/student_overall_stats_combined.csv,
#   data/teacher_student_file_simple_scores.csv, data/teacher_student_file_combined_scores.csv
#   (normalized averages are always rebuilt from teacher_student_filemeans_numbered.csv)

# Disable simple parsing/combined generation explicitly:
# python collect_grades.py --no-simple
```

---

## F) Legacy Absolute-Score Analysis
Purpose: Generate diagnostic absolute-score charts, normalized views, and rankings. These outputs are retained for audit and troubleshooting, but they are no longer the public quality leaderboard.

Main analysis pack:
```bash
python analysisb.py
# Emits, among others:
# - images/llm_overall_bar_start0_with_err.png, images/llm_overall_bar_zoomed_with_err.png
# - images/llm_overall_bar_zoomed_1to8.png, images/llm_overall_bar_zoomed_9Ato9J.png
# - images/normalized_llm_overall_bar_zoomed_1to8.png, images/normalized_llm_overall_bar_zoomed_9Ato9J.png
# - images/llm_overall_bar_start0_combined.png, images/llm_overall_bar_zoomed_combined.png
# - images/llm_overall_bar_start0_with_err_combined.png, images/llm_overall_bar_zoomed_with_err_combined.png
# - images/sentence_length_mean_by_llm.png, images/sentence_length_vs_score.png
#   Pass --include-weighted-ranking once data/grader_weights.csv exists to rebuild
#   the reliability-weighted #1-finish bar/pie charts.
```

Diagnostic standard leaderboard Markdown (raw mean scores):
```bash
python leaderboard.py --mode standard
# → reports/leaderboard.md
#   Requires shared model presentation metadata via /mnt/r/benchmark_utils and /mnt/r/connections
#   (`GET http://127.0.0.1:8006/v1/model_metadata` or the /mnt/r/connections module fallback).
```

Diagnostic normalized leaderboard PNG + Markdown:
```bash
python leaderboard.py
# → reports/normalized_leaderboard.md, images/normalized_leaderboard.png
#   (rebuilds data/normalized_avg_per_student.csv if the CSV is missing or older than the filemeans)
#   Uses the same shared model-presentation metadata surface as other reporting scripts.
```

---

## G) Per‑Question Comments → Summaries → General Summaries
Purpose: Build editor‑style briefs per model from Q1–Q8 grader comments.

Extract Q1–Q8 comments:
```bash
python collect_comments_1to6.py
# → comments_by_llm_1to8/q1..q8/<model>.txt
```

Create per‑question summary prompts:
```bash
python create_summary_prompts.py
# → /mnt/r/writing2-data/for_summarizing/q1..q8/<short-model>.txt
```

Generate per‑question summaries (adjust router/port in script or run locally):
```bash
python generate_summary_responses.py
# → summaries/q1..q8/<short-model>.txt
```

Create general‑summary prompts from eight summaries:
```bash
python create_general_summary_prompts.py
# → for_general_summary/<model>.txt
```

Generate general summaries:
```bash
python generate_general_summary_responses.py -m gpt-5-low -p 8040 -w 30 --overwrite
# → general_summaries/<model>.txt
```

---

## H) Pairwise Similarity → Diversity (10 − similarity)
Purpose: Diversity from pairwise story similarity judgements.

Tasks (K=50 pairs/LLM):
```bash
python build_similarity_tasks.py
# → data/story_similarity_tasks.csv
```

Run similarity evals (two evaluators by default):
```bash
python run_similarity_evals.py -p 8040 --evaluators "gpt-5-medium,qwen3-235b-a22b-thinking-2507" \
  --workers 16 --skip-existing
# → story_similarity_raw/..., data/story_similarity_scores.csv
```

Aggregate + charts:
```bash
python aggregate_similarity.py
# → data/llm_diversity_stats.csv, reports/diversity_leaderboard.md,
#   images/llm_diversity_bar_start0.png, images/llm_diversity_bar_zoomed.png
```

---

## I) Cross‑LLM Style Similarity (A vs B)
Purpose: Judge how similar two different writers are when they answered the same prompt, then build a closeness leaderboard + heat map.

Build prompts (exact element match, up to 50 shared indices):
```bash
python build_inter_llm_similarity_prompts.py --llm-a <A> --llm-b <B> --n 50 --sample --seed 1337
# → /mnt/r/writing2-data/inter_llm_similarity_prompts/<A>__vs__<B>/pair_####.txt
# → data/inter_llm_similarity_tasks.csv (appended + deduped)
```

Run evaluator (default `gpt-5.2-low`):
```bash
python run_inter_llm_similarity.py --llm-a <A> --llm-b <B> \
  --evaluator gpt-5.2-low -p 8040 --workers 12 --skip-existing
# → /mnt/r/writing2-data/inter_llm_similarity_raw/<evaluator>/<A>__vs__<B>/pair_####.txt
# → data/inter_llm_similarity_scores.csv (append)
```

Aggregate pair stats + matrix + heat map:
```bash
python aggregate_inter_llm_similarity.py
# → data/inter_llm_pair_stats.csv, data/inter_llm_similarity_matrix.csv,
#   reports/inter_llm_similarity_leaderboard.md, images/inter_llm_similarity_heatmap.png
```
Want to spotlight specific writers? Add `--focus-llms pony-alpha` (comma-separated for multiple) to restrict the leaderboard/heatmap to pairs containing those ids while keeping the CSV export full.

### New: Sweep one model vs all others (or all-pairs)
Use this when onboarding a fresh writer (e.g., `polaris-alpha`) and you need to see which existing LLM it most closely resembles.

```bash
python run_inter_llm_similarity_sweep.py \
  --target pony-alpha \
  --pairs 50 --sample --seed 2025 \
  --evaluator gpt-5-low --workers 20 -p 8040 \
  --skip-existing
```

Full all-pairs mode:
```bash
python run_inter_llm_similarity_sweep.py \
  --all-pairs \
  --pairs 50 --sample --seed 2025 \
  --evaluator gpt-5-low --workers 20 -p 8040 \
  --skip-existing
```

Flags:
- `--all-pairs` — run every unordered model pair in the selected roster.
- `--only llama4-maverick,gemini-2.5-pro` — restrict the comparison set.
- `--exclude qwen3-235b-a22b-thinking-2507` — skip specific LLMs.
- `--limit 5` — cap the selected model list before pair expansion.
- `--skip-aggregate` — run comparisons only; skip the final leaderboard rebuild.

The sweep:
1. Builds prompts for each `(target, other)` pair (deduplicating the tasks CSV).
2. Runs `run_inter_llm_similarity` for that pair with the provided evaluator settings.
3. Prints per-pair progress and a final summary (files processed, skips, errors, runtime).
4. Calls `aggregate_inter_llm_similarity.py` once at the end (unless `--skip-aggregate`).

Results land in the same CSV/PNG outputs listed above, so downstream notebooks stay unchanged.

---

## I) Poor‑Writing Analysis (quotes + severity)
Purpose: For each story, have an analyzer LLM find up to three concrete, quoted examples of very poor writing and rate each on a 1–10 scale (10 = worst). Outputs structured CSVs for downstream review.

1) Build analyzer prompt packets (one per story):
```bash
python build_poor_writing_prompts.py --llms deepseek-v32,claude-opus-4-6-0K,claude-opus-4-6-16K   # empty → all LLMs
# → /mnt/r/writing2-data/for_poor_writing/<llm>/analyze_story_wc_*.txt
```

2) Run analyzer (default `gpt-5-low`), parallel, safe to resume:
```bash
python run_poor_writing_analysis.py -p 8040 --analyzer gpt-5.2-medium --workers 410 --skip-existing --students deepseek-v32,claude-opus-4-6-0K,claude-opus-4-6-16K
# → /mnt/r/writing2-data/poor_writing_raw/<analyzer>/<llm>/story_wc_*.txt
# → data/poor_writing_run_log.csv
```

Flags:
- `--students "<llm1,llm2,...>"`: Limit to specific LLMs (defaults to all under `/mnt/r/writing2-data/for_poor_writing`).
- `--workers <N>`: ProcessPoolExecutor workers (defaults to 24).
- `--skip-existing`: Skip any story whose output file already exists.
- `-p/--port`: Local OpenAI-compatible proxy at `http://localhost:<port>/v1/`.

Run characteristics:
- Prints `[INFO] Pending analyzer calls: <n>` and `[PROGRESS] k/n done` every 50 tasks.
- On completion, prints start/end timestamps and total seconds.
- Appends a CSV log `data/poor_writing_run_log.csv` with columns:
  `timestamp, analyzer, student, prompt_path, raw_path, status` (`OK` or `ERROR <exc>`).

3) Aggregate parsed results:
```bash
python aggregate_poor_writing.py
# → data/poor_writing_examples.csv (per example)
#   - Sorted worst → least bad by severity
#   - Also writes per‑LLM splits: data/poor_writing_examples__<llm>.csv (sorted)
# → data/poor_writing_story_summary.csv (per story)
# → data/poor_writing_parse_errors.csv (diagnostics)
```

Template used: `prompts/prompt_poor_writing_analysis.txt` (loaded from repo root or `prompts/`).
Notes:
- Output uses simple XML-like tags (not real XML); the parser reads tags only.
- A single `<quote>` may include multiple short snippets (for repeated issues) separated by ` | `; total quote text ≤ 320 chars.

4) Thematic diagnostics per LLM (new themes beyond basic categories; default evaluator = `gpt-5-medium`):

Build prompts from per‑LLM CSVs (severity ≥ 7.0 by default, capped to a manageable size):
```bash
python build_poor_writing_theme_prompts.py --llms "" --min-severity 7.0 --max-examples 400
# → /mnt/r/writing2-data/for_poor_writing_themes/<llm>.txt
```

Run thematic analysis (safe to resume):
```bash
python run_poor_writing_thematic_analysis.py -p 8040 --evaluator gpt-5.2-medium --workers 100 --skip-existing
# → poor_writing_themes_raw/gpt-5-medium/<llm>.txt
# → data/poor_writing_theme_run_log.csv
```

Prompt template: `prompts/prompt_poor_writing_themes.txt`
Notes:
- The evaluator MUST invent clear, human‑readable themes (e.g., “Physically impossible actions by humans”) and must NOT reuse basic collection categories.
- Output uses strict tags under `<poor_writing_thematic_profile>` with theme counts, shares, quotes, recommendations, and quality gates.

5) Natural‑language synthesis (readable paragraphs per LLM; default evaluator = `gpt-5-medium`):

Combine the prior thematic profile with more high‑severity examples to produce flowing English paragraphs.

Run synthesis (safe to resume):
```bash
python run_poor_writing_theme_synthesis.py -p 8040 --evaluator gpt-5.2-medium --workers 120 --min-severity 7.0 --max-examples 120 --skip-existing
# → poor_writing_theme_summaries/gpt-5-medium/<llm>.txt
# → data/poor_writing_theme_synthesis_log.csv
```

Template used: `prompts/prompt_poor_writing_theme_synthesis.txt`.
Notes:
- Output is 3–6 paragraphs of natural English (no XML, no lists).
- Script weaves several short verbatim quotes from `data/poor_writing_examples__<llm>.csv` as evidence.

6) Easy‑to‑understand top‑N showcase (short, punchy explanations; default evaluator = `gpt-5-medium`):

Select the 20 examples that are most obvious to regular readers (also weighing severity and how briefly they can be explained), and generate crisp, sometimes lightly sarcastic one‑liners.

Run selection (safe to resume):
```bash
python run_poor_writing_easy20.py -p 8040 --evaluator gpt-5.2-medium --workers 50 --min-severity 7.0 --max-examples 300 --n-items 30 --skip-existing
# → poor_writing_easy20/gpt-5-medium/<llm>.txt  (exactly N items when enough input rows exist)
# → data/poor_writing_easy20_log.csv
```

Template used: `prompts/prompt_poor_writing_easy20.txt`.
Notes:
- Output contains exactly N items when enough input rows exist (default N=30); each item is two lines: first the quoted excerpt, then a short explanation; blank line between items.
- Quotes are verbatim (may be truncated with …), explanations are plain English and to the point.

---

## N) Inter‑LLM A‑vs‑B Comparison (same required elements)
Purpose: Use an evaluator LLM (gpt‑5‑low) to compare two writers’ stories that share the SAME required elements. The evaluator now produces two clearly separated sections: (1) rubric‑aligned differences (Q1–Q8 craft + 9A–J element integration) and (2) beyond‑rubric insights (meaningful distinctions not directly graded). Then summarize across all checked stories for the pair.

Recommended new-model intake policy:
- Pairwise comparison is the canonical scoring path for newly generated models. Independent rubric grading is optional QC, not the default next step.
- Start with readiness checks (`prepare_grading.py`, `vis_word_counts_script.py`), then inspect `data/word_count_issues_wc.txt`.
- Refresh the active roster from `/mnt/r/writing2-data/stories_wc/*` before any `--run-all` comparison. New story directories are not picked up automatically.
- Keep exclusion policy in two places when a model should stay out of future comparisons:
  - `inter_llm_comparison_story_excluded_models.txt` so the next roster rebuild does not re-add it
  - the current active roster file so current runs also exclude it
- Incomplete models may still be compared if overlap supports the chosen `--n`, but that should be an explicit exception and later reporting should call the model incomplete.
- For newly added models, prefer staged coverage: anchor pilot first, optional new-vs-new pass second, then broader expansion. Do not start with a full `--run-all` sweep unless you intentionally want that cost.
- For manually chosen leaderboard gaps, prefer `run_inter_llm_comparison_batch.py --pairs-file <path>` so only those exact unordered pairs run. Pair files contain one pair per non-comment line, separated by a comma or whitespace.
- Preferred cost control is “full evaluator roster + `--evaluators-per-pair`” rather than locking the whole run to one fixed small judge panel.
- If the evaluator roster changes materially, start a new protocol scope with a new versioned evaluator file and a new `template_id`.

1) Build A‑vs‑B comparison prompts (same‑elements filter applied):
```bash
python build_inter_llm_comparison_prompts.py --llm-a <A> --llm-b <B> --n 50 --sample --seed 12345
# → /mnt/r/writing2-data/inter_llm_comparison_prompts/<A>__vs__<B>/pair_####.txt
# → data/inter_llm_comparison_tasks.csv

# Alternate template (isolated by template_id)
python build_inter_llm_comparison_prompts.py --llm-a <A> --llm-b <B> --n 50 --sample --seed 12345 \
  --template-id alt_v2 \
  --template-path prompts/prompt_inter_llm_comparison_alt_v2.txt
# → /mnt/r/writing2-data/inter_llm_comparison_prompts/alt_v2/<A>__vs__<B>/pair_####.txt
```
Notes:
- The builder injects a rubric summary from `prompts/prompt_rubric_summary.txt` into each prompt (`<<<RUBRIC_SUMMARY>>>`). Edit that file to tune rubric guidance without touching code.
- The builder de‑duplicates `data/inter_llm_comparison_tasks.csv` by `(llm_a, llm_b, template_id, story_idx)` to prevent repeated runs from inflating the task list.
- The builder randomizes visible Story A/Story B sides deterministically per `(llm_a,llm_b,story_idx,seed)` and stores side mapping columns in `data/inter_llm_comparison_tasks.csv` to reduce position bias.
- Builder output now includes explicit before/after summary lines for:
  - prompt file count for the pair
  - tasks rows (global and pair-specific)
  - dedup rows removed
- For guaranteed net‑new additions, use:
  - `--only-new` to exclude indices already present for `(llm_a, llm_b)` in `data/inter_llm_comparison_tasks.csv`
  - `--require-exact-n` to fail if fewer than `--n` eligible indices remain

2) Run comparisons with one or more evaluators (non-batch default router: `8006`):
```bash
python run_inter_llm_comparisons.py --llm-a <A> --llm-b <B> --template-id default -p 8006 --workers 20
# → /mnt/r/writing2-data/inter_llm_comparison_raw/<evaluator>/<A>__vs__<B>/pair_####.txt
# → data/inter_llm_comparison_index.csv
# → data/inter_llm_comparison_scores.csv
```
Optional multi-evaluator mode:
```bash
python run_inter_llm_comparisons.py --llm-a <A> --llm-b <B> --template-id default -p 8006 --workers 20 \
  --evaluators "gpt-5-low,qwen3-235b-a22b-thinking-2507"

# Non-default template writes under /<evaluator>/<template_id>/<pair>/
# and records template_id in index/scores rows.
```
Notes:
- With no `--evaluator` or `--evaluators`, the runner uses the full versioned roster from `inter_llm_comparison_full_evaluators.txt`.
- The runner now skips existing raw outputs by default. Use `--overwrite` to force regeneration.
- `--evaluator` runs one evaluator; `--evaluators` runs one pass per evaluator in a single invocation.
- `--evaluators-per-pair N` deterministically selects up to `N` eligible evaluators per `(llm_a, llm_b, template_id)` after self-eval filtering.
- Use `--evaluator-selection-seed` to change that stable per-pair evaluator subset while keeping reruns deterministic.
- Comparison evaluator temperature defaults to `1.0` (override via `--temperature`).
- `--verbose` prints per-evaluator raw output directories in the final summary (otherwise it prints one compact pattern line).
- Self-evaluation exclusion defaults to `--self-eval-policy family`:
  - blocks exact evaluator==writer and same-family evaluator/writer pairings.
  - override with `--self-eval-policy exact` (exact model only) or `--self-eval-policy off`.
- Runtime output includes periodic `[PROGRESS]` lines (`done/total`, `%`, ok/warn/skipped) plus pair-level before/after row deltas for:
  - `data/inter_llm_comparison_index.csv`
  - `data/inter_llm_comparison_scores.csv`

Tag expectations per raw file:
- Required analysis tags: `<a_advantages>`, `<b_advantages>`, `<verdict>`, `<extra_insights>`.
- Required machine tags (strictly parsed): `<winner>`, `<margin>`.
- Preferred machine tag (continuous primary signal): `<signed_margin>` where positive favors Story A and negative favors Story B.
- Optional machine tag: `<confidence>` (defaults to `0.0` when absent).
- Optional diagnostics tag: `<flags>` (validated when present).
- Optional analysis tags: `<shared_or_parity>`, `<failure_modes>`.

2b) Aggregate structured pairwise outcomes into pair stats + global ratings:
```bash
python aggregate_inter_llm_comparison_scores.py --template-id default --bootstrap-samples 300 --bootstrap-seed 12345
# → data/inter_llm_comparison_pair_story.csv
# → data/inter_llm_comparison_pair_stats.csv
# → data/inter_llm_comparison_bt_ratings.csv
# → data/inter_llm_comparison_rating_diagnostics.csv
# → data/inter_llm_comparison_tie_sensitivity.csv
# → data/inter_llm_comparison_evaluator_diagnostics.csv
# → data/inter_llm_comparison_evaluator_agreement.csv
# → data/inter_llm_comparison_side_bias_corrections.csv
# → reports/inter_llm_comparison_score_leaderboard.md
```
2c) Render pairwise-comparison charts (large Plotly figures with shaded CI rectangles and shared model-brand logos where available):
```bash
python plot_inter_llm_comparison_charts.py
# → images/inter_llm_comparison_thurstone_ratings.png
# → images/inter_llm_comparison_bt_ratings.png
# → images/inter_llm_comparison_pair_margin_heatmap.png
#   Requires shared model presentation metadata via /mnt/r/benchmark_utils and /mnt/r/connections.
```
Notes:
- Pair stats are computed per unordered pair and story index (aggregated across evaluators).
- Global ranking is margin-primary (Thurstone-style on signed margins). This is the canonical public quality rating.
- BT is retained only as a reference/diagnostic column.
- BT outcomes are tie-aware from signed margins using `--tie-epsilon` (default `0.5`).
- Ranking diagnostics include Thurstone-vs-BT rank correlation (Spearman/Kendall) and sigma bootstrap stability (mean/std/CV).
- Ranking diagnostics also include triad-cycle transitivity checks (`triads_decisive`, `cycle_count`, `cycle_rate`, `weighted_cycle_rate`).
- Tie sensitivity diagnostics are exported across an epsilon grid (default `0.25,0.5,1.0`; override via `--tie-sensitivity-epsilons`).
- Uncertainty bands are bootstrapped over story indices and evaluators by default (hierarchical bootstrap).
- Use `--no-bootstrap-resample-evaluators` to fall back to legacy story-only bootstrap.
- Side-A evaluator bias correction is applied to signed margins by default before ratings.
- Use `--no-side-bias-correction` to disable this correction.
- Evaluator diagnostics include side-position bias checks, cross-evaluator agreement, and repeat self-consistency.
- Use `--all-templates` to aggregate all template IDs together (default scope is `--template-id default`).

3) Create a single summary prompt aggregating all pairwise findings (rubric‑aligned + beyond‑rubric evidence):
```bash
python create_inter_llm_comparison_summary_prompts.py \
  --llm-a <A> --llm-b <B> --template-id default
# → for_inter_llm_comparison_summary/<A>__vs__<B>.txt
```
or combine multiple evaluator folders:
```bash
python create_inter_llm_comparison_summary_prompts.py --llm-a <A> --llm-b <B> \
  --template-id default \
  --evaluators "gpt-5-low,qwen3-235b-a22b-thinking-2507"
```

4) Generate the final A‑vs‑B summary report (template separates rubric vs beyond‑rubric):
```bash
python generate_inter_llm_comparison_summary_responses.py -m gpt-5-low -p 8040 -w 8 \
  --template-id default \
  --llm-a <A> --llm-b <B>   # restrict to one pair
# → inter_llm_comparison_summaries/<A>__vs__<B>.txt
```

Artifacts overview:
- Pair prompts:
  - default template: `/mnt/r/writing2-data/inter_llm_comparison_prompts/<A>__vs__<B>/pair_*.txt`
  - non-default template: `/mnt/r/writing2-data/inter_llm_comparison_prompts/<template_id>/<A>__vs__<B>/pair_*.txt`
- Raw judge outputs:
  - default template: `/mnt/r/writing2-data/inter_llm_comparison_raw/<evaluator>/<A>__vs__<B>/pair_*.txt`
  - non-default template: `/mnt/r/writing2-data/inter_llm_comparison_raw/<evaluator>/<template_id>/<A>__vs__<B>/pair_*.txt`
- Parsed scores: `data/inter_llm_comparison_scores.csv`
- Aggregates: `data/inter_llm_comparison_pair_story.csv`, `data/inter_llm_comparison_pair_stats.csv`, `data/inter_llm_comparison_bt_ratings.csv`
- Rating diagnostics: `data/inter_llm_comparison_rating_diagnostics.csv`, `data/inter_llm_comparison_tie_sensitivity.csv`
- Evaluator diagnostics: `data/inter_llm_comparison_evaluator_diagnostics.csv`, `data/inter_llm_comparison_evaluator_agreement.csv`
- Side-bias correction table: `data/inter_llm_comparison_side_bias_corrections.csv`
- Score leaderboard: `reports/inter_llm_comparison_score_leaderboard.md`
- Charts: `images/inter_llm_comparison_thurstone_ratings.png`, `images/inter_llm_comparison_bt_ratings.png`, `images/inter_llm_comparison_pair_margin_heatmap.png`
- Summary prompt: `for_inter_llm_comparison_summary/<A>__vs__<B>.txt`
- Final summary: `inter_llm_comparison_summaries/<A>__vs__<B>.txt`
  - non-default template summaries are under `for_inter_llm_comparison_summary/<template_id>/...`
    and `inter_llm_comparison_summaries/<template_id>/...`

---

### One‑Command A‑vs‑B Pipeline
Run the full flow (build → compare → score aggregate → create summary prompt → generate summary) with a single command:

```bash
python run_inter_llm_comparison_pipeline.py \
  --llm-a kimi-k2-0905 \
  --llm-b gpt-5-medium \
  --n 50 --sample --seed 12345 \
  --template-id default \
  -p 8006 --compare-workers 50 \
  --pair-evaluators "gpt-5-low,qwen3-235b-a22b-thinking-2507" \
  --summary-model gpt-5-low --summary-workers 8
```

Options:
- `--skip-score-aggregate`: skip generation of the structured score aggregates/BT leaderboard.
- `--pair-evaluator`: single comparison evaluator (legacy/single mode).
- `--pair-evaluators`: comma-separated comparison evaluators (multi mode).
- With no pair-evaluator flags, the pipeline defaults to `inter_llm_comparison_full_evaluators.txt`.
- `--pair-evaluators-per-pair N`: deterministically keep only `N` eligible evaluators for this `(llm_a, llm_b, template_id)` after self-eval filtering.
- `--evaluator-selection-seed`: change the stable per-pair evaluator subset used by `--pair-evaluators-per-pair`.
- `--temperature`: comparison evaluator temperature (default `1.0`).
- `--template-id`: isolate one prompt-template experiment across prompts/raw/index/scores/summaries.
- `--template-path`: alternate pairwise comparison template passed to builder.
- `--only-new`, `--require-exact-n`: pass through to prompt builder for guaranteed net-new expansion controls.
- `--bootstrap-samples`, `--bootstrap-seed`: controls bootstrap uncertainty estimation for the BT leaderboard.
- `--bootstrap-resample-evaluators` / `--no-bootstrap-resample-evaluators`: toggle evaluator-level resampling during aggregation bootstrap.
- `--side-bias-correction` / `--no-side-bias-correction`: toggle side-A bias correction during aggregation.
- `--overwrite-compare`: force re-run comparisons even if raw outputs exist.
- `--overwrite-summary`: force re-generate final summaries.
  When used with the pipeline, only the summary for the specified `<A>__vs__<B>` pair is regenerated (other pairs are untouched).
- `--dry-run`: print commands without executing.

The orchestrator prints step markers and a final run summary with counts and paths:
- `[STEP 1/4]` build prompts
- `[STEP 2/4]` run comparisons
- `[STEP 3/4]` build summary prompt
- `[STEP 4/4]` generate final summary
- Prompts dir and count
- Raw outputs dir and per-evaluator counts
- Presence of the single summary prompt and final summary
- Before/after delta block (`[PIPELINE DELTA]`) for prompts/raw/task/index/score counts and summary existence
- Start time and runtime

Notes:
- The pipeline uses the same de‑duped task index and skip-by-default semantics documented above.

---

### Simple Batch Maintenance (no subcommands)
Use this helper for active-roster maintenance, all-pairs runs, incremental additions, and model drops:

```bash
# 0) Initialize active roster from /mnt/r/writing2-data/stories_wc/*
python run_inter_llm_comparison_batch.py --init-roster-from-stories
# → data/inter_llm_active_models.txt

# 0b) Initialize a full-run roster but exclude specific story models
python run_inter_llm_comparison_batch.py \
  --init-roster-from-stories \
  --overwrite-roster \
  --roster-path data/inter_llm_active_models_full.txt \
  --exclude-models-file inter_llm_comparison_story_excluded_models.txt
# → data/inter_llm_active_models_full.txt

# 1) Run all active pair combinations (with random sampling)
python run_inter_llm_comparison_batch.py \
  --run-all \
  --sample --n 50 --seed 12345 \
  --template-id default \
  --evaluators-file inter_llm_comparison_full_evaluators.txt \
  --workers 20

# 1b) Parallel pair runs with safe shard-merge writes
#     Total evaluator concurrency is capped by --max-workers-per-llm.
python run_inter_llm_comparison_batch.py \
  --run-all \
  --sample --n 50 --seed 12345 \
  --template-id default \
  --evaluators "gpt-5.2-low,claude-sonnet-4-6-16K,qwen3.5-397b-a17b" \
  --pair-workers 4 --workers 12 \
  --max-workers-per-llm 36

# 2) Add only net-new random matchups for all active pairs
python run_inter_llm_comparison_batch.py \
  --run-all \
  --sample --n 20 --seed 20260302 \
  --template-id default \
  --only-new --require-exact-n \
  --evaluator gpt-5-low --workers 20

# 2b) Run exact manually selected pairs from a file
python run_inter_llm_comparison_batch.py \
  --pairs-file temp/inter_llm_priority_pairs_top24.txt \
  --sample --n 20 --seed 20260418 \
  --template-id default \
  --only-new --require-exact-n \
  --evaluators-file inter_llm_comparison_full_evaluators.txt \
  --evaluators-per-pair 3 \
  --pair-workers 4 --workers 12 \
  --max-workers-per-llm 36

# 2c) Adaptive expansion: prioritize inconclusive pairs (CI crosses zero)
python run_inter_llm_comparison_batch.py \
  --adaptive-inconclusive \
  --adaptive-top-k 8 \
  --sample --n 30 --seed 20260302 \
  --template-id default \
  --evaluator gpt-5-low --workers 20

# 3) Evaluate newly added models only vs active roster
python run_inter_llm_comparison_batch.py \
  --added-models "new-model-a,new-model-b" \
  --sample --n 50 --seed 12345 \
  --template-id default \
  --evaluator gpt-5-low --workers 20

# 4) Drop models from tasks/index/scores, then rebuild rating artifacts
python run_inter_llm_comparison_batch.py \
  --drop-models "old-model-x,old-model-y" \
  --prune-dropped-artifacts

# 5) Repair stale comparison CSV state after path/root changes
python run_inter_llm_comparison_batch.py --repair-stale-paths
```

Notes:
- The helper keeps an explicit active roster file: `data/inter_llm_active_models.txt`.
- Full-run inter-LLM comparison control files are versioned:
  - `inter_llm_comparison_full_evaluators.txt`
  - `inter_llm_comparison_story_excluded_models.txt`
- `--init-roster-from-stories` must be rerun after new stories land if you want `--run-all` to include them.
- `--pairs-file <path>` schedules exact unordered pairs without expanding a roster. The file must contain one pair per non-comment line as either `model_a,model_b` or `model_a model_b`.
- `--added-models` compares each added model against the existing active roster, but it does not create comparisons among the added models themselves in that same invocation.
- Non-batch pairwise/pipeline runs default to port `8006`; batch manager defaults to `8040`.
- Cost/latency policy for inter-LLM batch:
  - Use `8006` for smoke tests, quick validation, small batches (roughly under 200 calls), and Gemini runs.
  - Use `8040` when you intentionally want cheaper batch routing for providers that actually support it.
  - `8040` is fine for larger production runs where there are many calls and slower batch execution is acceptable.
  - In practice, true `8040` batch support is limited to Gemini, OpenAI, and Anthropic; unsupported models are forwarded to `8006`.
  - Gemini is especially slow on `8040` and can take many hours, so keep Gemini in a separate `8006` invocation unless latency does not matter.
  - Port choice does not determine request fan-out by itself; concurrency comes from the effective `pair-workers * workers` combination.
- Use `--exclude-models` / `--exclude-models-file` to filter story models out of active roster/run scope.
- Use `--template-id` to keep prompt-template experiments isolated.
- Use `--template-path` with `--template-id` when building/running an alternate comparison prompt template.
- Evaluator selection in batch:
  - `--evaluator <model>`: single evaluator (legacy/single mode)
  - `--evaluators <m1,m2,...>`: multiple evaluators in one invocation
  - `--evaluators-file <path>`: file-driven evaluator list (one per line, or comma-separated lines)
  - `--evaluators-per-pair <N>`: deterministically keep only `N` eligible evaluators per pair after self-eval filtering
  - `--evaluator-selection-seed <int>`: change the stable per-pair evaluator subset used by `--evaluators-per-pair`
- `--verbose` echoes each subprocess command line (default keeps command echo quiet unless a subprocess fails).
- `--pair-workers` controls parallel pairs. When `>1`, compare outputs are written to per-pair shard CSVs and then merged into canonical `index/scores` CSVs to avoid write races.
- `--max-workers-per-llm` caps total evaluator workers across all parallel pair runs; the batch script auto-reduces effective pair concurrency and/or per-pair workers to stay within the cap.
- `--compare-only` skips build and runs comparisons only for pairs that already have tasks for `--template-id`.
- `--n 0` is valid only with `--compare-only` (no build stage).
- `--compare-shard-root` + `--defer-shard-merge` lets multiple batch invocations run in parallel safely by avoiding shared canonical CSV writes.
- `--merge-shards-from <dir1,dir2,...>` merges deferred shard outputs into canonical `data/inter_llm_comparison_index.csv` and `data/inter_llm_comparison_scores.csv`.
- `--adaptive-inconclusive` selects pairs from `data/inter_llm_comparison_pair_stats.csv`
  where `abs(mean_signed_margin_left) <= ci95_signed_margin_left`, ranked by
  `priority = ci95 - abs(mean)`. It forces net-new expansion behavior (`--only-new`).
- `--adaptive-disagreement` selects pairs from `data/inter_llm_comparison_scores.csv`
  with high cross-evaluator disagreement, ranked by
  `priority = mean_pairwise_abs_margin_diff * sqrt(overlap_story_pairs)`.
- For manual or scripted incremental batches, prioritize leaderboard-relevant uncertainty near the top of the ranking. Missing or inconclusive direct comparisons among high-ranked models should generally run before lower-table completion pairs when the call budget is limited.
- Use `--pairs-file` for exact high-value manual selections; temporary multi-model rosters are appropriate only when every combination among those models is intended.
- `--drop-models` filters rows from:
  - `data/inter_llm_comparison_tasks.csv`
  - `data/inter_llm_comparison_index.csv`
  - `data/inter_llm_comparison_scores.csv`
- `--repair-stale-paths` rewrites legacy comparison CSV path prefixes
  (`/mnt/r/writing2/inter_llm_comparison_*` → `/mnt/r/writing2-data/inter_llm_comparison_*`),
  backfills missing side columns in tasks, and removes rows whose prompt/raw files no longer exist.
- Aggregation is run by default after comparison runs and/or drops (use `--no-aggregate` to skip).
- If compatible legacy rows are intentionally backfilled into a canonical template scope, preserve their original prompt/raw paths. The aggregate report will show a scope note when rows for the selected `--template-id` point to prompt/raw paths outside that template directory.
- Aggregate controls are forwarded by batch:
  - `--bootstrap-resample-evaluators` / `--no-bootstrap-resample-evaluators`
  - `--side-bias-correction` / `--no-side-bias-correction`

Smoke-test split-port example (same template/seed, non-Gemini on cheap batch port, Gemini on fast non-batch port):
```bash
# pass 1: all but Gemini on 8040 (skip aggregate until all evaluator passes are done)
python run_inter_llm_comparison_batch.py \
  --roster-path data/inter_llm_active_models_pilot_valid.txt \
  --run-all --sample --n 12 --seed 12345 \
  --template-id pilot_split_ports \
  --evaluators "claude-sonnet-4-6-16K,qwen3.5-397b-a17b,kimi-k2.5,deepseek-v32,gpt-5.2-low,grok-4-1-fast-reasoning" \
  --port 8040 --pair-workers 4 --workers 25 --max-workers-per-llm 100 \
  --no-aggregate

# pass 2: Gemini-only on 8006 (same template/seed)
python run_inter_llm_comparison_batch.py \
  --roster-path data/inter_llm_active_models_pilot_valid.txt \
  --run-all --sample --n 12 --seed 12345 \
  --template-id pilot_split_ports \
  --evaluators "gemini-3.1-pro-preview" \
  --port 8006 --pair-workers 2 --workers 12 --max-workers-per-llm 24 \
  --no-aggregate

# final aggregate once
python aggregate_inter_llm_comparison_scores.py --template-id pilot_split_ports
```

Safe multi-process evaluator parallelism example (deferred shard merge):
```bash
# terminal 1: non-Gemini evaluators (writes only to shard files)
python run_inter_llm_comparison_batch.py \
  --roster-path data/inter_llm_active_models_full.txt \
  --run-all --compare-only --n 0 \
  --template-id prod_2026_03_03_full_n8_v1 \
  --evaluators "claude-sonnet-4-6-16K,qwen3.5-397b-a17b,kimi-k2.5,deepseek-v32,gpt-5.2-low,grok-4-1-fast-reasoning" \
  --port 8040 --pair-workers 50 --workers 8 --max-workers-per-llm 400 \
  --compare-shard-root data/inter_llm_comparison_batch_tmp/prod_non_gemini \
  --defer-shard-merge --no-aggregate

# terminal 2: Gemini-only evaluator (writes only to shard files)
python run_inter_llm_comparison_batch.py \
  --roster-path data/inter_llm_active_models_full.txt \
  --run-all --compare-only --n 0 \
  --template-id prod_2026_03_03_full_n8_v1 \
  --evaluator gemini-3.1-pro-preview \
  --port 8006 --pair-workers 91 --workers 4 --max-workers-per-llm 400 \
  --compare-shard-root data/inter_llm_comparison_batch_tmp/prod_gemini \
  --defer-shard-merge --no-aggregate

# after both finish: merge once, then aggregate once
python run_inter_llm_comparison_batch.py \
  --merge-shards-from "data/inter_llm_comparison_batch_tmp/prod_non_gemini,data/inter_llm_comparison_batch_tmp/prod_gemini" \
  --template-id prod_2026_03_03_full_n8_v1 --no-aggregate
python aggregate_inter_llm_comparison_scores.py --template-id prod_2026_03_03_full_n8_v1
```

Run all configured full-run evaluators in one invocation:
```bash
python run_inter_llm_comparison_batch.py \
  --roster-path data/inter_llm_active_models_full.txt \
  --run-all \
  --sample --n 50 --seed 12345 \
  --evaluators-file inter_llm_comparison_full_evaluators.txt \
  --pair-workers 4 --workers 25 --max-workers-per-llm 100
```

Optional fallback (sequential over evaluator list, each evaluator can still run pair-parallel):
```bash
while IFS= read -r ev; do
  [ -z "$ev" ] && continue
  [ "${ev#\#}" != "$ev" ] && continue
  python run_inter_llm_comparison_batch.py \
    --roster-path data/inter_llm_active_models_full.txt \
    --run-all \
    --sample --n 50 --seed 12345 \
    --evaluator "$ev" \
    --pair-workers 4 --workers 25 --max-workers-per-llm 100
done < inter_llm_comparison_full_evaluators.txt
```

---

## I) Style Fingerprints → Diversity (Weighted Gower)
Purpose: Compute stylistic fingerprints per story and derive a mixed‑type diversity metric.

Build fingerprints (adjust evaluators/temperature):
```bash
python build_style_fingerprints.py -p 8040 --evaluators "gpt-5-low" --workers 200 --skip-existing
# → style_fingerprint_raw/<evaluator>/<llm>/..., data/style_fingerprints.csv, data/style_fingerprints_v*.csv
```

Compute diversity metrics:
```bash
python compute_style_diversity.py --knn 5
# → data/story_diversity_metrics_by_evaluator.csv, data/story_diversity_metrics.csv, data/style_knn.csv
```

Diversity leaderboard (Weighted Gower):
```bash
python style_diversity_leaderboard.py
# → reports/diversity_leaderboard.md, images/diversity_leaderboard.png
```

Optional style charts pack:
```bash
python style_fingerprint_charts.py
# → images/style_*.png + data/style_*_data.csv
```

---

## J) Grader Evaluation → Weights → Weighted Reports
Purpose: Evaluate graders to derive reliability weights, then recompute weighted results.

Pick stories graded by all graders:
```bash
python grader_eval_select_stories.py
# → data/grader_eval_story_set.csv
```

Build tasks (default E=G or pass a file):
```bash
python build_grader_eval_tasks.py --evaluators-file evaluators_list.txt
# → data/grader_evaluation_tasks.csv
```

Run evaluator LLMs (resume with --skip-existing):
```bash
python run_grader_evals.py -p 8040 --workers 40 --skip-existing
# → /mnt/r/writing2-data/grader_eval_raw/... and data/grader_evaluations_raw.csv
```

Aggregate to weights and apply:
```bash
python aggregate_grader_evals.py
# → data/grader_weights.csv, data/student_overall_stats_weighted.csv
```

Produce weighted comparison + LLM×Question weighted means:
```bash
python weighted_reports.py
# → data/student_overall_weighted_vs_unweighted.csv, data/question_by_student_weighted.csv,
#   data/student_overall_stats_qweighted.csv
#   Requires complete upstream inputs: question-level SEMs must already be present and
#   question/model metadata mismatches now fail fast instead of falling back.
```

---

## K) Word‑Count Diagnostics (Standalone)
Purpose: Visual QC of 600–800 compliance and cleanup helpers.

```bash
python vis_word_counts_script.py
# → images/word_count_distribution_by_model.png, images/word_count_histogram.png,
#   images/avg_word_count_by_model.png, images/avg_word_count_ci.png,
#   images/outliers_too_low.png, images/outliers_too_high.png,
#   outliers/<model>_outliers.csv and outliers/<model>_outliers.bat cleanup lists
```

---

## L) Extra One‑Offs
- Best/worst story surfacing and CSV:
```bash
python best_worst_stories.py
```
- Alternate diversity leaderboard (marks):
```bash
python style_diversity_leaderboard_altmarks.py
```
- Additional chart packs:
```bash
python charts_bars.py
python charts_heatmaps.py
python charts_scatter.py
python charts_strip.py
```
- Copy all README‑referenced images to publish folder:
```bash
python copy_images.py
```
- The active README now references comparison charts. The older absolute-rating README and its stale README-linked chart PNGs live under `archive/absolute_ratings_v4_2026_04_19/`.

---

## M) Quick “Everything” Order (minimal happy path)
```bash
# Env
export PYTHONPATH="$PWD:$PYTHONPATH"

# A) Selection & rating
python create_prompts.py --count 400
python choose_cats.py -p 8040 --workers 50
python create_rate_prompts.py
python run_rate_prompts.py -p 8040 --workers 90 --models "gpt-5-low,claude-opus-4-1-20250805-0K,gemini-2.5-pro,qwen3-235b-a22b-thinking-2507"
python collect_ratings.py && python create_wc_prompts.py

# B) Stories
python run_wc_prompts.py -p 8040 --workers 30 --models "model-a,model-b"

# C) Pre‑grade + WC
python prepare_grading.py
# Optional simple overall prompts:
python prepare_grading.py --simple

# D) Optional gating & cleanup
python check_single_pov.py -p 8040 --max-workers 120
# (optional) python remove_grades_for_mismatches.py --apply

# E) Grading + aggregation
python create_grades.py -p 8040
python create_grades.py -p 8040 --simple
python collect_grades.py

# F) Analysis & leaderboard
python analysisb.py
#   (Use --include-weighted-ranking after aggregate_grader_evals.py creates data/grader_weights.csv.)
python leaderboard.py

# G) Summaries
python collect_comments_1to6.py
python create_summary_prompts.py
python generate_summary_responses.py
python create_general_summary_prompts.py
python generate_general_summary_responses.py -p 8040 -w 50

# H) Similarity diversity (10 − similarity)
python build_similarity_tasks.py
python run_similarity_evals.py -p 8040 --workers 16
python aggregate_similarity.py

# I) Style fingerprints + Gower diversity
python build_style_fingerprints.py -p 8040 --workers 200 --skip-existing
python compute_style_diversity.py
python style_diversity_leaderboard.py

# J) Grader evals → weights → weighted reports
python grader_eval_select_stories.py
python build_grader_eval_tasks.py
python run_grader_evals.py -p 8040 --workers 40 --skip-existing
python aggregate_grader_evals.py
python weighted_reports.py

# K) Word‑count visuals
python vis_word_counts_script.py
```

---

## Notes & Tips
- `run_wc_prompts.py` and `run_rate_prompts.py` support `--models` for one-off overrides; edit in-file model lists only when you want to change the default pool.
- Stick to 600–800 words; diagnostics enforce and visualize compliance.
- Prefer `--skip-existing` on large runs to resume safely.
- Validate CSVs between phases (counts, coverage) before committing to the next.
