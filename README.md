# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched stories in both orders and judge which is better. Their judgments produce relative scores for each writer model.

Higher ratings mean stronger estimated performance within this comparison set. Scores are centered at zero across all writer models in the comparison set.

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings_highlighted.png)

The ranking combines judgments from earlier and newer evaluator models. It covers **56 writer models**, **908 direct model pairings**, **15,172 distinct story pairs**, and **102,592 judgments**. Each direct model pairing can include stories from multiple matched prompts. The chart shows 26 selected models, with the six recent additions highlighted; the table lists every rated model with its overall rank.

The shaded ranges show how much scores vary across 300 resamples of stories and evaluators (bootstrap). The table gives the 95% bootstrap intervals. Estimated win chance is a model's average predicted probability of beating another model in the full comparison set.

### Leaderboard

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | Claude Fable 5.1 (high) | 3.796 | 93% | 3.702 to 3.896 |
| 2 | Claude Opus 5 (xhigh) | 3.777 | 93% | 3.726 to 3.836 |
| 3 | **Claude Opus 5.5 (high)** | 3.767 | 93% | 3.676 to 3.882 |
| 4 | GPT-6 Astra (high) | 3.455 | 91% | 3.381 to 3.519 |
| 5 | **Claude Opus 5 (high)** | 3.453 | 91% | 3.344 to 3.557 |
| 6 | GLM-5.3 (max) | 3.031 | 88% | 2.928 to 3.127 |
| 7 | Claude Fable 5 (high)§ | 2.872 | 86% | 2.803 to 2.946 |
| 8 | GPT-5.6 Sol (xhigh) | 2.488 | 83% | 2.407 to 2.561 |
| 9 | Kimi K3 | 2.452 | 82% | 2.383 to 2.527 |
| 10 | GPT-5.5 (xhigh) | 2.451 | 82% | 2.386 to 2.522 |
| 11 | GPT-5.6 Sol (high) | 2.299 | 81% | 2.217 to 2.368 |
| 12 | GPT-5.4 (medium) | 1.989 | 77% | 1.858 to 2.094 |
| 13 | GPT-5.4 (xhigh) | 1.982 | 77% | 1.864 to 2.080 |
| 14 | Claude Opus 4.7 (high)† | 1.782 | 75% | 1.683 to 1.872 |
| 15 | Claude Sonnet 4.6 Thinking 16K | 1.674 | 74% | 1.564 to 1.780 |
| 16 | **Xiaomi MiMo V2.6 Pro (thinking)※** | 1.594 | 73% | 1.449 to 1.747 |
| 17 | Claude Opus 4.6 Thinking 16K | 1.149 | 67% | 0.974 to 1.333 |
| 18 | Claude Opus 4.8 (xhigh) | 0.778 | 62% | 0.666 to 0.888 |
| 19 | Muse Spark 1.1 (high) | 0.774 | 62% | 0.672 to 0.876 |
| 20 | Muse Spark 1.3 (high) | 0.584 | 59% | 0.488 to 0.669 |
| 21 | DeepSeek V4 Pro (high) | 0.547 | 58% | 0.448 to 0.651 |
| 22 | GLM-5.2 (max) | 0.475 | 57% | 0.380 to 0.561 |
| 23 | **Grok 4.7 (high)** | 0.448 | 57% | 0.246 to 0.655 |
| 24 | GPT-5.2 (medium) | 0.353 | 55% | 0.201 to 0.517 |
| 25 | Claude Opus 4.8 (high)‡ | 0.263 | 54% | 0.163 to 0.371 |
| 26 | **Gemini 3.8 Flash (high)** | 0.215 | 53% | 0.079 to 0.368 |
| 27 | Qwen 3.8 Max¶ | 0.204 | 53% | 0.088 to 0.325 |
| 28 | Kimi K2.6 | 0.095 | 52% | 0.006 to 0.200 |
| 29 | Muse Spark 1.2 (high) | -0.028 | 50% | -0.126 to 0.067 |
| 30 | MiniMax-M3 | -0.063 | 49% | -0.197 to 0.069 |
| 31 | Mistral Medium 3.1 | -0.367 | 45% | -0.497 to -0.249 |
| 32 | **DeepSeek V4.1 Flash (high)** | -0.465 | 43% | -0.604 to -0.319 |
| 33 | DeepSeek V4 Pro Preview | -0.524 | 42% | -0.636 to -0.424 |
| 34 | Qwen3.8-27B^ | -0.641 | 40% | -0.813 to -0.480 |
| 35 | Qwen 3 Max Preview | -0.670 | 40% | -0.829 to -0.510 |
| 36 | Xiaomi MiMo V2.5 Pro | -0.677 | 40% | -0.801 to -0.545 |
| 37 | Gemini 3.7 Flash (high) | -0.729 | 39% | -0.853 to -0.614 |
| 38 | Qwen 3.6 Max Preview | -0.927 | 36% | -1.060 to -0.809 |
| 39 | GLM-5.1 | -1.030 | 35% | -1.229 to -0.844 |
| 40 | Kimi K2.5 Thinking | -1.071 | 34% | -1.225 to -0.904 |
| 41 | Xiaomi MiMo V2 Pro | -1.213 | 32% | -1.447 to -0.972 |
| 42 | Baidu Ernie 5.1 | -1.252 | 32% | -1.371 to -1.093 |
| 43 | Mistral Large 3 | -1.753 | 25% | -1.874 to -1.628 |
| 44 | Gemma 4 31B Reasoning | -1.869 | 24% | -1.985 to -1.778 |
| 45 | Gemini 3.5 Flash | -1.974 | 22% | -2.062 to -1.891 |
| 46 | ByteDance Seed2.0 Pro | -1.984 | 22% | -2.101 to -1.869 |
| 47 | Gemini 3.1 Pro Preview | -2.180 | 20% | -2.288 to -2.057 |
| 48 | Qwen 3.6 Plus | -2.263 | 19% | -2.423 to -2.101 |
| 49 | Mistral Medium 3.5 | -2.542 | 16% | -2.682 to -2.408 |
| 50 | Qwen 3.7 Max | -2.648 | 15% | -2.783 to -2.523 |
| 51 | Grok 4.6 (high) | -2.837 | 13% | -2.977 to -2.700 |
| 52 | DeepSeek V3.2 | -2.864 | 13% | -3.126 to -2.592 |
| 53 | GPT-OSS-120B | -3.109 | 11% | -3.238 to -2.992 |
| 54 | MiniMax-M2.7 | -3.753 | 7% | -3.898 to -3.622 |
| 55 | Grok 4.3 | -4.243 | 4% | -4.428 to -4.058 |
| 56 | Grok 4.5 (high) | -5.070 | 2% | -5.160 to -4.974 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Striped bars and badges identify incomplete story sets. Quality comparisons concern completed stories. The latest evaluations returned 23,085/23,148 planned judgments; 63 unavailable judgments are excluded from the scores. The Opus 5.5 high versus Opus 5 high comparison covers 50 matched prompts, with 298/300 usable judgments.

