# LLM Creative Story-Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

---
![Overall scores](/images/llm_overall_bar_zoomed_with_err.png)

---
## Method Summary
Each of the 41 LLMs produces 500 short stories - each targeted at 400–500 words long - that must organically integrate all assigned random elements. In total, 41 * 500 = 20,500 unique stories are generated.

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

*Note: they will be updated once Grok 3 API is available.*

In total, 41 * 500 * 6 * 16 = 1,968,000 grades are generated.

---
## Results
### Overall LLM Means

**Leaderboard:**
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
| 9 | Grok 3 Beta (No reasoning) | 8.17 |
| 10 | DeepSeek V3-0324 | 8.09 |
| 11 | Gemini 2.0 Pro Exp 02-05 | 8.08 |
| 12 | GPT-4.5 Preview | 8.07 |
| 13 | Claude 3.5 Haiku | 8.07 |
| 14 | Grok 3 Mini Beta (Low) | 7.99 |
| 15 | Gemini 1.5 Pro (Sept) | 7.97 |
| 16 | GPT-4o Feb 2025 | 7.96 |
| 17 | Gemini 2.0 Flash Thinking Exp Old | 7.87 |
| 18 | GPT-4o 2024-11-20 | 7.87 |
| 19 | Gemini 2.0 Flash Thinking Exp 01-21 | 7.82 |
| 20 | o1-preview | 7.74 |
| 21 | Gemini 2.0 Flash Exp | 7.65 |
| 22 | Qwen 2.5 Max | 7.64 |
| 23 | DeepSeek-V3 | 7.62 |
| 24 | o1 | 7.57 |
| 25 | Mistral Large 2 | 7.54 |
| 26 | Gemma 2 27B | 7.49 |
| 27 | Qwen QwQ Preview | 7.44 |
| 28 | GPT-4o mini | 7.37 |
| 29 | GPT-4o 2024-08-06 | 7.36 |
| 30 | o1-mini | 7.30 |
| 31 | Claude 3 Opus | 7.17 |
| 32 | Qwen 2.5 72B | 7.00 |
| 33 | o3-mini-high | 6.99 |
| 34 | Grok 2 12-12 | 6.98 |
| 35 | o3-mini | 6.90 |
| 36 | Microsoft Phi-4 | 6.89 |
| 37 | Amazon Nova Pro | 6.70 |
| 38 | Llama 4 Maverick | 6.67 |
| 39 | Llama 3.1 405B | 6.60 |
| 40 | Llama 3.3 70B | 5.95 |
| 41 | Claude 3 Haiku | 5.83 |

Qwen QwQ-32B joins DeepSeek R1 and Claude Sonnet as the clear overall winners. Notably, Claude 3.5 Haiku shows a large improvement upon Claude 3 Haiku and Gemma 3 shows a large improvement upon Gemma 2. Gemini models perform well, while Llama models lag behind. Interestingly, larger, more expensive models did not outperform smaller models by as much as one might expect. o3-mini performs worse than expected.

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all stories, with Grader LLMs marked in different colors:

