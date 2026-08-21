# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched story pairs and choose which one is better. Those choices are combined into a relative comparison score.

Higher scores mean stronger performance against the other models tested. Scores are relative, not grades: zero is near the middle of this comparison set, and overlapping uncertainty ranges can indicate similarly rated models.

---

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Leaderboard

Current comparison set:

- 47 rated models
- 630 direct model pairings
- 67,178 evaluator judgments
- the rating combines compatible evaluator-v2 and evaluator-v3 evidence after bridge validation
- the chart focuses on current models; the table retains all rated models for historical comparison
- striped bars and markers identify models that completed fewer than 400 stories


| Rank | Model | Comparison score | Estimated win chance | Uncertainty range |
|-----:|:------|-----------------:|---------------------:|:------------------|
| 1 | Claude Opus 5 (xhigh) | 4.2 | 96% | 4.1 to 4.2 |
| 2 | GLM-5.3 (max) | 3.5 | 92% | 3.3 to 3.6 |
| 3 | Claude Fable 5 (high)§ | 3.2 | 90% | 3.1 to 3.3 |
| 4 | Kimi K3 | 2.9 | 88% | 2.8 to 3.0 |
| 5 | GPT-5.6 Sol (xhigh) | 2.8 | 87% | 2.7 to 2.9 |
| 6 | GPT-5.5 (xhigh) | 2.7 | 86% | 2.7 to 2.8 |
| 7 | GPT-5.6 Sol (high) | 2.7 | 85% | 2.6 to 2.7 |
| 8 | GPT-5.4 (xhigh) | 2.3 | 81% | 2.2 to 2.4 |
| 9 | GPT-5.4 (medium) | 2.2 | 81% | 2.1 to 2.4 |
| 10 | Claude Opus 4.7 (adaptive)† | 2.1 | 79% | 2.0 to 2.2 |
| 11 | Claude Sonnet 4.6 (16K) | 2.0 | 78% | 1.9 to 2.1 |
| 12 | Claude Opus 4.6 (16K) | 1.4 | 71% | 1.2 to 1.6 |
| 13 | Muse Spark 1.1 (high) | 1.2 | 68% | 1.1 to 1.3 |
| 14 | Claude Opus 4.8 (xhigh) | 1.2 | 67% | 1.1 to 1.3 |
| 15 | DeepSeek V4 Pro (high) | 0.9 | 64% | 0.8 to 1.1 |
| 16 | GLM-5.2 (max) | 0.8 | 62% | 0.7 to 0.9 |
| 17 | Qwen 3.8 Max¶ | 0.7 | 60% | 0.5 to 0.8 |
| 18 | Claude Opus 4.8 (high)‡ | 0.7 | 60% | 0.6 to 0.8 |
| 19 | GPT-5.2 (medium) | 0.7 | 60% | 0.5 to 0.8 |
| 20 | Muse Spark 1.2 (high) | 0.6 | 58% | 0.4 to 0.8 |
| 21 | Kimi K2.6 | 0.5 | 57% | 0.3 to 0.6 |
| 22 | MiniMax-M3 | 0.4 | 56% | 0.2 to 0.5 |
| 23 | Qwen3.8-27B^ | 0.1 | 51% | -0.2 to 0.3 |
| 24 | Mistral Medium 3.1 | 0.0 | 50% | -0.1 to 0.1 |
| 25 | DeepSeek V4 Pro Preview | -0.2 | 47% | -0.3 to 0.0 |
| 26 | Xiaomi MiMo V2.5 Pro | -0.3 | 46% | -0.4 to -0.1 |
| 27 | Qwen 3 Max Preview | -0.3 | 45% | -0.5 to -0.1 |
| 28 | Gemini 3.7 Flash (high) | -0.4 | 44% | -0.5 to -0.2 |
| 29 | Qwen 3.6 Max Preview | -0.6 | 41% | -0.7 to -0.4 |
| 30 | GLM-5.1 | -0.7 | 40% | -0.8 to -0.5 |
| 31 | Kimi K2.5 | -0.7 | 39% | -0.9 to -0.5 |
| 32 | Xiaomi MiMo V2 Pro | -0.8 | 37% | -1.1 to -0.6 |
| 33 | Baidu Ernie 5.1 | -0.9 | 37% | -1.0 to -0.7 |
| 34 | Mistral Large 3 | -1.5 | 28% | -1.6 to -1.3 |
| 35 | Gemma 4 31B Reasoning | -1.6 | 27% | -1.7 to -1.5 |
| 36 | ByteDance Seed2.0 Pro | -1.7 | 26% | -1.8 to -1.5 |
| 37 | Gemini 3.5 Flash | -1.7 | 26% | -1.7 to -1.6 |
| 38 | Qwen 3.6 Plus | -1.9 | 23% | -2.1 to -1.7 |
| 39 | Gemini 3.1 Pro Preview | -1.9 | 22% | -2.1 to -1.8 |
| 40 | Mistral Medium 3.5 | -2.2 | 20% | -2.4 to -2.0 |
| 41 | Qwen 3.7 Max | -2.3 | 18% | -2.4 to -2.2 |
| 42 | DeepSeek V3.2 | -2.5 | 16% | -2.8 to -2.3 |
| 43 | Grok 4.6 (high) | -2.7 | 14% | -2.9 to -2.5 |
| 44 | GPT-OSS-120B | -2.9 | 13% | -3.0 to -2.8 |
| 45 | MiniMax-M2.7 | -3.4 | 8% | -3.6 to -3.3 |
| 46 | Grok 4.3 | -3.9 | 5% | -4.1 to -3.8 |
| 47 | Grok 4.5 (high) | -4.8 | 2% | -4.9 to -4.7 |

