# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched stories in both orders and judge which is better. Their judgments produce relative scores for each writer model.

Higher ratings mean stronger estimated performance within this comparison set. Scores are centered at zero across all writer models in the comparison set.

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings_highlighted.png)

The ranking combines judgments from earlier and newer evaluator models. It covers **59 writer models**, **977 direct model pairings**, **16,552 distinct story pairs**, and **110,748 judgments**. Each direct model pairing can include stories from multiple matched prompts. The chart shows 23 selected models; the table lists every rated model with its overall rank. Highlighted models: Gemini 4 Argon (high), Muse Wonder (high).

The shaded ranges show how much scores vary across 300 resamples of stories and evaluators (bootstrap). The table gives the 95% bootstrap intervals. Estimated win chance is a model's average predicted probability of beating another model in the full comparison set.

### Leaderboard

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | Claude Fable 5.1 (high) | 3.756 | 93% | 3.675 to 3.850 |
| 2 | Claude Opus 5 (xhigh) | 3.730 | 93% | 3.672 to 3.784 |
| 3 | Claude Opus 5.5 (high) | 3.715 | 93% | 3.621 to 3.809 |
| 4 | GPT-6 Astra (high) | 3.443 | 91% | 3.374 to 3.508 |
| 5 | Claude Opus 5 (high) | 3.372 | 91% | 3.271 to 3.471 |
| 6 | GLM-5.3 (max) | 3.028 | 88% | 2.942 to 3.107 |
| 7 | Claude Fable 5 (high)§ | 2.853 | 87% | 2.790 to 2.920 |
| 8 | GPT-5.6 Sol (xhigh) | 2.469 | 83% | 2.395 to 2.543 |
| 9 | GPT-5.5 (xhigh) | 2.433 | 82% | 2.366 to 2.496 |
| 10 | Kimi K3 | 2.420 | 82% | 2.342 to 2.501 |
| 11 | GPT-5.6 Sol (high) | 2.280 | 81% | 2.203 to 2.371 |
| 12 | GPT-5.4 (medium) | 1.968 | 77% | 1.846 to 2.108 |
| 13 | GPT-5.4 (xhigh) | 1.962 | 77% | 1.848 to 2.075 |
| 14 | **Muse Wonder (high)** | 1.960 | 77% | 1.870 to 2.053 |
| 15 | Claude Opus 4.7 (high)† | 1.764 | 75% | 1.658 to 1.871 |
| 16 | Claude Sonnet 4.6 Thinking 16K | 1.655 | 73% | 1.549 to 1.754 |
| 17 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.596 | 73% | 1.453 to 1.713 |
| 18 | Claude Opus 4.6 Thinking 16K | 1.128 | 67% | 0.968 to 1.289 |
| 19 | **Gemini 4 Argon (high)** | 0.800 | 62% | 0.683 to 0.918 |
| 20 | Claude Opus 4.8 (xhigh) | 0.759 | 61% | 0.649 to 0.862 |
| 21 | Muse Spark 1.1 (high) | 0.755 | 61% | 0.656 to 0.863 |
| 22 | Muse Spark 1.3 (high) | 0.559 | 58% | 0.476 to 0.658 |
| 23 | DeepSeek V4 Pro (high) | 0.517 | 58% | 0.399 to 0.631 |
| 24 | GLM-5.2 (max) | 0.457 | 57% | 0.345 to 0.548 |
| 25 | Grok 4.7 (high) | 0.432 | 56% | 0.218 to 0.623 |
| 26 | GPT-5.2 (medium) | 0.333 | 55% | 0.184 to 0.475 |
| 27 | Claude Opus 4.8 (high)‡ | 0.245 | 54% | 0.132 to 0.356 |
| 28 | Qwen 3.8 Max¶ | 0.176 | 53% | 0.067 to 0.297 |
| 29 | Gemini 3.8 Flash (high) | 0.148 | 52% | 0.008 to 0.276 |
| 30 | Kimi K2.6 | 0.078 | 51% | -0.027 to 0.193 |
| 31 | Muse Spark 1.2 (high) | -0.048 | 49% | -0.162 to 0.050 |
| 32 | MiniMax-M3 | -0.091 | 49% | -0.224 to 0.034 |
| 33 | Mistral Medium 3.1 | -0.386 | 44% | -0.539 to -0.261 |
| 34 | DeepSeek V4.1 Flash (high) | -0.488 | 43% | -0.611 to -0.353 |
| 35 | DeepSeek V4 Pro Preview | -0.541 | 42% | -0.651 to -0.417 |
| 36 | Qwen3.8-27B^ | -0.637 | 40% | -0.793 to -0.477 |
| 37 | Xiaomi MiMo V2.5 Pro | -0.677 | 40% | -0.812 to -0.554 |
| 38 | Qwen 3 Max Preview | -0.688 | 40% | -0.850 to -0.510 |
| 39 | Gemini 3.7 Flash (high) | -0.706 | 39% | -0.832 to -0.602 |
| 40 | Qwen 3.6 Max Preview | -0.941 | 36% | -1.060 to -0.801 |
| 41 | GLM-5.1 | -1.043 | 34% | -1.231 to -0.854 |
| 42 | Kimi K2.5 Thinking | -1.088 | 34% | -1.261 to -0.936 |
| 43 | Xiaomi MiMo V2 Pro | -1.227 | 32% | -1.450 to -0.981 |
| 44 | Baidu Ernie 5.1 | -1.258 | 31% | -1.391 to -1.125 |
| 45 | Mistral Large 4 (high) | -1.650 | 26% | -1.753 to -1.545 |
| 46 | Mistral Large 3 | -1.770 | 25% | -1.885 to -1.662 |
| 47 | Gemma 4 31B Reasoning | -1.888 | 23% | -1.979 to -1.793 |
| 48 | ByteDance Seed2.0 Pro | -1.980 | 22% | -2.090 to -1.862 |
| 49 | Gemini 3.5 Flash | -1.988 | 22% | -2.076 to -1.900 |
| 50 | Gemini 3.1 Pro Preview | -2.170 | 20% | -2.271 to -2.072 |
| 51 | Qwen 3.6 Plus | -2.281 | 19% | -2.458 to -2.087 |
| 52 | Mistral Medium 3.5 | -2.553 | 16% | -2.661 to -2.408 |
| 53 | Qwen 3.7 Max | -2.666 | 15% | -2.789 to -2.546 |
| 54 | DeepSeek V3.2 | -2.877 | 13% | -3.142 to -2.632 |
| 55 | Grok 4.6 (high) | -2.880 | 13% | -3.005 to -2.739 |
| 56 | GPT-OSS-120B | -3.160 | 11% | -3.271 to -3.049 |
| 57 | MiniMax-M2.7 | -3.768 | 7% | -3.904 to -3.620 |
| 58 | Grok 4.3 | -4.257 | 4% | -4.433 to -4.085 |
| 59 | Grok 4.5 (high) | -5.089 | 2% | -5.187 to -4.991 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Striped bars and badges identify incomplete story sets. Quality comparisons concern completed stories. The latest evaluations returned 31,241/31,428 planned judgments; 187 unavailable judgments are excluded from the scores. The Opus 5.5 high versus Opus 5 high comparison covers 50 matched prompts, with 298/300 usable judgments.

