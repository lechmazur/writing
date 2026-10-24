# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 60 writers, 999 direct model pairings, 17,022 distinct story pairs, and 113,566 judgments. All rated writers retain their overall ranks.

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

Only completed stories were compared.
