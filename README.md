# LLM Creative Story-Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

---
![Overall scores](/images/llm_overall_bar_zoomed_with_err.png)

---
## Method Summary
Each LLM produces 500 short stories, each approximately 400–500 words long, that must organically incorporate all assigned random elements.
In the updated April 2025 version of the benchmark, which uses newer grader LLMs, 33 of the latest models are evaluated. In the earlier version, 38 LLMs were assessed.

Seven LLMs grade each of these stories on 16 questions regarding:
1. Character Development & Motivation
2. Plot Structure & Coherence
3. World & Atmosphere
4. Storytelling Impact & Craft
5. Authenticity & Originality
6. Execution & Cohesion
7. 7A to 7J. Element fit for 10 required element: character, object, concept, attribute, action, method, setting, timeframe, motivation, tone

The new grading LLMs are:
1. GPT-4o Mar 2025
2. Claude 3.7 Sonnet
3. Llama 4 Maverick
4. DeepSeek V3-0324 
5. Grok 3 Beta (no reasoning)
6. Gemini 2.5 Pro Exp
7. Qwen 3 235B



---
## Results
### Overall LLM Means

**Leaderboard:**
| Rank | LLM               | Mean  |
|-----:|-------------------|------:|
| 1 | o3 (medium reasoning) | 8.39 |
| 2 | Qwen 3 235B A22B | 8.30 |
| 3 | DeepSeek R1 | 8.30 |
| 4 | GPT-4o Mar 2025 | 8.18 |
| 5 | Claude 3.7 Sonnet Thinking 16K | 8.11 |
| 6 | Gemini 2.5 Pro Preview 05-06 | 8.09 |
| 7 | Gemini 2.5 Pro Exp 03-25 | 8.05 |
| 8 | Claude 3.5 Sonnet 2024-10-22 | 8.03 |
| 9 | Qwen QwQ-32B 16K | 8.02 |
| 10 | Gemma 3 27B | 7.99 |
| 11 | Claude 3.7 Sonnet | 7.94 |
| 12 | Mistral Medium 3 | 7.73 |
| 13 | DeepSeek V3-0324 | 7.70 |
| 14 | Gemini 2.5 Flash Preview 24K | 7.65 |
| 15 | Grok 3 Beta (no reasoning) | 7.64 |
| 16 | GPT-4.5 Preview | 7.56 |
| 17 | Qwen 3 30B A3B | 7.53 |
| 18 | o4-mini (medium reasoning) | 7.50 |
| 19 | Gemini 2.0 Flash Think Exp 01-21 | 7.38 |
| 20 | Claude 3.5 Haiku | 7.35 |
| 21 | Grok 3 Mini Beta (low) | 7.35 |
| 22 | Qwen 2.5 Max | 7.29 |
| 23 | Gemini 2.0 Flash Exp | 7.15 |
| 24 | o1 (medium reasoning) | 7.02 |
| 25 | Mistral Large 2 | 6.90 |
| 26 | GPT-4o mini | 6.72 |
| 27 | o1-mini | 6.49 |
| 28 | Grok 2 12-12 | 6.36 |
| 29 | Microsoft Phi-4 | 6.26 |
| 30 | Llama 4 Maverick | 6.20 |
| 31 | o3-mini (high reasoning) | 6.17 |
| 32 | o3-mini (medium reasoning) | 6.15 |
| 33 | Amazon Nova Pro | 6.05 |
---

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all stories, with Grader LLMs marked in different colors:

![Normalized scores strip chart](/images/normalized_scores_strip.png)

---
### LLM vs. Question (Detailed)
A heatmap showing each LLM's mean rating per question:

![LLM per question](/images/llm_vs_question_detailed.png)


---
### LLM #1 Finishes
Which LLM ranked #1 the most times across all stories? This pie chart shows the distribution of #1 finishes:

