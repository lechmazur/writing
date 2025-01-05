# LLM Creative Story Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. A wide variety of required random elements ensures that LLMs must create diverse stories and cannot resort to repetition. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

![llm_overall_bar_zoomed](https://github.com/user-attachments/assets/7e2a36c5-1eb5-4671-95e2-ed9bc0fae45a)

## Method Summary
Each of the 20 LLMs produces 500 short stories - each targetted at 400–500 words long - that must organically integrate all assigned random elements. In total, 20 * 500 = 10,000 unique stories are generated.

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

In total, 20 * 500 * 6 * 16 = 960,000 grades are generated.

## Results
### Overall LLM Means

**Leaderboard:**
| Rank | LLM Full          | Mean  |
|-----:|-------------------|------:|
| 1 | Claude 3.5 Sonnet 2024-10-22 | 8.47 |
| 2 | Claude 3.5 Haiku | 8.07 |
| 3 | Gemini 1.5 Flash | 7.99 |
| 4 | Gemini 1.5 Pro (Sept) | 7.97 |
| 5 | Gemini 2.0 Flash Thinking Exp | 7.87 |
| 6 | o1-preview | 7.74 |
| 7 | Gemini 2.0 Flash Exp | 7.65 |
| 8 | DeepSeek-V3 | 7.62 |
| 9 | Mistral Large 2 | 7.54 |
| 10 | Gemma 2 27B | 7.49 |
| 11 | Qwen QwQ | 7.44 |
| 12 | GPT-4o mini | 7.37 |
| 13 | GPT-4o | 7.36 |
| 14 | o1-mini | 7.30 |
| 15 | Claude 3 Opus | 7.17 |
| 16 | Qwen 2.5 72B | 7.00 |
| 17 | Grok 2 12-12 | 6.98 |
| 18 | Llama 3.1 405B | 6.60 |
| 19 | Llama 3.3 70B | 5.95 |
| 20 | Claude 3 Haiku | 5.83 |

Claude 3.5 Sonnet emerges as the clear overall winner. Notably, Claude 3.5 Haiku shows a very large improvement over Claude 3 Haiku. Gemini models perform well, while Llama models lag behind. Interestingly, larger, more expensive models did not outperform smaller models by as much as one might expect.

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all questions, with Grader LLMs marked in different colors:

![questions_overall_strip](https://github.com/user-attachments/assets/bca4eefb-a25f-4178-9d5f-046150cfba76)

The plot reveals that Llama 3.1 405B occasionally, and DeepSeek-V3 sporadically, award a perfect 10 across the board, despite prompts explicitly asking them to be strict graders.

### LLM vs. Question (Detailed)
A heatmap showing each LLM's mean rating per question:

![llm_vs_question_detailed](https://github.com/user-attachments/assets/6686b012-d935-49a7-bc23-cce49e3adb54)

Claude 3.5 Sonnet ranks #1 on every single question!

### LLM #1 Finishes
Which LLM ranked #1 the most times across all stories? This pie chart shows the distribution of #1 finishes:

![llm_best_pie](https://github.com/user-attachments/assets/a9c37814-4cd9-4169-adf9-b7ec3355b0c3)

Claude 3.5 Sonnet's dominance is undeniable when analyzing the best scores by story.

### Grader-LLM Mean Heatmap
A heatmap of Grader (row) vs. LLM (column) average scores:

![grader_vs_llm_means](https://github.com/user-attachments/assets/0292c777-4d9d-45be-b4ec-f8e8e2025c8d)

The chart highlights that grading LLMs do not disproportionately overrate their own stories. Claude 3.5 Sonnet achieves the top score for nearly all grading LLMs, except when graded by Llama 3.1 405B, where it comes a very close second to Claude 3.5 Haiku.

### Grader-Grader Correlation
A correlation matrix (−1 to 1 scale) measuring how strongly multiple LLMs correlate when cross-grading the same stories:

![teacher_grader_correlation](https://github.com/user-attachments/assets/e3bbaf7b-0909-4e1c-9221-e5c7187c4374)

Llama 3.1 405B's grades show the least correlation with other LLMs, though the correlation remains relatively high, with a minimum of 0.66.

## Story Length
A basic prompt asking LLMs to create a 400-500 word story resulted in an unacceptable range of story lengths. A revised prompt instructing each LLM to track the number of words after each sentence improved consistency somewhat but still fell short of the accuracy needed for fair grading. These stories are available in [stories_first/](stories_first/). For example, Claude 3.5 Haiku consistently produced stories that were significantly too short:

![count-before](https://github.com/user-attachments/assets/b2a2f691-478a-49c0-a6c2-409b9342ac94)

Since the benchmark aims to evaluate how well LLMs write, not how well they count or follow prompts about the format, we adjusted the word counts in the prompt for different LLMs to approximately match the target story length - an approach similar to what someone dissatisfied with the initial story length might adopt. Qwen QwQ and Llama 3.x models required the most extensive prompt engineering to achieve the required word counts and to adhere to the proper output format across all 500 stories. Note that this did not require any evaluation of the story's content itself. These final stories were then graded and they are available in [stories_wc/](stories_wc/).

![count-after](https://github.com/user-attachments/assets/39b47c19-da29-4036-bb54-cccfc46ec704)

This chart shows the correlations between each LLM's scores and their story lengths:

![len_vs_score_overall_enhanced](https://github.com/user-attachments/assets/6c41dcaa-9e78-4c6c-b793-d20a50010f1c)

This chart shows the correlations between each Grader LLM's scores and the lengths of stories they graded:

![len_vs_score_grader_enhanced](https://github.com/user-attachments/assets/019b90d9-ed03-4edb-ae6d-f980c7ea1671)

## Best and Worst Stories
Here, we list the top 3 and the bottom 3 individual stories (written by any LLM) out of the 10,000 generated, based on the average scores from our grader LLMs, and include the required elements for each. Feel free to evaluate their quality for yourself!

### Top 3 Individual Stories (All Graders)

* **Story**: [story_400.txt](stories_wc/sonnet-20241022/story_400.txt) by Claude 3.5 Sonnet 2024-10-22
  - Overall Mean (All Graders): 9.18
  - Grader Score Range: 7.81 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: DeepSeek-V3)
  - Required Elements:
    - Character: guarded druid
    - Object: dull safety pin
    - Core Concept: breaking the silence
    - Attribute: fiercely ambivalent
    - Action: gather
    - Method: a special family meal prepared only on birthdays
    - Setting: glacial orchard suspended over a crevasse of blue ice
    - Timeframe: after the last human sets foot on earth
    - Motivation: to overcome a crippling fear
    - Tone: dour amusement

* **Story**: [story_489.txt](stories_wc/sonnet-20241022/story_489.txt) by Claude 3.5 Sonnet 2024-10-22
  - Overall Mean (All Graders): 9.17
  - Grader Score Range: 7.81 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: unseen observer
    - Object: basic plastic whistle
    - Core Concept: the undercurrent of wisdom
    - Attribute: aggressively kind
    - Action: fling
    - Method: by the call of a whale from the deep
    - Setting: haunted lighthouse watch room
    - Timeframe: at the instant a dancer’s foot first touches the stage
    - Motivation: to rescue ancient traditions
    - Tone: brazen calm

* **Story**: [story_169.txt](stories_wc/gemini_20_flash_thinking_exp/story_169.txt) by Gemini 2.0 Flash Thinking Exp
  - Overall Mean (All Graders): 9.14
  - Grader Score Range: 8.00 (lowest: Gemini 1.5 Pro (Sept)) .. 10.00 (highest: DeepSeek-V3)
  - Required Elements:
    - Character: soul-broker real estate agent
    - Object: dusty wine bottle
    - Core Concept: the art of persuasion
    - Attribute: weirdly static
    - Action: choreograph
    - Method: by reading reversed labels on dusty glass bottles
    - Setting: floating tea platform
    - Timeframe: throughout recycling
    - Motivation: to learn forgotten songs
    - Tone: grandiose modesty

### Bottom 3 Individual Stories (All Graders)

* **Story**: [story_385.txt](stories_wc/claude_mini/story_385.txt) by Claude 3 Haiku
  - Overall Mean (All Graders): 3.77
  - Grader Score Range: 1.31 (lowest: Grok 2 12-12) .. 6.12 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: pleasant meddler
    - Object: pair of rusted ice skates
    - Core Concept: scattered seeds
    - Attribute: openly manipulative
    - Action: weaken
    - Method: via the receding footprints of a nighttime beach wanderer
    - Setting: obsidian skyscraper
    - Timeframe: during the quiet shift before sunrise in a hospital ward
    - Motivation: to decode ancient symbols
    - Tone: lucid confusion

* **Story**: [story_450.txt](stories_wc/llama33_70b/story_450.txt) by Llama 3.3 70B
  - Overall Mean (All Graders): 3.86
  - Grader Score Range: 1.50 (lowest: Grok 2 12-12) .. 6.31 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: sharp-witted dancer
    - Object: patch from a crashed spaceship mission
    - Core Concept: the weight of denial
    - Attribute: linguistically inept
    - Action: mimic
    - Method: a family tradition of taking a yearly family photo
    - Setting: thought experiment chamber
    - Timeframe: during bubble baths
    - Motivation: to fulfill a final prophecy with a twist
    - Tone: saturated ambivalence

* **Story**: [story_4.txt](stories_wc/claude_mini/story_4.txt) by Claude 3 Haiku
  - Overall Mean (All Graders): 3.86
  - Grader Score Range: 1.56 (lowest: Grok 2 12-12) .. 6.25 (highest: Llama 3.1 405B)
  - Required Elements:
    - Character: dj who channels ancient gods
    - Object: vintage pencil case
    - Core Concept: the flickering vision
    - Attribute: traditionally playful
    - Action: exalt
    - Method: through the route traced by an unraveling sweater thread
    - Setting: alchemical orchard greenhouse shrouded in endless night
    - Timeframe: during filing
    - Motivation: to map sacred spaces
    - Tone: borrowed starlight


## Easiest and Hardest Combinations of Elements
This reveals which story concepts or sets of required elements consistently excelled or faltered, regardless of the LLM that authored them.

### Top 3 Highest-Rated Element Combinations

* **Story File**: story_355.txt
  - Overall Mean (All LLMs): 8.21
  - LLM Score Range: 7.40 (lowest: Qwen 2.5 72B) .. 8.81 (highest: Claude 3.5 Sonnet 2024-10-22)
  - Required Elements:
    - Character: aloof dancer
    - Object: cracked compass
    - Core Concept: letters home
    - Attribute: harshly compassionate
    - Action: ease
    - Method: by mapping scattered dreams
    - Setting: psychedelic art installation
    - Timeframe: after the last balloon deflates in an empty hall
    - Motivation: to free unspoken truths
    - Tone: forgotten revelry

* **Story File**: story_351.txt
  - Overall Mean (All LLMs): 8.19
  - LLM Score Range: 7.25 (lowest: Claude 3 Haiku) .. 8.71 (highest: Gemini 1.5 Flash)
  - Required Elements:
    - Character: dreamy poet
    - Object: brass sundial
    - Core Concept: a delicate undoing
    - Attribute: formally rebellious
    - Action: compel
    - Method: via cryptic shapes in the wax seal of an unopened letter
    - Setting: disused railway station overgrown with ivy
    - Timeframe: after the last riddle is solved
    - Motivation: to stand by the unremembered
    - Tone: quietly intense

* **Story File**: story_15.txt
  - Overall Mean (All LLMs): 8.13
  - LLM Score Range: 7.35 (lowest: Llama 3.3 70B) .. 9.06 (highest: Claude 3.5 Sonnet 2024-10-22)
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


## Bottom 3 Lowest-Rated Element Combinations

* **Story File**: story_451.txt
  - Overall Mean (All LLMs): 6.35
  - LLM Score Range: 4.21 (lowest: Llama 3.3 70B) .. 8.40 (highest: Claude 3.5 Sonnet 2024-10-22)
  - Required Elements:
    - Character: separated twin hiring actors to find identity
    - Object: baseball signed by a time traveler
    - Core Concept: forbidden knowledge
    - Attribute: typically unique
    - Action: subdue
    - Method: a clandestine meeting in a hidden location
    - Setting: mysterious mountain peak
    - Timeframe: amid farmers market bustle
    - Motivation: to outlive an apocalyptic prophecy
    - Tone: crystal shadows

* **Story File**: story_385.txt
  - Overall Mean (All LLMs): 6.44
  - LLM Score Range: 3.77 (lowest: Claude 3 Haiku) .. 8.25 (highest: Claude 3.5 Sonnet 2024-10-22)
  - Required Elements:
    - Character: pleasant meddler
    - Object: pair of rusted ice skates
    - Core Concept: scattered seeds
    - Attribute: openly manipulative
    - Action: weaken
    - Method: via the receding footprints of a nighttime beach wanderer
    - Setting: obsidian skyscraper
    - Timeframe: during the quiet shift before sunrise in a hospital ward
    - Motivation: to decode ancient symbols
    - Tone: lucid confusion

* **Story File**: story_484.txt
  - Overall Mean (All LLMs): 6.49
  - LLM Score Range: 4.06 (lowest: Claude 3 Haiku) .. 7.83 (highest: Claude 3.5 Sonnet 2024-10-22)
  - Required Elements:
    - Character: groggy brewer
    - Object: piece of a broken mirror
    - Core Concept: the encroaching darkness
    - Attribute: uniquely generic
    - Action: initiate
    - Method: via the slightest discoloration on a dusty spiral staircase
    - Setting: haunted mansion graveyard
    - Timeframe: during the lull in a protest when voices gather again
    - Motivation: to become a living embodiment of one's values
    - Tone: flippant solemnity


## Ablation

Excluding 10% worst stories per LLM does not significantly change the rankings:
### Rankings After Excluding the 50 Lowest-Rated Stories per LLM

| LLM      | Old Rank | Old Mean | New Rank | New Mean |
|----------|---------:|---------:|---------:|---------:|
| Claude 3.5 Sonnet 2024-10-22 | 1 | 8.47 | 1 | 8.54 |
| Claude 3.5 Haiku | 2 | 8.07 | 2 | 8.15 |
| Gemini 1.5 Flash | 3 | 7.99 | 3 | 8.09 |
| Gemini 1.5 Pro (Sept) | 4 | 7.97 | 4 | 8.06 |
| Gemini 2.0 Flash Thinking Exp | 5 | 7.87 | 5 | 7.96 |
| o1-preview | 6 | 7.74 | 6 | 7.85 |
| Gemini 2.0 Flash Exp | 7 | 7.65 | 7 | 7.76 |
| DeepSeek-V3 | 8 | 7.62 | 8 | 7.74 |
| Mistral Large 2 | 9 | 7.54 | 9 | 7.65 |
| Gemma 2 27B | 10 | 7.49 | 10 | 7.60 |
| Qwen QwQ | 11 | 7.44 | 11 | 7.55 |
| GPT-4o | 13 | 7.36 | 12 | 7.47 |
| GPT-4o mini | 12 | 7.37 | 13 | 7.46 |
| o1-mini | 14 | 7.30 | 14 | 7.44 |
| Claude 3 Opus | 15 | 7.17 | 15 | 7.30 |
| Grok 2 12-12 | 17 | 6.98 | 16 | 7.12 |
| Qwen 2.5 72B | 16 | 7.00 | 17 | 7.12 |
| Llama 3.1 405B | 18 | 6.60 | 18 | 6.72 |
| Llama 3.3 70B | 19 | 5.95 | 19 | 6.08 |
| Claude 3 Haiku | 20 | 5.83 | 20 | 5.97 |


Excluding any one LLM from grading also does not siginificantly change the rankings. For example, here is what happens when LLama 3.1 405B is excluded:
### Ranking after Excluding LLama 3.1 405B from Grading

| LLM                | Old Rank | Old Mean | New Rank | New Mean |
|--------------------|---------:|---------:|---------:|---------:|
| Claude 3.5 Sonnet 2024-10-22 | 1 | 8.47 | 1 | 8.25 |
| Claude 3.5 Haiku | 2 | 8.07 | 2 | 7.75 |
| Gemini 1.5 Flash | 3 | 7.99 | 3 | 7.73 |
| Gemini 1.5 Pro (Sept) | 4 | 7.97 | 4 | 7.73 |
| Gemini 2.0 Flash Thinking Exp | 5 | 7.87 | 5 | 7.64 |
| o1-preview | 6 | 7.74 | 6 | 7.47 |
| DeepSeek-V3 | 8 | 7.62 | 7 | 7.36 |
| Gemini 2.0 Flash Exp | 7 | 7.65 | 8 | 7.36 |
| Gemma 2 27B | 10 | 7.49 | 9 | 7.29 |
| Mistral Large 2 | 9 | 7.54 | 10 | 7.24 |
| Qwen QwQ | 11 | 7.44 | 11 | 7.18 |
| GPT-4o mini | 12 | 7.37 | 12 | 7.09 |
| GPT-4o | 13 | 7.36 | 13 | 7.03 |
| o1-mini | 14 | 7.30 | 14 | 6.91 |
| Claude 3 Opus | 15 | 7.17 | 15 | 6.84 |
| Qwen 2.5 72B | 16 | 7.00 | 16 | 6.66 |
| Grok 2 12-12 | 17 | 6.98 | 17 | 6.63 |
| Llama 3.1 405B | 18 | 6.60 | 18 | 6.18 |
| Llama 3.3 70B | 19 | 5.95 | 19 | 5.41 |
| Claude 3 Haiku | 20 | 5.83 | 20 | 5.32 |



## Details
Strip plots divided between questions 1-6 and questions 7A-7J:

![questions_1to6_strip](https://github.com/user-attachments/assets/4e860b4c-4a13-43ad-b357-54095c491efc)

![questions_7A_J_strip](https://github.com/user-attachments/assets/3e6aff05-0d27-4c5f-ab31-19fc518f88d8)

Full range of scores:

![llm_overall_bar_start0](https://github.com/user-attachments/assets/74003aa9-1d20-469b-b5e1-2ffce93c446f)


## Updates and Other Benchmarks
- Also check out the [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/), [NYT Connections Benchmark](https://github.com/lechmazur/nyt-connections/), [LLM Deception Benchmark](https://github.com/lechmazur/deception) and [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent).
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
