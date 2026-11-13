# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 64 writers, 1,093 direct model pairings, 18,902 distinct story pairs, and 124,844 judgments. All rated writers retain their overall ranks.

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | **Claude Fable 5.2 (high)** | 3.687 | 93% | 3.623 to 3.771 |
| 2 | Claude Fable 5.1 (high) | 3.636 | 93% | 3.560 to 3.722 |
| 3 | Claude Opus 5 (xhigh) | 3.558 | 92% | 3.496 to 3.617 |
| 4 | Claude Opus 5.5 (high) | 3.555 | 92% | 3.470 to 3.635 |
| 5 | GPT-6 Astra (high) | 3.318 | 91% | 3.254 to 3.382 |
| 6 | Claude Opus 5 (high) | 3.180 | 89% | 3.086 to 3.284 |
| 7 | GLM-5.3 (max) | 2.806 | 86% | 2.713 to 2.889 |
| 8 | Claude Fable 5 (high)§ | 2.691 | 85% | 2.629 to 2.755 |
| 9 | Kimi K3.1 Pro (high) | 2.550 | 83% | 2.461 to 2.639 |
| 10 | GPT-5.6 Sol (xhigh) | 2.305 | 81% | 2.226 to 2.386 |
| 11 | GPT-5.5 (xhigh) | 2.273 | 81% | 2.207 to 2.336 |
| 12 | Kimi K3 | 2.218 | 80% | 2.143 to 2.289 |
| 13 | **Tencent Hy4 (high)** | 2.211 | 80% | 2.121 to 2.297 |
| 14 | GPT-5.6 Sol (high) | 2.118 | 79% | 2.031 to 2.192 |
| 15 | GPT-5.4 (medium) | 1.799 | 75% | 1.651 to 1.918 |
| 16 | GPT-5.4 (xhigh) | 1.793 | 75% | 1.681 to 1.896 |
| 17 | **Gemini 4 Carbon (high)** | 1.752 | 74% | 1.670 to 1.860 |
| 18 | Muse Wonder (high) | 1.749 | 74% | 1.674 to 1.826 |
| 19 | Claude Opus 4.7 (high)† | 1.601 | 72% | 1.500 to 1.709 |
| 20 | Claude Sonnet 4.6 Thinking 16K | 1.490 | 71% | 1.385 to 1.598 |
| 21 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.318 | 69% | 1.204 to 1.435 |
| 22 | Claude Opus 4.6 Thinking 16K | 0.960 | 64% | 0.804 to 1.123 |
| 23 | Claude Opus 4.8 (xhigh) | 0.602 | 59% | 0.499 to 0.711 |
| 24 | Muse Spark 1.1 (high) | 0.598 | 59% | 0.479 to 0.697 |
| 25 | Gemini 4 Argon (high) | 0.551 | 58% | 0.453 to 0.654 |
| 26 | Muse Spark 1.3 (high) | 0.340 | 55% | 0.247 to 0.426 |
| 27 | GLM-5.2 (max) | 0.291 | 54% | 0.178 to 0.393 |
| 28 | DeepSeek V4 Pro (high) | 0.258 | 54% | 0.161 to 0.368 |
| 29 | Grok 4.7 (high) | 0.183 | 52% | -0.002 to 0.362 |
| 30 | GPT-5.2 (medium) | 0.164 | 52% | -0.002 to 0.317 |
| 31 | Claude Opus 4.8 (high)‡ | 0.089 | 51% | -0.001 to 0.200 |
| 32 | Qwen 3.8 Max¶ | -0.052 | 49% | -0.148 to 0.038 |
| 33 | Gemini 3.8 Flash (high) | -0.075 | 49% | -0.178 to 0.039 |
| 34 | Kimi K2.6 | -0.085 | 48% | -0.181 to 0.027 |
| 35 | **Step 5 Preview (high)** | -0.103 | 48% | -0.228 to 0.021 |
| 36 | Muse Spark 1.2 (high) | -0.220 | 46% | -0.313 to -0.115 |
| 37 | MiniMax-M3 | -0.294 | 45% | -0.415 to -0.182 |
| 38 | Mistral Medium 3.1 | -0.554 | 41% | -0.690 to -0.418 |
| 39 | DeepSeek V4.1 Flash (high) | -0.697 | 39% | -0.792 to -0.599 |
| 40 | DeepSeek V4 Pro Preview | -0.708 | 39% | -0.826 to -0.600 |
| 41 | Xiaomi MiMo V2.5 Pro | -0.848 | 37% | -0.987 to -0.713 |
| 42 | Qwen 3 Max Preview | -0.852 | 37% | -1.045 to -0.671 |
| 43 | Qwen3.8-27B^ | -0.866 | 37% | -0.986 to -0.733 |
| 44 | Gemini 3.7 Flash (high) | -0.886 | 37% | -1.012 to -0.760 |
| 45 | Qwen 3.6 Max Preview | -1.098 | 34% | -1.219 to -0.983 |
| 46 | GLM-5.1 | -1.196 | 32% | -1.346 to -1.018 |
| 47 | Kimi K2.5 Thinking | -1.250 | 31% | -1.418 to -1.092 |
| 48 | Xiaomi MiMo V2 Pro | -1.379 | 30% | -1.617 to -1.158 |
| 49 | Baidu Ernie 5.1 | -1.408 | 29% | -1.546 to -1.292 |
| 50 | Mistral Large 4 (high) | -1.799 | 24% | -1.891 to -1.694 |
| 51 | Mistral Large 3 | -1.937 | 23% | -2.058 to -1.808 |
| 52 | Gemma 4 31B Reasoning | -1.991 | 22% | -2.065 to -1.910 |
| 53 | ByteDance Seed2.0 Pro | -2.059 | 21% | -2.174 to -1.960 |
| 54 | Gemini 3.5 Flash | -2.148 | 20% | -2.248 to -2.062 |
| 55 | Gemini 3.1 Pro Preview | -2.334 | 18% | -2.425 to -2.223 |
| 56 | Qwen 3.6 Plus | -2.446 | 17% | -2.633 to -2.260 |
| 57 | Mistral Medium 3.5 | -2.633 | 15% | -2.753 to -2.498 |
| 58 | Qwen 3.7 Max | -2.827 | 13% | -2.948 to -2.708 |
| 59 | DeepSeek V3.2 | -3.028 | 12% | -3.279 to -2.796 |
| 60 | Grok 4.6 (high) | -3.060 | 11% | -3.221 to -2.914 |
| 61 | GPT-OSS-120B | -3.233 | 10% | -3.318 to -3.139 |
| 62 | MiniMax-M2.7 | -3.922 | 6% | -4.062 to -3.790 |
| 63 | Grok 4.3 | -4.412 | 4% | -4.574 to -4.226 |
| 64 | Grok 4.5 (high) | -5.246 | 1% | -5.341 to -5.160 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed. 20 of these required refusal retries (1 retry round).
- ^ Qwen3.8-27B: 389 of 400 stories completed. 46 of these required refusal retries (1 retry round).
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.

Only completed stories were compared.
