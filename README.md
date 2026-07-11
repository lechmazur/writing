# LLM Creative Story-Writing Benchmark

This benchmark measures short-fiction writing with **head-to-head story comparisons**. Models write stories to the same constrained creative briefs, and evaluator LLMs compare pairs of stories written for the same required elements. Those pairwise judgments are aggregated into a global comparison score.

Higher scores mean a model more often wins direct story comparisons against the rest of the pool. The exact score scale is relative to this comparison graph, so differences and confidence intervals matter more than the absolute number.

---

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Leaderboard

Current comparison set:

- 38 rated models
- 423 direct model pairings
- about 49.1k parsed evaluator judgments
- uncertainty resampled across both stories and evaluators
- side-position bias correction enabled
- the main chart above hides chart-suppressed models for readability; this table includes every rated model
- Markers indicate partial story coverage

| Rank | Model | Comparison Score | Win Prob vs Pool | 95% CI |
|-----:|:------|-----------------:|-----------------:|:-------|
| 1 | Claude Fable 5 (high)§ | 3.3 | 0.91 | 3.2..3.4 |
| 2 | GPT-5.5 (xhigh) | 3.1 | 0.89 | 3.0..3.1 |
| 3 | GPT-5.6 Sol (xhigh) | 3.0 | 0.88 | 2.9..3.0 |
| 4 | gpt-5.4-xhigh | 2.8 | 0.87 | 2.7..3.0 |
| 5 | GPT-5.6 Sol (high) | 2.8 | 0.86 | 2.7..2.9 |
| 6 | gpt-5.4-medium | 2.7 | 0.86 | 2.6..2.9 |
| 7 | claude-opus-4-7-adaptive† | 2.5 | 0.83 | 2.4..2.6 |
| 8 | claude-sonnet-4-6-16K | 2.3 | 0.82 | 2.2..2.4 |
| 9 | claude-opus-4-6-16K | 1.8 | 0.75 | 1.6..2.0 |
| 10 | Claude Opus 4.8 (xhigh) | 1.5 | 0.71 | 1.3..1.6 |
| 11 | Muse Spark 1.1 (high) | 1.4 | 0.71 | 1.3..1.6 |
| 12 | gpt-5.2-medium | 1.0 | 0.65 | 0.8..1.2 |
| 13 | GLM-5.2 (max) | 1.0 | 0.64 | 0.9..1.1 |
| 14 | Claude Opus 4.8 (high)‡ | 0.9 | 0.64 | 0.8..1.1 |
| 15 | Kimi K2.6 | 0.8 | 0.61 | 0.6..0.9 |
| 16 | MiniMax-M3 | 0.7 | 0.60 | 0.5..0.8 |
| 17 | Mistral Medium 3.1 | 0.3 | 0.54 | 0.1..0.4 |
| 18 | DeepSeek V4 Pro | 0.2 | 0.52 | 0.0..0.3 |
| 19 | Xiaomi MiMo V2.5 Pro | 0.0 | 0.50 | -0.2..0.1 |
| 20 | qwen3-max-preview | 0.0 | 0.49 | -0.2..0.2 |
| 21 | qwen3.6-max-preview | -0.3 | 0.45 | -0.4..-0.2 |
| 22 | glm-5.1 | -0.4 | 0.43 | -0.7..-0.2 |
| 23 | kimi-k2.5 | -0.5 | 0.42 | -0.7..-0.3 |
| 24 | Baidu Ernie 5.1 | -0.6 | 0.41 | -0.8..-0.4 |
| 25 | mimo-v2-pro | -0.6 | 0.40 | -0.9..-0.4 |
| 26 | Mistral Large 3 | -1.3 | 0.31 | -1.5..-1.2 |
| 27 | Gemma 4 31B Reasoning | -1.3 | 0.30 | -1.5..-1.2 |
| 28 | Gemini 3.5 Flash | -1.4 | 0.29 | -1.6..-1.4 |
| 29 | ByteDance Seed2.0 Pro | -1.5 | 0.28 | -1.6..-1.3 |
| 30 | Gemini 3.1 Pro Preview | -1.8 | 0.25 | -1.9..-1.6 |
| 31 | qwen3.6-plus | -1.8 | 0.25 | -2.0..-1.5 |
| 32 | Mistral Medium 3.5 | -2.0 | 0.22 | -2.2..-1.8 |
| 33 | Qwen 3.7 Max | -2.0 | 0.21 | -2.2..-1.9 |
| 34 | deepseek-v32 | -2.3 | 0.18 | -2.6..-2.1 |
| 35 | GPT-OSS-120B | -2.6 | 0.15 | -2.8..-2.5 |
| 36 | minimax-m2.7 | -3.2 | 0.10 | -3.4..-3.1 |
| 37 | grok-4.3 | -3.7 | 0.06 | -3.9..-3.5 |
| 38 | Grok 4.5 (high) | -4.6 | 0.03 | -4.7..-4.5 |

