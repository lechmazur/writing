# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 59 writers, 977 direct model pairings, 16,552 distinct story pairs, and 110,748 judgments. All rated writers retain their overall ranks.

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

Only completed stories were compared.
