# LLM Creative Story‑Writing Benchmark V3

This benchmark evaluates how well large language models (LLMs) follow a creative brief while still producing engaging fiction. Every story must meaningfully incorporate ten **required elements**: character, object, concept, attribute, action, method, setting, timeframe, motivation, and tone. With these building blocks standardized and length tightly controlled, differences in **constraint satisfaction** and **literary quality** become directly comparable. Multiple independent “grader” LLMs score each story on an 18‑question rubric, and we aggregate those judgments into model‑level results.

---

![Overall scores](images/llm_overall_bar_zoomed_with_err.png)

---

## What’s measured

### 1) Craft and coherence (Q1–Q8)

Eight questions focus on narrative craft: character depth and motivation, plot structure and coherence, world building and atmosphere, story impact, originality, thematic cohesion, voice/point‑of‑view, and line‑level prose quality.

### 2) Element integration (Q9A–Q9J)

Ten questions check whether the story **organically** uses each required element: the specified character, object, core concept, attribute, action, method, setting, timeframe, motivation, and tone. If a category in the prompt is “None,” graders mark the corresponding 9‑series item as N/A.

### 3) Overall story score

We score each story per grader with a **60/40 weighted power mean (Hölder mean, p = 0.5)** over the 18 rubric items (Q1–Q8 = 60%, 9A–9J = 40%, split evenly within each group). Compared with a plain average, p = 0.5 acts like a soft‑minimum: it sits closer to the lowest dimensions, so weaknesses pull more than highs can offset and well‑rounded craft is rewarded. The final story score is the mean of the per‑grader scores.

---

## Results

### Overall model means

The top bar chart summarizes **mean story quality** for each model with uncertainty bands. (Grader‑unweighted means; questions weighted 60/40.)

#### Full overall leaderboard

| Rank | LLM                    | Mean Score | Samples | SEM |
|-----:|------------------------|-----------:|--------:|----:|
| 1 | Kimi K2-0905 | 8.729 | 2800 | 0.0115 |
| 2 | GPT-5 (medium reasoning) | 8.723 | 2800 | 0.0100 |
| 3 | Qwen 3 Max Preview | 8.711 | 2800 | 0.0108 |
| 4 | Kimi K2 | 8.693 | 2800 | 0.0101 |
| 5 | Mistral Medium 3.1 | 8.629 | 2800 | 0.0110 |
| 6 | o3-pro (medium reasoning) | 8.628 | 2800 | 0.0103 |
| 7 | Gemini 2.5 Pro | 8.602 | 2800 | 0.0100 |
| 8 | Claude Opus 4.1 (no reasoning) | 8.538 | 2800 | 0.0110 |
| 9 | DeepSeek V3.1 Reasoner | 8.517 | 2800 | 0.0099 |
| 10 | DeepSeek V3.1 Non-Think | 8.507 | 2800 | 0.0100 |
| 11 | Qwen 3 235B A22B 25-07 Think | 8.495 | 2800 | 0.0115 |
| 12 | Grok 4 Fast Reasoning | 8.114 | 2800 | 0.0141 |
| 13 | Baidu Ernie 4.5 300B A47B | 8.110 | 2800 | 0.0130 |
| 14 | Grok 4 | 8.068 | 2800 | 0.0137 |
| 15 | GLM-4.5 | 7.803 | 2800 | 0.0175 |
| 16 | GPT-OSS-120B | 7.726 | 2800 | 0.0177 |
| 17 | Cohere Command A | 7.459 | 2800 | 0.0172 |
| 18 | Llama 4 Maverick | 6.370 | 2800 | 0.0226 |

#### Full normalized leaderboard

