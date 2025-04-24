# LLM Creative Story-Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

---
![Overall scores](/images/llm_overall_bar_zoomed_with_err.png)

---
## Method Summary
Each LLM produces 500 short stories, each approximately 400–500 words long, that must organically incorporate all assigned random elements.
In the updated April 2025 version of the benchmark, which uses newer grader LLMs, 27 of the latest models are evaluated. In the earlier version, 38 LLMs were assessed.

Six LLMs grade each of these stories on 16 questions regarding:
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



---
## Results
### Overall LLM Means

**Leaderboard:**
| Rank | LLM               | Mean  |
|-----:|-------------------|------:|
| 1 | o3 (medium reasoning) | 8.43 |
| 2 | DeepSeek R1 | 8.34 |
| 3 | GPT-4o Mar 2025 | 8.22 |
| 4 | Claude 3.7 Sonnet Thinking 16K | 8.15 |
| 5 | Gemini 2.5 Pro Exp 03-25 | 8.10 |
| 6 | Qwen QwQ-32B 16K | 8.07 |
| 7 | Gemma 3 27B | 8.04 |
| 8 | Claude 3.7 Sonnet | 8.00 |
| 9 | DeepSeek V3-0324 | 7.78 |
| 10 | Gemini 2.5 Flash Preview 24K | 7.72 |
| 11 | Grok 3 Beta (no reasoning) | 7.71 |
| 12 | GPT-4.5 Preview | 7.65 |
| 13 | o4-mini (medium reasoning) | 7.60 |
| 14 | Gemini 2.0 Flash Think Exp 01-21 | 7.49 |
| 15 | Claude 3.5 Haiku | 7.49 |
| 16 | Grok 3 Mini Beta (low) | 7.47 |
| 17 | Qwen 2.5 Max | 7.42 |
| 18 | Gemini 2.0 Flash Exp | 7.27 |
| 19 | o1 (medium reasoning) | 7.15 |
| 20 | Mistral Large 2 | 7.00 |
| 21 | GPT-4o mini | 6.84 |
| 22 | o1-mini | 6.64 |
| 23 | Microsoft Phi-4 | 6.40 |
| 24 | o3-mini (high reasoning) | 6.38 |
| 25 | o3-mini (medium reasoning) | 6.36 |
| 26 | Llama 4 Maverick | 6.35 |
| 27 | Amazon Nova Pro | 6.22 |
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
We record the grader LLMs' assessments of each story and summarize each model's writing. Detailed per-question comments from all grader LLMs are available in [comments_by_llm_1to6/](comments_by_llm_1to6/). Per-question summaries can be found in [summaries/](summaries/). Overall summaries are located in [general_summaries/](general_summaries/). hese summaries add much-needed color to otherwise dry numbers and are valuable for understanding each LLM's creative writing strengths and weaknesses.

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
  - Overall Mean (All Graders): 9.01
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

* **Story**: [story_364.txt](stories_wc/o3/story_364.txt) by o3 (medium reasoning)
  - Overall Mean (All Graders): 8.98
  - Grader Score Range: 6.30 (lowest: Grok 3 Beta (no reasoning)) .. 9.44 (highest: Claude 3.7 Sonnet)
  - Required Elements:
    - Character: skewed visionary
    - Object: botanical sketches
    - Core Concept: reexamining the familiar
    - Attribute: cryptically clear
    - Action: advise
    - Method: by following smudged hieroglyphs on broken pottery
    - Setting: temporal anomaly study
    - Timeframe: across the hush of a silent revolution
    - Motivation: to photograph vanishing trades
    - Tone: mundane miracles

* **Story**: [story_15.txt](stories_wc/r1/story_15.txt) by DeepSeek R1
  - Overall Mean (All Graders): 8.96
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


### Bottom 3 Individual Stories (All Graders)

* **Story**: [story_150.txt](stories_wc/nova-pro/story_150.txt) by Amazon Nova Pro. 4.44
* **Story**: [story_431.txt](stories_wc/nova-pro/story_431.txt) by Amazon Nova Pro. 4.86
* **Story**: [story_412.txt](stories_wc/nova-pro/story_412.txt) by Amazon Nova Pro. 4.92


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
| o3 (medium reasoning) | 1 | 8.43 | 1 | 8.47 |
| DeepSeek R1 | 2 | 8.34 | 2 | 8.39 |
| GPT-4o Mar 2025 | 3 | 8.22 | 3 | 8.27 |
| Claude 3.7 Sonnet Thinking 16K | 4 | 8.15 | 4 | 8.20 |
| Gemini 2.5 Pro Exp 03-25 | 5 | 8.10 | 5 | 8.16 |
| Qwen QwQ-32B 16K | 6 | 8.07 | 6 | 8.13 |
| Gemma 3 27B | 7 | 8.04 | 7 | 8.10 |
| Claude 3.7 Sonnet | 8 | 8.00 | 8 | 8.05 |
| DeepSeek V3-0324 | 9 | 7.78 | 9 | 7.84 |
| Gemini 2.5 Flash Preview 24K | 10 | 7.72 | 10 | 7.79 |
| Grok 3 Beta (no reasoning) | 11 | 7.71 | 11 | 7.78 |
| GPT-4.5 Preview | 12 | 7.65 | 12 | 7.72 |
| o4-mini (medium reasoning) | 13 | 7.60 | 13 | 7.68 |
| Gemini 2.0 Flash Think Exp 01-21 | 14 | 7.49 | 14 | 7.57 |
| Claude 3.5 Haiku | 15 | 7.49 | 15 | 7.56 |
| Grok 3 Mini Beta (low) | 16 | 7.47 | 16 | 7.54 |
| Qwen 2.5 Max | 17 | 7.42 | 17 | 7.49 |
| Gemini 2.0 Flash Exp | 18 | 7.27 | 18 | 7.35 |
| o1 (medium reasoning) | 19 | 7.15 | 19 | 7.23 |
| Mistral Large 2 | 20 | 7.01 | 20 | 7.10 |
| GPT-4o mini | 21 | 6.84 | 21 | 6.92 |
| o1-mini | 22 | 6.64 | 22 | 6.73 |
| Microsoft Phi-4 | 23 | 6.40 | 23 | 6.50 |
| o3-mini (high reasoning) | 24 | 6.38 | 24 | 6.47 |
| o3-mini (medium reasoning) | 25 | 6.36 | 25 | 6.44 |
| Llama 4 Maverick | 26 | 6.35 | 26 | 6.44 |
| Amazon Nova Pro | 27 | 6.22 | 27 | 6.32 |


