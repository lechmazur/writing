# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched stories in both orders and judge which is better. Their judgments produce relative scores for each writer model.

Higher ratings mean stronger estimated performance within this comparison set. Scores are centered at zero across all writer models in the comparison set.

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

The ranking combines judgments from earlier and newer evaluator models. It covers **60 writer models**, **999 direct model pairings**, **17,022 distinct story pairs**, and **113,566 judgments**. Each direct model pairing can include stories from multiple matched prompts. The chart shows 23 selected models; the table lists every rated model with its overall rank.

The shaded ranges show how much scores vary across 300 resamples of stories and evaluators (bootstrap). The table gives the 95% bootstrap intervals. Estimated win chance is a model's average predicted probability of beating another model in the full comparison set.

### Leaderboard

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | Claude Fable 5.1 (high) | 3.745 | 93% | 3.663 to 3.829 |
| 2 | Claude Opus 5.5 (high) | 3.693 | 93% | 3.586 to 3.776 |
| 3 | Claude Opus 5 (xhigh) | 3.685 | 93% | 3.635 to 3.735 |
| 4 | GPT-6 Astra (high) | 3.416 | 91% | 3.355 to 3.494 |
| 5 | Claude Opus 5 (high) | 3.322 | 90% | 3.233 to 3.431 |
| 6 | GLM-5.3 (max) | 2.950 | 87% | 2.856 to 3.047 |
| 7 | Claude Fable 5 (high)§ | 2.810 | 86% | 2.745 to 2.869 |
| 8 | **Kimi K3.1 Pro (high)** | 2.723 | 85% | 2.634 to 2.799 |
| 9 | GPT-5.6 Sol (xhigh) | 2.425 | 82% | 2.353 to 2.512 |
| 10 | GPT-5.5 (xhigh) | 2.390 | 82% | 2.322 to 2.459 |
| 11 | Kimi K3 | 2.347 | 81% | 2.279 to 2.418 |
| 12 | GPT-5.6 Sol (high) | 2.237 | 80% | 2.153 to 2.305 |
| 13 | GPT-5.4 (medium) | 1.922 | 77% | 1.808 to 2.034 |
| 14 | GPT-5.4 (xhigh) | 1.916 | 76% | 1.801 to 2.025 |
| 15 | Muse Wonder (high) | 1.900 | 76% | 1.809 to 1.994 |
| 16 | Claude Opus 4.7 (high)† | 1.720 | 74% | 1.623 to 1.821 |
| 17 | Claude Sonnet 4.6 Thinking 16K | 1.610 | 73% | 1.507 to 1.712 |
| 18 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.520 | 72% | 1.399 to 1.645 |
| 19 | Claude Opus 4.6 Thinking 16K | 1.083 | 66% | 0.918 to 1.275 |
| 20 | Gemini 4 Argon (high) | 0.719 | 61% | 0.603 to 0.825 |
| 21 | Claude Opus 4.8 (xhigh) | 0.717 | 61% | 0.605 to 0.828 |
| 22 | Muse Spark 1.1 (high) | 0.713 | 61% | 0.608 to 0.801 |
| 23 | Muse Spark 1.3 (high) | 0.500 | 57% | 0.428 to 0.581 |
| 24 | DeepSeek V4 Pro (high) | 0.441 | 57% | 0.342 to 0.555 |
| 25 | GLM-5.2 (max) | 0.412 | 56% | 0.312 to 0.492 |
| 26 | Grok 4.7 (high) | 0.351 | 55% | 0.154 to 0.540 |
| 27 | GPT-5.2 (medium) | 0.287 | 54% | 0.131 to 0.439 |
| 28 | Claude Opus 4.8 (high)‡ | 0.204 | 53% | 0.111 to 0.320 |
| 29 | Qwen 3.8 Max¶ | 0.116 | 52% | 0.005 to 0.221 |
| 30 | Gemini 3.8 Flash (high) | 0.081 | 51% | -0.035 to 0.215 |
| 31 | Kimi K2.6 | 0.034 | 50% | -0.078 to 0.143 |
| 32 | Muse Spark 1.2 (high) | -0.095 | 48% | -0.182 to 0.003 |
| 33 | MiniMax-M3 | -0.143 | 48% | -0.244 to -0.024 |
| 34 | Mistral Medium 3.1 | -0.432 | 43% | -0.566 to -0.306 |
| 35 | DeepSeek V4.1 Flash (high) | -0.550 | 42% | -0.665 to -0.439 |
| 36 | DeepSeek V4 Pro Preview | -0.587 | 41% | -0.700 to -0.469 |
| 37 | Qwen3.8-27B^ | -0.703 | 39% | -0.858 to -0.549 |
| 38 | Xiaomi MiMo V2.5 Pro | -0.723 | 39% | -0.858 to -0.596 |
| 39 | Qwen 3 Max Preview | -0.732 | 39% | -0.893 to -0.572 |
| 40 | Gemini 3.7 Flash (high) | -0.755 | 39% | -0.870 to -0.640 |
| 41 | Qwen 3.6 Max Preview | -0.983 | 35% | -1.102 to -0.863 |
| 42 | GLM-5.1 | -1.084 | 34% | -1.257 to -0.897 |
| 43 | Kimi K2.5 Thinking | -1.131 | 33% | -1.314 to -0.953 |
| 44 | Xiaomi MiMo V2 Pro | -1.267 | 31% | -1.490 to -1.035 |
| 45 | Baidu Ernie 5.1 | -1.297 | 31% | -1.418 to -1.170 |
| 46 | Mistral Large 4 (high) | -1.681 | 26% | -1.787 to -1.583 |
| 47 | Mistral Large 3 | -1.815 | 24% | -1.932 to -1.704 |
| 48 | Gemma 4 31B Reasoning | -1.910 | 23% | -2.007 to -1.823 |
| 49 | ByteDance Seed2.0 Pro | -2.000 | 22% | -2.114 to -1.893 |
| 50 | Gemini 3.5 Flash | -2.031 | 22% | -2.114 to -1.946 |
| 51 | Gemini 3.1 Pro Preview | -2.214 | 19% | -2.314 to -2.110 |
| 52 | Qwen 3.6 Plus | -2.325 | 18% | -2.485 to -2.142 |
| 53 | Mistral Medium 3.5 | -2.565 | 16% | -2.699 to -2.432 |
| 54 | Qwen 3.7 Max | -2.709 | 14% | -2.828 to -2.580 |
| 55 | DeepSeek V3.2 | -2.917 | 13% | -3.162 to -2.680 |
| 56 | Grok 4.6 (high) | -2.930 | 12% | -3.084 to -2.776 |
| 57 | GPT-OSS-120B | -3.174 | 11% | -3.282 to -3.066 |
| 58 | MiniMax-M2.7 | -3.808 | 6% | -3.941 to -3.660 |
| 59 | Grok 4.3 | -4.298 | 4% | -4.474 to -4.141 |
| 60 | Grok 4.5 (high) | -5.131 | 2% | -5.209 to -5.044 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Striped bars and badges identify incomplete story sets. Quality comparisons concern completed stories. The latest evaluations returned 34,059/34,248 planned judgments; 189 unavailable judgments are excluded from the scores. The Opus 5.5 high versus Opus 5 high comparison covers 50 matched prompts, with 298/300 usable judgments.