![Normalized scores strip chart](/images/normalized_scores_strip.png)

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
| GPT-4o Mar 2025 | 1 | 8.55 | 1 | 8.61 |
| DeepSeek R1 | 2 | 8.54 | 2 | 8.60 |
| Claude 3.7 Sonnet Thinking 16K | 3 | 8.51 | 3 | 8.57 |
| Claude 3.5 Sonnet 2024-10-22 | 4 | 8.47 | 4 | 8.54 |
| Claude 3.7 Sonnet | 5 | 8.39 | 5 | 8.45 |
| Qwen QwQ-32B 16K | 6 | 8.34 | 6 | 8.41 |
| Gemini 2.5 Pro Exp 03-24 | 7 | 8.30 | 7 | 8.36 |
| Gemma 3 27B | 8 | 8.22 | 8 | 8.29 |
| Grok 3 Beta (No reasoning) | 9 | 8.17 | 9 | 8.24 |
| DeepSeek V3-0324 | 10 | 8.09 | 10 | 8.17 |
| Gemini 2.0 Pro Exp 02-05 | 11 | 8.08 | 11 | 8.16 |
| GPT-4.5 Preview | 12 | 8.07 | 12 | 8.16 |
| Claude 3.5 Haiku | 13 | 8.07 | 13 | 8.15 |
| Grok 3 Mini Beta (Low) | 14 | 7.99 | 14 | 8.07 |
| Gemini 1.5 Pro (Sept) | 15 | 7.97 | 15 | 8.06 |
| GPT-4o Feb 2025 | 16 | 7.96 | 16 | 8.05 |
| Gemini 2.0 Flash Thinking Exp Old | 17 | 7.87 | 17 | 7.96 |
| GPT-4o 2024-11-20 | 18 | 7.87 | 18 | 7.95 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 19 | 7.82 | 19 | 7.93 |
| o1-preview | 20 | 7.74 | 20 | 7.85 |
| Gemini 2.0 Flash Exp | 21 | 7.65 | 21 | 7.76 |
| DeepSeek-V3 | 23 | 7.62 | 22 | 7.74 |
| Qwen 2.5 Max | 22 | 7.64 | 23 | 7.74 |
| o1 | 24 | 7.57 | 24 | 7.68 |
| Mistral Large 2 | 25 | 7.54 | 25 | 7.65 |
| Gemma 2 27B | 26 | 7.49 | 26 | 7.60 |
| Qwen QwQ Preview | 27 | 7.44 | 27 | 7.55 |
| GPT-4o 2024-08-06 | 29 | 7.36 | 28 | 7.47 |
| GPT-4o mini | 28 | 7.37 | 29 | 7.46 |
| o1-mini | 30 | 7.30 | 30 | 7.44 |
| Claude 3 Opus | 31 | 7.17 | 31 | 7.30 |
| o3-mini-high | 33 | 6.99 | 32 | 7.12 |
| Grok 2 12-12 | 34 | 6.98 | 33 | 7.12 |
| Qwen 2.5 72B | 32 | 7.00 | 34 | 7.12 |
| o3-mini | 35 | 6.90 | 35 | 7.04 |
| Microsoft Phi-4 | 36 | 6.89 | 36 | 7.02 |
| Amazon Nova Pro | 37 | 6.70 | 37 | 6.84 |
| Llama 4 Maverick | 38 | 6.67 | 38 | 6.80 |
| Llama 3.1 405B | 39 | 6.60 | 39 | 6.72 |
| Llama 3.3 70B | 40 | 5.95 | 40 | 6.08 |
| Claude 3 Haiku | 41 | 5.83 | 41 | 5.97 |


Excluding any one LLM from grading also does not significantly change the rankings. For example, here is what happens when LLama 3.1 405B is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| DeepSeek R1 | 2 | 8.54 | 1 | 8.36 |
| GPT-4o Mar 2025 | 1 | 8.55 | 2 | 8.32 |
| Claude 3.7 Sonnet Thinking 16K | 3 | 8.51 | 3 | 8.29 |
| Claude 3.5 Sonnet 2024-10-22 | 4 | 8.47 | 4 | 8.25 |
| Qwen QwQ-32B 16K | 6 | 8.34 | 5 | 8.17 |
| Claude 3.7 Sonnet | 5 | 8.39 | 6 | 8.17 |
| Gemini 2.5 Pro Exp 03-24 | 7 | 8.30 | 7 | 8.13 |
| Gemma 3 27B | 8 | 8.22 | 8 | 8.05 |
| Grok 3 Beta (No reasoning) | 9 | 8.17 | 9 | 7.95 |
| DeepSeek V3-0324 | 10 | 8.09 | 10 | 7.90 |
| Gemini 2.0 Pro Exp 02-05 | 11 | 8.08 | 11 | 7.87 |
| GPT-4.5 Preview | 12 | 8.07 | 12 | 7.80 |
| GPT-4o Feb 2025 | 16 | 7.96 | 13 | 7.78 |
| Claude 3.5 Haiku | 13 | 8.07 | 14 | 7.75 |
| Gemini 1.5 Pro (Sept) | 15 | 7.97 | 15 | 7.73 |
| Grok 3 Mini Beta (Low) | 14 | 8.00 | 16 | 7.72 |
| GPT-4o 2024-11-20 | 18 | 7.87 | 17 | 7.69 |
| Gemini 2.0 Flash Thinking Exp Old | 17 | 7.87 | 18 | 7.64 |
| Gemini 2.0 Flash Thinking Exp 01-21 | 19 | 7.82 | 19 | 7.54 |
| o1-preview | 20 | 7.74 | 20 | 7.47 |
| Qwen 2.5 Max | 22 | 7.64 | 21 | 7.42 |
| DeepSeek-V3 | 23 | 7.62 | 22 | 7.36 |
| Gemini 2.0 Flash Exp | 21 | 7.65 | 23 | 7.36 |
| o1 | 24 | 7.57 | 24 | 7.29 |
| Gemma 2 27B | 26 | 7.49 | 25 | 7.29 |
| Mistral Large 2 | 25 | 7.54 | 26 | 7.24 |
| Qwen QwQ Preview | 27 | 7.44 | 27 | 7.18 |
| GPT-4o mini | 28 | 7.37 | 28 | 7.09 |
| GPT-4o 2024-08-06 | 29 | 7.36 | 29 | 7.03 |
| o1-mini | 30 | 7.30 | 30 | 6.91 |
| Claude 3 Opus | 31 | 7.17 | 31 | 6.84 |
| Qwen 2.5 72B | 32 | 7.00 | 32 | 6.66 |
| Grok 2 12-12 | 34 | 6.98 | 33 | 6.63 |
| o3-mini-high | 33 | 6.99 | 34 | 6.49 |
| Microsoft Phi-4 | 36 | 6.89 | 35 | 6.49 |
| o3-mini | 35 | 6.90 | 36 | 6.38 |
| Amazon Nova Pro | 37 | 6.70 | 37 | 6.34 |
| Llama 4 Maverick | 38 | 6.67 | 38 | 6.28 |
| Llama 3.1 405B | 39 | 6.60 | 39 | 6.18 |
| Llama 3.3 70B | 40 | 5.95 | 40 | 5.41 |
| Claude 3 Haiku | 41 | 5.83 | 41 | 5.32 |

