# LLM Creative Story-Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

![llm_overall_bar_zoomed_with_err](https://github.com/user-attachments/assets/75c398f4-acec-4754-80f9-bebc17966288)

## Method Summary
Each of the 25 LLMs produces 500 short stories - each targeted at 400–500 words long - that must organically integrate all assigned random elements. In total, 26 * 500 = 13,000 unique stories are generated.

Six LLMs grade each of these stories on 16 questions regarding:
1. Character Development & Motivation
2. Plot Structure & Coherence
3. World & Atmosphere
4. Storytelling Impact & Craft
5. Authenticity & Originality
6. Execution & Cohesion
7. 7A to 7J. Element fit for 10 required element: character, object, concept, attribute, action, method, setting, timeframe, motivation, tone

The grading LLMs are:
1. GPT-4o
2. Claude 3.5 Sonnet 2024-10-22
3. LLama 3.1 405B
4. DeepSeek-V3
5. Grok 2 12-12
6. Gemini 1.5 Pro (Sept)

In total, 26 * 500 * 6 * 16 = 1,248,000 grades are generated.

## Results
### Overall LLM Means

**Leaderboard:**
| Rank | LLM               | Mean  |
|-----:|-------------------|------:|
| 1 | DeepSeek R1 | 8.54 |
| 2 | Claude 3.5 Sonnet 2024-10-22 | 8.47 |
| 3 | Claude 3.5 Haiku | 8.07 |
| 4 | Gemini 1.5 Flash | 7.99 |
| 5 | Gemini 1.5 Pro (Sept) | 7.97 |
| 6 | Gemini 2.0 Flash Thinking Exp Old | 7.87 |
| 7 | Gemini 2.0 Flash Thinking Exp 01-21 | 7.82 |
| 8 | o1-preview | 7.74 |
| 9 | Gemini 2.0 Flash Exp | 7.65 |
| 10 | Qwen 2.5 Max | 7.64 |
| 11 | DeepSeek-V3 | 7.62 |
| 12 | o1 | 7.57 |
| 13 | Mistral Large 2 | 7.54 |
| 14 | Gemma 2 27B | 7.49 |
| 15 | Qwen QwQ | 7.44 |
| 16 | GPT-4o mini | 7.37 |
| 17 | GPT-4o | 7.36 |
| 18 | o1-mini | 7.30 |
| 19 | Claude 3 Opus | 7.17 |
| 20 | Qwen 2.5 72B | 7.00 |
| 21 | Grok 2 12-12 | 6.98 |
| 22 | Microsoft Phi-4 | 6.89 |
| 23 | Amazon Nova Pro | 6.70 |
| 24 | Llama 3.1 405B | 6.60 |
| 25 | Llama 3.3 70B | 5.95 |
| 26 | Claude 3 Haiku | 5.83 |

DeepSeek R1 and Claude 3.5 Sonnet emerge as the clear overall winners. Notably, Claude 3.5 Haiku shows a large improvement over Claude 3 Haiku. Gemini models perform well, while Llama models lag behind. Interestingly, larger, more expensive models did not outperform smaller models by as much as one might expect.

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all questions, with Grader LLMs marked in different colors:

![questions_overall_strip](https://github.com/user-attachments/assets/357b2855-62e1-47d1-b824-c5a5cf590fa1)

![normalized_scores_strip](https://github.com/user-attachments/assets/4cc77170-5445-4d73-973c-bf2f2b72a64b)

The plot reveals that Llama 3.1 405B occasionally, and DeepSeek-V3 sporadically, award a perfect 10 across the board, despite prompts explicitly asking them to be strict graders.

### LLM vs. Question (Detailed)
A heatmap showing each LLM's mean rating per question:

![llm_vs_question_detailed](https://github.com/user-attachments/assets/70dd58e1-c1b3-40c8-b49a-b0bf2b2ff9ef)

Before DeepSeek R1's release, Claude 3.5 Sonnet ranked #1 on every single question.

### LLM #1 Finishes
Which LLM ranked #1 the most times across all stories? This pie chart shows the distribution of #1 finishes:

![llm_best_pie](https://github.com/user-attachments/assets/9faceac4-2ac3-49a4-a3f5-f3fa9ef2e1f2)

Claude 3.5 Sonnet's and R1's dominance is undeniable when analyzing the best scores by story.

### Grader - LLM Mean Heatmap
A heatmap of Grader (row) vs. LLM (column) average scores:

![grader_vs_llm_means](https://github.com/user-attachments/assets/53c4879c-32f9-463d-bfb9-c0574eeb5909)

The chart highlights that grading LLMs do not disproportionately overrate their own stories. 

### Grader-Grader Correlation
A correlation matrix (−1 to 1 scale) measuring how strongly multiple LLMs correlate when cross-grading the same stories:

![teacher_grader_correlation](https://github.com/user-attachments/assets/bb20ca48-ea7b-4fd2-8cef-d0e6d21e1bd5)

Llama 3.1 405B's grades show the least correlation with other LLMs, though the correlation remains relatively high, with a minimum of 0.66.

## Story Length
A basic prompt asking LLMs to create a 400-500 word story resulted in an unacceptable range of story lengths. A revised prompt instructing each LLM to track the number of words after each sentence improved consistency somewhat but still fell short of the accuracy needed for fair grading. These stories are available in [stories_first/](stories_first/). For example, Claude 3.5 Haiku consistently produced stories that were significantly too short:

![count-before](https://github.com/user-attachments/assets/b2a2f691-478a-49c0-a6c2-409b9342ac94)

Since the benchmark aims to evaluate how well LLMs write, not how well they count or follow prompts about the format, we adjusted the word counts in the prompt for different LLMs to approximately match the target story length - an approach similar to what someone dissatisfied with the initial story length might adopt. Qwen QwQ and Llama 3.x models required the most extensive prompt engineering to achieve the required word counts and to adhere to the proper output format across all 500 stories. Note that this did not require any evaluation of the story's content itself. These final stories were then graded and they are available in [stories_wc/](stories_wc/).

![word_count](https://github.com/user-attachments/assets/21a2aa55-d359-4680-a058-d279481d27b9)

This chart shows the correlations between each LLM's scores and their story lengths:

![len_vs_score_overall_enhanced](https://github.com/user-attachments/assets/bc01b859-73cb-4ae2-a77a-d8a1f10163f0)

This chart shows the correlations between each Grader LLM's scores and the lengths of stories they graded:

![len_vs_score_grader_enhanced](https://github.com/user-attachments/assets/12f14a43-5cc2-4e66-96d1-e964424093d7)

## Best and Worst Stories
Here, we list the top 3 and the bottom 3 individual stories (written by any LLM) out of the 13,000 generated, based on the average scores from our grader LLMs, and include the required elements for each. Feel free to evaluate their quality for yourself!

### Top 3 Individual Stories (All Graders)

* **Story**: [story_386.txt](stories_wc/r1/story_386.txt) by DeepSeek R1
  - Overall Mean (All Graders): 9.27
  - Grader Score Range: 8.31 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: time refugee from a forgotten empire
    - Object: embroidered tablecloth
    - Core Concept: quietly defiant
    - Attribute: trustworthy strange
    - Action: catapult
    - Method: by the alignment of the stars
    - Setting: atom-powered lighthouse
    - Timeframe: in the hush of a line that never moves
    - Motivation: to bind old wounds with unstoppable will
    - Tone: borrowed dawn

* **Story**: [story_185.txt](stories_wc/r1/story_185.txt) by DeepSeek R1
  - Overall Mean (All Graders): 9.24
  - Grader Score Range: 7.56 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: peculiar collector
    - Object: old pencil stub
    - Core Concept: buried talents
    - Attribute: infuriatingly calm
    - Action: tweak
    - Method: by decoding the arrangement of keys left in a piano bench
    - Setting: probability mapping center
    - Timeframe: across millennia
    - Motivation: to make a final stand
    - Tone: fractured grace

* **Story**: [story_166.txt](stories_wc/r1/story_166.txt) by DeepSeek R1
  - Overall Mean (All Graders): 9.22
  - Grader Score Range: 8.19 (lowest: Claude 3.5 Sonnet 2024-10-22) .. 10.00 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: ghostly caretaker
    - Object: plastic straw
    - Core Concept: weaving through fate
    - Attribute: solemnly silly
    - Action: perforate
    - Method: through forbidden expedition logs
    - Setting: frozen orchard feeding off geothermal streams
    - Timeframe: after the last wish is granted
    - Motivation: to communicate with animals
    - Tone: gentle chaos

### Bottom 3 Individual Stories (All Graders)

* **Story**: [story_385.txt](stories_wc/claude_mini/story_385.txt) by Claude 3 Haiku. 3.77
* **Story**: [story_450.txt](stories_wc/llama33_70b/story_450.txt) by Llama 3.3 70B. 3.88
* **Story**: [story_4.txt](stories_wc/claude_mini/story_4.txt) by Claude 3 Haiku. 3.86

## Ablation

A valid concern is whether LLM graders can accurately score questions 1 to 6 (Major Story Aspects), such as Character Development & Motivation. However, questions 7A to 7J (Element Integration) are clearly much easier for LLM graders to evaluate correctly, and we observe a very high correlation between the grades for questions 1 to 6 and 7A to 7J across all grader - LLM combinations. We also observe a high correlation among the grader LLMs themselves. Overall, the per-story correlation of 1-6 vs 7A-7J is 0.949 (N=78,000). While we cannot be certain that these ratings are correct without human validation, the consistency suggests that something real is being measured. But we can simply ignore questions 1 to 6 and just use ratings for 7A to 7J:

### Questions 7A to 7J Only: Element Integration

![llm_overall_bar_zoomed_7Ato7J](https://github.com/user-attachments/assets/58df1484-999f-4bb6-849c-5819e1beaa99)

Excluding 10% worst stories per LLM does not significantly change the rankings:
### Rankings After Excluding the 50 Lowest-Rated Stories per LLM

| LLM Full | Old Rank | Old Mean | New Rank | New Mean |
|----------|---------:|---------:|---------:|---------:|
| DeepSeek R1 | 1 | 8.54 | 1 | 8.60 |
| Claude 3.5 Sonnet 2024-10-22 | 2 | 8.47 | 2 | 8.54 |
| Claude 3.5 Haiku | 3 | 8.07 | 3 | 8.15 |
| Gemini 1.5 Flash | 4 | 7.99 | 4 | 8.09 |
| Gemini 1.5 Pro (Sept) | 5 | 7.97 | 5 | 8.06 |
| Gemini 2.0 Flash Thinking Exp Old | 6 | 7.87 | 6 | 7.96 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 7 | 7.82 | 7 | 7.93 |
| o1-preview | 8 | 7.74 | 8 | 7.85 |
| Gemini 2.0 Flash Exp | 9 | 7.65 | 9 | 7.76 |
| DeepSeek-V3 | 11 | 7.62 | 10 | 7.74 |
| Qwen 2.5 Max | 10 | 7.64 | 11 | 7.74 |
| o1 | 12 | 7.57 | 12 | 7.68 |
| Mistral Large 2 | 13 | 7.54 | 13 | 7.65 |
| Gemma 2 27B | 14 | 7.49 | 14 | 7.60 |
| Qwen QwQ | 15 | 7.44 | 15 | 7.55 |
| GPT-4o | 17 | 7.36 | 16 | 7.47 |
| GPT-4o mini | 16 | 7.37 | 17 | 7.46 |
| o1-mini | 18 | 7.30 | 18 | 7.44 |
| Claude 3 Opus | 19 | 7.17 | 19 | 7.30 |
| Grok 2 12-12 | 21 | 6.98 | 20 | 7.12 |
| Qwen 2.5 72B | 20 | 7.00 | 21 | 7.12 |
| Microsoft Phi-4 | 22 | 6.89 | 22 | 7.02 |
| Amazon Nova Pro | 23 | 6.70 | 23 | 6.84 |
| Llama 3.1 405B | 24 | 6.60 | 24 | 6.72 |
| Llama 3.3 70B | 25 | 5.95 | 25 | 6.08 |
| Claude 3 Haiku | 26 | 5.83 | 26 | 5.97 |


Excluding any one LLM from grading also does not significantly change the rankings. For example, here is what happens when LLama 3.1 405B is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| DeepSeek R1 | 1 | 8.54 | 1 | 8.36 |
| Claude 3.5 Sonnet 2024-10-22 | 2 | 8.47 | 2 | 8.25 |
| Claude 3.5 Haiku | 3 | 8.07 | 3 | 7.75 |
| Gemini 1.5 Flash | 4 | 7.99 | 4 | 7.73 |
| Gemini 1.5 Pro (Sept) | 5 | 7.97 | 5 | 7.73 |
| Gemini 2.0 Flash Thinking Exp Old | 6 | 7.87 | 6 | 7.64 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 7 | 7.82 | 7 | 7.54 |
| o1-preview | 8 | 7.74 | 8 | 7.47 |
| Qwen 2.5 Max | 10 | 7.64 | 9 | 7.42 |
| DeepSeek-V3 | 11 | 7.62 | 10 | 7.36 |
| Gemini 2.0 Flash Exp | 9 | 7.65 | 11 | 7.36 |
| o1 | 12 | 7.57 | 12 | 7.29 |
| Gemma 2 27B | 14 | 7.49 | 13 | 7.29 |
| Mistral Large 2 | 13 | 7.54 | 14 | 7.24 |
| Qwen QwQ | 15 | 7.44 | 15 | 7.18 |
| GPT-4o mini | 16 | 7.37 | 16 | 7.09 |
| GPT-4o | 17 | 7.36 | 17 | 7.03 |
| o1-mini | 18 | 7.30 | 18 | 6.91 |
| Claude 3 Opus | 19 | 7.17 | 19 | 6.84 |
| Qwen 2.5 72B | 20 | 7.00 | 20 | 6.66 |
| Grok 2 12-12 | 21 | 6.98 | 21 | 6.63 |
| Microsoft Phi-4 | 22 | 6.89 | 22 | 6.49 |
| Amazon Nova Pro | 23 | 6.70 | 23 | 6.34 |
| Llama 3.1 405B | 24 | 6.60 | 24 | 6.18 |
| Llama 3.3 70B | 25 | 5.95 | 25 | 5.41 |
| Claude 3 Haiku | 26 | 5.83 | 26 | 5.32 |

Normalizing each grader’s scores doesn’t significantly alter the rankings:

### Normalized Mean Leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | DeepSeek R1 | 1.092 |
| 2 | Claude 3.5 Sonnet 2024-10-22 | 1.044 |
| 3 | Claude 3.5 Haiku | 0.641 |
| 4 | Gemini 1.5 Flash | 0.564 |
| 5 | Gemini 1.5 Pro (Sept) | 0.543 |
| 6 | Gemini 2.0 Flash Thinking Exp Old | 0.449 |
| 7 | Gemini 2.0 Flash Thinking Exp 01-21 | 0.399 |
| 8 | o1-preview | 0.332 |
| 9 | Gemini 2.0 Flash Exp | 0.255 |
| 10 | DeepSeek-V3 | 0.200 |
| 11 | Qwen 2.5 Max | 0.193 |
| 12 | o1 | 0.156 |
| 13 | Mistral Large 2 | 0.142 |
| 14 | Gemma 2 27B | 0.024 |
| 15 | Qwen QwQ | -0.018 |
| 16 | GPT-4o | -0.040 |
| 17 | o1-mini | -0.048 |
| 18 | GPT-4o mini | -0.054 |
| 19 | Claude 3 Opus | -0.229 |
| 20 | Grok 2 12-12 | -0.388 |
| 21 | Qwen 2.5 72B | -0.399 |
| 22 | Microsoft Phi-4 | -0.496 |
| 23 | Amazon Nova Pro | -0.718 |
| 24 | Llama 3.1 405B | -0.747 |
| 25 | Llama 3.3 70B | -1.358 |
| 26 | Claude 3 Haiku | -1.537 |



## Details
Strip plots divided between questions 1-6 and questions 7A-7J:

![questions_1to6_strip](https://github.com/user-attachments/assets/bb462817-9d86-4bf2-9ea1-40963908002d)

![questions_7A_J_strip](https://github.com/user-attachments/assets/12ba3463-1a8e-4809-9e4c-50c48960bb59)

Full range of scores:

![llm_overall_bar_start0_with_err](https://github.com/user-attachments/assets/305d7170-a324-46e7-9fb9-f5c9fee9b5bd)


## Updates and Other Benchmarks
- Jan 31, 2025: DeepSeek R1, o1, Gemini 2.0 Flash Thinking Exp 01-21, Microsoft Phi-4, Amazon Nova Pro added.
- Also check out the [LLM Step Game](https://github.com/lechmazur/step_game), [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization), [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/), [NYT Connections Benchmark](https://github.com/lechmazur/nyt-connections/), [LLM Deception Benchmark](https://github.com/lechmazur/deception) and [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent).
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