### Coverage Note

- † Claude Opus 4.7 refused some story-generation prompts in this run. It produced 347 completed stories out of 400 prompts. The comparison score uses completed stories only; no score was imputed for refused prompts.
- ‡ Claude Opus 4.8 high refused one story-generation prompt in this run. It produced 399 completed stories out of 400 prompts. The comparison score uses completed stories only; no score was imputed for the refused prompt.
- § Claude Fable 5 high refused five story-generation prompts in this run. It produced 395 completed stories out of 400 prompts. The comparison score uses completed stories only; no score was imputed for refused prompts.

---

## Grok 4.5 High Failure Audit

Grok 4.5 high placed last in the current comparison set, so I also ran a quote-based poor-writing audit across its 400 story outputs. The audit found 1,200 concrete examples. Its worst recurring tendency is style-over-substance: high-concept or mystical language is asserted before the story has stable rules, scene mechanics, or physical continuity.

Common failure modes:

- pseudo-mechanisms that treat feelings, vows, symbols, or abstractions as if they were engineered physical systems
- plot solutions stated as outcomes instead of earned through observable actions
- compressed premise labels that never become clear people, tools, places, or institutions
- continuity errors where objects, constraints, time, or environmental conditions drift between adjacent beats
- overloaded abstract sentences that sound portentous but do not parse cleanly

Selected examples:

| Quote | Issue |
|:------|:------|
| "thermal signatures left by feelings" | Treats emotion as a long-lived heat source without establishing rules. |
| "deathly vitality" | Uses a self-canceling phrase, then repeats it as if repetition adds meaning. |
| "While reality shifts transformed the world outside the walls remained a haven of perfect silence." | The sentence collapses grammatically before the scene can work. |
| "the pioneering cart glider contemplated new applications" | Turns a vehicle into a thinking character without setup. |
| "dust from butterfly wing that preprocesses reality via decay" | Stacks concepts until the mechanism becomes incoherent. |
| "a small diving apparatus" for a deep underwater expedition | Uses an implausibly tiny tool to solve an extreme-environment problem. |
| "altered to rapid short pants" | A typo turns a tense beat into accidental comedy. |
| "journeyed across a giant's nap" | Treats an abstract or impossible setting as a traversable place without grounding it. |
| "integrity was assured by design" because vows would collapse together | Mistakes mutual fragility for a robust system. |
| "storm diverting slightly thanks to accurate monitoring" | Confuses observing a storm with controlling one. |

---

## Pairwise Margin Map

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap.png)

Each cell is the average signed comparison margin for the row model against the column model. Positive values mean the row model tended to beat the column model on stories written to the same required elements. Both axes are ordered from best to worst by the current Thurstone leaderboard.

---

## Diagnostics

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

This matrix shows how similarly evaluator models used the signed pairwise-margin scale on shared comparison tasks. Higher Pearson correlation means closer agreement between evaluators.