Grok 4.7 (high) versus Grok 4.6 (high): 50 matched prompts, 300/300 judgments. Xiaomi MiMo V2.6 Pro (thinking) versus Xiaomi MiMo V2.5 Pro: 50 matched prompts, 300/300 judgments.

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap_highlighted.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order. Earlier and newer evaluations contribute to both this chart and the rankings.

Every highlighted model has direct comparisons against all 25 other displayed models. Opus 5.5 high has now been compared with Fable 5.1 high on 50 matched prompts, Opus 5 xhigh on 60, and GPT-6 Astra high on 40. Fable 5.1 high versus Opus 5 xhigh covers 20 prompts. An additional 24 story comparisons check Fable and Opus 5 xhigh against four weaker opponents using prompts and evaluators already used for Opus 5.5. [Comparison sample sizes](data/writing_opus_precision_20260927/pair_stats.csv), [the additional comparison schedule](data/writing_opus_precision_20260927/matchup_schedule.csv), and [rank stability and evaluator sensitivity](data/writing_opus_precision_20260927/rank_uncertainty.md) provide the details.

## Additional Results

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

The matrix includes earlier and newer evaluator models. Each number shows how similarly two evaluators scored the story pairs they both read. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Orange indicates negative correlations, and blue indicates positive correlations. Blank cells lack enough varied judgments to calculate a correlation; the diagonal is omitted. Agreement on these stories does not establish evaluator accuracy.

