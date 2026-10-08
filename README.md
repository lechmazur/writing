# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched stories in both orders and judge which is better. Their judgments produce relative scores for each writer model.

Higher ratings mean stronger estimated performance within this comparison set. Scores are centered at zero across all writer models in the comparison set.

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings_highlighted.png)

The ranking combines judgments from earlier and newer evaluator models. It covers **57 writer models**, **934 direct model pairings**, **15,692 distinct story pairs**, and **105,704 judgments**. Each direct model pairing can include stories from multiple matched prompts. The chart shows 22 selected models; the table lists every rated model with its overall rank. Mistral Large 4 (high) is the only highlighted model.

The shaded ranges show how much scores vary across 300 resamples of stories and evaluators (bootstrap). The table gives the 95% bootstrap intervals. Estimated win chance is a model's average predicted probability of beating another model in the full comparison set.

### Leaderboard

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | Claude Opus 5 (xhigh) | 3.777 | 93% | 3.722 to 3.839 |
| 2 | Claude Fable 5.1 (high) | 3.760 | 93% | 3.675 to 3.860 |
| 3 | Claude Opus 5.5 (high) | 3.718 | 93% | 3.630 to 3.810 |
| 4 | GPT-6 Astra (high) | 3.461 | 91% | 3.388 to 3.535 |
| 5 | Claude Opus 5 (high) | 3.414 | 91% | 3.313 to 3.531 |
| 6 | GLM-5.3 (max) | 3.025 | 88% | 2.928 to 3.113 |
| 7 | Claude Fable 5 (high)§ | 2.901 | 87% | 2.838 to 2.974 |
| 8 | GPT-5.6 Sol (xhigh) | 2.519 | 83% | 2.452 to 2.600 |
| 9 | GPT-5.5 (xhigh) | 2.482 | 83% | 2.415 to 2.565 |
| 10 | Kimi K3 | 2.469 | 83% | 2.387 to 2.546 |
| 11 | GPT-5.6 Sol (high) | 2.329 | 81% | 2.250 to 2.409 |
| 12 | GPT-5.4 (medium) | 2.018 | 78% | 1.896 to 2.149 |
| 13 | GPT-5.4 (xhigh) | 2.012 | 78% | 1.905 to 2.134 |
| 14 | Claude Opus 4.7 (high)† | 1.815 | 75% | 1.696 to 1.923 |
| 15 | Claude Sonnet 4.6 Thinking 16K | 1.705 | 74% | 1.611 to 1.812 |
| 16 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.617 | 73% | 1.469 to 1.754 |
| 17 | Claude Opus 4.6 Thinking 16K | 1.178 | 67% | 0.995 to 1.338 |
| 18 | Claude Opus 4.8 (xhigh) | 0.808 | 62% | 0.710 to 0.910 |
| 19 | Muse Spark 1.1 (high) | 0.804 | 62% | 0.714 to 0.910 |
| 20 | Muse Spark 1.3 (high) | 0.624 | 60% | 0.539 to 0.718 |
| 21 | DeepSeek V4 Pro (high) | 0.590 | 59% | 0.483 to 0.720 |
| 22 | GLM-5.2 (max) | 0.505 | 58% | 0.419 to 0.600 |
| 23 | Grok 4.7 (high) | 0.444 | 57% | 0.236 to 0.641 |
| 24 | GPT-5.2 (medium) | 0.383 | 56% | 0.214 to 0.546 |
| 25 | Claude Opus 4.8 (high)‡ | 0.294 | 55% | 0.204 to 0.397 |
| 26 | Gemini 3.8 Flash (high) | 0.266 | 54% | 0.139 to 0.401 |
| 27 | Qwen 3.8 Max¶ | 0.258 | 54% | 0.137 to 0.368 |
| 28 | Kimi K2.6 | 0.128 | 52% | 0.028 to 0.235 |
| 29 | Muse Spark 1.2 (high) | 0.000 | 50% | -0.091 to 0.102 |
| 30 | MiniMax-M3 | -0.013 | 50% | -0.136 to 0.117 |
| 31 | Mistral Medium 3.1 | -0.335 | 45% | -0.453 to -0.192 |
| 32 | DeepSeek V4.1 Flash (high) | -0.407 | 44% | -0.529 to -0.273 |
| 33 | DeepSeek V4 Pro Preview | -0.490 | 43% | -0.591 to -0.384 |
| 34 | Qwen3.8-27B^ | -0.562 | 42% | -0.742 to -0.393 |
| 35 | Xiaomi MiMo V2.5 Pro | -0.628 | 41% | -0.765 to -0.480 |
| 36 | Qwen 3 Max Preview | -0.640 | 41% | -0.808 to -0.491 |
| 37 | Gemini 3.7 Flash (high) | -0.653 | 40% | -0.748 to -0.537 |
| 38 | Qwen 3.6 Max Preview | -0.893 | 37% | -1.018 to -0.754 |
| 39 | GLM-5.1 | -0.996 | 35% | -1.184 to -0.831 |
| 40 | Kimi K2.5 Thinking | -1.039 | 35% | -1.203 to -0.853 |
| 41 | Xiaomi MiMo V2 Pro | -1.178 | 33% | -1.413 to -0.945 |
| 42 | Baidu Ernie 5.1 | -1.198 | 32% | -1.348 to -1.058 |
| 43 | **Mistral Large 4 (high)** | -1.585 | 27% | -1.698 to -1.458 |
| 44 | Mistral Large 3 | -1.720 | 25% | -1.836 to -1.603 |
| 45 | Gemma 4 31B Reasoning | -1.840 | 24% | -1.941 to -1.742 |
| 46 | ByteDance Seed2.0 Pro | -1.936 | 23% | -2.060 to -1.802 |
| 47 | Gemini 3.5 Flash | -1.939 | 23% | -2.043 to -1.843 |
| 48 | Gemini 3.1 Pro Preview | -2.139 | 20% | -2.251 to -2.027 |
| 49 | Qwen 3.6 Plus | -2.232 | 19% | -2.406 to -2.053 |
| 50 | Mistral Medium 3.5 | -2.509 | 16% | -2.635 to -2.379 |
| 51 | Qwen 3.7 Max | -2.614 | 15% | -2.748 to -2.485 |
| 52 | DeepSeek V3.2 | -2.829 | 13% | -3.075 to -2.565 |
| 53 | Grok 4.6 (high) | -2.833 | 13% | -2.967 to -2.678 |
| 54 | GPT-OSS-120B | -3.130 | 11% | -3.249 to -3.006 |
| 55 | MiniMax-M2.7 | -3.719 | 7% | -3.845 to -3.573 |
| 56 | Grok 4.3 | -4.208 | 4% | -4.376 to -4.025 |
| 57 | Grok 4.5 (high) | -5.040 | 2% | -5.135 to -4.956 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Striped bars and badges identify incomplete story sets. Quality comparisons concern completed stories. The latest evaluations returned 26,197/26,268 planned judgments; 71 unavailable judgments are excluded from the scores. The Opus 5.5 high versus Opus 5 high comparison covers 50 matched prompts, with 298/300 usable judgments.

