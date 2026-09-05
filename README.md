# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched story pairs and choose which one is better. Those choices are combined into a relative comparison score.

Higher scores mean stronger performance against the other models tested. Scores are relative, not grades: zero is near the middle of this comparison set, and overlapping uncertainty ranges can indicate similarly rated models.

---

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Leaderboard

Current comparison set:

- 50 rated models
- 773 direct model pairings
- 79,507 evaluator judgments
- the rating combines compatible evaluator-v2 and evaluator-v3 evidence after bridge validation
- the chart focuses on selected current models; the table retains all rated models for historical comparison
- striped bars and markers identify models that completed fewer than 400 stories


| Rank | Model | Comparison score | Estimated win chance | Uncertainty range |
|-----:|:------|-----------------:|---------------------:|:------------------|
| 1 | Claude Opus 5 (xhigh) | 4.0 | 95% | 3.9 to 4.1 |
| 2 | Claude Fable 5.1 (high) | 4.0 | 94% | 3.9 to 4.1 |
| 3 | GPT-6 Astra (high) | 3.5 | 92% | 3.4 to 3.6 |
| 4 | GLM-5.3 (max) | 3.1 | 89% | 3.0 to 3.3 |
| 5 | Claude Fable 5 (high)§ | 3.1 | 88% | 3.0 to 3.1 |
| 6 | Kimi K3 | 2.7 | 85% | 2.6 to 2.8 |
| 7 | GPT-5.6 Sol (xhigh) | 2.7 | 84% | 2.6 to 2.7 |
| 8 | GPT-5.5 (xhigh) | 2.6 | 84% | 2.6 to 2.7 |
| 9 | GPT-5.6 Sol (high) | 2.5 | 83% | 2.4 to 2.6 |
| 10 | GPT-5.4 (medium) | 2.2 | 79% | 2.1 to 2.3 |
| 11 | GPT-5.4 (xhigh) | 2.2 | 79% | 2.1 to 2.3 |
| 12 | Claude Opus 4.7 (high)† | 2.0 | 77% | 1.9 to 2.1 |
| 13 | Claude Sonnet 4.6 Thinking 16K | 1.9 | 76% | 1.8 to 2.0 |
| 14 | Claude Opus 4.6 Thinking 16K | 1.4 | 69% | 1.2 to 1.5 |
| 15 | Claude Opus 4.8 (xhigh) | 1.0 | 64% | 0.9 to 1.1 |
| 16 | Muse Spark 1.1 (high) | 1.0 | 64% | 0.9 to 1.1 |
| 17 | Muse Spark 1.3 (high) | 0.8 | 61% | 0.7 to 0.9 |
| 18 | DeepSeek V4 Pro (high) | 0.7 | 61% | 0.6 to 0.9 |
| 19 | GLM-5.2 (max) | 0.6 | 60% | 0.5 to 0.7 |
| 20 | GPT-5.2 (medium) | 0.5 | 58% | 0.4 to 0.7 |
| 21 | Qwen 3.8 Max¶ | 0.5 | 57% | 0.3 to 0.6 |
| 22 | Claude Opus 4.8 (high)‡ | 0.5 | 57% | 0.3 to 0.6 |
| 23 | Kimi K2.6 | 0.3 | 55% | 0.2 to 0.4 |
| 24 | Muse Spark 1.2 (high) | 0.2 | 52% | 0.0 to 0.3 |
| 25 | MiniMax-M3 | 0.1 | 52% | 0.0 to 0.3 |
| 26 | Mistral Medium 3.1 | -0.2 | 47% | -0.3 to 0.0 |
| 27 | DeepSeek V4 Pro Preview | -0.3 | 45% | -0.4 to -0.2 |
| 28 | Xiaomi MiMo V2.5 Pro | -0.4 | 44% | -0.6 to -0.3 |
| 29 | Qwen 3 Max Preview | -0.5 | 43% | -0.6 to -0.3 |
| 30 | Qwen3.8-27B^ | -0.5 | 43% | -0.7 to -0.3 |
| 31 | Gemini 3.7 Flash (high) | -0.5 | 42% | -0.7 to -0.4 |
| 32 | Qwen 3.6 Max Preview | -0.7 | 39% | -0.9 to -0.6 |
| 33 | GLM-5.1 | -0.8 | 38% | -1.0 to -0.7 |
| 34 | Kimi K2.5 Thinking | -0.9 | 37% | -1.0 to -0.7 |
| 35 | Xiaomi MiMo V2 Pro | -1.0 | 35% | -1.2 to -0.8 |
| 36 | Baidu Ernie 5.1 | -1.0 | 35% | -1.2 to -0.9 |
| 37 | Mistral Large 3 | -1.6 | 27% | -1.7 to -1.5 |
| 38 | Gemma 4 31B Reasoning | -1.7 | 26% | -1.8 to -1.6 |
| 39 | Gemini 3.5 Flash | -1.8 | 24% | -1.9 to -1.7 |
| 40 | ByteDance Seed2.0 Pro | -1.8 | 24% | -2.0 to -1.7 |
| 41 | Gemini 3.1 Pro Preview | -2.1 | 22% | -2.1 to -1.9 |
| 42 | Qwen 3.6 Plus | -2.1 | 21% | -2.3 to -1.9 |
| 43 | Mistral Medium 3.5 | -2.4 | 18% | -2.5 to -2.2 |
| 44 | Qwen 3.7 Max | -2.5 | 17% | -2.6 to -2.3 |
| 45 | DeepSeek V3.2 | -2.7 | 15% | -3.0 to -2.4 |
| 46 | Grok 4.6 (high) | -2.7 | 14% | -2.9 to -2.6 |
| 47 | GPT-OSS-120B | -3.0 | 12% | -3.1 to -2.8 |
| 48 | MiniMax-M2.7 | -3.6 | 8% | -3.7 to -3.4 |
| 49 | Grok 4.3 | -4.1 | 5% | -4.3 to -3.9 |
| 50 | Grok 4.5 (high) | -4.9 | 2% | -5.0 to -4.8 |

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

