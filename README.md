# LLM Creative Story-Writing Benchmark

This benchmark now uses **pairwise head-to-head comparisons** as its canonical quality signal. Models write short fiction to the same constrained creative briefs; evaluator LLMs compare two stories written for the same required elements; the resulting signed margins are aggregated into a global **Thurstone-style rating**.

The previous absolute 0-10 rubric-rating publication is archived and is no longer the main leaderboard. Absolute ratings may still be useful as diagnostics, but future public rankings should be based on pairwise comparison ratings.

Archived absolute-rating publication:
- [archive/absolute_ratings_v4_2026_04_19/README.md](archive/absolute_ratings_v4_2026_04_19/README.md)
- Its old README-linked chart PNGs were moved locally under `archive/absolute_ratings_v4_2026_04_19/images/`.

---

## Current Results

![Thurstone comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Canonical Leaderboard

Current canonical scope: `pilot_2026_04_18_anchor_n20_fullroster_cap3_v1`.

Coverage at the last aggregation:
- 23 rated models
- 134 direct model-pair rows
- 9,139 in-scope score rows
- 2,462 of those score rows use legacy-compatible prompt/raw path provenance
- Bootstrap uncertainty resamples both stories and evaluators
- Evaluator side-A bias correction is enabled

| Rank | LLM | Thurstone Rating | Win Prob vs Pool | 95% CI | BT (Ref) |
|-----:|:----|-----------------:|-----------------:|-------:|---------:|
| 1 | gpt-5.4-xhigh | 4.0412 | 0.917 | 3.7887..4.3457 | 6.1057 |
| 2 | gpt-5.4-medium | 3.6311 | 0.888 | 3.3705..3.9094 | 5.9413 |
| 3 | claude-opus-4-7-adaptive | 3.3423 | 0.865 | 3.1730..3.4691 | 6.0631 |
| 4 | claude-opus-4-6-16K | 3.1530 | 0.849 | 2.6867..3.6050 | 5.8529 |
| 5 | gpt-5.2-medium | 3.0438 | 0.839 | 2.5438..3.4927 | 4.2152 |
| 6 | claude-sonnet-4-6-16K | 2.5355 | 0.792 | 2.3303..2.7672 | 5.4205 |
| 7 | mistral-medium-2508 | 1.6599 | 0.699 | 1.4802..1.8590 | 2.5247 |
| 8 | kimi-k2.5 | 0.8286 | 0.600 | 0.6171..1.0372 | 1.7458 |
| 9 | glm-5 | 0.5227 | 0.561 | -0.0707..1.0973 | 1.3106 |
| 10 | glm-5.1 | 0.4796 | 0.556 | 0.2743..0.7507 | 1.2808 |
| 11 | mimo-v2-pro | 0.3428 | 0.538 | 0.1527..0.5313 | 1.4750 |
| 12 | seed-2.0-pro | -0.1930 | 0.469 | -0.5023..0.0651 | 0.7023 |
| 13 | mistral-large-2512 | -0.5438 | 0.424 | -1.0682..-0.0613 | 0.4926 |
| 14 | qwen3.6-plus | -0.5850 | 0.419 | -0.7889..-0.3594 | 0.2295 |
| 15 | gemini-3.1-pro-preview | -0.7073 | 0.403 | -0.9164..-0.4697 | 0.1220 |
| 16 | gemma-4-31b-it-reasoning | -0.8888 | 0.380 | -1.0988..-0.6936 | -0.0430 |
| 17 | ernie-5 | -1.3284 | 0.326 | -2.1063..-0.5255 | -14.9843 |
| 18 | grok-4-1-fast-reasoning | -1.4181 | 0.316 | -2.3198..-0.6669 | -14.9843 |
| 19 | deepseek-v32 | -1.7766 | 0.275 | -2.0652..-1.4464 | -0.7867 |
| 20 | minimax-m2.7 | -3.2200 | 0.140 | -3.4310..-2.9874 | -2.4366 |
| 21 | gpt-oss-120b | -3.4224 | 0.126 | -3.6469..-3.2022 | -2.3555 |
| 22 | qwen3.5-397b-a17b | -3.7738 | 0.102 | -4.0209..-3.5689 | -3.1551 |
| 23 | grok-4.20-beta-0309-reasoning | -5.7232 | 0.018 | -5.9281..-5.5065 | -4.7365 |

BT is retained as a reference diagnostic, not as the primary ranking. The Thurstone rating is the canonical comparison score.

---

## Pairwise Margin Map

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap.png)

Each cell is the mean signed comparison margin for the row model against the column model. Positive values mean the row model tends to beat the column model on stories written to the same required elements.

---

## What Is Measured

Every story must meaningfully incorporate ten required elements:
- character
- object
- concept
- attribute
- action
- method
- setting
- timeframe
- motivation
- tone

The comparison protocol keeps the prompt and required elements matched within each A-vs-B task. This makes the judgment about which story better satisfies the same creative brief, not about which model happened to receive an easier prompt.

Evaluator prompts still separate rubric-aligned observations from beyond-rubric observations, but the public model score is no longer an average of absolute 0-10 rubric grades. The public score is the model's position in the pairwise comparison graph.

---

## Method Summary

1. Generate or collect stories in the strict benchmark format.
2. Build matched A-vs-B comparison prompts for stories sharing the same required elements.
3. Run evaluator LLMs on those pairwise prompts.
4. Parse each evaluator response into signed margins and winner labels.
5. Correct measured side-A bias in signed margins.
6. Aggregate story-level pair margins into a global Thurstone-style model rating.
7. Use bootstrap uncertainty over stories and evaluators for confidence bands.

The current chart and leaderboard artifacts are produced by:

```bash
export PYTHONPATH=/mnt/r/writing2:/mnt/r/benchmark_utils:$PYTHONPATH

python aggregate_inter_llm_comparison_scores.py \
  --template-id pilot_2026_04_18_anchor_n20_fullroster_cap3_v1

python plot_inter_llm_comparison_charts.py
```

The plot script reads shared model display names, family colors, and model-brand logos through `/mnt/r/benchmark_utils`.

---

## Operational Notes

- Pairwise comparison is the canonical intake path for new models.
- Incremental comparison coverage should prioritize uncertainty near the top of the leaderboard, especially missing or inconclusive direct matchups among highly ranked models.
- Use `run_inter_llm_comparison_batch.py --pairs-file <path>` for manually selected high-value gaps.
- Use a new explicit `template_id` when the comparison prompt, evaluator roster, or benchmark-critical protocol changes materially.
- Gemini evaluators are fine on the fast router. Gemini is specifically slow on the batch router (`8040`), so split Gemini into a separate `8006` invocation when turnaround matters.
- Absolute rubric ratings and their old charts are archived; do not use them as the main public ranking going forward.

More operational detail is in [PIPELINES.md](PIPELINES.md) and [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md).

---

## Related Benchmarks

Multi-agent benchmarks:
- [PACT - Benchmarking LLM negotiation skill in multi-round buyer-seller bargaining](https://github.com/lechmazur/pact)
- [BAZAAR - Evaluating LLMs in Economic Decision-Making within a Competitive Simulated Market](https://github.com/lechmazur/bazaar)
- [Public Goods Game Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception Under Pressure](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)

Other benchmarks:
- [LLM Round-Trip Translation Benchmark](https://github.com/lechmazur/translation/)
- [Extended NYT Connections](https://github.com/lechmazur/nyt-connections/)
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)

Follow [@lechmazur](https://x.com/LechMazur) on X for other benchmarks and updates.
