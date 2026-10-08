# Combined-panel comparison data

[Ratings and 95% bootstrap intervals](ratings.csv) · [Direct margins](pair_stats.csv) · [Unique story pairs](pair_story.csv) · [Evaluator agreement](evaluator_agreement.csv) · [Panel bridges](panel_bridges.csv) · [Story lengths](word_count_summary.csv)

This is a pooled observed-panel fit, using the same Thurstone estimator, side-bias correction and 300 story/evaluator bootstrap draws (seed 12345) as the pre-migration publication. Every accepted historical and current-panel judgment remains in the source ledger. Compatible source scopes are collapsed before fitting: one vote per distinct evaluator/story and one fit row per matched story pair. Grader versions are distinct; repeated source scopes do not confer extra votes.

Bootstrap intervals describe the pooled observed comparison set; they do not provide worst-case bounds for unavailable judgments or incomplete generations. The shaded chart strips restore the earlier density rendering derived from bootstrap interval widths.

[Previous calibrated-v4 analysis](../writing_v4_opus50/README.md) remains a separate snapshot with a different target and uncertainty method. Its wide bounded intervals are not reused as pooled bootstrap intervals.

The tables cover 57 writers, 934 direct model pairings, 15,692 distinct story pairs, and 105,704 judgments. All rated writers retain their overall ranks.

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

Only completed stories were compared.