This chart shows how similarly the evaluator models scored the same story pairs. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Its colorblind-safe scale uses orange for negative relationships and blue for positive relationships.

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

Candidate combinations are proposed for coherence and originality, then independently rated; the strongest set for each seed becomes a fixed brief used by every writer model. A typical brief might combine a neutron-star researcher, butterfly-wing dust, gradual change, a storm-damaged greenhouse, "after the flood," and kindled humility.

Evaluators reward integration rather than keyword inclusion: the required object should affect the plot, the motivation should produce a consequential choice, and the tone should shape the story's development. Both stories in every comparison answer the same brief, holding prompt difficulty constant. Evaluators also consider prose, coherence, character, originality, and overall effectiveness. The public score combines their choices; it is not an average 0-10 grade.

Because the combinations are pre-screened for creative potential, the benchmark measures story construction under deliberately combinable constraints—not completely free-form writing or recovery from arbitrary incoherent prompts.

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


[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects nine release-to-predecessor reports on a separate page.

---

## Public Artifacts

The published bundle includes the story prompts and generated story text files for models visible in the public comparison charts, plus the linked qualitative reports. Prompt files are under `prompts_wc/`; model outputs are under `stories_wc/<model>/`.

[Public benchmark data](data/README.md) provides machine-readable leaderboard, head-to-head, pair-story, and evaluator-diagnostic tables. It also links to an immutable data release containing the exact evaluator prose for both story orders, excluded or superseded responses, and the referenced story and prompt texts. Provider envelopes, request identifiers, internal paths, and implementation code are not published.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates

- September 5, 2026: Added GPT-6 Astra high, Muse Spark 1.3.
- September 2, 2026: Added Claude Fable 5.1.
- August 23, 2026: Published machine-readable comparison data and an auditable evaluator-prose release.
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