| Rank | LLM                    | Normalized Mean |
|-----:|------------------------|-----------------:|
| 1 | Kimi K2-0905 | 0.675 |
| 2 | Qwen 3 Max Preview | 0.639 |
| 3 | GPT-5 (medium reasoning) | 0.626 |
| 4 | Kimi K2 | 0.605 |
| 5 | Mistral Medium 3.1 | 0.512 |
| 6 | o3-pro (medium reasoning) | 0.505 |
| 7 | Gemini 2.5 Pro | 0.463 |
| 8 | Claude Opus 4.1 (no reasoning) | 0.385 |
| 9 | DeepSeek V3.1 Reasoner | 0.356 |
| 10 | Qwen 3 235B A22B 25-07 Think | 0.342 |
| 11 | DeepSeek V3.1 Non-Think | 0.342 |
| 12 | Grok 4 Fast Reasoning | -0.202 |
| 13 | Baidu Ernie 4.5 300B A47B | -0.214 |
| 14 | Grok 4 | -0.234 |
| 15 | GLM-4.5 | -0.571 |
| 16 | GPT-OSS-120B | -0.654 |
| 17 | Cohere Command A | -1.063 |
| 18 | Llama 4 Maverick | -2.514 |

#### Element integration only (9A–9J)

A valid concern is whether LLM graders can accurately score questions 1 to 8 (Major Story Aspects), such as Character Development & Motivation. However, questions 9A to 9J (Element Integration) are clearly easier for graders to evaluate reliably. We observe high correlation between the per‑(grader, LLM) means for craft (Q1–Q8) and element‑fit (9A–9J), and a strong overall correlation aggregated across all files. While we cannot be certain these ratings are correct without human validation, their consistency suggests that something real is being measured. For an element‑only view, you can ignore Q1–Q8 and use only 9A–9J:

![Element integration (9A–9J)](images/llm_overall_bar_zoomed_9Ato9J.png)

Normalized view (per‑grader z‑scores):

![Element integration — normalized (9A–9J)](images/normalized_llm_overall_bar_zoomed_9Ato9J.png)

#### Craft only (Q1–Q8)

![Craft (Q1–Q8)](images/llm_overall_bar_zoomed_1to8.png)

Normalized view (per‑grader z‑scores):

![Craft — normalized (Q1–Q8)](images/normalized_llm_overall_bar_zoomed_1to8.png)

---

### LLM vs. Question (Detailed)

The detailed heatmap shows each model’s **mean score on each rubric question**. It is a fast way to spot models that excel at **voice and prose** but trail on **plot** or **element integration**, or vice versa.

![LLM per question](images/llm_vs_question_detailed.png)

---

### Which model “wins” the most prompts?

For every prompt, we rank models by their cross‑grader story score and tally the **number of #1 finishes**. This captures consistency at the very top rather than just the average.

