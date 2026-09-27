# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 56 writers, 838 direct model pairings, 14,624 distinct story pairs, and 99,309 judgments. All rated writers retain their overall ranks.

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | **Claude Opus 5.5 (high)** | 3.870 | 94% | 3.754 to 3.990 |
| 2 | Claude Fable 5.1 (high) | 3.822 | 93% | 3.721 to 3.920 |
| 3 | Claude Opus 5 (xhigh) | 3.805 | 93% | 3.752 to 3.865 |
| 4 | **Claude Opus 5 (high)** | 3.548 | 92% | 3.440 to 3.665 |
| 5 | GPT-6 Astra (high) | 3.439 | 91% | 3.362 to 3.506 |
| 6 | GLM-5.3 (max) | 3.022 | 88% | 2.905 to 3.120 |
| 7 | Claude Fable 5 (high)§ | 2.877 | 86% | 2.818 to 2.944 |
| 8 | GPT-5.6 Sol (xhigh) | 2.491 | 83% | 2.406 to 2.561 |
| 9 | GPT-5.5 (xhigh) | 2.456 | 82% | 2.392 to 2.521 |
| 10 | Kimi K3 | 2.451 | 82% | 2.371 to 2.520 |
| 11 | GPT-5.6 Sol (high) | 2.301 | 81% | 2.229 to 2.387 |
| 12 | GPT-5.4 (medium) | 1.995 | 77% | 1.867 to 2.124 |
| 13 | GPT-5.4 (xhigh) | 1.989 | 77% | 1.874 to 2.104 |
| 14 | Claude Opus 4.7 (high)† | 1.789 | 75% | 1.682 to 1.904 |
| 15 | Claude Sonnet 4.6 Thinking 16K | 1.680 | 74% | 1.569 to 1.791 |
| 16 | **Xiaomi MiMo V2.6 Pro (thinking)※** | 1.584 | 72% | 1.427 to 1.733 |
| 17 | Claude Opus 4.6 Thinking 16K | 1.155 | 67% | 0.977 to 1.328 |
| 18 | Claude Opus 4.8 (xhigh) | 0.781 | 62% | 0.676 to 0.892 |
| 19 | Muse Spark 1.1 (high) | 0.777 | 62% | 0.655 to 0.874 |
| 20 | Muse Spark 1.3 (high) | 0.584 | 59% | 0.490 to 0.675 |
| 21 | DeepSeek V4 Pro (high) | 0.544 | 58% | 0.429 to 0.658 |
| 22 | GLM-5.2 (max) | 0.477 | 57% | 0.369 to 0.569 |
| 23 | **Grok 4.7 (high)** | 0.400 | 56% | 0.191 to 0.610 |
| 24 | GPT-5.2 (medium) | 0.360 | 56% | 0.187 to 0.511 |
| 25 | Claude Opus 4.8 (high)‡ | 0.266 | 54% | 0.158 to 0.379 |
| 26 | Qwen 3.8 Max¶ | 0.201 | 53% | 0.074 to 0.323 |
| 27 | **Gemini 3.8 Flash (high)** | 0.128 | 52% | -0.013 to 0.315 |
| 28 | Kimi K2.6 | 0.101 | 52% | -0.003 to 0.210 |
| 29 | Muse Spark 1.2 (high) | -0.024 | 50% | -0.145 to 0.071 |
| 30 | MiniMax-M3 | -0.026 | 50% | -0.148 to 0.109 |
| 31 | Mistral Medium 3.1 | -0.360 | 45% | -0.492 to -0.230 |
| 32 | DeepSeek V4 Pro Preview | -0.517 | 42% | -0.630 to -0.399 |
| 33 | Xiaomi MiMo V2.5 Pro | -0.659 | 40% | -0.793 to -0.542 |
| 34 | Qwen3.8-27B^ | -0.662 | 40% | -0.849 to -0.479 |
| 35 | Qwen 3 Max Preview | -0.664 | 40% | -0.854 to -0.495 |
| 36 | **DeepSeek V4.1 Flash (high)** | -0.673 | 40% | -0.807 to -0.522 |
| 37 | Gemini 3.7 Flash (high) | -0.708 | 40% | -0.825 to -0.559 |
| 38 | Qwen 3.6 Max Preview | -0.923 | 36% | -1.057 to -0.806 |
| 39 | GLM-5.1 | -1.027 | 35% | -1.196 to -0.875 |
| 40 | Kimi K2.5 Thinking | -1.064 | 34% | -1.250 to -0.885 |
| 41 | Xiaomi MiMo V2 Pro | -1.207 | 32% | -1.404 to -0.975 |
| 42 | Baidu Ernie 5.1 | -1.217 | 32% | -1.392 to -1.044 |
| 43 | Mistral Large 3 | -1.767 | 25% | -1.884 to -1.645 |
| 44 | Gemma 4 31B Reasoning | -1.879 | 24% | -1.987 to -1.782 |
| 45 | Gemini 3.5 Flash | -1.969 | 23% | -2.072 to -1.864 |
| 46 | ByteDance Seed2.0 Pro | -1.988 | 22% | -2.117 to -1.844 |
| 47 | Gemini 3.1 Pro Preview | -2.212 | 20% | -2.305 to -2.098 |
| 48 | Qwen 3.6 Plus | -2.260 | 19% | -2.430 to -2.080 |
| 49 | Mistral Medium 3.5 | -2.539 | 16% | -2.678 to -2.386 |
| 50 | Qwen 3.7 Max | -2.645 | 15% | -2.765 to -2.522 |
| 51 | Grok 4.6 (high) | -2.847 | 13% | -2.988 to -2.694 |
| 52 | DeepSeek V3.2 | -2.860 | 13% | -3.118 to -2.610 |
| 53 | GPT-OSS-120B | -3.141 | 11% | -3.275 to -3.014 |
| 54 | MiniMax-M2.7 | -3.748 | 7% | -3.882 to -3.629 |
| 55 | Grok 4.3 | -4.237 | 4% | -4.409 to -4.038 |
| 56 | Grok 4.5 (high) | -5.067 | 2% | -5.158 to -4.992 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed.
- ^ Qwen3.8-27B: 389 of 400 stories completed.
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Only completed stories were compared.
