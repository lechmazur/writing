# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 56 writers, 908 direct model pairings, 15,043 distinct story pairs, and 101,819 judgments. All rated writers retain their overall ranks.

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

Only completed stories were compared.
