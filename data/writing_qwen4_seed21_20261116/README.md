# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 66 writers, 1,142 direct model pairings, 19,882 distinct story pairs, and 130,724 judgments. All rated writers retain their overall ranks.

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | **Qwen 4 Max (high)⁂** | 3.712 | 93% | 3.638 to 3.797 |
| 2 | Claude Fable 5.2 (high) | 3.633 | 93% | 3.553 to 3.711 |
| 3 | Claude Fable 5.1 (high) | 3.583 | 92% | 3.498 to 3.662 |
| 4 | Claude Opus 5 (xhigh) | 3.509 | 92% | 3.448 to 3.576 |
| 5 | Claude Opus 5.5 (high) | 3.469 | 91% | 3.387 to 3.555 |
| 6 | GPT-6 Astra (high) | 3.267 | 90% | 3.203 to 3.325 |
| 7 | Claude Opus 5 (high) | 3.126 | 89% | 3.028 to 3.222 |
| 8 | GLM-5.3 (max) | 2.722 | 85% | 2.643 to 2.811 |
| 9 | Claude Fable 5 (high)§ | 2.645 | 84% | 2.572 to 2.705 |
| 10 | Kimi K3.1 Pro (high) | 2.464 | 82% | 2.381 to 2.545 |
| 11 | GPT-5.6 Sol (xhigh) | 2.259 | 80% | 2.181 to 2.332 |
| 12 | GPT-5.5 (xhigh) | 2.227 | 80% | 2.161 to 2.301 |
| 13 | Kimi K3 | 2.169 | 79% | 2.088 to 2.237 |
| 14 | Tencent Hy4 (high) | 2.140 | 79% | 2.064 to 2.232 |
| 15 | GPT-5.6 Sol (high) | 2.072 | 78% | 1.996 to 2.143 |
| 16 | GPT-5.4 (medium) | 1.753 | 74% | 1.632 to 1.869 |
| 17 | GPT-5.4 (xhigh) | 1.747 | 74% | 1.663 to 1.863 |
| 18 | Muse Wonder (high) | 1.696 | 74% | 1.631 to 1.782 |
| 19 | Gemini 4 Carbon (high) | 1.694 | 74% | 1.602 to 1.774 |
| 20 | Claude Opus 4.7 (high)† | 1.556 | 72% | 1.456 to 1.664 |
| 21 | Claude Sonnet 4.6 Thinking 16K | 1.444 | 70% | 1.339 to 1.561 |
| 22 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.275 | 68% | 1.148 to 1.389 |
| 23 | Claude Opus 4.6 Thinking 16K | 0.914 | 63% | 0.721 to 1.100 |
| 24 | Claude Opus 4.8 (xhigh) | 0.557 | 58% | 0.436 to 0.669 |
| 25 | Muse Spark 1.1 (high) | 0.552 | 58% | 0.438 to 0.660 |
| 26 | Gemini 4 Argon (high) | 0.511 | 58% | 0.409 to 0.602 |
| 27 | Muse Spark 1.3 (high) | 0.302 | 54% | 0.214 to 0.375 |
| 28 | GLM-5.2 (max) | 0.243 | 54% | 0.146 to 0.329 |
| 29 | DeepSeek V4 Pro (high) | 0.215 | 53% | 0.129 to 0.302 |
| 30 | GPT-5.2 (medium) | 0.118 | 52% | -0.044 to 0.288 |
| 31 | Grok 4.7 (high) | 0.116 | 52% | -0.104 to 0.265 |
| 32 | Claude Opus 4.8 (high)‡ | 0.044 | 51% | -0.041 to 0.161 |
| 33 | Gemini 3.8 Flash (high) | -0.098 | 48% | -0.193 to 0.020 |
| 34 | Qwen 3.8 Max¶ | -0.102 | 48% | -0.183 to -0.008 |
| 35 | Kimi K2.6 | -0.131 | 48% | -0.234 to -0.027 |
| 36 | Step 5 Preview (high) | -0.137 | 48% | -0.246 to -0.027 |
| 37 | Muse Spark 1.2 (high) | -0.268 | 46% | -0.367 to -0.171 |
| 38 | MiniMax-M3 | -0.333 | 45% | -0.428 to -0.225 |
| 39 | Mistral Medium 3.1 | -0.600 | 41% | -0.740 to -0.465 |
| 40 | **ByteDance Seed2.1 Pro** | -0.618 | 41% | -0.714 to -0.505 |
| 41 | DeepSeek V4.1 Flash (high) | -0.729 | 39% | -0.816 to -0.611 |
| 42 | DeepSeek V4 Pro Preview | -0.754 | 39% | -0.858 to -0.630 |
| 43 | Xiaomi MiMo V2.5 Pro | -0.894 | 37% | -1.011 to -0.751 |
| 44 | Qwen 3 Max Preview | -0.898 | 37% | -1.065 to -0.729 |
| 45 | Qwen3.8-27B^ | -0.913 | 36% | -1.036 to -0.785 |
| 46 | Gemini 3.7 Flash (high) | -0.933 | 36% | -1.050 to -0.824 |
| 47 | Qwen 3.6 Max Preview | -1.145 | 33% | -1.273 to -1.020 |
| 48 | GLM-5.1 | -1.243 | 32% | -1.396 to -1.075 |
| 49 | Kimi K2.5 Thinking | -1.296 | 31% | -1.455 to -1.122 |
| 50 | Xiaomi MiMo V2 Pro | -1.426 | 29% | -1.662 to -1.201 |
| 51 | Baidu Ernie 5.1 | -1.448 | 29% | -1.572 to -1.336 |
| 52 | Mistral Large 4 (high) | -1.852 | 24% | -1.952 to -1.761 |
| 53 | Mistral Large 3 | -1.984 | 22% | -2.109 to -1.865 |
| 54 | Gemma 4 31B Reasoning | -2.032 | 21% | -2.106 to -1.948 |
| 55 | ByteDance Seed2.0 Pro | -2.118 | 21% | -2.223 to -2.016 |
| 56 | Gemini 3.5 Flash | -2.194 | 20% | -2.285 to -2.111 |
| 57 | Gemini 3.1 Pro Preview | -2.380 | 18% | -2.464 to -2.286 |
| 58 | Qwen 3.6 Plus | -2.492 | 17% | -2.671 to -2.309 |
| 59 | Mistral Medium 3.5 | -2.671 | 15% | -2.768 to -2.562 |
| 60 | Qwen 3.7 Max | -2.873 | 13% | -2.998 to -2.744 |
| 61 | DeepSeek V3.2 | -3.075 | 11% | -3.299 to -2.843 |
| 62 | Grok 4.6 (high) | -3.109 | 11% | -3.276 to -2.948 |
| 63 | GPT-OSS-120B | -3.273 | 10% | -3.350 to -3.193 |
| 64 | MiniMax-M2.7 | -3.967 | 6% | -4.102 to -3.804 |
| 65 | Grok 4.3 | -4.458 | 4% | -4.632 to -4.274 |
| 66 | Grok 4.5 (high) | -5.292 | 1% | -5.385 to -5.204 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed. 20 of these required refusal retries (1 retry round).
- ^ Qwen3.8-27B: 389 of 400 stories completed. 46 of these required refusal retries (1 retry round).
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.
- ⁂ Qwen 4 Max (high): 397 of 400 stories completed.

Only completed stories were compared.