Normalizing each grader’s scores doesn’t significantly alter the rankings:

### Normalized Mean Leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | GPT-4o Mar 2025 | 0.954 |
| 2 | DeepSeek R1 | 0.908 |
| 3 | Claude 3.7 Sonnet Thinking 16K | 0.888 |
| 4 | Claude 3.5 Sonnet 2024-10-22 | 0.860 |
| 5 | Claude 3.7 Sonnet | 0.761 |
| 6 | Qwen QwQ-32B 16K | 0.689 |
| 7 | Gemini 2.5 Pro Exp 03-24 | 0.645 |
| 8 | Gemma 3 27B | 0.587 |
| 9 | Grok 3 Beta (No reasoning) | 0.540 |
| 10 | GPT-4.5 Preview | 0.462 |
| 11 | Claude 3.5 Haiku | 0.458 |
| 12 | Gemini 2.0 Pro Exp 02-05 | 0.444 |
| 13 | DeepSeek V3-0324 | 0.425 |
| 14 | Grok 3 Mini Beta (Low) | 0.392 |
| 15 | Gemini 1.5 Pro (Sept) | 0.359 |
| 16 | GPT-4o Feb 2025 | 0.321 |
| 17 | Gemini 2.0 Flash Thinking Exp Old | 0.263 |
| 18 | GPT-4o 2024-11-20 | 0.216 |
| 19 | Gemini 2.0 Flash Thinking Exp 01-21 | 0.214 |
| 20 | o1-preview | 0.147 |
| 21 | Gemini 2.0 Flash Exp | 0.070 |
| 22 | DeepSeek-V3 | 0.014 |
| 23 | Qwen 2.5 Max | 0.005 |
| 24 | o1 | -0.030 |
| 25 | Mistral Large 2 | -0.043 |
| 26 | Gemma 2 27B | -0.163 |
| 27 | Qwen QwQ Preview | -0.205 |
| 28 | GPT-4o 2024-08-06 | -0.225 |
| 29 | o1-mini | -0.232 |
| 30 | GPT-4o mini | -0.239 |
| 31 | Claude 3 Opus | -0.418 |
| 32 | o3-mini-high | -0.567 |
| 33 | Grok 2 12-12 | -0.576 |
| 34 | Qwen 2.5 72B | -0.588 |
| 35 | o3-mini | -0.629 |
| 36 | Microsoft Phi-4 | -0.683 |
| 37 | Llama 4 Maverick | -0.885 |
| 38 | Amazon Nova Pro | -0.909 |
| 39 | Llama 3.1 405B | -0.938 |
| 40 | Llama 3.3 70B | -1.549 |
| 41 | Claude 3 Haiku | -1.732 |



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
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