Excluding any one LLM from grading also does not significantly change the rankings. For example, here is what happens when LLama 4 Maverick is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| o3 (medium reasoning) | 1 | 8.43 | 1 | 8.30 |
| DeepSeek R1 | 2 | 8.34 | 2 | 8.21 |
| GPT-4o Mar 2025 | 3 | 8.22 | 3 | 8.07 |
| Claude 3.7 Sonnet Thinking 16K | 4 | 8.15 | 4 | 8.00 |
| Gemini 2.5 Pro Exp 03-25 | 5 | 8.10 | 5 | 7.95 |
| Qwen QwQ-32B 16K | 6 | 8.07 | 6 | 7.91 |
| Gemma 3 27B | 7 | 8.04 | 7 | 7.89 |
| Claude 3.7 Sonnet | 8 | 8.00 | 8 | 7.82 |
| DeepSeek V3-0324 | 9 | 7.78 | 9 | 7.57 |
| Gemini 2.5 Flash Preview 24K | 10 | 7.72 | 10 | 7.50 |
| Grok 3 Beta (no reasoning) | 11 | 7.71 | 11 | 7.49 |
| GPT-4.5 Preview | 12 | 7.65 | 12 | 7.43 |
| o4-mini (medium reasoning) | 13 | 7.60 | 13 | 7.34 |
| Gemini 2.0 Flash Think Exp 01-21 | 14 | 7.49 | 14 | 7.23 |
| Claude 3.5 Haiku | 15 | 7.49 | 15 | 7.23 |
| Grok 3 Mini Beta (low) | 16 | 7.47 | 16 | 7.20 |
| Qwen 2.5 Max | 17 | 7.42 | 17 | 7.19 |
| Gemini 2.0 Flash Exp | 18 | 7.27 | 18 | 6.98 |
| o1 (medium reasoning) | 19 | 7.15 | 19 | 6.84 |
| Mistral Large 2 | 20 | 7.00 | 20 | 6.70 |
| GPT-4o mini | 21 | 6.84 | 21 | 6.52 |
| o1-mini | 22 | 6.64 | 22 | 6.24 |
| Microsoft Phi-4 | 23 | 6.40 | 23 | 6.00 |
| Llama 4 Maverick | 26 | 6.35 | 24 | 5.94 |
| o3-mini (high reasoning) | 24 | 6.38 | 25 | 5.93 |
| o3-mini (medium reasoning) | 25 | 6.36 | 26 | 5.90 |
| Amazon Nova Pro | 27 | 6.22 | 27 | 5.80 |

Normalizing each grader’s scores doesn’t significantly alter the rankings:

---
### Normalized Mean Leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | o3 (medium reasoning) | 1.141 |
| 2 | DeepSeek R1 | 1.029 |
| 3 | GPT-4o Mar 2025 | 0.927 |
| 4 | Claude 3.7 Sonnet Thinking 16K | 0.820 |
| 5 | Qwen QwQ-32B 16K | 0.734 |
| 6 | Gemini 2.5 Pro Exp 03-25 | 0.720 |
| 7 | Gemma 3 27B | 0.663 |
| 8 | Claude 3.7 Sonnet | 0.651 |
| 9 | DeepSeek V3-0324 | 0.402 |
| 10 | Gemini 2.5 Flash Preview 24K | 0.330 |
| 11 | Grok 3 Beta (no reasoning) | 0.327 |
| 12 | GPT-4.5 Preview | 0.286 |
| 13 | o4-mini (medium reasoning) | 0.257 |
| 14 | Grok 3 Mini Beta (low) | 0.112 |
| 15 | Claude 3.5 Haiku | 0.105 |
| 16 | Gemini 2.0 Flash Think Exp 01-21 | 0.096 |
| 17 | Qwen 2.5 Max | -0.074 |
| 18 | Gemini 2.0 Flash Exp | -0.138 |
| 19 | o1 (medium reasoning) | -0.296 |
| 20 | Mistral Large 2 | -0.503 |
| 21 | GPT-4o mini | -0.727 |
| 22 | o1-mini | -0.810 |
| 23 | o3-mini (high reasoning) | -1.071 |
| 24 | o3-mini (medium reasoning) | -1.088 |
| 25 | Microsoft Phi-4 | -1.180 |
| 26 | Llama 4 Maverick | -1.269 |
| 27 | Amazon Nova Pro | -1.442 |


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