![#1 stories pie chart](images/llm_best_pie.png)

---

### Grader ↔ LLM interactions

We publish two complementary views:

* **Mean heatmap (Grader × LLM).** Useful for seeing whether any model is especially favored or disfavored by a particular grader.

![Grader vs LLM](images/grader_vs_llm_means.png)

* **Normalized heatmap.** Z‑scores each grader’s scale so only **relative** preferences remain.

![Grader vs LLM normalized](images/grader_vs_llm_normalized_means.png)

Additional view: grader–grader correlation (how graders align with each other).

![Grader correlation](images/teacher_grader_correlation.png)

---

## Method Summary 

**Stories and length.** Each model contributes short stories that must land in a **strict 600–800 word range**. We verify counts, flag outliers, and generate compliance charts before any grading. 

**Grading.** Each story is scored independently by **seven grader LLMs** using the 18‑question rubric above. 

**Aggregation.** For every story: compute the power mean (Hölder mean) with p = 0.5 across the 18 questions with a 60/40 per‑question weighting (Q1–Q8 vs. 9A–9J), then average across graders. For every model: average across its stories. We also compute **per‑question** means so readers can see where a model is strong (e.g., prose) or weak (e.g., plot or tone fit).

### Grading LLMs

The following grader models scored stories:

- Claude Opus 4.1 (no reasoning)
- DeepSeek V3.1 Reasoner
- Gemini 2.5 Pro
- GPT-5 (low reasoning)
- Grok 4
- Kimi K2
- Qwen 3 235B A22B 25-07 Think

 
---

## How the ten required elements are chosen

We use a two‑stage LLM‑assisted pipeline that starts from large curated pools and converges on one coherent set per prompt:

 - The ten categories are defined in the elements catalog (character, object, core concept, attribute, action, method, setting, timeframe, motivation, tone).
- Seed prompts with candidates: For each seed index, we randomly sample ten options per category (plus the literal option “None”) from those pools and write a selection prompt.
- Proposer selection: Multiple proposer LLMs each pick exactly one element per category, allowing “None” in at most one category when that improves coherence. Each proposer returns a complete 10‑line set.
- Rate for fit: We deduplicate sets per seed and have several independent rater LLMs score how well each set “hangs together” (1–10). Scores are z‑normalized per rater to remove leniency differences and then averaged.
- Choose the winner: For each seed we take the top normalized‑mean set (ties are broken consistently). That set becomes the “required elements” block for the final story prompt.

Notes
- Within a prompt, categories never repeat; one category may be “None,” which means that element is not required for that prompt.
- There is no separate cross‑prompt coverage optimizer. Variety comes from the breadth of the curated pools and independent per‑seed sampling plus LLM selection and rating. As a result, duplicates across different prompts are possible but uncommon.

---

## Scoring scale 

- **Scale:** 0.0–10.0 per question, in 0.1 increments (e.g., 7.3).
- **Story score:** Power mean (Hölder mean) with p = 0.5 across the 18 questions with 60/40 per‑question weights (Q1–Q8 vs. 9A–9J), then averaged across graders.
- **Model score:** average of its story scores. Uncertainty bands reflect variation across prompts and sample size.

Coverage: each story is evaluated by seven independent LLM graders. Each prompt specifies one choice in each of ten categories; at most one category may be “None” (not required), keeping brief‑following comparable across models. If a category is “None,” graders mark that 9‑series sub‑question as N/A. N/As are excluded from aggregation and the per‑question weights are re‑normalized over the remaining questions.

Graders used (7): Claude Opus 4.1 (no reasoning), DeepSeek V3.1 Reasoner, Gemini 2.5 Pro, GPT‑5 (low reasoning), Grok 4, Kimi K2, Qwen 3 235B A22B 25‑07 Think.

---

## Robustness checks

- Exclude bottom 10% per LLM: Rankings and means change only marginally; top models retain their order. We drop the lowest‑scoring decile of stories per model, recompute means, and compare ranks. 
- Leave‑one‑grader‑out: Recomputing means while excluding each grader in turn yields the same top tier; movements are within noise for most models. See per‑grader views and aggregates in the summary tables.
- Grader‑weighted vs unweighted: Weighting graders by reliability barely shifts ordering; deltas are recorded in the summary tables. Sample:

  | LLM | Mean (unweighted) | Mean (weighted) | Δ |
  |-----|-------------------:|----------------:|---:|
  | Kimi K2‑0905 | 8.695 | 8.798 | +0.103 |
  | GPT‑5 (medium reasoning) | 8.668 | 8.766 | +0.098 |
  | Qwen 3 Max Preview | 8.655 | 8.756 | +0.101 |
  | Kimi K2 | 8.635 | 8.728 | +0.093 |
  | Mistral Medium 3.1 | 8.569 | 8.674 | +0.105 |



---

### Bottom 10% per‑LLM exclusion (top 15)

| LLM | Old Rank | Old Mean | New Rank | New Mean | ΔRank |
|-----|---------:|---------:|---------:|---------:|------:|
| Kimi K2‑0905 | 1 | 8.726 | 1 | 8.782 | 0 |
| GPT‑5 (medium reasoning) | 2 | 8.685 | 2 | 8.723 | 0 |
| Qwen 3 Max Preview | 3 | 8.684 | 3 | 8.722 | 0 |
| Kimi K2 | 4 | 8.667 | 4 | 8.705 | 0 |
| o3‑pro (medium reasoning) | 5 | 8.596 | 5 | 8.636 | 0 |
| Mistral Medium 3.1 | 6 | 8.589 | 6 | 8.627 | 0 |
| Gemini 2.5 Pro | 7 | 8.569 | 7 | 8.607 | 0 |
| Claude Opus 4.1 (no reasoning) | 8 | 8.511 | 8 | 8.556 | 0 |
| Qwen 3 235B A22B 25‑07 Think | 9 | 8.487 | 9 | 8.542 | 0 |
| DeepSeek V3.1 Reasoner | 10 | 8.486 | 10 | 8.528 | 0 |
| DeepSeek V3.1 Non‑Think | 11 | 8.474 | 11 | 8.520 | 0 |
| Grok 4 | 12 | 8.086 | 12 | 8.155 | 0 |
| Baidu Ernie 4.5 300B A47B | 13 | 8.082 | 13 | 8.147 | 0 |
| GLM‑4.5 | 14 | 7.804 | 14 | 7.890 | 0 |
| GPT‑OSS‑120B | 15 | 7.727 | 15 | 7.809 | 0 |

### Leave‑one‑grader‑out re‑rank (max change, top 15)

| LLM | Old Rank | Old Mean | Worst ΔRank | New Rank (worst) | New Mean (worst) | Removed grader |
|-----|---------:|---------:|------------:|------------------:|-----------------:|----------------|
| GPT‑5 (medium reasoning) | 2 | 8.685 | 2 | 4 | 8.586 | Gemini 2.5 Pro |
| Qwen 3 235B A22B 25‑07 Think | 9 | 8.487 | 2 | 11 | 8.511 | GPT‑5 (low reasoning) |
| o3‑pro (medium reasoning) | 5 | 8.596 | 2 | 7 | 8.607 | GPT‑5 (low reasoning) |
| Grok 4 | 12 | 8.086 | 1 | 13 | 7.958 | DeepSeek V3.1 Reasoner |
| Baidu Ernie 4.5 300B A47B | 13 | 8.082 | -1 | 12 | 7.969 | DeepSeek V3.1 Reasoner |
| DeepSeek V3.1 Non‑Think | 11 | 8.474 | -1 | 10 | 8.514 | GPT‑5 (low reasoning) |
| DeepSeek V3.1 Reasoner | 10 | 8.487 | -1 | 9 | 8.400 | DeepSeek V3.1 Reasoner |
| Gemini 2.5 Pro | 7 | 8.569 | -1 | 6 | 8.611 | GPT‑5 (low reasoning) |
| Kimi K2 | 4 | 8.667 | -1 | 3 | 8.595 | Gemini 2.5 Pro |
| Claude Opus 4.1 (no reasoning) | 8 | 8.511 | 0 | 8 | 8.659 | Claude Opus 4.1 (no reasoning) |
| Cohere Command A | 16 | 7.427 | 0 | 16 | 7.634 | Claude Opus 4.1 (no reasoning) |
| GLM‑4.5 | 14 | 7.804 | 0 | 14 | 8.030 | Claude Opus 4.1 (no reasoning) |
| GPT‑OSS‑120B | 15 | 7.727 | 0 | 15 | 7.952 | Claude Opus 4.1 (no reasoning) |
| Kimi K2‑0905 | 1 | 8.726 | 0 | 1 | 8.902 | Claude Opus 4.1 (no reasoning) |
| Llama 4 Maverick | 17 | 6.345 | 0 | 17 | 6.585 | Claude Opus 4.1 (no reasoning) |


## Do Graders Agree?

We measure agreement three ways, then visualize the results with fixed, symmetric color ranges so “cool vs. warm” maps cleanly to lower vs. higher agreement:

1. **Story‑level overall.** Pairwise Pearson r (95% CI), Spearman ρ, and Lin’s concordance capture how similarly graders rank complete stories.
2. **Question‑level.** For each rubric question, we correlate graders across the shared set of stories and summarize agreement for craft questions (Q1–Q8) and element‑fit questions (9A–9J).
3. **Within‑story profile shape.** For each story we center each grader’s 18‑dimensional score vector (removing severity differences) and correlate the **shape** of judgments (“do graders like the same strengths and notice the same weaknesses?”).

Outputs include heatmaps and concise tables (e.g., “most disagreed‑upon stories,” coverage gaps). In practice, graders show **solid, repeatable alignment** on both story‑level and question‑level judgments, and profile‑shape agreement helps reveal where differences come from (e.g., one grader reacting more to tone than plot).

**Figures:**
![Story agreement heatmap](images/grader_story_corr_heatmap.png)
![Q1–Q8 agreement](images/grader_q_corr_heatmap_Q1to8.png)
![9A–9J agreement](images/grader_q_corr_heatmap_9Ato9J.png)
![Profile‑shape agreement](images/grader_profile_shape_corr_heatmap.png)

---

## Best and Worst Stories

We highlight **standout individual stories** (highest cross‑grader means) and a short list of **lowest‑rated** pieces, with direct links and the ten **required elements** under each entry. This lets you compare top work side‑by‑side with weak outcomes and see how the elements were interpreted. Refusals to incorporate a required element remain visible here and typically land near the bottom.

- Data: The dataset includes story‑level winners/laggards with links and grader‑range diagnostics.
- Comments: Per‑question grader comments are collated under `comments_by_llm_1to8/`.
- Summaries: per‑story and per‑LLM summaries live under `summaries/` and `general_summaries/`.

### Examples (Top 3 / Bottom 3)

Top 3 individual stories (all graders):

* **Story**: [story_wc_63.txt](stories_wc/kimi-k2-0905/story_wc_63.txt) by Kimi K2‑0905
  - Overall Mean (All Graders): 9.13
  - Grader Score Range: 8.23 (lowest: Claude Opus 4.1 (no reasoning)) .. 9.82 (highest: Gemini 2.5 Pro)
  - Required Elements:
    - Character: precise local clock tower winder
    - Object: clock tower pendulum bob
    - Core Concept: incremental absolution
    - Attribute: ethically diligent
    - Action: emerge
    - Method: through tiny inscriptions carved along a broken rake handle
    - Setting: tidal obsidian ridge
    - Timeframe: during the pause in a pendulum's swing
    - Motivation: to restore shared balance
    - Tone: searing reverie

* **Story**: [story_wc_346.txt](stories_wc/kimi-k2-0905/story_wc_346.txt) by Kimi K2‑0905
  - Overall Mean (All Graders): 9.13
  - Grader Score Range: 8.09 (lowest: Claude Opus 4.1 (no reasoning)) .. 9.71 (highest: Gemini 2.5 Pro)
  - Required Elements:
    - Character: doomsday clock adjuster
    - Object: broken puppet head
    - Core Concept: a pane of hush
    - Attribute: beautifully flawed
    - Action: vouchsafe
    - Method: through nested patterns
    - Setting: hidden lighthouse at dusk
    - Timeframe: across the hush of time’s final ripple
    - Motivation: to whisper a lullaby across a thousand lifetimes
    - Tone: bruised awe

* **Story**: [story_wc_79.txt](stories_wc/kimi-k2-0905/story_wc_79.txt) by Kimi K2‑0905
  - Overall Mean (All Graders): 9.13
  - Grader Score Range: 8.39 (lowest: Claude Opus 4.1 (no reasoning)) .. 9.63 (highest: Gemini 2.5 Pro)
  - Required Elements:
    - Character: spiral-shell cartographer
    - Object: reed whistle
    - Core Concept: lost expedition
    - Attribute: quietly driven
    - Action: crack
    - Method: through pattern languages
    - Setting: city built on the shells of gargantuan turtles
    - Timeframe: after the gate rusts shut
    - Motivation: to question the silent watchers on the horizon
    - Tone: sunwashed dread

Bottom 3 individual stories (all graders):

* **Story**: [story_wc_323.txt](stories_wc/llama4-maverick/story_wc_323.txt) by Llama 4 Maverick
  - Overall Mean (All Graders): 4.73
  - Grader Score Range: 2.70 (lowest: Qwen 3 235B A22B 25‑07 Think) .. 7.41 (highest: DeepSeek V3.1 Reasoner)
  - Required Elements:
    - Character: navigation instructor
    - Object: boat anchor chain link
    - Core Concept: unfolded horizons
    - Attribute: balancedly curious
    - Action: expand
    - Method: edge geometry
    - Setting: benthic city
    - Timeframe: after discovering aliens
    - Motivation: to learn to navigate by starlight
    - Tone: somber marvel

* **Story**: [story_wc_305.txt](stories_wc/llama4-maverick/story_wc_305.txt) by Llama 4 Maverick
  - Overall Mean (All Graders): 4.91
  - Grader Score Range: 3.47 (lowest: Claude Opus 4.1 (no reasoning)) .. 7.66 (highest: DeepSeek V3.1 Reasoner)
  - Required Elements:
    - Character: committed caretaker
    - Object: antique hairpin
    - Core Concept: the cycle of rebirth
    - Attribute: kindly decisive
    - Action: scallop
    - Method: climbing trees to think better
    - Setting: umbral grotto above the clouds
    - Timeframe: after forgiving the unforgivable
    - Motivation: to find the source of contentment
    - Tone: vineyard hush

* **Story**: [story_wc_240.txt](stories_wc/llama4-maverick/story_wc_240.txt) by Llama 4 Maverick
  - Overall Mean (All Graders): 4.96
  - Grader Score Range: 4.08 (lowest: Kimi K2) .. 6.82 (highest: DeepSeek V3.1 Reasoner)
  - Required Elements:
    - Character: intrusion detection specialist
    - Object: laser pointer button
    - Core Concept: familiar strangers
    - Attribute: spatially gifted
    - Action: revolutionize
    - Method: through permeable barriers
    - Setting: bioluminescent mushroom farm
    - Timeframe: before the echo of morning birdsong
    - Motivation: to understand the physics of letting go
    - Tone: quiet wildfire

---

## Head‑to‑Head Comparisons

We include A‑vs‑B analyses for stories written to the same required elements, separating rubric‑aligned differences (Q1–Q8 craft; 9A–9J element fit) from beyond‑rubric observations (e.g., risk appetite, cultural specificity).

Head‑to‑head summaries are provided in `inter_llm_comparison_summaries/` (where available).

---

## Example writer summaries

Short excerpts from model‑level writer summaries (see `general_summaries/` for full text):

### GPT‑5 (medium reasoning)

1) Executive profile

