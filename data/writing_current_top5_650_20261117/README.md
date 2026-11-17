# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 67 writers, 1,167 direct model pairings, 20,589 distinct story pairs, and 134,964 judgments. All rated writers retain their overall ranks.

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | **GPT-6.2 Astra (high)** | 4.302 | 96% | 4.223 to 4.379 |
| 2 | Claude Fable 5.2 (high) | 3.564 | 92% | 3.498 to 3.636 |
| 3 | **Qwen 4 Max (high)⁂** | 3.548 | 92% | 3.469 to 3.625 |
| 4 | Claude Fable 5.1 (high) | 3.510 | 91% | 3.428 to 3.588 |
| 5 | Claude Opus 5 (xhigh) | 3.443 | 91% | 3.378 to 3.502 |
| 6 | Claude Opus 5.5 (high) | 3.355 | 90% | 3.286 to 3.425 |
| 7 | GPT-6 Astra (high) | 3.166 | 89% | 3.105 to 3.225 |
| 8 | Claude Opus 5 (high) | 3.049 | 88% | 2.945 to 3.148 |
| 9 | GLM-5.3 (max) | 2.613 | 84% | 2.529 to 2.695 |
| 10 | Claude Fable 5 (high)§ | 2.585 | 83% | 2.522 to 2.653 |
| 11 | Kimi K3.1 Pro (high) | 2.366 | 81% | 2.290 to 2.440 |
| 12 | GPT-5.6 Sol (xhigh) | 2.199 | 79% | 2.112 to 2.280 |
| 13 | GPT-5.5 (xhigh) | 2.169 | 79% | 2.112 to 2.241 |
| 14 | Kimi K3 | 2.104 | 78% | 2.034 to 2.173 |
| 15 | Tencent Hy4 (high) | 2.046 | 78% | 1.971 to 2.116 |
| 16 | GPT-5.6 Sol (high) | 2.011 | 77% | 1.935 to 2.083 |
| 17 | GPT-5.4 (medium) | 1.691 | 73% | 1.580 to 1.799 |
| 18 | GPT-5.4 (xhigh) | 1.685 | 73% | 1.580 to 1.789 |
| 19 | Gemini 4 Carbon (high) | 1.618 | 72% | 1.535 to 1.705 |
| 20 | Muse Wonder (high) | 1.609 | 72% | 1.537 to 1.681 |
| 21 | Claude Opus 4.7 (high)† | 1.496 | 71% | 1.389 to 1.602 |
| 22 | Claude Sonnet 4.6 Thinking 16K | 1.385 | 70% | 1.283 to 1.497 |
| 23 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.191 | 67% | 1.075 to 1.292 |
| 24 | Claude Opus 4.6 Thinking 16K | 0.852 | 62% | 0.679 to 1.041 |
| 25 | Claude Opus 4.8 (xhigh) | 0.500 | 57% | 0.398 to 0.606 |
| 26 | Muse Spark 1.1 (high) | 0.495 | 57% | 0.382 to 0.599 |
| 27 | Gemini 4 Argon (high) | 0.454 | 57% | 0.354 to 0.551 |
| 28 | Muse Spark 1.3 (high) | 0.234 | 54% | 0.151 to 0.309 |
| 29 | GLM-5.2 (max) | 0.182 | 53% | 0.086 to 0.276 |
| 30 | DeepSeek V4 Pro (high) | 0.140 | 52% | 0.054 to 0.229 |
| 31 | GPT-5.2 (medium) | 0.056 | 51% | -0.103 to 0.232 |
| 32 | Grok 4.7 (high) | 0.029 | 51% | -0.146 to 0.178 |
| 33 | Claude Opus 4.8 (high)‡ | -0.013 | 50% | -0.137 to 0.096 |
| 34 | Gemini 3.8 Flash (high) | -0.157 | 48% | -0.243 to -0.061 |
| 35 | Qwen 3.8 Max¶ | -0.174 | 48% | -0.269 to -0.075 |
| 36 | Step 5 Preview (high) | -0.185 | 47% | -0.285 to -0.094 |
| 37 | Kimi K2.6 | -0.191 | 47% | -0.315 to -0.084 |
| 38 | Muse Spark 1.2 (high) | -0.330 | 45% | -0.445 to -0.237 |
| 39 | MiniMax-M3 | -0.389 | 44% | -0.514 to -0.272 |
| 40 | Mistral Medium 3.1 | -0.660 | 40% | -0.784 to -0.520 |
| 41 | **ByteDance Seed2.1 Pro** | -0.667 | 40% | -0.784 to -0.565 |
| 42 | DeepSeek V4.1 Flash (high) | -0.797 | 38% | -0.882 to -0.701 |
| 43 | DeepSeek V4 Pro Preview | -0.814 | 38% | -0.927 to -0.693 |
| 44 | Qwen3.8-27B^ | -0.956 | 36% | -1.068 to -0.833 |
| 45 | Xiaomi MiMo V2.5 Pro | -0.957 | 36% | -1.079 to -0.819 |
| 46 | Qwen 3 Max Preview | -0.959 | 36% | -1.133 to -0.781 |
| 47 | Gemini 3.7 Flash (high) | -0.995 | 35% | -1.101 to -0.868 |
| 48 | Qwen 3.6 Max Preview | -1.206 | 32% | -1.317 to -1.083 |
| 49 | GLM-5.1 | -1.302 | 31% | -1.471 to -1.119 |
| 50 | Kimi K2.5 Thinking | -1.358 | 30% | -1.533 to -1.194 |
| 51 | Xiaomi MiMo V2 Pro | -1.488 | 29% | -1.678 to -1.265 |
| 52 | Baidu Ernie 5.1 | -1.498 | 28% | -1.612 to -1.384 |
| 53 | Mistral Large 4 (high) | -1.894 | 23% | -1.993 to -1.803 |
| 54 | Mistral Large 3 | -2.046 | 22% | -2.162 to -1.910 |
| 55 | Gemma 4 31B Reasoning | -2.058 | 21% | -2.124 to -1.987 |
| 56 | ByteDance Seed2.0 Pro | -2.180 | 20% | -2.294 to -2.077 |
| 57 | Gemini 3.5 Flash | -2.253 | 19% | -2.335 to -2.175 |
| 58 | Gemini 3.1 Pro Preview | -2.441 | 17% | -2.533 to -2.336 |
| 59 | Qwen 3.6 Plus | -2.553 | 16% | -2.772 to -2.358 |
| 60 | Mistral Medium 3.5 | -2.699 | 15% | -2.802 to -2.601 |
| 61 | Qwen 3.7 Max | -2.931 | 13% | -3.065 to -2.821 |
| 62 | DeepSeek V3.2 | -3.137 | 11% | -3.380 to -2.906 |
| 63 | Grok 4.6 (high) | -3.173 | 11% | -3.327 to -3.014 |
| 64 | GPT-OSS-120B | -3.290 | 10% | -3.398 to -3.197 |
| 65 | MiniMax-M2.7 | -4.026 | 6% | -4.157 to -3.889 |
| 66 | Grok 4.3 | -4.516 | 3% | -4.703 to -4.351 |
| 67 | Grok 4.5 (high) | -5.350 | 1% | -5.443 to -5.262 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed. 20 of these required refusal retries (1 retry round).
- ^ Qwen3.8-27B: 389 of 400 stories completed. 46 of these required refusal retries (1 retry round).
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.
- ⁂ Qwen 4 Max (high): 397 of 400 stories completed.

Only completed stories were compared.