Mistral Large 4 (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 43 prompts required another draw, for 446 total generation calls. Its comparisons cover 26 opponents, including Mistral Large 3, with 20 matched stories per opponent and 3,112/3,120 usable judgments. [Comparison coverage](data/writing_mistral_large4_20261007/mistral_matchup_coverage.csv).

Muse Wonder (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 2 prompts required another draw, for 402 total generation calls. Its comparisons cover 21 opponents, including Muse Spark 1.3 (high), with 20 matched stories per opponent and 2,467/2,520 usable judgments. [Comparison coverage](data/writing_gemini_argon_20261013/muse_wonder_matchup_coverage.csv).

Gemini 4 Argon (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 0 prompts required another draw, for 410 total generation calls. Its comparisons cover 22 opponents, including Gemini 3.8 Flash (high) and Muse Wonder (high), with 20 matched stories per opponent and 2,577/2,640 usable judgments. [Comparison coverage](data/writing_gemini_argon_20261013/gemini_argon_matchup_coverage.csv). 10 provider failures returned no story text; a documented retry recovered 10 stories. Those failed calls are included in the generation total and excluded from the length-redraw count.

Kimi K3.1 Pro (high) completed all 400 prompts, accepting the first 600–800-word response to each prompt. There were 400 generation calls and 0 prompts needing another draw; accepted lengths range from 612 to 776 words. Its comparisons cover 22 opponents, including Kimi K3, with 20 matched stories per opponent and 50 against Kimi K3, for 2,818/2,820 usable judgments. [Comparison coverage](data/writing_kimi_k31_depth50_20261024/kimi_k31_matchup_coverage.csv).

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order. Earlier and newer evaluations contribute to both this chart and the rankings.

The [Kimi K3.1 Pro (high) versus Kimi K3 qualitative comparison](reports/pair_analysis/kimi-k3.1-pro-high__vs__kimi-k3__comparator_v2_eval_v4_kimi_k31_vs_k3_20261024_n50__subjective_v5_habits_range.md) examines style, narrative control, recurring habits, and range across 50 matched prompts, with blinded readings from three independent model families. [Quantitative comparison](reports/pair_analysis/kimi-k3.1-pro-high__vs__kimi-k3__comparator_v2_eval_v4_kimi_k31_vs_k3_20261024_n50__quantitative.md): 300/300 usable judgments, retaining the original 20 prompts and adding 30 previously unused prompts. All 50 prompts now contribute to the leaderboard and head-to-head chart.

The [Gemini 4 Argon (high) versus Gemini 3.1 Pro Preview comparison](reports/pair_analysis/gemini-4-argon-high__vs__gemini-3.1-pro-preview__comparator_v2_eval_v4_gemini_argon_vs_gemini31_20261013_n50__quantitative.md) covers 50 matched prompts and 294/300 usable judgments. Argon wins all 50 at the story-level margin threshold; six unavailable judgments are excluded. These additional comparisons support the focused report and are separate from the main leaderboard's intake sample.

## Additional Results

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

The matrix includes earlier and newer evaluator models. Each number shows how similarly two evaluators scored the story pairs they both read. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Orange indicates negative correlations, and blue indicates positive correlations. Blank cells lack enough varied judgments to calculate a correlation; the diagonal is omitted. Agreement on these stories does not establish evaluator accuracy.

GLM-5.1 / Muse Spark 1.1 (high): only two shared stories. [Shared-story counts](data/writing_kimi_k31_depth50_20261024/evaluator_agreement.csv) accompany every evaluator pair.

### Word Count Compliance

![Story word counts](images/inter_llm_comparison_word_count_ci.png)

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

[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects fourteen release comparisons, including Gemini 4 Argon versus Gemini 3.1 Pro Preview, on a separate page.

New analyses give recurring writing habits, range and adaptability, and consistency separate treatment, with examples across different prompts. They examine repeated phrasing and story patterns as well as how flexibly each model changes its voice, tone, form, and narrative approach.

---

## Data, Stories, and Prompts

Story prompts are available under `prompts_wc/`, and generated stories under `stories_wc/<model>/`.

[Current ratings and chart data](data/writing_kimi_k31_depth50_20261024/README.md) include machine-readable leaderboard scores and uncertainty intervals, direct head-to-head results, matched story-pair results, and evaluator diagnostics.

[Earlier benchmark data](data/README.md) links to the immutable August 23, 2026 data release. That archive contains the exact evaluator commentary for both story orders, excluded or superseded responses, and the accompanying source story and prompt texts.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates

- October 23, 2026: Added Kimi K3.1 Pro high.
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