Across Q1–Q8, this writer‑LLM is most reliable in Track A: single POV, accumulative/textural builds, 1–2 on‑page characters, and an interior drive‑lens that remains coherent through closure. Its dominant strength is embodied, character‑bound storytelling...

Signature moves (sample):
- Embodied motivation in scene: micro‑choices that visibly trade values.
- Micro‑setting as constraint—objects steer tactics and charge closure images.
- Pattern‑teaching with motif repricing at closure.

### Kimi K2

1) Executive profile

Kimi K2’s dominant strengths span embodied interiority, tight voice control, and accumulative patterning that guides readers toward earned, on‑page closure...

Signature moves (sample):
- Embodied perception as engine; sensory specifics anchor motive and choice.
- Objects as micro‑settings; voice‑world mesh with pressure‑responsive rhythm.
- Final images reweight a taught motif rather than state a thesis.

## Word count and length effects

Length is part of the test design. Tight control limits “padding” advantages and keeps attention on **writing quality** and **element integration**.

* **Compliance dashboard.** We show a per‑model strip plot of story lengths, an overall histogram, and per‑model averages with **95% confidence intervals**, plus lists of outliers (too short/long). Use these to check that models aren’t gaining from padding or being penalized for minor over‑runs.
* **Correlation checks.** We also examine whether length correlates with score overall and by grader.

