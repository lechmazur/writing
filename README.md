# LLM Creative Story Writing Benchmark

This benchmark tests how well large language models (LLMs) incorporate a set of 10 mandatory story elements (characters, objects, core concepts, attributes, motivations, etc.) in a short narrative. This is particularly relevant for creative LLM use cases. Because every story has the same required building blocks and similar length, their resulting cohesiveness and creativity become directly comparable across models. The benchmark captures both constraint satisfaction (did the LLM incorporate all elements properly?) and literary quality (how engaging or coherent is the final piece?). By applying a multi-question grading rubric and multiple "grader" LLMs, we can pinpoint differences in how well each model integrates the assigned elements, develops characters, maintains atmosphere, and sustains an overall coherent plot. It measures more than fluency or style: it probes whether each model can adapt to rigid requirements, remain original, and produce a cohesive story that meaningfully uses every single assigned element.

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
4. Deepseek-V3
5. Grok 2 12-12
6. Gemini 1.5 Pro (Sept)

In total, 20 * 500 * 6 * 16 = 960,000 grades are generated.

## Results
### Overall LLM Means
Chart:

Leaderboard:

Claude 3.5 Sonnet emerges as the clear overall winner. Notably, Claude 3.5 Haiku shows a large over Claude 3 Haiku, achieving a strong performance. Gemini models perform well, while Llama models lag behind. Interestingly, larger, more expensive models did not outperform smaller models by as much as one might expect.

### Overall Strip Plot of Questions
A strip plot illustrating distributions of scores (y-axis) by LLM (x-axis) across all questions:

The plot reveals that Llama 3.1 405B occasionally, and Deepseek-v3 sporadically, award a perfect 10 across the board, despite prompts explicitly asking them to be strict graders.

### LLM vs. Question (Detailed)
A heatmap showing each LLM's mean rating per question:

Claude 3.5 Sonnet ranks #1 on every single question!

### LLM #1 Finishes
Which LLM ranked #1 the most times across all stories? This pie chart shows the distribution of #1 finishes:

Claude 3.5 Sonnet’s dominance is undeniable when analyzing the best scores by story.

### Grader-LLM Mean Heatmap
A heatmap of Grader (row) vs. LLM (column) average scores:

The chart highlights that grading LLMs do not disproportionately overrate their own stories. Claude 3.5 Sonnet achieves the top score for nearly all grading LLMs, except when graded by Llama 3.1 405B, where it comes a very close second to Claude 3.5 Haiku.

### Grader-Grader Correlation
A correlation matrix (−1 to 1 scale) measuring how strongly multiple LLMs correlate when cross-grading the same stories:

Llama 3.1 405B's grades show the least correlation with other LLMs, though the correlation remains relatively high, with a minimum of 0.66.

## Story Length
A basic prompt asking LLMs to create a 400-500 word story resulted in an unacceptable range of story lengths. A revised prompt instructing each LLM to track the number of words after each sentence improved consistency somewhat but still fell short of the accuracy needed for fair grading. These stories are available in [stories_first/](stories_first/). For example, Claude 3.5 Haiku consistently produced stories that were significantly too short:

Since the benchmark aims to evaluate how well LLMs write, not how well they count or follow prompts about the format, we adjusted the word counts in the prompt for different LLMs to approximately match the target story length - an approach similar to what someone dissatisfied with the initial story length might adopt. Qwen QwQ and Llama 3.x models required the most extensive prompt engineering to achieve the required word counts and to adhere to the proper output format across all 500 stories. Note that this did not require any evaluation of the story's content itself. These final stories were then graded and they are available in [stories_wc/](stories_wc/).

## Best and worst stories
Here, we list the top 3 and the bottom 3 stories out of the 10,000 generated, based on the average scores from our grader LLMs, and include the required elements for each. Feel free to evaluate their quality for yourself!

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
This reveals which story concepts or sets of required elements consistently excelled or faltered, regardless of the LLM that authored them

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




### Ablation

Excluding 10% worst stories per LLM does not siginificantly change the rankings:

Excluding any one LLM from grading does not siginificantly change the rankings:




## Updates and Other Benchmarks
- Also check out the [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/), [NYT Connections Benchmark](https://github.com/lechmazur/nyt-connections/), [LLM Deception Benchmark](https://github.com/lechmazur/deception) and [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent).
- Follow [@lechmazur](https://x.com/LechMazur) on X (Twitter) for other upcoming benchmarks and more.
