# Opus 5.5 rank uncertainty

This companion analysis uses 2,000 joint resamples of prompt IDs across the comparison graph. Comparisons sharing a prompt and the same evaluator roster share their evaluator resamples. This preserves the matching of the added comparisons. The public chart intervals retain their established 300-draw, within-matchup story/evaluator bootstrap; the two procedures answer different sensitivity questions.

Rank frequencies describe resampling stability for the observed stories and graders. They are not posterior probabilities of true quality. Side-bias estimates, missing stories and evaluator availability are held fixed. The selected opponents and comparison budget were fixed before these new judgments, using earlier results. Sampling seed: 2026092705.

| Model | Current rank | First | Second | Third | Top three |
| --- | ---: | ---: | ---: | ---: | ---: |
| Claude Fable 5.1 high | 1 | 47.8% | 26.4% | 25.9% | 100.0% |
| Claude Opus 5 xhigh | 2 | 26.2% | 44.0% | 29.8% | 100.0% |
| Claude Opus 5.5 high | 3 | 26.1% | 29.6% | 44.2% | 100.0% |
| Claude Opus 5 high | 5 | 0.0% | 0.0% | 0.0% | 0.0% |
| GPT-6 Astra high | 4 | 0.0% | 0.0% | 0.1% | 0.1% |

## Opus 5.5 relative to its closest competitors

| Opponent | Resamples with Opus rated higher | 95% resampled rating-gap interval |
| --- | ---: | --- |
| Claude Fable 5.1 high | 38.2% | -0.213 to 0.158 |
| Claude Opus 5 xhigh | 43.5% | -0.162 to 0.150 |
| Claude Opus 5 high | 100.0% | 0.134 to 0.496 |
| GPT-6 Astra high | 100.0% | 0.144 to 0.483 |

## Evaluator sensitivity

Leaving out one entire evaluator family at a time, including its earlier versions, places Opus 5.5 between ranks 1 and 3. Each fit recomputes presentation-order corrections. These are robustness checks, not alternative official rankings or confidence bounds.

[All rank frequencies](rank_probabilities.csv) · [Rating-gap frequencies](opus_rating_gap_probabilities.csv) · [Family omission results](grader_family_sensitivity.csv) · [Matched anchor observations](matched_anchor_controls.csv)

## Matched weaker-opponent check

The two rival writers were compared against the same four opponents, prompts and evaluators already used for Opus 5.5. Differences below are Opus's margin minus the rival's margin against the same opponent. Only evaluator/story observations available for all three writers enter this check.

| Rival | Matched story pairs | Mean margin difference |
| --- | ---: | ---: |
| Claude Fable 5.1 high | 12 | +0.040 |
| Claude Opus 5 xhigh | 12 | +0.036 |