Mistral Large 4 (high) completed all 400 prompts. Stories outside 600–800 words were regenerated from their original prompts, retaining the first response within range; 43 prompts required another draw, for 446 total generation calls. Its comparisons cover 26 opponents, including Mistral Large 3, with 20 matched stories per opponent and 3,112/3,120 usable judgments. [Comparison coverage](data/writing_mistral_large4_20261007/mistral_matchup_coverage.csv).

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap_highlighted.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order. Earlier and newer evaluations contribute to both this chart and the rankings.

## Additional Results

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

The matrix includes earlier and newer evaluator models. Each number shows how similarly two evaluators scored the story pairs they both read. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns. Orange indicates negative correlations, and blue indicates positive correlations. Blank cells lack enough varied judgments to calculate a correlation; the diagonal is omitted. Agreement on these stories does not establish evaluator accuracy.

GLM-5.1 / Muse Spark 1.1 (high): only two shared stories. [Shared-story counts](data/writing_mistral_large4_20261007/evaluator_agreement.csv) accompany every evaluator pair.

### Word Count Compliance

![Story word counts](images/inter_llm_comparison_word_count_ci_highlighted.png)

Each dot is one completed story; diamonds mark model averages. Thin vertical lines show uncertainty around the averages. The shaded band is the 600–800-word target. The chart includes 8,762 completed stories from all 22 displayed models. This measures length rather than writing quality.

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

Each report describes the models and stories compared. The Opus 5.5, Grok 4.7, and MiMo V2.6 Pro reports use newer evaluators; earlier reports use the evaluators available at the time.

[New Models Compared with Their Predecessors](reports/pair_analysis/new_models_compared_with_predecessors.md) collects twelve release-to-predecessor reports on a separate page.

New analyses give recurring writing habits, range and adaptability, and consistency separate treatment, with examples across different prompts. They examine repeated phrasing and story patterns as well as how flexibly each model changes its voice, tone, form, and narrative approach.

---

## Data, Stories, and Prompts

Story prompts are available under `prompts_wc/`, and generated stories under `stories_wc/<model>/`.

[Current ratings and chart data](data/writing_mistral_large4_20261007/README.md) include machine-readable leaderboard scores and uncertainty intervals, direct head-to-head results, matched story-pair results, and evaluator diagnostics.

[Earlier benchmark data](data/README.md) links to the immutable August 23, 2026 data release. That archive contains the exact evaluator commentary for both story orders, excluded or superseded responses, and the accompanying source story and prompt texts.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates

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