### Word Count Compliance

![Word count compliance](images/inter_llm_comparison_word_count_ci.png)

This is an input-compliance diagnostic, not a quality ranking. It shows individual completed story lengths, plus model-level mean length and 95% confidence intervals against the 600-800 word target range. Models are sorted alphabetically by display name.

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

The comparison protocol keeps the prompt and required elements matched within each story pair. This makes the judgment about which story better satisfies the same creative brief, rather than which model happened to receive an easier prompt.

Evaluator prompts separate rubric-aligned observations from important beyond-rubric observations, but the public model score is not an average absolute grade. It is the model's position in the pairwise comparison graph.

---

## Method Summary

1. Generate stories in the benchmark format.
2. Build matched story-comparison prompts for models that wrote to the same required elements.
3. Compare both visible story orders to reduce position bias.
4. Parse evaluator responses into winner labels and signed margins.
5. Correct measured side-position bias in signed margins.
6. Average opposite-order judgments before story-level aggregation.
7. Aggregate story-level pair margins into a global comparison score.
8. Bootstrap over stories and evaluators to estimate uncertainty.

The rating chart and pairwise margin map use shared display names, family colors, and model-brand logos where available. The pairwise margin map uses the current Thurstone leaderboard order on both axes. Its x-axis logo strip intentionally sits below the chart, with reserved bottom margin so the plotted grid remains unobscured.

---

## Public Artifacts

The published bundle includes the story prompts and generated story text files for models visible in the public comparison charts. Prompt files are under `prompts_wc/`; model outputs are under `stories_wc/<model>/`.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates
- July 11, 2026: Expanded direct-comparison coverage for closely ranked models and refreshed the leaderboard and charts.
- July 10, 2026: Added GPT-5.6 xhigh and refreshed the pairwise comparison charts.
- July 9, 2026: Added GPT-5.6 high, Muse Spark 1.1 high, and Grok 4.5 high; refreshed the pairwise comparison charts and added a quote-based Grok failure audit.
- June 9, 2026: Added Claude Fable 5.
- May 29, 2026: Added Claude Opus 4.8 high and xhigh.
- May 26, 2026: Ernie 5.1, Qwen 3.7 Max, Mistral Medium 3.5, and Grok 4.3 added.
- May 20, 2026: Added Gemini 3.5 Flash.
- Apr 29, 2026: Refreshed the leaderboard with newer models, including GPT-5.5, Kimi K2.6, DeepSeek V4 Pro, Xiaomi MiMo V2.5 Pro, Qwen 3 Max Preview, Gemini 3.1 Pro Preview, ByteDance Seed2.0 Pro, Qwen 3.6 Max Preview, and MiniMax-M2.7.

---

## Related Benchmarks

Multi-agent benchmarks:

- [PACT - Benchmarking LLM negotiation skill in multi-round buyer-seller bargaining](https://github.com/lechmazur/pact)
- [BAZAAR - Evaluating LLMs in Economic Decision-Making within a Competitive Simulated Market](https://github.com/lechmazur/bazaar)
- [Buyout Game - Multi-Agent Negotiation and Coalition Benchmark](https://github.com/lechmazur/buyout_game)
- [LLM Debate Benchmark](https://github.com/lechmazur/debate)
- [Public Goods Game Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception Under Pressure](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)
- [LLM Persuasion Benchmark](https://github.com/lechmazur/persuasion)

Other benchmarks:

- [LLM Position Bias Benchmark](https://github.com/lechmazur/position_bias)
- [LLM Round-Trip Translation Benchmark](https://github.com/lechmazur/translation/)
- [Extended NYT Connections](https://github.com/lechmazur/nyt-connections/)
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Sycophancy Benchmark](https://github.com/lechmazur/sycophancy)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)

Follow [@lechmazur](https://x.com/LechMazur) on X for other benchmarks and updates.
