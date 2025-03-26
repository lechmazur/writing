# LLM Creative Story-Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

---
![Overall scores](/images/llm_overall_bar_zoomed_with_err.png)

---
## Method Summary
Each of the 37 LLMs produces 500 short stories - each targeted at 400–500 words long - that must organically integrate all assigned random elements. In total, 37 * 500 = 18,500 unique stories are generated.

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

In total, 37 * 500 * 6 * 16 = 1,776,000 grades are generated.

---
## Results
### Overall LLM Means

**Leaderboard:**
| Rank | LLM               | Mean  |
|-----:|-------------------|------:|
| 1 | DeepSeek R1 | 8.54 |
| 2 | Claude 3.7 Sonnet Thinking 16K | 8.51 |
| 3 | Claude 3.5 Sonnet 2024-10-22 | 8.47 |
| 4 | Claude 3.7 Sonnet | 8.39 |
| 5 | Qwen QwQ-32B 16K | 8.34 |
| 6 | Gemini 2.5 Pro Exp 03-24 | 8.30 |
| 7 | Gemma 3 27B | 8.22 |
| 8 | DeepSeek V3-0324 | 8.09 |
| 9 | Gemini 2.0 Pro Exp 02-05 | 8.08 |
| 10 | GPT-4.5 Preview | 8.07 |
| 11 | Claude 3.5 Haiku | 8.07 |
| 12 | Gemini 1.5 Pro (Sept) | 7.97 |
| 13 | GPT-4o Feb 2025 | 7.96 |
| 14 | Gemini 2.0 Flash Thinking Exp Old | 7.87 |
| 15 | GPT-4o 2024-11-20 | 7.87 |
| 16 | Gemini 2.0 Flash Thinking Exp 01-21 | 7.82 |
| 17 | o1-preview | 7.74 |
| 18 | Gemini 2.0 Flash Exp | 7.65 |
| 19 | Qwen 2.5 Max | 7.64 |
| 20 | DeepSeek-V3 | 7.62 |
| 21 | o1 | 7.57 |
| 22 | Mistral Large 2 | 7.54 |
| 23 | Gemma 2 27B | 7.49 |
| 24 | Qwen QwQ Preview | 7.44 |
| 25 | GPT-4o mini | 7.37 |
| 26 | GPT-4o 2024-08-06 | 7.36 |
| 27 | o1-mini | 7.30 |
| 28 | Claude 3 Opus | 7.17 |
| 29 | Qwen 2.5 72B | 7.00 |
| 30 | o3-mini-high | 6.99 |
| 31 | Grok 2 12-12 | 6.98 |
| 32 | o3-mini | 6.90 |
| 33 | Microsoft Phi-4 | 6.89 |
| 34 | Amazon Nova Pro | 6.70 |
| 35 | Llama 3.1 405B | 6.60 |
| 36 | Llama 3.3 70B | 5.95 |
| 37 | Claude 3 Haiku | 5.83 |

Qwen QwQ-32B joins DeepSeek R1 and Claude Sonnet as the clear overall winners. Notably, Claude 3.5 Haiku shows a large improvement upon Claude 3 Haiku and Gemma 3 shows a large improvement upon Gemma 2. Gemini models perform well, while Llama models lag behind. Interestingly, larger, more expensive models did not outperform smaller models by as much as one might expect. o3-mini performs worse than expected.

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all stories, with Grader LLMs marked in different colors:

![Normalized scores strip chart](/images/normalized_scores_strip)

The plot reveals that Llama 3.1 405B occasionally, and DeepSeek-V3 sporadically, award a perfect 10 across the board, despite prompts explicitly asking them to be strict graders.

### LLM vs. Question (Detailed)
A heatmap showing each LLM's mean rating per question:

![LLM per question](/images/llm_vs_question_detailed.png)

Before DeepSeek R1's release, Claude 3.5 Sonnet ranked #1 on every single question.

### LLM #1 Finishes
Which LLM ranked #1 the most times across all stories? This pie chart shows the distribution of #1 finishes:

