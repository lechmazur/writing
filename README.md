# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched stories in both orders and judge which is better. Their judgments produce relative scores for each writer model.

Higher ratings mean stronger estimated performance within this comparison set. Scores are centered at zero across all writer models in the comparison set.

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings_highlighted.png)

The ranking combines judgments from earlier and newer evaluator models. It covers **56 writer models**, **908 direct model pairings**, **15,043 distinct story pairs**, and **101,819 judgments**. Each direct model pairing can include stories from multiple matched prompts. The chart shows 26 selected models, with the six recent additions highlighted; the table lists every rated model with its overall rank.

The shaded ranges show how much scores vary across 300 resamples of stories and evaluators (bootstrap). The table gives the 95% bootstrap intervals. Estimated win chance is a model's average predicted probability of beating another model in the full comparison set.

### Leaderboard

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | Claude Fable 5.1 (high) | 3.830 | 93% | 3.719 to 3.941 |
| 2 | Claude Opus 5 (xhigh) | 3.805 | 93% | 3.745 to 3.868 |
| 3 | **Claude Opus 5.5 (high)** | 3.757 | 93% | 3.660 to 3.867 |
| 4 | **Claude Opus 5 (high)** | 3.454 | 91% | 3.333 to 3.563 |
| 5 | GPT-6 Astra (high) | 3.442 | 91% | 3.371 to 3.513 |
| 6 | GLM-5.3 (max) | 3.029 | 88% | 2.911 to 3.131 |
| 7 | Claude Fable 5 (high)§ | 2.874 | 86% | 2.811 to 2.933 |
| 8 | GPT-5.6 Sol (xhigh) | 2.487 | 83% | 2.401 to 2.573 |
| 9 | GPT-5.5 (xhigh) | 2.451 | 82% | 2.389 to 2.515 |
| 10 | Kimi K3 | 2.451 | 82% | 2.369 to 2.524 |
| 11 | GPT-5.6 Sol (high) | 2.298 | 81% | 2.215 to 2.383 |
| 12 | GPT-5.4 (medium) | 1.992 | 77% | 1.868 to 2.129 |
| 13 | GPT-5.4 (xhigh) | 1.984 | 77% | 1.887 to 2.096 |
| 14 | Claude Opus 4.7 (high)† | 1.783 | 75% | 1.683 to 1.883 |
| 15 | Claude Sonnet 4.6 Thinking 16K | 1.675 | 74% | 1.574 to 1.775 |
| 16 | **Xiaomi MiMo V2.6 Pro (thinking)※** | 1.596 | 73% | 1.460 to 1.726 |
| 17 | Claude Opus 4.6 Thinking 16K | 1.152 | 67% | 0.984 to 1.313 |
| 18 | Claude Opus 4.8 (xhigh) | 0.777 | 62% | 0.658 to 0.886 |
| 19 | Muse Spark 1.1 (high) | 0.773 | 62% | 0.672 to 0.860 |
| 20 | Muse Spark 1.3 (high) | 0.586 | 59% | 0.490 to 0.692 |
| 21 | DeepSeek V4 Pro (high) | 0.547 | 58% | 0.427 to 0.658 |
| 22 | GLM-5.2 (max) | 0.474 | 57% | 0.374 to 0.568 |
| 23 | **Grok 4.7 (high)** | 0.449 | 57% | 0.253 to 0.655 |
| 24 | GPT-5.2 (medium) | 0.356 | 55% | 0.185 to 0.509 |
| 25 | Claude Opus 4.8 (high)‡ | 0.262 | 54% | 0.165 to 0.388 |
| 26 | **Gemini 3.8 Flash (high)** | 0.217 | 53% | 0.088 to 0.337 |
| 27 | Qwen 3.8 Max¶ | 0.204 | 53% | 0.094 to 0.314 |
| 28 | Kimi K2.6 | 0.095 | 52% | 0.001 to 0.192 |
| 29 | Muse Spark 1.2 (high) | -0.027 | 50% | -0.116 to 0.067 |
| 30 | MiniMax-M3 | -0.061 | 49% | -0.198 to 0.061 |
| 31 | Mistral Medium 3.1 | -0.367 | 45% | -0.495 to -0.222 |
| 32 | **DeepSeek V4.1 Flash (high)** | -0.464 | 43% | -0.594 to -0.309 |
| 33 | DeepSeek V4 Pro Preview | -0.523 | 42% | -0.634 to -0.424 |
| 34 | Qwen3.8-27B^ | -0.641 | 40% | -0.837 to -0.460 |
| 35 | Qwen 3 Max Preview | -0.669 | 40% | -0.861 to -0.472 |
| 36 | Xiaomi MiMo V2.5 Pro | -0.677 | 40% | -0.798 to -0.555 |
| 37 | Gemini 3.7 Flash (high) | -0.728 | 39% | -0.829 to -0.593 |
| 38 | Qwen 3.6 Max Preview | -0.927 | 36% | -1.041 to -0.802 |
| 39 | GLM-5.1 | -1.032 | 35% | -1.214 to -0.859 |
| 40 | Kimi K2.5 Thinking | -1.070 | 34% | -1.258 to -0.909 |
| 41 | Xiaomi MiMo V2 Pro | -1.212 | 32% | -1.440 to -0.994 |
| 42 | Baidu Ernie 5.1 | -1.257 | 32% | -1.412 to -1.080 |
| 43 | Mistral Large 3 | -1.754 | 25% | -1.896 to -1.616 |
| 44 | Gemma 4 31B Reasoning | -1.870 | 24% | -1.964 to -1.768 |
| 45 | Gemini 3.5 Flash | -1.975 | 22% | -2.054 to -1.893 |
| 46 | ByteDance Seed2.0 Pro | -1.984 | 22% | -2.111 to -1.843 |
| 47 | Gemini 3.1 Pro Preview | -2.199 | 20% | -2.316 to -2.094 |
| 48 | Qwen 3.6 Plus | -2.262 | 19% | -2.414 to -2.088 |
| 49 | Mistral Medium 3.5 | -2.543 | 16% | -2.681 to -2.399 |
| 50 | Qwen 3.7 Max | -2.650 | 15% | -2.776 to -2.525 |
| 51 | Grok 4.6 (high) | -2.837 | 14% | -2.989 to -2.704 |
| 52 | DeepSeek V3.2 | -2.864 | 13% | -3.091 to -2.611 |
| 53 | GPT-OSS-120B | -3.136 | 11% | -3.246 to -3.003 |
| 54 | MiniMax-M2.7 | -3.754 | 7% | -3.917 to -3.633 |
| 55 | Grok 4.3 | -4.244 | 4% | -4.422 to -4.050 |
| 56 | Grok 4.5 (high) | -5.071 | 2% | -5.156 to -4.989 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Striped bars and badges identify incomplete story sets. Quality comparisons concern completed stories. The latest evaluations returned 22,312/22,374 planned judgments; 62 unavailable judgments are excluded from the scores. The Opus 5.5 high versus Opus 5 high comparison covers 50 matched prompts, with 298/300 usable judgments.

