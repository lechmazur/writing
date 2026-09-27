# Aligned v4 ratings

[All 56 fitted writers](ratings.csv) · [Known-answer validation](validation_coverage.csv)

The main chart/table show selected current models; this CSV preserves every fitted writer. Ranks order rating midpoints and do not establish a definitive order where uncertainty overlaps. The generation_coverage_note column records known completion caveats for every affected writer, including historical writers not shown in the main chart.

The ranges are conservative pointwise 95% bounds conditional on the fixed finite story population, grader assignments and potential responses, observed pilot and sampling allocation. They cover random sample selection and every allowed completion of missing judgments. They do not cover fresh-generation uncertainty or provide simultaneous rank intervals.

The method applies bounded-variable Hoeffding/Bernstein bounds to independent sampling strata, using known full-frame influence limits and the unsampled complement near a census. The smaller bound is chosen using the frozen design, independently of new judgments. The sampling-without-replacement reduction is described by [Bardenet and Maillard (2015)](https://arxiv.org/pdf/1309.4029). Missing-response bounds are added separately.

Validation used five known-answer synthetic populations and 5,000 production-design samples each. The conservative bounds covered every simulated target. Normal/Student intervals failed rare-case stress tests; those diagnostic intervals are not used in the current chart. Simulation results check the implementation, not real-world accuracy on unseen judgments.

Story coverage markers: ※ MiMo V2.6 Pro 375/400; ¶ Qwen 3.8 Max 398/400; ^ Qwen3.8-27B 389/400. Their quality estimates concern completed stories. Earlier historical data releases remain separate.