![#1 stories pie chart](/images/llm_best_pie.png)

Claude Sonnet's and R1's dominance is undeniable when analyzing the best scores by story. Qwen QwQ-32B and Gemma 3 27B get some victories.

### Grader - LLM Mean Heatmap
A heatmap of Grader (row) vs. LLM (column) average scores:

![Grader vs LLM normalized](/images/grader_vs_llm_normalized_means.png)

The chart highlights that grading LLMs do not disproportionately overrate their own stories. Llama 3.1 405B is impressed by the o3-mini, while other grading LLMs dislike its stories.

### Grader-Grader Correlation
A correlation matrix (−1 to 1 scale) measuring how strongly multiple LLMs correlate when cross-grading the same stories:

![Grader vs LLM correlation](/images/teacher_grader_correlation.png)

Llama 3.1 405B's grades show the least correlation with other LLMs.

## Story Length
A basic prompt asking LLMs to create a 400-500 word story resulted in an unacceptable range of story lengths. A revised prompt instructing each LLM to track the number of words after each sentence improved consistency somewhat but still fell short of the accuracy needed for fair grading. These stories are available in [stories_first/](stories_first/). For example, Claude 3.5 Haiku consistently produced stories that were significantly too short:

![count-before](https://github.com/user-attachments/assets/b2a2f691-478a-49c0-a6c2-409b9342ac94)

Since the benchmark aims to evaluate how well LLMs write, not how well they count or follow prompts about the format, we adjusted the word counts in the prompt for different LLMs to approximately match the target story length - an approach similar to what someone dissatisfied with the initial story length might adopt. Qwen QwQ and Llama 3.x models required the most extensive prompt engineering to achieve the required word counts and to adhere to the proper output format across all 500 stories. Note that this did not require any evaluation of the story's content itself. These final stories were then graded and they are available in [stories_wc/](stories_wc/).

![Word count distribution by model](/images/word_count_distribution_by_model.png)

This chart shows the correlations between each LLM's scores and their story lengths:

![Len vs score](/images/len_vs_score_overall_enhanced.png)

o3-mini and o1 seem to force too many of their stories to be exactly within the specified limits, which may hurt their grades.

This chart shows the correlations between each Grader LLM's scores and the lengths of stories they graded:

![Length vs score by grader](/images/len_vs_score_grader_enhanced.png)

---
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

* **Story**: [story_197.txt](stories_wc/claude-3-7-sonnet-20250219-thinking/story_197.txt) by Claude 3.7 Sonnet Thinking 16K
  - Overall Mean (All Graders): 9.25
  - Grader Score Range: 7.56 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: high-altitude con artist
    - Object: piece of fabric scrap
    - Core Concept: where nightmares collide
    - Attribute: mundanely terrifying
    - Action: further
    - Method: by unscrambling a set of sticky notes rearranged daily
    - Setting: yggdrasil-like tree
    - Timeframe: during the hush after a child’s last bedtime story
    - Motivation: to compose a cosmic lullaby
    - Tone: pristine chaos

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


### Bottom 3 Individual Stories (All Graders)

* **Story**: [story_385.txt](stories_wc/claude_mini/story_385.txt) by Claude 3 Haiku. 3.77
* **Story**: [story_450.txt](stories_wc/llama33_70b/story_450.txt) by Llama 3.3 70B. 3.88
* **Story**: [story_4.txt](stories_wc/claude_mini/story_4.txt) by Claude 3 Haiku. 3.86

---

## Ablation

A valid concern is whether LLM graders can accurately score questions 1 to 6 (Major Story Aspects), such as Character Development & Motivation. However, questions 7A to 7J (Element Integration) are clearly much easier for LLM graders to evaluate correctly, and we observe a very high correlation between the grades for questions 1 to 6 and 7A to 7J across all grader - LLM combinations. We also observe a high correlation among the grader LLMs themselves. Overall, the per-story correlation of 1-6 vs 7A-7J is 0.949 (N=78,000). While we cannot be certain that these ratings are correct without human validation, the consistency suggests that something real is being measured. But we can simply ignore questions 1 to 6 and just use ratings for 7A to 7J:

### Questions 7A to 7J Only: Element Integration

![Element Integration](/images/llm_overall_bar_zoomed_7Ato7J.png)


Excluding 10% worst stories per LLM does not significantly change the rankings:
### Rankings After Excluding the 50 Lowest-Rated Stories per LLM

| LLM Full | Old Rank | Old Mean | New Rank | New Mean |
|----------|---------:|---------:|---------:|---------:|
| DeepSeek R1 | 1 | 8.54 | 1 | 8.60 |
| Claude 3.7 Sonnet Thinking 16K | 2 | 8.51 | 2 | 8.57 |
| Claude 3.5 Sonnet 2024-10-22 | 3 | 8.47 | 3 | 8.54 |
| Claude 3.7 Sonnet | 4 | 8.39 | 4 | 8.45 |
| Qwen QwQ-32B 16K | 5 | 8.34 | 5 | 8.41 |
| Gemini 2.5 Pro Exp 03-24 | 6 | 8.30 | 6 | 8.36 |
| Gemma 3 27B | 7 | 8.22 | 7 | 8.29 |
| DeepSeek V3-0324 | 8 | 8.09 | 8 | 8.17 |
| Gemini 2.0 Pro Exp 02-05 | 9 | 8.08 | 9 | 8.16 |
| GPT-4.5 Preview | 10 | 8.07 | 10 | 8.16 |
| Claude 3.5 Haiku | 11 | 8.07 | 11 | 8.15 |
| Gemini 1.5 Pro (Sept) | 12 | 7.97 | 12 | 8.06 |
| GPT-4o Feb 2025 | 13 | 7.96 | 13 | 8.05 |
| Gemini 2.0 Flash Thinking Exp Old | 14 | 7.87 | 14 | 7.96 |
| GPT-4o 2024-11-20 | 15 | 7.87 | 15 | 7.95 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 16 | 7.82 | 16 | 7.93 |
| o1-preview | 17 | 7.74 | 17 | 7.85 |
| Gemini 2.0 Flash Exp | 18 | 7.65 | 18 | 7.76 |
| DeepSeek-V3 | 20 | 7.62 | 19 | 7.74 |
| Qwen 2.5 Max | 19 | 7.64 | 20 | 7.74 |
| o1 | 21 | 7.57 | 21 | 7.68 |
| Mistral Large 2 | 22 | 7.54 | 22 | 7.65 |
| Gemma 2 27B | 23 | 7.49 | 23 | 7.60 |
| Qwen QwQ Preview | 24 | 7.44 | 24 | 7.55 |
| GPT-4o 2024-08-06 | 26 | 7.36 | 25 | 7.47 |
| GPT-4o mini | 25 | 7.37 | 26 | 7.46 |
| o1-mini | 27 | 7.30 | 27 | 7.44 |
| Claude 3 Opus | 28 | 7.17 | 28 | 7.30 |
| o3-mini-high | 30 | 6.99 | 29 | 7.12 |
| Grok 2 12-12 | 31 | 6.98 | 30 | 7.12 |
| Qwen 2.5 72B | 29 | 7.00 | 31 | 7.12 |
| o3-mini | 32 | 6.90 | 32 | 7.04 |
| Microsoft Phi-4 | 33 | 6.89 | 33 | 7.02 |
| Amazon Nova Pro | 34 | 6.70 | 34 | 6.84 |
| Llama 3.1 405B | 35 | 6.60 | 35 | 6.72 |
| Llama 3.3 70B | 36 | 5.95 | 36 | 6.08 |


Excluding any one LLM from grading also does not significantly change the rankings. For example, here is what happens when LLama 3.1 405B is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| DeepSeek R1 | 1 | 8.54 | 1 | 8.36 |
| Claude 3.7 Sonnet Thinking 16K | 2 | 8.51 | 2 | 8.29 |
| Claude 3.5 Sonnet 2024-10-22 | 3 | 8.47 | 3 | 8.25 |
| Qwen QwQ-32B 16K | 5 | 8.34 | 4 | 8.17 |
| Claude 3.7 Sonnet | 4 | 8.39 | 5 | 8.17 |
| Gemini 2.5 Pro Exp 03-24 | 6 | 8.30 | 6 | 8.13 |
| Gemma 3 27B | 7 | 8.22 | 7 | 8.05 |
| DeepSeek V3-0324 | 8 | 8.09 | 8 | 7.90 |
| Gemini 2.0 Pro Exp 02-05 | 9 | 8.08 | 9 | 7.87 |
| GPT-4.5 Preview | 10 | 8.07 | 10 | 7.80 |
| GPT-4o Feb 2025 | 13 | 7.96 | 11 | 7.78 |
| Claude 3.5 Haiku | 11 | 8.07 | 12 | 7.75 |
| Gemini 1.5 Pro (Sept) | 12 | 7.97 | 13 | 7.73 |
| GPT-4o 2024-11-20 | 15 | 7.87 | 14 | 7.69 |
| Gemini 2.0 Flash Thinking Exp Old | 14 | 7.87 | 15 | 7.64 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 16 | 7.82 | 16 | 7.54 |
| o1-preview | 17 | 7.74 | 17 | 7.47 |
| Qwen 2.5 Max | 19 | 7.64 | 18 | 7.42 |
| DeepSeek-V3 | 20 | 7.62 | 19 | 7.36 |
| Gemini 2.0 Flash Exp | 18 | 7.65 | 20 | 7.36 |
| o1 | 21 | 7.57 | 21 | 7.29 |
| Gemma 2 27B | 23 | 7.49 | 22 | 7.29 |
| Mistral Large 2 | 22 | 7.54 | 23 | 7.24 |
| Qwen QwQ Preview | 24 | 7.44 | 24 | 7.18 |
| GPT-4o mini | 25 | 7.37 | 25 | 7.09 |
| GPT-4o 2024-08-06 | 26 | 7.36 | 26 | 7.03 |
| o1-mini | 27 | 7.30 | 27 | 6.91 |
| Claude 3 Opus | 28 | 7.17 | 28 | 6.84 |
| Qwen 2.5 72B | 29 | 7.00 | 29 | 6.66 |
| Grok 2 12-12 | 31 | 6.98 | 30 | 6.63 |
| o3-mini-high | 30 | 6.99 | 31 | 6.49 |
| Microsoft Phi-4 | 33 | 6.89 | 32 | 6.49 |
| o3-mini | 32 | 6.90 | 33 | 6.38 |
| Amazon Nova Pro | 34 | 6.70 | 34 | 6.34 |
| Llama 3.1 405B | 35 | 6.60 | 35 | 6.18 |
| Llama 3.3 70B | 36 | 5.95 | 36 | 5.41 |
| Claude 3 Haiku | 37 | 5.83 | 37 | 5.32 |

Normalizing each grader’s scores doesn’t significantly alter the rankings:

### Normalized Mean Leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | DeepSeek R1 | 0.935 |
| 2 | Claude 3.7 Sonnet Thinking 16K | 0.915 |
| 3 | Claude 3.5 Sonnet 2024-10-22 | 0.887 |
| 4 | Claude 3.7 Sonnet | 0.787 |
| 5 | Qwen QwQ-32B 16K | 0.715 |
| 6 | Gemini 2.5 Pro Exp 03-24 | 0.672 |
| 7 | Gemma 3 27B | 0.614 |
| 8 | GPT-4.5 Preview | 0.489 |
| 9 | Claude 3.5 Haiku | 0.485 |
| 10 | Gemini 2.0 Pro Exp 02-05 | 0.471 |
| 11 | DeepSeek V3-0324 | 0.452 |
| 12 | Gemini 1.5 Pro (Sept) | 0.386 |
| 13 | GPT-4o Feb 2025 | 0.348 |
| 14 | Gemini 2.0 Flash Thinking Exp Old | 0.290 |
| 15 | GPT-4o 2024-11-20 | 0.242 |
| 16 | Gemini 2.0 Flash Thinking Exp 01-21 | 0.241 |
| 17 | o1-preview | 0.174 |
| 18 | Gemini 2.0 Flash Exp | 0.097 |
| 19 | DeepSeek-V3 | 0.041 |
| 20 | Qwen 2.5 Max | 0.031 |
| 21 | o1 | -0.003 |
| 22 | Mistral Large 2 | -0.016 |
| 23 | Gemma 2 27B | -0.137 |
| 24 | Qwen QwQ Preview | -0.178 |
| 25 | GPT-4o 2024-08-06 | -0.197 |
| 26 | o1-mini | -0.204 |
| 27 | GPT-4o mini | -0.212 |
| 28 | Claude 3 Opus | -0.392 |
| 29 | o3-mini-high | -0.540 |
| 30 | Grok 2 12-12 | -0.549 |
| 31 | Qwen 2.5 72B | -0.561 |
| 32 | o3-mini | -0.602 |
| 33 | Microsoft Phi-4 | -0.655 |
| 34 | Amazon Nova Pro | -0.883 |
| 35 | Llama 3.1 405B | -0.912 |
| 36 | Llama 3.3 70B | -1.523 |
| 37 | Claude 3 Haiku | -1.706 |


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
- Mar 26, 2025: Gemini 2.5 Pro Exp 03-25, DeepSeek V3-0324, o3-mini-high added.
- Mar 13, 2025: Gemma 3 27B added.
- Mar 10, 2025: Qwen QwQ-32B added.
- Feb 26, 2025: GPT-4.5 Preview added.
- Feb 25, 2025: Claude 3.7 Sonnet, Claude 3.7 Sonnet Thinking, GPT-4o Feb 2025, GPT-4o 2024-11-20, Gemini 2.0 Pro Exp 02-05 added.
- Feb 1, 2025: o3-mini (medium reasoning effort) added.
- Jan 31, 2025: DeepSeek R1, o1, Gemini 2.0 Flash Thinking Exp 01-21, Microsoft Phi-4, Amazon Nova Pro added.
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