Grok 4.7 (high) versus Grok 4.6 (high): 50 matched prompts, 300/300 judgments. Xiaomi MiMo V2.6 Pro (thinking) versus Xiaomi MiMo V2.5 Pro: 50 matched prompts, 300/300 judgments.

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap_highlighted.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order. Earlier and newer evaluations contribute to both this chart and the rankings.

Every highlighted model has direct comparisons against all 25 other displayed models. The 70 newly added matchups cover 419 matched story pairs, with 3–10 prompts per matchup selected before evaluation. Each story pair was assigned three eligible newer evaluators, reading both orders. [Comparison sample sizes](data/writing_missing_matchups_20260927/pair_stats.csv) and the [new matchup schedule](data/writing_missing_matchups_20260927/matchup_schedule.csv) give the coverage of individual matchups.

## Additional Results

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

The matrix includes earlier and newer evaluator models. Each number shows how similarly two evaluators scored the story pairs they both read. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Orange indicates negative correlations, and blue indicates positive correlations. Blank cells lack enough varied judgments to calculate a correlation; the diagonal is omitted. Agreement on these stories does not establish evaluator accuracy.

GLM-5.1 / Muse Spark 1.1 (high): only two shared stories. [Shared-story counts](data/writing_missing_matchups_20260927/evaluator_agreement.csv) accompany every evaluator pair.

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

[Current ratings and chart data](data/writing_missing_matchups_20260927/README.md) include machine-readable leaderboard scores and uncertainty intervals, direct head-to-head results, matched story-pair results, and evaluator diagnostics.

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
