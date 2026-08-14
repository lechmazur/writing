# LLM Creative Story-Writing Benchmark

This benchmark compares short stories written to the same constrained creative briefs. Separate evaluator models read matched story pairs and choose which one is better. Those choices are combined into a relative comparison score.

Higher scores mean stronger performance against the other models tested. Scores are relative, not grades: zero is near the middle of this comparison set, and overlapping uncertainty ranges can indicate similarly rated models.

---

## Current Results

![Comparison ratings](images/inter_llm_comparison_thurstone_ratings.png)

### Leaderboard

Current comparison set:

- 44 rated models
- 537 direct model pairings
- 62,860 evaluator judgments
- the rating combines compatible evaluator-v2 and evaluator-v3 evidence after bridge validation
- the chart focuses on current models; the table retains all rated models for historical comparison
- striped bars and markers identify models that completed fewer than 400 stories

Labels such as `high`, `xhigh`, `max`, and `adaptive` identify the reasoning setting used for that model.
Estimated win chance is the model's average expected chance against another model in the full comparison set.

| Rank | Model | Comparison score | Estimated win chance | Uncertainty range |
|-----:|:------|-----------------:|---------------------:|:------------------|
| 1 | Claude Opus 5 (xhigh) | 4.2 | 96% | 4.2 to 4.3 |
| 2 | Claude Fable 5 (high)§ | 3.3 | 91% | 3.2 to 3.4 |
| 3 | Kimi K3 | 3.0 | 88% | 2.9 to 3.1 |
| 4 | GPT-5.6 Sol (xhigh) | 2.9 | 88% | 2.8 to 3.0 |
| 5 | GPT-5.5 (xhigh) | 2.9 | 87% | 2.8 to 2.9 |
| 6 | GPT-5.6 Sol (high) | 2.7 | 86% | 2.7 to 2.8 |
| 7 | GPT-5.4 (xhigh) | 2.4 | 82% | 2.3 to 2.5 |
| 8 | GPT-5.4 (medium) | 2.3 | 82% | 2.2 to 2.5 |
| 9 | Claude Opus 4.7 (adaptive)† | 2.2 | 81% | 2.1 to 2.3 |
| 10 | Claude Sonnet 4.6 (16K) | 2.1 | 79% | 2.0 to 2.2 |
| 11 | Claude Opus 4.6 (16K) | 1.5 | 72% | 1.3 to 1.7 |
| 12 | Muse Spark 1.1 (high) | 1.3 | 69% | 1.2 to 1.4 |
| 13 | Claude Opus 4.8 (xhigh) | 1.3 | 69% | 1.2 to 1.4 |
| 14 | GLM-5.2 (max) | 0.9 | 64% | 0.8 to 1.0 |
| 15 | Claude Opus 4.8 (high)‡ | 0.8 | 62% | 0.7 to 0.9 |
| 16 | GPT-5.2 (medium) | 0.8 | 62% | 0.6 to 0.9 |
| 17 | DeepSeek V4 Pro (high) | 0.8 | 61% | 0.6 to 0.9 |
| 18 | Qwen 3.8 Max¶ | 0.6 | 59% | 0.4 to 0.8 |
| 19 | Kimi K2.6 | 0.6 | 59% | 0.5 to 0.7 |
| 20 | MiniMax-M3 | 0.5 | 57% | 0.4 to 0.6 |
| 21 | Mistral Medium 3.1 | 0.1 | 51% | 0.0 to 0.2 |
| 22 | DeepSeek V4 Pro Preview | 0.0 | 49% | -0.2 to 0.1 |
| 23 | Xiaomi MiMo V2.5 Pro | -0.2 | 48% | -0.3 to 0.0 |
| 24 | Qwen 3 Max Preview | -0.2 | 47% | -0.4 to 0.0 |
| 25 | Gemini 3.7 Flash (high) | -0.4 | 44% | -0.5 to -0.2 |
| 26 | Qwen 3.6 Max Preview | -0.5 | 43% | -0.6 to -0.3 |
| 27 | GLM-5.1 | -0.5 | 42% | -0.7 to -0.4 |
| 28 | Kimi K2.5 | -0.6 | 41% | -0.8 to -0.4 |
| 29 | Xiaomi MiMo V2 Pro | -0.7 | 39% | -1.0 to -0.5 |
| 30 | Baidu Ernie 5.1 | -0.7 | 39% | -0.9 to -0.6 |
| 31 | Mistral Large 3 | -1.4 | 30% | -1.5 to -1.2 |
| 32 | Gemma 4 31B Reasoning | -1.4 | 29% | -1.6 to -1.3 |
| 33 | ByteDance Seed2.0 Pro | -1.5 | 27% | -1.7 to -1.4 |
| 34 | Gemini 3.5 Flash | -1.6 | 27% | -1.6 to -1.5 |
| 35 | Qwen 3.6 Plus | -1.8 | 24% | -2.0 to -1.6 |
| 36 | Gemini 3.1 Pro Preview | -1.8 | 23% | -2.0 to -1.7 |
| 37 | Mistral Medium 3.5 | -2.1 | 21% | -2.2 to -1.9 |
| 38 | Qwen 3.7 Max | -2.2 | 20% | -2.3 to -2.0 |
| 39 | DeepSeek V3.2 | -2.4 | 17% | -2.8 to -2.2 |
| 40 | Grok 4.6 (high) | -2.6 | 15% | -2.8 to -2.4 |
| 41 | GPT-OSS-120B | -2.7 | 14% | -2.8 to -2.5 |
| 42 | MiniMax-M2.7 | -3.3 | 9% | -3.5 to -3.2 |
| 43 | Grok 4.3 | -3.8 | 6% | -4.0 to -3.7 |
| 44 | Grok 4.5 (high) | -4.7 | 2% | -4.8 to -4.6 |

