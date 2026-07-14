# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched story pairs and choose which one is better. Those choices are combined into a relative comparison score.

Higher scores mean stronger performance against the other models tested. Scores are relative, not grades: zero is near the middle of this comparison set, and overlapping uncertainty ranges can indicate similarly rated models.

---

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Leaderboard

Current comparison set:

- 38 rated models
- 423 direct model pairings
- about 49,100 evaluator judgments
- the chart focuses on current models; the table retains all rated models for historical comparison
- striped bars and markers identify models that completed fewer than 400 stories

Labels such as `high`, `xhigh`, `max`, and `adaptive` identify the reasoning setting used for that model.
Estimated win chance is the model's average expected chance against another model in the full comparison set.

| Rank | Model | Comparison score | Estimated win chance | Uncertainty range |
|-----:|:------|-----------------:|---------------------:|:------------------|
| 1 | Claude Fable 5 (high)§ | 3.3 | 91% | 3.2 to 3.4 |
| 2 | GPT-5.5 (xhigh) | 3.1 | 89% | 3.0 to 3.1 |
| 3 | GPT-5.6 Sol (xhigh) | 3.0 | 88% | 2.9 to 3.0 |
| 4 | GPT-5.4 (xhigh) | 2.8 | 87% | 2.7 to 3.0 |
| 5 | GPT-5.6 Sol (high) | 2.8 | 86% | 2.7 to 2.9 |
| 6 | GPT-5.4 (medium) | 2.7 | 86% | 2.6 to 2.9 |
| 7 | Claude Opus 4.7 (adaptive)† | 2.5 | 83% | 2.4 to 2.6 |
| 8 | Claude Sonnet 4.6 (16K) | 2.3 | 82% | 2.2 to 2.4 |
| 9 | Claude Opus 4.6 (16K) | 1.8 | 75% | 1.6 to 2.0 |
| 10 | Claude Opus 4.8 (xhigh) | 1.5 | 71% | 1.3 to 1.6 |
| 11 | Muse Spark 1.1 (high) | 1.4 | 71% | 1.3 to 1.6 |
| 12 | GPT-5.2 (medium) | 1.0 | 65% | 0.8 to 1.2 |
| 13 | GLM-5.2 (max) | 1.0 | 64% | 0.9 to 1.1 |
| 14 | Claude Opus 4.8 (high)‡ | 0.9 | 64% | 0.8 to 1.1 |
| 15 | Kimi K2.6 | 0.8 | 61% | 0.6 to 0.9 |
| 16 | MiniMax-M3 | 0.7 | 60% | 0.5 to 0.8 |
| 17 | Mistral Medium 3.1 | 0.3 | 54% | 0.1 to 0.4 |
| 18 | DeepSeek V4 Pro | 0.2 | 52% | 0.0 to 0.3 |
| 19 | Xiaomi MiMo V2.5 Pro | 0.0 | 50% | -0.2 to 0.1 |
| 20 | Qwen 3 Max Preview | 0.0 | 49% | -0.2 to 0.2 |
| 21 | Qwen 3.6 Max Preview | -0.3 | 45% | -0.4 to -0.2 |
| 22 | GLM-5.1 | -0.4 | 43% | -0.7 to -0.2 |
| 23 | Kimi K2.5 | -0.5 | 42% | -0.7 to -0.3 |
| 24 | Baidu Ernie 5.1 | -0.6 | 41% | -0.8 to -0.4 |
| 25 | Xiaomi MiMo V2 Pro | -0.6 | 40% | -0.9 to -0.4 |
| 26 | Mistral Large 3 | -1.3 | 31% | -1.5 to -1.2 |
| 27 | Gemma 4 31B Reasoning | -1.3 | 30% | -1.5 to -1.2 |
| 28 | Gemini 3.5 Flash | -1.4 | 29% | -1.6 to -1.4 |
| 29 | ByteDance Seed 2.0 Pro | -1.5 | 28% | -1.6 to -1.3 |
| 30 | Gemini 3.1 Pro Preview | -1.8 | 25% | -1.9 to -1.6 |
| 31 | Qwen 3.6 Plus | -1.8 | 25% | -2.0 to -1.5 |
| 32 | Mistral Medium 3.5 | -2.0 | 22% | -2.2 to -1.8 |
| 33 | Qwen 3.7 Max | -2.0 | 21% | -2.2 to -1.9 |
| 34 | DeepSeek V3.2 | -2.3 | 18% | -2.6 to -2.1 |
| 35 | GPT-OSS-120B | -2.6 | 15% | -2.8 to -2.5 |
| 36 | MiniMax-M2.7 | -3.2 | 10% | -3.4 to -3.1 |
| 37 | Grok 4.3 | -3.7 | 6% | -3.9 to -3.5 |
| 38 | Grok 4.5 (high) | -4.6 | 3% | -4.7 to -4.5 |

### Coverage Note

- † Claude Opus 4.7 completed 347 of 400 stories. Only completed stories were compared.
- ‡ Claude Opus 4.8 high completed 399 of 400 stories. Only completed stories were compared.
- § Claude Fable 5 high completed 395 of 400 stories. Only completed stories were compared.

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
5. Calculate relative model scores and their uncertainty ranges.

---

## Public Artifacts

The published bundle includes the story prompts and generated story text files for models visible in the public comparison charts. Prompt files are under `prompts_wc/`; model outputs are under `stories_wc/<model>/`.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates
- July 14, 2026: Added GPT-5.6, Muse Spark 1.1 high, and Grok 4.5.
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