Mistral Large 4 (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 43 prompts required another draw, for 446 total generation calls. Its comparisons cover 26 opponents, including Mistral Large 3, with 20 matched stories per opponent and 3,112/3,120 usable judgments. [Comparison coverage](data/writing_mistral_large4_20261007/mistral_matchup_coverage.csv).

Muse Wonder (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 2 prompts required another draw, for 402 total generation calls. Its comparisons cover 21 opponents, including Muse Spark 1.3 (high), with 20 matched stories per opponent and 2,467/2,520 usable judgments. [Comparison coverage](data/writing_gemini_argon_20261013/muse_wonder_matchup_coverage.csv).

Gemini 4 Argon (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 0 prompts required another draw, for 410 total generation calls. Its comparisons cover 22 opponents, including Gemini 3.8 Flash (high) and Muse Wonder (high), with 20 matched stories per opponent and 2,577/2,640 usable judgments. [Comparison coverage](data/writing_gemini_argon_20261013/gemini_argon_matchup_coverage.csv). 10 provider failures returned no story text; a documented retry recovered 10 stories. Those failed calls are included in the generation total and excluded from the length-redraw count.

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap_highlighted.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order. Earlier and newer evaluations contribute to both this chart and the rankings.

The [Gemini 4 Argon (high) versus Gemini 3.1 Pro Preview comparison](reports/pair_analysis/gemini-4-argon-high__vs__gemini-3.1-pro-preview__comparator_v2_eval_v4_gemini_argon_vs_gemini31_20261013_n50__quantitative.md) covers 50 matched prompts and 294/300 usable judgments. Argon wins all 50 at the story-level margin threshold; six unavailable judgments are excluded. These additional comparisons support the focused report and are separate from the main leaderboard's intake sample.

## Additional Results

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

The matrix includes earlier and newer evaluator models. Each number shows how similarly two evaluators scored the story pairs they both read. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Orange indicates negative correlations, and blue indicates positive correlations. Blank cells lack enough varied judgments to calculate a correlation; the diagonal is omitted. Agreement on these stories does not establish evaluator accuracy.

GLM-5.1 / Muse Spark 1.1 (high): only two shared stories. [Shared-story counts](data/writing_gemini_argon_20261013/evaluator_agreement.csv) accompany every evaluator pair.

### Word Count Compliance

![Story word counts](images/inter_llm_comparison_word_count_ci_highlighted.png)

Each dot is one completed story; diamonds mark model averages. Thin vertical lines show uncertainty around the averages. The shaded band is the 600–800-word target. The chart includes 9,162 completed stories from all 23 displayed models. This measures length rather than writing quality.

Before the Mistral intake, six stories that exceeded 800 words were regenerated using their original prompts; the first replacement within 600–800 words was retained. The 12 comparisons that used a replaced story were rerun with the same evaluators and both story orders. The rankings and charts use these replacements.

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

Each report describes the models and stories compared. The Argon, Opus 5.5, Grok 4.7, and MiMo V2.6 Pro reports use newer evaluators; earlier reports use the evaluators available at the time.

[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects thirteen release comparisons, including Gemini 4 Argon versus Gemini 3.1 Pro Preview, on a separate page.

New analyses give recurring writing habits, range and adaptability, and consistency separate treatment, with examples across different prompts. They examine repeated phrasing and story patterns as well as how flexibly each model changes its voice, tone, form, and narrative approach.

---

## Data, Stories, and Prompts

Story prompts are available under `prompts_wc/`, and generated stories under `stories_wc/<model>/`.

[Current ratings and chart data](data/writing_gemini_argon_20261013/README.md) include machine-readable leaderboard scores and uncertainty intervals, direct head-to-head results, matched story-pair results, and evaluator diagnostics.

[Earlier benchmark data](data/README.md) links to the immutable August 23, 2026 data release. That archive contains the exact evaluator commentary for both story orders, excluded or superseded responses, and the accompanying source story and prompt texts.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates

- October 13, 2026: Added Gemini 4 Argon high.
- October 13, 2026: Added Muse Wonder high.
- October 8, 2026: Added Mistral Large 4 high.
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