![Word count distribution by model](images/word_count_distribution_by_model.png)
![Length vs score (overall)](images/len_vs_score_overall_enhanced.png)
![Length vs score (by grader)](images/len_vs_score_grader_enhanced.png)
 

---

## Normalized (z‑scored) perspective

Because graders use slightly different scales, we also show a **normalized view** where each grader’s scores are z‑scored before aggregation. This helps confirm that top models remain strong even after “leniency” differences are removed. The normalized **Grader × LLM** heatmap on this page uses that approach.

### Normalized distributions

![Normalized scores strip chart](images/normalized_scores_strip_zoomed.png)

### Normalized leaderboard

![Normalized leaderboard](images/normalized_leaderboard.png)

---

## Ablation: Q1–Q8 vs 9A–9J

Correlation between craft (Q1–Q8) and element fit (9A–9J) is high across graders and models.

- Overall correlation: 0.836 (N = 47,600) — from `data/question_range_correlation.csv` (overall row).
- Per‑grader × model correlations are included in the correlation report.
- Complementary element‑only view: ![9A–9J](images/llm_overall_bar_zoomed_9Ato9J.png)

---


## What’s new in V3

* **Required elements pipeline:** moved from fewer, randomly selected elements (no "None" allowed) to a curated, ten‑category catalog with large, diverse pools and an LLM proposer→rater selection process; at most one category may be explicitly set to **None** when that improves coherence.
* **Rubric expansion:** grew from 7 craft items to an **18‑question rubric** (8 craft + 10 element‑fit), with clearer, more granular definitions; Q7 and Q8 now separate voice/POV from prose quality.
* **Story length:** increased from 400–500 words to a strict **600–800** window with upfront enforcement and compliance dashboards. Enforcement is applied at prompt level and in pre‑grading extraction, with compliance dashboards and optional cleanup tools; it is not a hard inclusion gate during aggregation unless you apply the cleanup step.
* **Aggregation change:** replaced simple averages with a **power mean (Hölder mean, p = 0.5)** and 60/40 weighting (Q1–Q8 vs. 9A–9J) to reward balanced performance and penalize weak dimensions more.
* **Grader refresh:** upgraded the grader set—previously: GPT‑4o Mar 2025, Claude 3.7 Sonnet, Llama 4 Maverick, DeepSeek V3‑0324, Grok 3 Beta (no reasoning), Gemini 2.5 Pro Exp, Qwen 3 235B; now: Claude Opus 4.1 (no reasoning), DeepSeek V3.1 Reasoner, Gemini 2.5 Pro, GPT‑5 (low reasoning), Grok 4, Kimi K2, Qwen 3 235B A22B 25‑07 Think.
* **Model set additions:** added Kimi K2‑0905, Qwen 3 Max Preview, Mistral Medium 3.1, Claude Opus 4.1 (no reasoning), DeepSeek V3.1 Reasoner, and DeepSeek V3.1 Non‑Think to the evaluated models.
* **New analyses:** added head‑to‑head A‑vs‑B comparisons, model‑level style summaries, and intra‑model style diversity analysis (previously none).
* **Agreement views:** expanded beyond only grader‑grader correlations to include Grader×LLM mean and normalized matrices, story‑level disagreement tables, and leave‑one‑grader‑out robustness checks.
* **Optional grader weighting:** available for users who prefer grader‑reliability‑weighted summaries.