GLM-5.1 / Muse Spark 1.1 (high): only two shared stories. [Shared-story counts](data/writing_opus_precision_20260927/evaluator_agreement.csv) accompany every evaluator pair.

### Word Count Compliance

![Story word counts](images/inter_llm_comparison_word_count_ci_highlighted.png)

Each dot is one completed story; diamonds mark model averages. Thin vertical lines show uncertainty around the averages. The shaded band is the 600–800-word target. The chart includes 10,362 completed stories from all 26 displayed models. This measures length rather than writing quality.

Six stories that exceeded 800 words were regenerated using their original prompts; the first replacement within 600–800 words was retained. The 12 comparisons that used a replaced story were rerun with the same evaluators and both story orders. The rankings and charts use these replacements. All 10,362 displayed stories now fall within the word limit.

### Combining Evaluations Over Time

Earlier and newer evaluators use the same instructions and scoring criteria. They have judged 1,200 of the same story pairs, covering all previously tested writer models. Different evaluator versions count separately, with one averaged judgment per evaluator on each story pair. Each story pair receives equal weight in the ranking. Ratings use a Thurstone statistical model with a correction for story presentation order.

The intervals reflect variation in completed comparisons. They do not account for how missing stories or judgments might change the scores, or how results would differ if only newer evaluators were used. Overlapping intervals mean small differences in rank may be uncertain.

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

Candidate combinations are proposed for coherence and originality, then independently rated. The strongest combination for each seed becomes a fixed brief used by every writer model. A typical brief might combine a neutron-star researcher, butterfly-wing dust, gradual change, a storm-damaged greenhouse, "after the flood," and kindled humility.

Evaluators reward integration rather than keyword inclusion: the required object should affect the plot, the motivation should produce a consequential choice, and the tone should shape the story's development. Both stories in every comparison answer the same brief, holding prompt difficulty constant. Evaluators also consider prose, coherence, character, originality, and overall effectiveness. The public score combines their choices; it is not an average 0-10 grade.

Because the combinations are pre-screened for creative potential, the benchmark measures story construction under deliberately combinable constraints—not completely free-form writing or recovery from arbitrary incoherent prompts.

---

## Method Summary

1. Generate stories in the benchmark format.
2. Build matched story-comparison prompts for models that wrote to the same required elements.
3. Show each pair in both story orders to reduce first- or second-position effects.
4. Repeat comparisons across evaluators and combine their choices.
5. When evaluator models change, compare their judgments on shared stories before combining results.
6. Calculate relative model scores and their uncertainty ranges.

---

## Qualitative Pair Reports

Each report describes the models and stories compared. The Opus 5.5, Grok 4.7, and MiMo V2.6 Pro reports use newer evaluators; earlier reports use the evaluators available at the time.

[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects twelve release-to-predecessor reports on a separate page.

New analyses give recurring writing habits, range and adaptability, and consistency separate treatment, with examples across different prompts. They examine repeated phrasing and story patterns as well as how flexibly each model changes its voice, tone, form, and narrative approach.

---

## Data, Stories, and Prompts

Story prompts are available under `prompts_wc/`, and generated stories under `stories_wc/<model>/`.

[Current ratings and chart data](data/writing_opus_precision_20260927/README.md) include machine-readable leaderboard scores and uncertainty intervals, direct head-to-head results, matched story-pair results, and evaluator diagnostics.

[Earlier benchmark data](data/README.md) links to the immutable August 23, 2026 data release. That archive contains the exact evaluator commentary for both story orders, excluded or superseded responses, and the accompanying source story and prompt texts.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates

- September 26, 2026: Added Claude Opus 5.5 high, Claude Opus 5 high, MiMo V2.6 Pro thinking, DeepSeek V4.1 Flash high, Gemini 3.8 Flash high, and Grok 4.7 high.
- September 5, 2026: Added GPT-6 Astra high, Muse Spark 1.3.
- September 2, 2026: Added Claude Fable 5.1.
- August 23, 2026: Published comparison data and written evaluations.
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