### Coverage Note

- † Claude Opus 4.7 completed 347 of 400 stories. Only completed stories were compared.
- ‡ Claude Opus 4.8 high completed 399 of 400 stories. Only completed stories were compared.
- § Claude Fable 5 high completed 395 of 400 stories. Only completed stories were compared.
- ¶ Qwen 3.8 Max completed 398 of 400 stories after one audited recovery pass. Only completed stories were compared.

---

## Head-to-Head Comparisons

![Pairwise margin heatmap](images/inter_llm_comparison_pair_margin_heatmap.png)

Read each cell by row. Red means the row model performed better, blue means the column model performed better, and grey means the models were not directly compared. Near-white cells indicate close results. Both axes follow the leaderboard order.

---

## Diagnostics

### Evaluator Agreement

![Evaluator agreement matrix](images/inter_llm_comparison_evaluator_agreement.png)

This chart shows how similarly the evaluator models scored the same story pairs. Values closer to 1 indicate stronger agreement; 0 means no consistent relationship, and negative values mean opposing scoring patterns.

### Word Count Compliance

![Word count compliance](images/inter_llm_comparison_word_count_ci.png)

Each dot is one story, and each diamond is a model's average length. Thin vertical lines show uncertainty around the averages. The shaded band is the 600-800-word target. This chart measures story length, not writing quality.

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

The comparison protocol keeps the prompt and required elements matched within each story pair. This makes the judgment about which story better satisfies the same creative brief, rather than which model happened to receive an easier prompt.

Evaluators consider required-element use, prose, coherence, character, originality, and overall effectiveness. The public score combines their choices; it is not an average 0-10 grade.

---

## Method Summary

1. Generate stories in the benchmark format.
2. Build matched story-comparison prompts for models that wrote to the same required elements.
3. Show each pair in both story orders to reduce first- or second-position effects.
4. Repeat comparisons across evaluators and combine their choices.
5. When an evaluator roster changes, validate shared prompts and bridge matchups before combining evidence.
6. Calculate relative model scores and their uncertainty ranges.

---

## Qualitative Pair Reports

For any two models with a direct comparison, `analyze_inter_llm_pair.py` can build a source-grounded report about recurring differences that a single winner score cannot express—for example, whether one writer seems more causally aware, strategically controlled, or intellectually convincing. The default analysis uses three independent critics on blinded groups of four or five matched stories, verifies every quoted example against the source text, and then runs one evidence-aware synthesis. Each report opens with a self-contained paragraph distilling its most useful comparison-specific findings.

```bash
python analyze_inter_llm_pair.py <focus-model> <comparison-model> --stage all
```

A typical 20-story comparison uses seven model calls. Run `--stage prepare` first to inspect the deterministic packet plan without making any model calls.

### New Models Compared with Their Predecessors