### Coverage Note

- † Claude Opus 4.7 completed 347 of 400 stories. Only completed stories were compared.
- ‡ Claude Opus 4.8 high completed 399 of 400 stories. Only completed stories were compared.
- § Claude Fable 5 high completed 395 of 400 stories. Only completed stories were compared.
- ¶ Qwen 3.8 Max completed 398 of 400 stories after one audited recovery pass. Only completed stories were compared.
- ^ Qwen3.8-27B completed 389 of 400 stories after one audited recovery pass. Only completed stories were compared.

---

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order.

---

## Diagnostics

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

This chart shows how similarly the evaluator models scored the same story pairs. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns.

### Word Count Compliance

![Word count compliance](images/inter_llm_comparison_word_count_ci.png)

Each dot is one story, and each diamond is a model's average length. Thin vertical lines show uncertainty around the averages. The shaded band is the 600-800-word target. This chart measures story length, not writing quality.

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

Evaluators consider required-element use, prose, coherence, character, originality, and overall effectiveness. The public score combines their choices; it is not an average 0-10 grade.

---

## Method Summary

1. Generate stories in the benchmark format.
2. Build matched story-comparison prompts for models that wrote to the same required elements.
3. Show each pair in both story orders to reduce first- or second-position effects.
4. Repeat comparisons across evaluators and combine their choices.
5. When an evaluator roster changes, validate shared prompts and bridge matchups before combining evidence.
6. Calculate relative model scores and their uncertainty ranges.

---

## Qualitative Pair Reports


[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects the six highlighted model reports on a separate page.

---

## Public Artifacts

The published bundle includes the story prompts and generated story text files for models visible in the public comparison charts, plus the linked qualitative reports. Prompt files are under `prompts_wc/`; model outputs are under `stories_wc/<model>/`.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates
- August 20, 2026: Added Muse Spark 1.2 high, DeepSeek V4 Pro high, Qwen 3.8 Max, Gemini 3.7 Flash high, and Grok 4.6 high. Added predecessor reports.
- July 25, 2026: Added Claude Opus 5.
- July 18, 2026: Added Kimi K3, updated evaluators.
- July 14, 2026: Added GPT-5.6, Muse Spark 1.1 high, and Grok 4.5.
- July 9, 2026: Added Grok 4.5.
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