---

## Limitations

* This quality benchmark grades stories **individually**. Collection‑level style diversity is analyzed separately in the companion study “Mapping LLM Style and Range in Flash Fiction.” See the link below for within‑model range results.
* LLM graders are consistent, but they remain automated judges. We publish multiple views (overall means, question breakdowns, #1 finishes, agreement checks) to keep interpretations grounded.
* Hard length limits test precise compliance, which is useful here, but they are not a claim about ideal length for fiction.

---
## Details
Full range of scores:

![Full range](images/llm_overall_bar_start0_with_err.png)

---


## Related work

If you want a deeper look at **style and diversity** (stylometry, cluster maps, and within‑model diversity scored as a collection), see the companion study: **[https://github.com/lechmazur/writing\_styles](https://github.com/lechmazur/writing_styles)**.

---

## Archive (Previous Version)

For the prior edition’s full leaderboard and the list of “old” grader LLMs, see: [v2/README.md](v2/README.md).


## Other multi-agent benchmarks
- [PACT - Benchmarking LLM negotiation skill in multi-round buyer-seller bargaining](https://github.com/lechmazur/pact)
- [BAZAAR - Evaluating LLMs in Economic Decision-Making within a Competitive Simulated Market](https://github.com/lechmazur/bazaar)
- [Public Goods Game (PGG) Benchmark: Contribute & Punish](https://github.com/lechmazur/pgg_bench/)
- [Elimination Game: Social Reasoning and Deception in Multi-Agent LLMs](https://github.com/lechmazur/elimination_game/)
- [Step Race: Collaboration vs. Misdirection Under Pressure](https://github.com/lechmazur/step_game/)

## Other benchmarks
- [LLM Round‑Trip Translation Benchmark](https://github.com/lechmazur/translation/)
- [Extended NYT Connections](https://github.com/lechmazur/nyt-connections/)
- [LLM Thematic Generalization Benchmark](https://github.com/lechmazur/generalization/)
- [LLM Confabulation/Hallucination Benchmark](https://github.com/lechmazur/confabulations/)
- [LLM Deceptiveness and Gullibility](https://github.com/lechmazur/deception/)
- [LLM Divergent Thinking Creativity Benchmark](https://github.com/lechmazur/divergent/)
---


## Updates 
- Sep 23, 2025: Grok 4 Fast Reasoning added.
- Sep 9, 2025: Major new version of the benchmark: V3. See the section "What’s new in V3"

- Follow [@lechmazur](https://x.com/LechMazur) on X for other upcoming benchmarks and more.
