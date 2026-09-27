# Aligned v4 ratings with the 50-prompt Opus comparison

[All 56 fitted writers](ratings.csv) · [Known-answer validation](validation_coverage.csv)

The main chart/table show selected current models; this CSV preserves every fitted writer. Ranks order rating midpoints and do not establish a definitive order where uncertainty overlaps. The generation_coverage_note column records known completion caveats for every affected writer, including historical writers not shown in the main chart.

The ranges are conservative pointwise 95% bounds conditional on the fixed finite story population, grader assignments and potential responses, observed pilot and sampling allocation. They cover random sample selection and every allowed completion of missing judgments. They do not cover fresh-generation uncertainty or provide simultaneous rank intervals.

The method applies bounded-variable Hoeffding/Bernstein bounds to independent sampling strata, using known full-frame influence limits and the unsampled complement near a census. The smaller bound is chosen using the frozen design, independently of new judgments. The sampling-without-replacement reduction is described by [Bardenet and Maillard (2015)](https://arxiv.org/pdf/1309.4029). Missing-response bounds are added separately.

Validation used five known-answer synthetic populations and 5,000 production-design samples each. The conservative bounds covered every simulated target. Normal/Student intervals failed rare-case stress tests; those diagnostic intervals are not used in the current chart. Simulation results check the implementation, not real-world accuracy on unseen judgments.

Story coverage markers: ※ MiMo V2.6 Pro 375/400; ¶ Qwen 3.8 Max 398/400; ^ Qwen3.8-27B 389/400. Their quality estimates concern completed stories. Earlier historical data releases remain separate.

This update adds 180 judgments on 30 uniformly selected unused Opus 5.5 high versus Opus 5 high prompts. The original 20 prompts remain included once, yielding 298/300 usable judgments across 50/400 shared prompts. The sample size was fixed before the added judgments. The matchup's sample-sized graph weight increases from 20 to 50; other allocations are unchanged. The full joint fit and bounded uncertainty were recalculated, with 5,000 validation draws in each of the five original scenarios.

[Changes from the previous ranking](rank_changes.csv) · [Previous aligned v4 snapshot](../writing_v4_aligned/README.md)
