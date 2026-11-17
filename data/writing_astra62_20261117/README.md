# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 67 writers, 1,167 direct model pairings, 20,382 distinct story pairs, and 133,723 judgments. All rated writers retain their overall ranks.

| Rank | Model | Comparison score | Estimated win chance | 95% bootstrap interval |
| ---: | --- | ---: | ---: | --- |
| 1 | **GPT-6.2 Astra (high)** | 4.169 | 95% | 4.083 to 4.261 |
| 2 | **Qwen 4 Max (high)⁂** | 3.618 | 92% | 3.544 to 3.690 |
| 3 | Claude Fable 5.2 (high) | 3.555 | 92% | 3.476 to 3.625 |
| 4 | Claude Fable 5.1 (high) | 3.512 | 91% | 3.430 to 3.589 |
| 5 | Claude Opus 5 (xhigh) | 3.446 | 91% | 3.383 to 3.505 |
| 6 | Claude Opus 5.5 (high) | 3.374 | 90% | 3.306 to 3.455 |
| 7 | GPT-6 Astra (high) | 3.184 | 89% | 3.125 to 3.246 |
| 8 | Claude Opus 5 (high) | 3.053 | 88% | 2.952 to 3.161 |
| 9 | GLM-5.3 (max) | 2.612 | 84% | 2.538 to 2.692 |
| 10 | Claude Fable 5 (high)§ | 2.586 | 83% | 2.521 to 2.654 |
| 11 | Kimi K3.1 Pro (high) | 2.364 | 81% | 2.287 to 2.448 |
| 12 | GPT-5.6 Sol (xhigh) | 2.201 | 79% | 2.126 to 2.285 |
| 13 | GPT-5.5 (xhigh) | 2.170 | 79% | 2.098 to 2.233 |
| 14 | Kimi K3 | 2.105 | 78% | 2.018 to 2.176 |
| 15 | Tencent Hy4 (high) | 2.044 | 78% | 1.969 to 2.126 |
| 16 | GPT-5.6 Sol (high) | 2.013 | 77% | 1.932 to 2.099 |
| 17 | GPT-5.4 (medium) | 1.693 | 73% | 1.565 to 1.815 |
| 18 | GPT-5.4 (xhigh) | 1.687 | 73% | 1.578 to 1.815 |
| 19 | Gemini 4 Carbon (high) | 1.616 | 72% | 1.542 to 1.708 |
| 20 | Muse Wonder (high) | 1.607 | 72% | 1.537 to 1.691 |
| 21 | Claude Opus 4.7 (high)† | 1.497 | 71% | 1.389 to 1.607 |
| 22 | Claude Sonnet 4.6 Thinking 16K | 1.386 | 70% | 1.284 to 1.489 |
| 23 | Xiaomi MiMo V2.6 Pro (thinking)※ | 1.190 | 67% | 1.092 to 1.287 |
| 24 | Claude Opus 4.6 Thinking 16K | 0.854 | 62% | 0.686 to 1.034 |
| 25 | Claude Opus 4.8 (xhigh) | 0.501 | 57% | 0.387 to 0.594 |
| 26 | Muse Spark 1.1 (high) | 0.496 | 57% | 0.401 to 0.607 |
| 27 | Gemini 4 Argon (high) | 0.452 | 57% | 0.359 to 0.544 |
| 28 | Muse Spark 1.3 (high) | 0.234 | 54% | 0.154 to 0.314 |
| 29 | GLM-5.2 (max) | 0.183 | 53% | 0.088 to 0.284 |
| 30 | DeepSeek V4 Pro (high) | 0.140 | 52% | 0.051 to 0.231 |
| 31 | GPT-5.2 (medium) | 0.057 | 51% | -0.095 to 0.217 |
| 32 | Grok 4.7 (high) | 0.028 | 51% | -0.112 to 0.173 |
| 33 | Claude Opus 4.8 (high)‡ | -0.012 | 50% | -0.118 to 0.096 |
| 34 | Gemini 3.8 Flash (high) | -0.159 | 48% | -0.257 to -0.062 |
| 35 | Qwen 3.8 Max¶ | -0.171 | 48% | -0.245 to -0.084 |
| 36 | Step 5 Preview (high) | -0.187 | 47% | -0.297 to -0.073 |
| 37 | Kimi K2.6 | -0.189 | 47% | -0.295 to -0.100 |
| 38 | Muse Spark 1.2 (high) | -0.329 | 45% | -0.442 to -0.229 |
| 39 | MiniMax-M3 | -0.390 | 44% | -0.495 to -0.267 |
| 40 | Mistral Medium 3.1 | -0.659 | 40% | -0.788 to -0.518 |
| 41 | **ByteDance Seed2.1 Pro** | -0.669 | 40% | -0.761 to -0.555 |
| 42 | DeepSeek V4.1 Flash (high) | -0.798 | 38% | -0.885 to -0.694 |
| 43 | DeepSeek V4 Pro Preview | -0.813 | 38% | -0.926 to -0.702 |
| 44 | Xiaomi MiMo V2.5 Pro | -0.955 | 36% | -1.067 to -0.836 |
| 45 | Qwen 3 Max Preview | -0.957 | 36% | -1.116 to -0.777 |
| 46 | Qwen3.8-27B^ | -0.959 | 36% | -1.084 to -0.846 |
| 47 | Gemini 3.7 Flash (high) | -0.994 | 35% | -1.122 to -0.873 |
| 48 | Qwen 3.6 Max Preview | -1.205 | 32% | -1.347 to -1.085 |
| 49 | GLM-5.1 | -1.301 | 31% | -1.474 to -1.137 |
| 50 | Kimi K2.5 Thinking | -1.356 | 30% | -1.537 to -1.194 |
| 51 | Xiaomi MiMo V2 Pro | -1.486 | 29% | -1.736 to -1.280 |
| 52 | Baidu Ernie 5.1 | -1.499 | 28% | -1.622 to -1.377 |
| 53 | Mistral Large 4 (high) | -1.896 | 23% | -1.978 to -1.811 |
| 54 | Mistral Large 3 | -2.044 | 22% | -2.162 to -1.938 |
| 55 | Gemma 4 31B Reasoning | -2.060 | 21% | -2.127 to -1.976 |
| 56 | ByteDance Seed2.0 Pro | -2.179 | 20% | -2.281 to -2.068 |
| 57 | Gemini 3.5 Flash | -2.252 | 19% | -2.340 to -2.153 |
| 58 | Gemini 3.1 Pro Preview | -2.439 | 17% | -2.536 to -2.350 |
| 59 | Qwen 3.6 Plus | -2.551 | 16% | -2.739 to -2.329 |
| 60 | Mistral Medium 3.5 | -2.700 | 15% | -2.800 to -2.601 |
| 61 | Qwen 3.7 Max | -2.930 | 13% | -3.058 to -2.789 |
| 62 | DeepSeek V3.2 | -3.135 | 11% | -3.394 to -2.922 |
| 63 | Grok 4.6 (high) | -3.172 | 11% | -3.327 to -3.038 |
| 64 | GPT-OSS-120B | -3.292 | 10% | -3.389 to -3.206 |
| 65 | MiniMax-M2.7 | -4.025 | 6% | -4.160 to -3.889 |
| 66 | Grok 4.3 | -4.515 | 3% | -4.682 to -4.326 |
| 67 | Grok 4.5 (high) | -5.349 | 1% | -5.447 to -5.247 |

### Coverage Note

- † Claude Opus 4.7: 347 of 400 stories completed.
- ‡ Claude Opus 4.8 high: 399 of 400 stories completed.
- § Claude Fable 5 high: 395 of 400 stories completed.
- ¶ Qwen 3.8 Max: 398 of 400 stories completed. 20 of these required refusal retries (1 retry round).
- ^ Qwen3.8-27B: 389 of 400 stories completed. 46 of these required refusal retries (1 retry round).
- ※ MiMo V2.6 Pro: 375 of 400 stories completed.
- ⁂ Qwen 4 Max (high): 397 of 400 stories completed.

Only completed stories were compared.