Given the same short-fiction prompts, DeepSeek V4 Pro High usually turns the required ingredients into obstacles, tools, and choices, while DeepSeek V4 Pro Preview more often turns them into luminous symbols whose meaning is announced and then fulfilled. The contrast is clearest when both receive a cracked magical instrument: High first makes the crack spoil the note, so the protagonist must discover how to work through the defect; Preview declares at once that the crack is the feature that makes the ritual succeed. That difference carries into endings. High tends to leave guilt, grief, or material damage in place after the revelation, whereas Preview more often lets private insight restore the surrounding world. Preview is plainly the more lavish image-maker, with denser metaphors and larger set pieces, but that strength does not offset its looser causal joints and habit of explaining significance. Overall, DeepSeek V4 Pro High produces the stronger fiction: its prompt elements more often do several jobs at once, and its resolutions grant only what the preceding events have earned.

Give both Qwen models the same short-fiction prompt and the difference shows up in what the required ingredients are made to do. Qwen 3.7 Max names them and then reassures you about them; Qwen 3.8 Max puts them to work and lets them cost something. In a story about a hidden government weather program, Qwen 3.7 Max's investigator seals his one incriminating ledger under a loose cobblestone in a courtyard he knows is watched, and the narration treats this as an unassailable triumph, while Qwen 3.8 Max's protagonist reasons that a single accusation can be erased and a widely shared record cannot, and sends it out to many hands. The habit extends to people. In Qwen 3.7 Max's stories nobody speaks aloud or asks the protagonist anything, so no one is ever corrected, and the threat is usually reported as already defeated; Qwen 3.8 Max's secondary characters bargain, testify, and ask the question that turns the scene. Endings follow from that: peace, home, and mastery on one side, and on the other a gain that names what it did not fix. Across twenty shared prompts the pattern held without exception. Qwen 3.7 Max remains the better writer of hands, tools, and physical procedure.

Given the same short-fiction prompts, Gemini 3.7 Flash (high) and Gemini 3.5 Flash work in the same lush allegorical register, but they treat the required ingredients differently. Gemini 3.5 Flash places each assigned object, trait, and deadline where the reader can see it and has the narration explain its significance; Gemini 3.7 Flash (high) connects the pieces so they cause one another, letting a pause between lightning and thunder become the reason a message can travel. The difference is clearest at the ending. Faced with a dead engineer's hidden confession, Gemini 3.5 Flash clicks restore and brings its lost people home; Gemini 3.7 Flash (high) leaves the engineer dead and scatters the confession through thousands of forgotten songs where no purge would think to look, keeping the testimony alive instead of erasing the grief. One model's stories close into comfort; the other's keep costs visible and send characters back to ordinary work. The gap is consistency, not range: Gemini 3.5 Flash sometimes finds the sharper conflict, as when it collides infinite patience with a real deadline, and Gemini 3.7 Flash (high)'s machinery is occasionally costume rather than engineering. Still, across shared prompts, the pattern rarely reversed.

Given the same short-fiction prompts, Grok 4.5 tends to recite its assignment: required phrases return verbatim as sentence subjects, the narrator explains what each symbol means, and closing lines sometimes certify that all elements “wove together seamlessly.” Grok 4.6 more often puts the same requirements to work: a mandated stretch of waiting becomes the story's theme, sediment layers narrate a city's collapse, a projector lens is used to project. Endings diverge just as sharply—Grok 4.5 declares the problem solved, in stability, harmony, and peace, while Grok 4.6 lets success arrive without canceling the contradiction, leaving merged timelines in permanent arrival and departure. The result feels like reading a completer beside a withholder. The pattern is consistent: Grok 4.6 produced the stronger story in fifteen of twenty shared prompts while writing slightly less. The qualification that matters is Grok 4.5's unevenness—it wrote the single most satisfying scene, a compassion ritual in which a broker realizes the anonymous benefactor being described is himself, alongside the boldest conceit and the clumsiest sentences. Choosing the best individual story gives Grok 4.5 a real case; choosing the typical one does not.

---

## Public Artifacts

The published bundle includes the story prompts and generated story text files for models visible in the public comparison charts. Prompt files are under `prompts_wc/`; model outputs are under `stories_wc/<model>/`.

---

## Archived Absolute Ratings

Earlier versions of this benchmark used absolute 0-10 rubric ratings rather than direct story comparisons. Those results remain historical context, but the current public quality ranking should use the pairwise comparison results above.

---

## Recent Updates
- August 14, 2026: Added DeepSeek V4 Pro high, Qwen 3.8 Max, Gemini 3.7 Flash high, and Grok 4.6 high, with matched qualitative comparisons against their predecessors.
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