![#1 stories pie chart](/images/llm_best_pie.png)


---
### Grader - LLM Mean Heatmap
A heatmap of Grader (row) vs. LLM (column) average scores:

![Grader vs LLM normalized](/images/grader_vs_llm_normalized_means.png)

The chart highlights that grading LLMs do not disproportionately overrate their own stories. 

---
### Grader-Grader Correlation
A correlation matrix (−1 to 1 scale) measuring how strongly multiple LLMs correlate when cross-grading the same stories:

![Grader vs LLM correlation](/images/teacher_grader_correlation.png)

---
## Summaries
We record the grader LLMs' assessments of each story and summarize each model's writing. Detailed per-question comments from all grader LLMs are available in [comments_by_llm_1to6/](comments_by_llm_1to6/). Per-question summaries can be found in [summaries/](summaries/). Overall summaries are located in [general_summaries/](general_summaries/). These summaries add much-needed color to otherwise dry numbers and are valuable for understanding each LLM's creative writing strengths and weaknesses.

### For example, here is the general assessment of **o4-mini**:

**Strengths:**
o4-mini consistently demonstrates a robust technical command of contemporary literary style, structure, and conceptual sophistication. Across all tasks, its prose is fluent and often displays striking imagery, inventive metaphor, and an ability to construct cohesive narrative arcs within varied word constraints. The model is adept at integrating assigned elements (e.g., objects, settings, required themes), often weaving them into atmospheres that are rich, immersive, and sometimes philosophically resonant. Thematic ambition is a hallmark, with recurring explorations of memory, transformation, contradiction, and existential stakes—attesting to its “breadth of subject matter and conceptual ingenuity.” Symbols, motifs, and metaphors are frequently deployed in ways that demonstrate an understanding of advanced literary devices.

**Weaknesses:**
Despite these technical strengths, the model’s writing often falls short in delivering narrative and emotional depth. Characters tend to function as conduits for themes or plot, lacking distinctive voices, specific motivations, or authentic psychological transformation—resulting in “surface-level characterization” and a “mechanical” sense of emotional change. Conflict, stakes, and genuine struggle are frequently underdeveloped or circumvented via poetic abstraction, with “telling” vastly outpacing “showing.” The resolve towards ornate, lyrical language brings diminishing returns: stories are saturated with decorative or “purple” prose, which too often obscures clarity, action, or genuine feeling. Abstraction and symbolism, while inventive, routinely displace specificity, leading to a sense of aesthetic sameness across outputs—where different stories begin to blur into stylistic variations on the same exercise. Even when the integration of assigned elements is seamless, this is often cosmetic; true organic unity—where every aspect is motivated by character or plot necessity—is rare. Endings are poetically gestured at rather than earned, with “thematic closure” favored over narrative resolution.

**Summary Judgment:**
o4-mini is a skilled mimic of modern literary fiction’s forms and ambitions, but it struggles to transcend simulation. Its stylistic confidence and conceptual facility often mask a persistent emotional hollowness, avoidance of narrative risk, and an unearned reliance on abstraction. To reach the next level—to produce fiction that lingers and moves—it must ground its aesthetic and thematic flights in lived, dramatized, and character-specific experience, embracing risk, specificity, and the unpredictable complexity of human drama.


---
## Best and Worst Stories
Here, we list the top 3 and the bottom 3 individual stories (written by any LLM) out of the 13,000 generated, based on the average scores from our grader LLMs, and include the required elements for each. Feel free to evaluate their quality for yourself!

### Top 3 Individual Stories (All Graders)

* **Story**: [story_403.txt](stories_wc/r1/story_403.txt) by DeepSeek R1
  - Overall Mean (All Graders): 9.00
  - Grader Score Range: 7.76 (lowest: Grok 3 Beta (no reasoning)) .. 9.64 (highest: Llama 4 Maverick)
  - Required Elements:
    - Character: hope-worn knight
    - Object: ordinary seashell
    - Core Concept: consistent miracles
    - Attribute: deeply superficial
    - Action: seclude
    - Method: by reading faint notations on a faded fortune teller’s booth
    - Setting: floating library
    - Timeframe: across the boundary between real and myth
    - Motivation: to escape the limitations of perception
    - Tone: joyful agony

* **Story**: [story_15.txt](stories_wc/r1/story_15.txt) by DeepSeek R1
  - Overall Mean (All Graders): 8.99
  - Grader Score Range: 7.57 (lowest: Grok 3 Beta (no reasoning)) .. 9.50 (highest: Llama 4 Maverick)
  - Required Elements:
    - Character: gracious widow
    - Object: blacksmith’s forge
    - Core Concept: tethered by hope
    - Attribute: solemnly absurd
    - Action: nurture
    - Method: through mysterious postcards
    - Setting: ruined orchard district lost in centuries of thick fog
    - Timeframe: between meals
    - Motivation: to defy the gods
    - Tone: serious playfulness

* **Story**: [story_360.txt](stories_wc/o3/story_360.txt) by o3 (medium reasoning)
  - Overall Mean (All Graders): 8.93
  - Grader Score Range: 6.97 (lowest: Grok 3 Beta (no reasoning)) .. 9.50 (highest: Claude 3.7 Sonnet)
  - Required Elements:
    - Character: meek necromancer
    - Object: fountain pen with a broken nib
    - Core Concept: the tangled tapestry
    - Attribute: peculiarly sincere
    - Action: regain
    - Method: through the way light reflects off a dew drop
    - Setting: underground city of the goblins
    - Timeframe: amid playground sounds
    - Motivation: to decode a universal riddle
    - Tone: mystic simplicity


### Bottom 3 Individual Stories (All Graders)

* **Story**: [story_150.txt](stories_wc/nova-pro/story_150.txt) by Amazon Nova Pro. 4.44
* **Story**: [story_194.txt](stories_wc/o3-mini/story_194.txt) by o3-mini (medium reasoning). 4.59
* **Story**: [story_431.txt](stories_wc/nova-pro/story_431.txt) by Amazon Nova Pro. 4.71


---
## Story Length
A basic prompt asking LLMs to create a 400-500 word story resulted in an unacceptable range of story lengths. A revised prompt instructing each LLM to track the number of words after each sentence improved consistency somewhat but still fell short of the accuracy needed for fair grading. 

Since the benchmark aims to evaluate how well LLMs write, not how well they count or follow prompts about the format, we adjusted the word counts in the prompt for different LLMs to approximately match the target story length - an approach similar to what someone dissatisfied with the initial story length might adopt. Note that this did not require any evaluation of the story's content itself. These final stories were then graded and they are available in [stories_wc/](stories_wc/).

![Word count distribution by model](/images/word_count_distribution_by_model.png)

This chart shows the correlations between each LLM's scores and their story lengths:

![Len vs score](/images/len_vs_score_overall_enhanced.png)

This chart shows the correlations between each Grader LLM's scores and the lengths of stories they graded:

![Length vs score by grader](/images/len_vs_score_grader_enhanced.png)

---

## Ablation

A valid concern is whether LLM graders can accurately score questions 1 to 6 (Major Story Aspects), such as Character Development & Motivation. However, questions 7A to 7J (Element Integration) are clearly much easier for LLM graders to evaluate correctly, and we observe a very high correlation between the grades for questions 1 to 6 and 7A to 7J across all grader - LLM combinations. We also observe a high correlation among the grader LLMs themselves. Overall, the per-story correlation of 1-6 vs 7A-7J is 0.926 (N=N=81,000). While we cannot be certain that these ratings are correct without human validation, the consistency suggests that something real is being measured. But we can simply ignore questions 1 to 6 and just use ratings for 7A to 7J:

### Questions 7A to 7J Only: Element Integration

![Element Integration](/images/llm_overall_bar_zoomed_7Ato7J.png)


---
Excluding 10% worst stories per LLM does not significantly change the rankings:
### Rankings After Excluding the 50 Lowest-Rated Stories per LLM

| LLM Full | Old Rank | Old Mean | New Rank | New Mean |
|----------|---------:|---------:|---------:|---------:|
| o3 (medium reasoning) | 1 | 8.39 | 1 | 8.44 |
| Qwen 3 235B A22B | 2 | 8.30 | 2 | 8.36 |
| DeepSeek R1 | 3 | 8.30 | 3 | 8.36 |
| GPT-4o Mar 2025 | 4 | 8.18 | 4 | 8.23 |
| Claude 3.7 Sonnet Thinking 16K | 5 | 8.11 | 5 | 8.17 |
| Gemini 2.5 Pro Preview 05-06 | 6 | 8.09 | 6 | 8.15 |
| Gemini 2.5 Pro Exp 03-25 | 7 | 8.05 | 7 | 8.11 |
| Claude 3.5 Sonnet 2024-10-22 | 8 | 8.03 | 8 | 8.09 |
| Qwen QwQ-32B 16K | 9 | 8.02 | 9 | 8.09 |
| Gemma 3 27B | 10 | 7.99 | 10 | 8.06 |
| Claude 3.7 Sonnet | 11 | 7.94 | 11 | 8.00 |
| Mistral Medium 3 | 12 | 7.73 | 12 | 7.82 |
| DeepSeek V3-0324 | 13 | 7.69 | 13 | 7.77 |
| Gemini 2.5 Flash Preview 24K | 14 | 7.65 | 14 | 7.73 |
| Grok 3 Beta (no reasoning) | 15 | 7.64 | 15 | 7.70 |
| GPT-4.5 Preview | 16 | 7.56 | 16 | 7.63 |
| Qwen 3 30B A3B | 17 | 7.53 | 17 | 7.61 |
| o4-mini (medium reasoning) | 18 | 7.50 | 18 | 7.58 |
| Gemini 2.0 Flash Think Exp 01-21 | 19 | 7.38 | 19 | 7.47 |
| Claude 3.5 Haiku | 20 | 7.35 | 20 | 7.43 |
| Grok 3 Mini Beta (low) | 21 | 7.35 | 21 | 7.42 |
| Qwen 2.5 Max | 22 | 7.29 | 22 | 7.37 |
| Gemini 2.0 Flash Exp | 23 | 7.15 | 23 | 7.24 |
| o1 (medium reasoning) | 24 | 7.02 | 24 | 7.11 |
| Mistral Large 2 | 25 | 6.90 | 25 | 7.00 |
| GPT-4o mini | 26 | 6.72 | 26 | 6.80 |
| o1-mini | 27 | 6.49 | 27 | 6.58 |
| Grok 2 12-12 | 28 | 6.36 | 28 | 6.46 |
| Microsoft Phi-4 | 29 | 6.26 | 29 | 6.35 |
| Llama 4 Maverick | 30 | 6.20 | 30 | 6.29 |
| o3-mini (high reasoning) | 31 | 6.17 | 31 | 6.26 |
| o3-mini (medium reasoning) | 32 | 6.15 | 32 | 6.24 |
| Amazon Nova Pro | 33 | 6.05 | 33 | 6.15 |


Excluding any one LLM from grading also does not significantly change the rankings. For example, here is what happens when LLama 4 Maverick is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| o3 (medium reasoning) | 1 | 8.39 | 1 | 8.27 |
| DeepSeek R1 | 3 | 8.30 | 2 | 8.19 |
| Qwen 3 235B A22B | 2 | 8.30 | 3 | 8.19 |
| GPT-4o Mar 2025 | 4 | 8.18 | 4 | 8.04 |
| Claude 3.7 Sonnet Thinking 16K | 5 | 8.11 | 5 | 7.98 |
| Gemini 2.5 Pro Preview 05-06 | 6 | 8.09 | 6 | 7.96 |
| Gemini 2.5 Pro Exp 03-25 | 7 | 8.05 | 7 | 7.92 |
| Claude 3.5 Sonnet 2024-10-22 | 8 | 8.03 | 8 | 7.89 |
| Qwen QwQ-32B 16K | 9 | 8.02 | 9 | 7.88 |
| Gemma 3 27B | 10 | 7.99 | 10 | 7.85 |
| Claude 3.7 Sonnet | 11 | 7.94 | 11 | 7.78 |
| Mistral Medium 3 | 12 | 7.73 | 12 | 7.55 |
| DeepSeek V3-0324 | 13 | 7.69 | 13 | 7.51 |
| Gemini 2.5 Flash Preview 24K | 14 | 7.65 | 14 | 7.46 |
| Grok 3 Beta (no reasoning) | 15 | 7.64 | 15 | 7.44 |
| GPT-4.5 Preview | 16 | 7.56 | 16 | 7.36 |
| Qwen 3 30B A3B | 17 | 7.53 | 17 | 7.32 |
| o4-mini (medium reasoning) | 18 | 7.50 | 18 | 7.26 |
| Gemini 2.0 Flash Think Exp 01-21 | 19 | 7.38 | 19 | 7.14 |
| Claude 3.5 Haiku | 20 | 7.35 | 20 | 7.11 |
| Grok 3 Mini Beta (low) | 21 | 7.35 | 21 | 7.10 |
| Qwen 2.5 Max | 22 | 7.29 | 22 | 7.08 |
| Gemini 2.0 Flash Exp | 23 | 7.15 | 23 | 6.89 |
| o1 (medium reasoning) | 24 | 7.02 | 24 | 6.74 |
| Mistral Large 2 | 25 | 6.90 | 25 | 6.63 |
| GPT-4o mini | 26 | 6.72 | 26 | 6.43 |
| o1-mini | 27 | 6.49 | 27 | 6.13 |
| Grok 2 12-12 | 28 | 6.36 | 28 | 6.03 |
| Microsoft Phi-4 | 29 | 6.26 | 29 | 5.90 |
| Llama 4 Maverick | 30 | 6.20 | 30 | 5.83 |
| o3-mini (high reasoning) | 31 | 6.17 | 31 | 5.76 |
| o3-mini (medium reasoning) | 32 | 6.15 | 32 | 5.73 |
| Amazon Nova Pro | 33 | 6.05 | 33 | 5.67 |

Normalizing each grader’s scores doesn’t significantly alter the rankings:

---
### Normalized Mean Leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | o3 (medium reasoning) | 1.069 |
| 2 | DeepSeek R1 | 0.963 |
| 3 | Qwen 3 235B A22B | 0.962 |
| 4 | GPT-4o Mar 2025 | 0.860 |
| 5 | Claude 3.7 Sonnet Thinking 16K | 0.766 |
| 6 | Claude 3.5 Sonnet 2024-10-22 | 0.687 |
| 7 | Qwen QwQ-32B 16K | 0.677 |
| 8 | Gemini 2.5 Pro Preview 05-06 | 0.675 |
| 9 | Gemini 2.5 Pro Exp 03-25 | 0.667 |
| 10 | Gemma 3 27B | 0.608 |
| 11 | Claude 3.7 Sonnet | 0.591 |
| 12 | Mistral Medium 3 | 0.341 |
| 13 | DeepSeek V3-0324 | 0.337 |
| 14 | Gemini 2.5 Flash Preview 24K | 0.276 |
| 15 | Grok 3 Beta (no reasoning) | 0.269 |
| 16 | GPT-4.5 Preview | 0.216 |
| 17 | Qwen 3 30B A3B | 0.190 |
| 18 | o4-mini (medium reasoning) | 0.176 |
| 19 | Grok 3 Mini Beta (low) | 0.023 |
| 20 | Gemini 2.0 Flash Think Exp 01-21 | 0.017 |
| 21 | Claude 3.5 Haiku | 0.009 |
| 22 | Qwen 2.5 Max | -0.143 |
| 23 | Gemini 2.0 Flash Exp | -0.213 |
| 24 | o1 (medium reasoning) | -0.361 |
| 25 | Mistral Large 2 | -0.536 |
| 26 | GPT-4o mini | -0.760 |
| 27 | o1-mini | -0.877 |
| 28 | Grok 2 12-12 | -1.139 |
| 29 | o3-mini (high reasoning) | -1.173 |
| 30 | o3-mini (medium reasoning) | -1.188 |
| 31 | Microsoft Phi-4 | -1.212 |
| 32 | Llama 4 Maverick | -1.301 |
| 33 | Amazon Nova Pro | -1.476 |



---
## Old Leaderboard
| Rank | LLM               | Mean  |
|-----:|-------------------|------:|
| 1 | GPT-4o Mar 2025 | 8.55 |
| 2 | DeepSeek R1 | 8.54 |
| 3 | Claude 3.7 Sonnet Thinking 16K | 8.51 |
| 4 | Claude 3.5 Sonnet 2024-10-22 | 8.47 |
| 5 | Claude 3.7 Sonnet | 8.39 |
| 6 | Qwen QwQ-32B 16K | 8.34 |
| 7 | Gemini 2.5 Pro Exp 03-24 | 8.30 |
| 8 | Gemma 3 27B | 8.22 |
| 9 | DeepSeek V3-0324 | 8.09 |
| 10 | Gemini 2.0 Pro Exp 02-05 | 8.08 |
| 11 | GPT-4.5 Preview | 8.07 |
| 12 | Claude 3.5 Haiku | 8.07 |
| 13 | Gemini 1.5 Pro (Sept) | 7.97 |
| 14 | GPT-4o Feb 2025 | 7.96 |
| 15 | Gemini 2.0 Flash Thinking Exp Old | 7.87 |
| 16 | GPT-4o 2024-11-20 | 7.87 |
| 17 | Gemini 2.0 Flash Thinking Exp 01-21 | 7.82 |
| 18 | o1-preview | 7.74 |
| 19 | Gemini 2.0 Flash Exp | 7.65 |
| 20 | Qwen 2.5 Max | 7.64 |
| 21 | DeepSeek-V3 | 7.62 |
| 22 | o1 | 7.57 |
| 23 | Mistral Large 2 | 7.54 |
| 24 | Gemma 2 27B | 7.49 |
| 25 | Qwen QwQ Preview | 7.44 |
| 26 | GPT-4o mini | 7.37 |
| 27 | GPT-4o 2024-08-06 | 7.36 |
| 28 | o1-mini | 7.30 |
| 29 | Claude 3 Opus | 7.17 |
| 30 | Qwen 2.5 72B | 7.00 |
| 31 | o3-mini-high | 6.99 |
| 32 | Grok 2 12-12 | 6.98 |
| 33 | o3-mini | 6.90 |
| 34 | Microsoft Phi-4 | 6.89 |
| 35 | Amazon Nova Pro | 6.70 |
| 36 | Llama 4 Maverick | 6.67 |
| 37 | Llama 3.1 405B | 6.60 |
| 38 | Llama 3.3 70B | 5.95 |
| 39 | Claude 3 Haiku | 5.83 |


The old grading LLMs were:
1. GPT-4o
2. Claude 3.5 Sonnet 2024-10-22
3. LLama 3.1 405B
4. DeepSeek V3
5. Grok 2 12-12
6. Gemini 1.5 Pro (Sept)

---
## Details
Full range of scores:

![Full range](/images/llm_overall_bar_start0_with_err.png)

---
## Limitations

It's important to note that each story is graded individually rather than as part of a collection. Consequently, LLMs may exhibit repetitive creative patterns, such as recurring plot devices, themes, or character archetypes across different stories. Future assessments will include criteria evaluating originality and variety.

---

## Other multi-agent benchmarks
- [Public Goods Game (PGG) Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception in Multi-Agent LLMs](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)

## Other benchmarks
- [Extended NYT Connections](https://github.com/lechmazur/nyt-connections/)
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)
---
## Updates 
- May 8, 2025: Gemini 2.5 Pro Preview 05-06 and Mistral Medium 3 added.
- May 1, 2025: Qwen 3 models added. Qwen 3 235B added as a grader.
- Apr 24, 2025: Major update: grader LLMs replaced with newer versions, additional specific grading criteria, 0.1 grading granularity, summaries. Added: o3, o4-mini, Gemini 2.5 Flash Preview 16K.
- Apr 11, 2025: Grok 3 added.
- Apr 6, 2025: Llama 4 Maverick added. Some older models excluded from charts.
- Mar 28, 2025: GPT-4o March 2025 added.
- Mar 26, 2025: Gemini 2.5 Pro Exp 03-25, DeepSeek V3-0324, o3-mini-high added.
- Mar 13, 2025: Gemma 3 27B added.
- Mar 10, 2025: Qwen QwQ-32B added.
- Feb 26, 2025: GPT-4.5 Preview added.
- Feb 25, 2025: Claude 3.7 Sonnet, Claude 3.7 Sonnet Thinking, GPT-4o Feb 2025, GPT-4o 2024-11-20, Gemini 2.0 Pro Exp 02-05 added.
- Feb 1, 2025: o3-mini (medium reasoning effort) added.
- Jan 31, 2025: DeepSeek R1, o1, Gemini 2.0 Flash Thinking Exp 01-21, Microsoft Phi-4, Amazon Nova Pro added.
- Follow [@lechmazur](https://x.com/LechMazur) on X for other upcoming benchmarks and more.
