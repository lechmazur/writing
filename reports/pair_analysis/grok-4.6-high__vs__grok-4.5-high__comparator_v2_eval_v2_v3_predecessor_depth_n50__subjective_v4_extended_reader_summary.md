# Grok 4.6 (high) vs. grok-4.5-high: comparative writing analysis

Focus model: `grok-4.6-high`. Comparison model: `grok-4.5-high`. Direct-comparison scope: `comparator_v2_eval_v2_v3_predecessor_depth_n50`.

## In one paragraph

When Grok 4.5 and Grok 4.6 are given the same short-fiction briefs, the difference is less what they invent than what they do with the required ingredients. Grok 4.5 tends to keep those ingredients visible as quoted phrases — method, motive, and tone restated until the narration doubles as proof of compliance — and its endings often step outside the fiction to certify that every element was successfully integrated [C012]. Grok 4.6 more often dissolves the same requirements into working machinery: a projector lens actually projects, a storm gets overdubbed into music, a mandated doubt survives the climax as part of the solution [C038]. Its victories stay partial and proportionate, leaving the larger problem alive instead of cured [C039]. The result reads like the difference between a story reporting that it worked and one still in motion. That preference is highly consistent, but not absolute: in a handful of stories Grok 4.5 is the one that tracks consequences past the climax, as when a communal cure leaves permanent bodily residue in the caregiver rather than lifting on cue [C004].

## Quantitative context

Across 50 matched prompts, the focus model recorded 42 wins, 2 ties, and 6 losses at the ±0.5 tie threshold. Its mean signed margin was +1.993 ± 0.524 (95% normal half-width).

Mean lengths were 692.2 and 737.3 words; the correlation between length difference and margin was +0.048.

Focus: **Grok 4.6** (grok-4.6-high). Comparison: **Grok 4.5** (grok-4.5-high). Evidence base: 14 blinded packet readings by three analysts (gpt-5.6-high, kimi-k3, claude-opus-5-xhigh), an 87-claim verified ledger, evaluator notes, and quantitative context over 50 matched pairs.

## Comparative portrait

Both models run the same constrained-element machine. Both insert required phrases nearly verbatim, both favor a solitary specialist who applies a prescribed method to a prescribed object and receives a revelation, and both resolve benignly with little humor, dialogue, or formal experiment [C075][C080][C084]. The recurring difference is what happens to a required element after it first appears. Grok 4.6 more often metabolizes it into a mechanism, a practice, a cost, or a constraint on the ending; Grok 4.5 more often preserves it as an item to be re-quoted, functionally deployed, and finally certified complete. This split is panel-supported: it appears independently in reads by gpt-5.6-high [C006][C064], kimi-k3 [C008][C025][C084], and claude-opus-5-xhigh [C013][C046][C058], and is a difference of density and consequence, not of kind, since Grok 4.6 also leaks checklist language [C042][C075].

Endings are the most diagnostic site. Grok 4.5 tends to close with total resolution plus a self-auditing summary addressed to whoever is checking the list; Grok 4.6 tends to close on bounded, proportionate outcomes that leave the problem class alive [C012][C015][C033][C058][C082][C083]. A related economy governs objects and miracles: Grok 4.6 spends the marvel and prices the transformation, while Grok 4.5 pockets the souvenir and upgrades the temporary to the permanent [C014][C039][C059]. Both writers share real limitations: frictionless worlds in which the landscape applauds, technocratic uplift without dissent, machines that pronounce absolution, pre-solved symbolism, and declared rather than developed motives [C005][C019][C024][C056][C080].

**Cohort replication.** The portrait replicates in the extension cohort and strengthens. Quantitatively, the original cohort (20 pairs) ran 15/0/5 with mean margin +1.473; the extension cohort (30 pairs) ran 27/2/1 with mean margin +2.339 and a tighter CI. Material changes: comparison wins collapsed from five to one, and the margin widened rather than regressing. The word-count gap simultaneously narrowed (−59.9 → −35.4), and the word-count/margin correlation is +0.048, so the advantage is not a brevity artifact. Qualitatively, every core pattern recurs across all 14 packets with no sign of cohort confinement.

## Does either model seem smarter?

Treating "seems smarter" strictly as a reader impression produced by writing choices, yes — Grok 4.6 creates the stronger and more consistent impression, and the basis is decomposable rather than a generalized halo.

- **Causal and structural foresight.** Grok 4.6 supplies intermediate operations, feedback, and verification between intention and success; devices have differentiated parts; decodings are cross-checked and yield downstream action [C020][C038][C047][C052][C076][C079][C086]. Caveat: some of its mechanisms are decorative technobabble or plausibility theater [C021][C079].
- **Psychological inference.** Grok 4.6 selects compromising emotional particulars and lets assigned traits constrain the plot to the final page, where Grok 4.5's traits are typically cured at the moment of success [C040][C065][C085]. This is a narrow edge: both writers' interiority is thin, with motives declared rather than developed [C080].
- **Conceptual compression.** Grok 4.6 finds hinges that fuse arbitrary elements — a timeframe becoming the theme, a backwards prophecy organizing cosmology, doubt becoming part of the procedure [C029][C076][C021]. Grok 4.5's conceptual intelligence is aphoristic and intermittent: real theses about grief and myth, stated flat and undramatized [C016][C068]. The cleanest proxy separation in the corpus is the mathematics-of-mercy prompt, where Grok 4.5's calculus decoration collapses under inspection while Grok 4.6's plainer reframe actually resolves the story's setup [C041].
- **Relevant-detail selection.** Grok 4.6's details carry evidentiary weight — legible stratigraphy, specified contents and locations of revelations, motivations weighted by cost and history [C001][C026][C032][C072].
- **Constraint synthesis.** Required language is rebuilt into functioning sentences and world-rules, including repairing incoherent briefs by invention [C006][C042][C060][C064].
- **Restraint.** Grok 4.6's hedged futures and threshold endings concede what the story cannot claim [C007][C015][C083] — with the standing caveat, preserved as a minority reading, that this restraint sometimes verges on evasion or underdevelopment [C007][C034].
- **Reader trust.** Grok 4.6 withholds glosses and lets earlier sentences change meaning retroactively; Grok 4.5 states what objects represent and grades its own compliance [C026][C028][C043][C046][C058].

Not verbosity or polish: Grok 4.6 is on average the *shorter* writer (692 vs. 737 words). Grammar polish does contribute to the control impression, and several claims flag that sensitivity [C008][C073], but the load-bearing observations — object fates, repetition counts, ending scale, specified evidence — are checkable independent of polish [C014][C018][C041]. **Cohort check:** the impression replicates; the six comparison wins map almost exactly onto the ledger's flagged reversals, and five of the six occurred in the original cohort, while the extension cohort preserved every core pattern and narrowed Grok 4.5's wins to one.

## Narrative reasoning and aesthetic judgment

The ending handling is where the two models' narrative reasoning diverges most sharply. Grok 4.6 treats an assigned tone as a constraint on the outcome — stellar doubt survives as a necessary harmonic, melancholy persists inside success, a merged timeline preserves its paradox as a permanent operating condition [C044][C077][C087][C002]. Grok 4.5 applies tone as adjectival color and then cancels it at the close, dispelling doubt forever and converting friction into harmony [C044]. Grok 4.6's resolutions also tend to perform the theme as an action and occasionally regenerate the problem they solved, modeling how contested knowledge actually behaves, while Grok 4.5's resolutions terminate in unanimous conversion and summary connectives [C045][C071][C082].

On objects: Grok 4.6 more often lets a thing act according to what it is — a projector lens projects, a coin's mass does clamp work, a mapping rule between silence and music is specified — while Grok 4.5 more often grants objects arbitrary powers and then states their meanings [C031][C057]. This is a tendency, not a trait: the ledger's own counterexample-bearing claim shows the pattern reversing cleanly between stories [C018]. Character attributes divide the same way — engines that persist versus defects the plot cures [C040][C085]. Information management differs: Grok 4.6 withholds so that opening sentences are reweighted later, absorbs premises into figurative language, and uses the supernatural as rehearsal for a still-required act; Grok 4.5 front-loads, states the rule and then breaks it, and uses magic to perform the act for the protagonist [C043][C049][C048]. Figuration shows a functional split rather than a quality gap: Grok 4.6's best similes explain concepts from the story's own inventory; Grok 4.5's best define temperament from a character's trade [C037][C061].

Aesthetic risks run both directions and are preserved: Grok 4.6's restraint can curdle into aphoristic shorthand or imported melodrama, and its open endings risk hardening into formula [C003][C028][C034]; Grok 4.5's liturgical repetition is defensible as fable or parable register, a minority reading noted by multiple analysts, though the repeated strings coincide exactly with required-element phrasing, which undercuts the design reading [C087][C009]. **Cohort check:** all of these patterns recur across packets spanning the full story range; nothing in the extension cohort confined or reversed them.

## Range, recurring habits, and floor versus ceiling

Grok 4.6 has the steadier floor — one analyst found its five pieces nearly interchangeable in competence — but its variance is real and bimodal: it lapses into full checklist mode, offstage discovery, and padded editorial recaps in particular stories [C036][C018][C070][C075]. Grok 4.5 shows the wider spread: packet-best structures and packet-worst control coexist, from a genuinely moving closed loop of obligation to run-on prose and grammar breaks precisely at constraint-insertion points [C036][C008][C042][C073].

Both models' habits are partly prompt-dependent. Grok 4.5 relaxes into concrete, varied scene-building when the tone slot is empty, suggesting tone-imitation consumes its craft budget; ritual-structured prompts suit its litany mode [C030][C009]. Grok 4.6's advantage is partly register-dependent: when it drops into a flat, short-sentence mode, its causal staging and selective detail drop with it — a genuine surface-cue-sensitive finding [C018][C034]. Shared range limits are substantial: no humor, no sustained dialogue, no formal experiment, recycled character names in both, and a shared solitary epistemology in which truth is discovered through static, ripples, and letters rather than tested against another person's resistance [C080][C062]. One stable axis is better read as a difference in the shape of desire than in skill: Grok 4.6 empties the frame to one figure alone with an object; Grok 4.5 populates and diffuses endings into communities and institutions [C035][C062].

**Cohort check and material change:** the floor-versus-ceiling framing survives only partially. Per-packet, Grok 4.5 did produce both peaks and troughs [C036], and its ceiling is genuine. But the extension cohort (27/2/1) shows those ceiling wins were concentrated early; across 30 fresh pairs Grok 4.5 won once. The aggregate picture is lopsided — 42/2/6 with median margin +2.467 exceeding the mean +1.993, indicating a consistent advantage with a small tail of comparison wins — so the evidence does not support a compensating "higher ceiling" narrative overall, only a real but situational one.

## What each model still does better

Grok 4.6's persisting edges: epistemic restraint that keeps the marvelous doubtful and doubt functional [C087][C077]; specified evidence instead of announced resolution [C001][C032]; motifs that return as actions rather than explanations [C055]; constraint circuitry in which several assigned elements share one mechanism [C076][C079]; resolutions that regenerate successor problems [C045]; and timeframes literalized into structure [C007][C029][C066].

Grok 4.5's persisting edges are genuine, recurring as a minority pattern, and should not be flattened: social and civic architecture — compassion enacted as a participatory protocol, epiphanies that seek institutions, obligations that close loops on stage [C022][C036][C062][C078]; reflexive moral reasoning in one standout story, where the investigator incriminates his own surveillance as the price of transparency (one-story observation) [C017]; superior consequence aftercare in one story, where a cure leaves permanent bodily residue (one-story observation) [C004]; the corpus's boldest single conceits, risked at the edge of incoherence — a self-planted message loop, a taboo turned instrument, a marionette grammar for possibility [C011][C045][C081]; under-credited systems imagination when unconstrained by tone (prompt-dependent) [C030]; and occasional aphoristic theses stranger than anything Grok 4.6 attempts [C016][C068]. These strengths are situational rather than general: they produced five wins in the original cohort and only one in the extension.

## Findings beyond the existing judging

The blinded packet analyses surfaced diagnostics that ordinary pairwise judging is built to miss; these are new relative to the evaluator notes, though all are corroborated in the ledger:

- **The evaluator as hidden addressee.** Grok 4.5 repeatedly ends by auditing its own compliance — "all elements wove together seamlessly," "communed successfully" — a tell of constraint-anxiety Grok 4.6 rarely exhibits and rubrics reward rather than catch [C012][C046][C058][C082].
- **Two grammars of scaffolding leak.** Grok 4.5 leaks as narrator-bookkeeping ("the action unfolded"); Grok 4.6 leaks as ontology (converting an empty timeframe field into timelessness). Grok 4.5 also imports prompt phrases with their original tense fossilized inside past-tense narration — a specific, checkable tell [C013][C046][C084].
- **A fidelity tradeoff axis.** The writers split which requirement they will violate: Grok 4.6 sacrifices the staged action to keep the timeframe; Grok 4.5 abandons the timeframe to stage the payoff. Rubrics have no vocabulary for ranking that trade [C007][C029].
- **Object afterlives.** Grok 4.6 tends to leave objects unread, stored, or spent; Grok 4.5 tends to decode or deplete them — a quiet figure for ongoing versus finished worlds [C014][C031][C057].
- **Terminal social shape.** Stewardship-at-a-distance versus absorption into community, stable per writer and better read as desire than skill (low confidence) [C035][C062].
- **Figurative division of labor.** Explanatory versus characterological analogy; both writers also share one figurative reservoir, reaching independently for the same stock images, which narrows freshness claims to degree [C037][C061].
- **Convergences that discipline the gap.** Both writers break syntax at identical insertion coordinates, both resolve guilt through absolution-delivering machines, and both rebuild civilizations without political resistance — symmetric failures that halo-effect readings of Grok 4.6 must absorb [C075][C024][C005].

Quantitatively, two beyond-judging observations: the six comparison wins correspond almost one-to-one with the ledger's minority findings (0035→[C004]; 0128→[C022][C036]; 0195→[C081]; 0210→[C030]; 0216→[C011]; 0236→[C018]), meaning the critics' reversals were independently confirmed by scoring; and mean evaluator disagreement (0.632) plus AB/BA order sensitivity (~0.998) are modest relative to the median margin (+2.467), so the ranking is not an artifact of judge noise or presentation order.

## Disagreements and limitations

Preserved minority readings, held at the confidence the analysts assigned: Grok 4.6's restraint may be evasion of hard-to-write scenes or anticlimax rather than discipline [C007][C034]; Grok 4.5's repetition may be intentional liturgy or fable convention, though its exact match to required phrasing weakens the design reading (speculative) [C087][C009]; the bootstrap-paradox story is suspended between most-original and least-coherent [C011]; the interior-goods fork is a genuine poetics difference, not a quality difference [C034]; and the ceiling/floor split means best-work-based and average-based decisions could diverge [C036].

Surface-cue-sensitive findings: grammar polish contributes to the control impression [C008][C073]; naming can masquerade as characterization depth [C010]; stasis reads as sophistication by default [C007]; technical vocabulary functions as an intelligence proxy in both writers — including Grok 4.6's decorative mathematics and both models' content-free "fairness equations" [C052][C069]; and melancholy may be reflexively coded as deeper [C044]. Findings resting on one story are labeled as such above and include [C004][C017][C030][C081]; social-intelligence claims are the least stable in the corpus, with positions reversing across prompts [C050]. One trait-level claim in the ledger failed generalization outright: object integration flips between stories and cannot be attributed to either writer as a stable property [C018]. Untested or shared-limited domains: political resistance, humor, dialogue-heavy scenes, formal experiment, and genuinely contested social interaction [C005][C019][C080]. A final epistemic caveat, raised within the evidence itself: if evaluation rewards detectable element presence, Grok 4.5's recitation is rational optimization, and the judgment against it depends on valuing integration over detectability [C084]. **Cohort check:** none of these disagreements resolved in the extension cohort; the material change is that comparison wins nearly vanished there, which strengthens the central ranking while leaving the minority strengths documented mostly by earlier stories.

## Representative case studies

- **0068 (margin +4.217).** The most multi-claim corroborated pair: Grok 4.6 keeps evidence partial and gives competing narratives social bearers with interests, while Grok 4.5 announces a precise compromise history it never earns; the same pair shows glossed symbolism versus a single accusatory simile, and an ending that opens a practice versus one that certifies [C001][C025][C026][C027][C028].
- **0310 (+4.333).** The tone-as-construct case: doubt absorbed as a necessary harmonic and an ending scoped to "aligned enough for this remaining instant," versus doubt "dispelled forever" and a fulfillment that betrays the premise [C044][C077][C082].
- **0281 (+4.417).** The attribute-persistence case: a skeptic who keeps tabulating explanations mid-ecstasy, with grief recontextualizing the opening on a second read, versus skepticism that melts at the moment of success [C040][C043][C085].
- **0128 (−2.817, comparison win).** Grok 4.5's best-built sequence in the corpus: a reciprocity loop enacted on stage in which the broker discovers he was the earlier anonymous giver — stronger social imagination, though a one-story observation [C022][C036][C032].
- **0195 (−2.000, comparison win).** The clean reversal: Grok 4.5's marionette program becomes a working grammar of strings and possibility while Grok 4.6 lapses into checklist mode, defeating any general claim about object integration [C081][C074][C018].
- **0266 (+2.967).** The fork in poetics: courage relocated from a findable cave into a manner of travel, against a literal chamber containing the packet's best image of unlived acts; restraint versus event, with no neutral verdict [C003][C034].
- **0201 (+1.467).** The proxy-separation case: pseudo-mathematical formulas that collapse under inspection versus a plain reframing that resolves the story's own setup — vocabulary as a false signal of thought [C041].

## Cited claim ledger

- **C075 — Symmetric seams narrow the apparent gap:** Both writers fail identically where the prompt is hardest to absorb, pasting a present-tense attribute into past-tense narration, and both lean on verbatim repetition of required phrases as a crutch. The much-discussed gap is smaller at the sentence-insertion level than at the arc level.
  - Story 0078, `grok-4.6-high`:
    > His gift, or his burden, was that he interprets cloud movements, translating their slow dances into forecasts of fortune and threat.
    Grok 4.6 (high) breaks tense to accommodate the attribute verbatim; grok-4.5-high breaks agreement at the same spot with "how he interprets cloud movements that revealed secrets." Both also repeat required phrases unchanged throughout, and in 0195 Grok 4.6 (high)'s repetition rate matches grok-4.5-high's.
- **C080 — Motives without inner weather:** Both writers frequently substitute declared motivation for psychological development. Characters know what they want immediately, encounter little ambivalence unrelated to the assigned tone, and complete procedures that validate their initial orientation. This makes them effective conceptual operators but weakly individuated people.
  - Story 0195, `grok-4.5-high`:
    > His sole motivation remained to capture the shape of possibility before it dissolved into the endless night.
    The narrator supplies a complete, singular motive from outside; the story does not uncover competing loyalties or a personal reason that this particular knight needs possibility.
  - Story 0195, `grok-4.6-high`:
    > His motivation drove him onward to capture the shape of possibility amid the flux.
    Grok 4.6 (high) likewise presents motivation as a task directive rather than an evolving psychological pressure.
- **C084 — Required elements metabolized versus name-checked:** grok-4.5-high frequently labels the assignment's parts inside the fiction and redeploys the exact required phrases many times per story (variants of "against the current" appear roughly eight times in grok-4.5-high's 0048, and "Lucidly watchful" five-plus). Grok 4.6 (high) usually enacts each element once in action and then lets it operate silently. grok-4.5-high even bends grammar to lodge an element, turning the required action verb into a noun.
  - Story 0247, `grok-4.5-high`:
    > The core concept that bound their efforts was sign language.
    The story announces its own required-element slot ("core concept") rather than letting sign language simply function; nearby sentences likewise label "His method" and "his motivation."
  - Story 0197, `grok-4.5-high`:
    > The reappear of these figures felt natural under the coded starlight.
    "Reappear" is forced into a noun to guarantee the element's presence, showing that detectability outranks syntax; compare Grok 4.6 (high) 0197, where suppressed events "reappear in attics and basements" as a working verb.
- **C006 — Prompt digestion versus prompt recitation:** Writer Grok 4.6 (high) more often turns supplied abstractions into observable relations: persistence becomes knowing when to offer and withdraw a hand, while interconnectedness becomes a recurring motif across stone, water, stars, and memories. Writer grok-4.5-high more often restates the required method or tone as an explanatory label. This is a difference in semantic selectivity rather than vocabulary.
  - Story 0266, `grok-4.6-high`:
    > The guides remained gently persistent, offering a hand only when the fog grew too thick, then releasing it.
    The attribute is embodied as calibrated assistance. “Gentle” and “persistent” acquire distinct behavioral meanings instead of remaining decorative adjectives.
  - Story 0321, `grok-4.6-high`:
    > He studied the grotto carefully and discovered via interconnected patterns how every crack in the stone, every ripple in the water, and every star aligned in repeating motifs.
    The required method receives perceptible components and becomes something the character can actually inspect and communicate.
  - Story 0321, `grok-4.5-high`:
    > The method of via interconnected patterns proved the perfect way to achieve his motivation of merging parallel timelines.
    The sentence reports compliance with the method and motivation but adds no new mechanism, perception, or consequence. Its awkward syntax preserves the supplied phrase instead of assimilating it.
- **C064 — Elements made load-bearing:** Grok 4.6 (high) more often fuses prompt elements into a single conceptual structure rather than assigning each one a separate explanatory sentence. In the clock-tower story, literal grain silos, linguistic isolation, and the desired bridges become mutually interpreting scales of the same problem.
  - Story 0350, `grok-4.6-high`:
    > Mira believed these talks revealed a deeper truth: the people who filled the elevators lived equally isolated lives, trapped in their own cultural and personal silos.
    The talking architecture does not merely satisfy a surreal requirement; it gives Mira a social diagnosis and converts “silos” from setting into a model of communal separation.
- **C008 — Required-phrase recitation versus integration:** Both writers name required elements almost verbatim, but grok-4.5-high repeats the assigned phrases at nearly double Grok 4.6 (high)'s rate and stacks them until they function as labels rather than meaning. In 0258 grok-4.5-high deploys "steadily curious" six times and closes by packing three required phrases into one sentence; in 0323 "balancedly curious" appears five times, including an ungrammatical insertion ("He balancedly curious nature drove him to experiment"), which shows template behavior overriding syntax. grok-4.5-high likewise cites "the mirrored hush" five times in 0313, while Grok 4.6 (high)'s third use reworks it into psychology ("The hush was mirrored in his own soul"). The difference is between citing a constraint and metabolizing it.
  - Story 0258, `grok-4.5-high`:
    > Her steadily curious eyes already scanned for the next set of cards to reverse engineer further truths by multiplying paths yet unexplored.
    Three distinct required elements (attribute, core concept, method) are recited verbatim in a single closing sentence, contributing nothing beyond confirming their presence. This is the terminal instance of a story-long pattern in which the attribute phrase alone appears six times.
- **C025 — Element recitation versus element enactment:** grok-4.5-high discharges required elements by repeating their exact phrases as sentence subjects, so the prose's job becomes re-asserting compliance rather than building a scene. Grok 4.6 (high) discharges the same elements by instantiating them as procedures and evidence. The difference is visible within single sentences: grok-4.5-high reuses a required phrase twice inside one line, while Grok 4.6 (high) renders the same kind of required method as legible stratigraphy that does narrative work.
  - Story 0095, `grok-4.5-high`:
    > They paused to examine the half-painted sundial once more verifying the revelations via the coded angles in a half-painted sundial.
    The required method phrase is repeated verbatim twice within one sentence, and this exact string appears three times across the story; repetition here certifies coverage rather than adding information.
  - Story 0068, `grok-4.6-high`:
    > Each layer told a partial story of collapse: silt over cobblestones, then ash, then more silt mixed with household trash.
    The same required method is enacted as ordered, readable evidence; the layers themselves narrate the city's collapse, so the element performs story work instead of being name-checked.
- **C013 — Two kinds of scaffolding leak: receipt versus ontology:** Both writers surface the prompt's element names, but grok-4.5-high names them as completed tasks, using narrator-level bookkeeping vocabulary ("the action unfolded," "Motivation satisfied") that turns the text into a checklist confirmation. Grok 4.6 (high)'s leaks are converted into world-facts — most strikingly by treating an empty prompt field as an assertion about time. The leak costs Grok 4.6 (high) less because it buys content.
  - Story 0103, `grok-4.5-high`:
    > Then the action unfolded as the images started to disintegrate through hyperbolic geometry.
    "The action" is prompt-category language, not story language; the sentence certifies that a required event has occurred rather than rendering it.
  - Story 0103, `grok-4.6-high`:
    > No timeframe bound this moment; it existed outside chronology, an eternal now where past and future dissolved into pure sensation.
    Grok 4.6 (high) is also leaking the prompt (the "Timeframe: None" field), but recasts the absence as a metaphysical property consistent with the story's premise.
- **C046 — Narration that grades its own compliance:** grok-4.5-high repeatedly steps outside the fiction to certify that the required elements combined and that the method succeeded, including re-importing prompt phrases with their original tense intact. This converts the ending into a report on the assignment. Grok 4.6 (high) does this too, but less often and less terminally.
  - Story 0153, `grok-4.5-high`:
    > No longer haunted she walked free the method of messages in condensation on windows having bridged worlds perfectly.
    > The action to evoke the vital moment succeeded only because every element from spirits to shard aligned with her need.
    The narration names the "method" and the "action" as categories and audits their success, which is checklist commentary rather than event.
  - Story 0064, `grok-4.5-high`:
    > The blithe cemetery gardener, whose smile never faded no matter how many funerals he attended, arrived at this spot after the chess clock runs down.
    The present-tense prompt phrase is embedded unaltered in a past-tense sentence — a grammatical fossil showing the constraint was pasted rather than absorbed.
  - Story 0064, `grok-4.6-high`:
    > All elements of the night had aligned to reveal what intentions truly formed when time itself had run its course.
    Grok 4.6 (high) commits the same offense as a closing line, which limits how strongly this can be claimed as a writer-level distinction.
- **C058 — Endings that leave residue versus endings that certify completion:** grok-4.5-high's stories characteristically continue past their climax, adding summary paragraphs that inventory the brief and confirm the mission succeeded; Grok 4.6 (high) more often stops on a concrete image or a bounded outcome. This is a control difference visible in structure rather than sentence quality: grok-4.5-high's codas restate rather than extend.
  - Story 0006, `grok-4.5-high`:
    > She had used every element of her journey the black sand the coin method the graft itself to create harmony.
    The narrator audits the prompt list from inside the fiction, and this occurs after the story has already delivered two prior farewells.
  - Story 0167, `grok-4.5-high`:
    > The reflective harbor glazier had communed successfully before everything shifts.
    A final line that grades the character's performance against the assignment, complete with tense mismatch imported from the brief.
  - Story 0249, `grok-4.6-high`:
    > Climbing down, the experimental treatment guinea pig returned to the sound wave garden, his quietly rebellious heart now carrying a piece of living starlight.
    Grok 4.6 (high) closes on an image of what remains rather than a verdict on whether the goal was met.
- **C042 — Constraint absorption: mandated phrases metabolized versus bolted on:** Both writers must insert identical required language, but grok-4.5-high periodically warps grammar to force the phrasing in, while Grok 4.6 (high) usually rebuilds the sentence so the element functions. The skill being measured, invisible under standard rubrics, is how completely a writer hides the seams of the constraint.
  - Story 0197, `grok-4.5-high`:
    > The reappear of these figures felt natural under the coded starlight.
    The required action is forced into noun position, and the same passage has tense drift ("scenes of old rebellions reappear"); 0201 similarly yields "after the anesthesia wear-off residual." These are control failures under constraint pressure.
  - Story 0197, `grok-4.6-high`:
    > Static-laced broadcasts would make suppressed events reappear in attics and basements where old radios still functioned.
    The identical mandated verb is grammatically integrated and simultaneously given mechanism (old radios, analog signals), so the constraint disappears into the fiction.
- **C012 — Self-auditing endings that address the evaluator:** grok-4.5-high twice closes a story by announcing that the required elements have been successfully integrated, a rhetorical gesture aimed at whoever is checking the list rather than at a reader inside the fiction. These benedictions ("narrative of growth through challenge," "coherent path to enlightenment") summarize the story's own completeness and retroactively certify the method, object, and concept. Grok 4.6 (high)'s endings never comment on the story's construction; they stay inside the fiction's forward motion, however muted. The habit corroborates the recitation pattern in claim two: grok-4.5-high's prose is oriented toward demonstrable compliance, while Grok 4.6 (high)'s is oriented toward the constraint as a container to inhabit.
  - Story 0095, `grok-4.5-high`:
    > Thus all elements of the day wove together seamlessly supporting a narrative of growth through challenge.
    The final sentence steps outside the story to affirm that its components "wove together seamlessly," language that belongs to a compliance report rather than to the fiction. Story 0216 ends the same way: "all integrated elements wove a coherent path to enlightenment under the silo's watch."
- **C015 — Total victory versus surviving remainder:** grok-4.5-high's closes eliminate the problem class entirely and often universalize the cure to all future people; Grok 4.6 (high)'s closes usually leave the problem structurally intact and claim only a local, partial gain. The remainder is what makes Grok 4.6 (high)'s outcomes feel proportionate to the small events that produced them.
  - Story 0110, `grok-4.5-high`:
    > Ultimately the power of transparency had thawed every last shred of lingering mistrust.
    Absolute quantifier ("every last shred") on a social problem resolved by one annotated ticket; the outcome is disproportionate to its cause, which flattens the stakes retroactively.
  - Story 0110, `grok-4.6-high`:
    > Future concerts would surely produce new doodles, some perhaps concealing fresh tensions.
    Grok 4.6 (high) concedes the mechanism of mistrust survives the episode; the win is scoped to one night and one accused man.
- **C033 — Calibrated endings versus totalizing endings:** Grok 4.6 (high)'s closes admit remainder, recurrence, and partiality; grok-4.5-high's tend to claim completeness and permanence. The effect is not tonal gloom versus optimism but epistemic scale: Grok 4.6 (high)'s narrators concede they cannot see the whole, grok-4.5-high's narrators assert the whole.
  - Story 0110, `grok-4.6-high`:
    > Future concerts would surely produce new doodles, some perhaps concealing fresh tensions.
    The resolution is treated as one instance in an ongoing series, with "perhaps" preserving the narrator's limited knowledge.
  - Story 0110, `grok-4.5-high`:
    > Ultimately the power of transparency had thawed every last shred of lingering mistrust.
    "Every last shred" claims exhaustive success, which the story has not earned and which removes the residue that would let the world persist after the page.
- **C082 — Completion-report endings:** grok-4.5-high often closes as though certifying that every assigned operation has been completed, using summary language that sits outside the character's immediate perception. Grok 4.6 (high)'s strongest endings compress the elements into a provisional image or measured state. This gives Grok 4.6 (high) greater selective control and leaves more resonance after the mechanism stops.
  - Story 0167, `grok-4.5-high`:
    > The reflective harbor glazier had communed successfully before everything shifts.
    The adverb “successfully” turns an ambiguous spiritual encounter into an evaluated task, and the sentence restates several requirements rather than developing the scene.
  - Story 0310, `grok-4.6-high`:
    > On the ambered observatory deck the cast lots decision maker remained, quietly enthusiastic still, coins in hand, listening after the universe contracts, aligned enough for this remaining instant.
    “Aligned enough” limits the achievement, while the continuing act of listening preserves doubt, setting, object, and motive without declaring final mastery.
- **C083 — Resolution scale proportioned to the premise:** Grok 4.6 (high) repeatedly ends with the problem diminished but intact, so the world's resistance stays credible and the required tone (coded freedom, joyful sorrow, swirling hush) survives the ending. grok-4.5-high escalates to public, often total resolution: mass assemblies, restored memories, finished histories. The difference is not mood but causal proportion — how much change one person's action plausibly buys.
  - Story 0197, `grok-4.6-high`:
    > She knew the transmissions would not topple the regime overnight, yet they would chip at the tyranny of indifference one awakened mind at a time.
    The victory is explicitly bounded; the tyranny persists and the work continues, which is what makes the freedom "coded" rather than declared.
  - Story 0197, `grok-4.5-high`:
    > Faces of forgotten leaders took solid form along the bank.
    > Living descendants of those leaders stepped from the shadows to join them.
    One key-turn summons an instant revolutionary multitude out of nowhere; the premise's whole point (apathy enforced by erasure) is dissolved in a single night.
- **C014 — Whether the marvel gets spent:** Given the identical prop, grok-4.5-high retains it as a souvenir and Grok 4.6 (high) destroys it. Grok 4.6 (high) consistently makes the fantastic instrument pay for the revelation, which creates the sense of an economy; grok-4.5-high's transformations cost nothing, so the climax is announcement rather than exchange.
  - Story 0103, `grok-4.5-high`:
    > The halo fragment he tucked away as a reminder of the day's miracle.
    The object survives intact and becomes memorabilia; nothing has been traded for the insight, so the "discovery" carries no consequence.
  - Story 0103, `grok-4.6-high`:
    > Elias smiled, pocketing the empty space where the halo fragment had been, knowing that true relics now lived within him.
    Same prompt, same object: Grok 4.6 (high) expends it and even dramatizes the gesture of pocketing a vacancy, so the transformation has a price.
  - Story 0385, `grok-4.6-high`:
    > Through progressive disclosure it showed him the cost: those who echoed paid with fragments of their future selves.
    Grok 4.6 (high) explicitly prices the story's central metaphysical gift and links that price back to the required tone (melancholy), making the atmosphere a consequence rather than a decoration.
- **C039 — Resolutions proportional to the stated struggle:** Grok 4.6 (high)'s endings carry cost or deliberate incompleteness that matches the conflict's weight; grok-4.5-high's endings are total and free, with conflict evaporating at assertion. The criterion is internal consistency, not darkness: Grok 4.6 (high) also ends hopefully, but routes hope through loss or partial victory.
  - Story 0100, `grok-4.6-high`:
    > In the chased stillness that had become a lullaby, the undertaker closed his eyes and joined the collection, his purpose fulfilled at last.
    Giving rest a permanent address is fulfilled by the undertaker becoming one of the sheltered dead; the motivation is completed through self-cost, and the chased stillness transforms into lullaby only at that price.
  - Story 0197, `grok-4.6-high`:
    > She knew the transmissions would not topple the regime overnight, yet they would chip at the tyranny of indifference one awakened mind at a time.
    Victory is scaled to a single operative after total plan collapse; contrast grok-4.5-high's 0197, where one key turn restores the true record to the whole public and the spell of indifference shatters in a night.
- **C059 — Transformation with a price versus transformation granted outright:** Grok 4.6 (high) more often bounds the miracle in time or extracts physical effort for it, keeping the wish partly unfulfilled; grok-4.5-high more often upgrades the temporary to the permanent and softens violent required verbs into harmless ones. The prose cue is Grok 4.6 (high)'s willingness to write strain and reversal, against grok-4.5-high's negating constructions ("not destroy, but liberate," "not to bind but to share life").
  - Story 0249, `grok-4.6-high`:
    > He had succeeded in breathing life into their shared dream, if only during the hush, and that knowledge filled him with a profound, glowing ache.
    The stated motivation is met only inside a stated window, and the emotional result is mixed rather than triumphant.
  - Story 0249, `grok-4.5-high`:
    > The auric lagoon under starlight surged and overflowed, flooding the garden with liquid gold that sealed the dream into the physical realm at last.
    The same premise resolves by removing the constraint entirely; the phantom becomes "solid and warm," so the cosmic pause imposes no limit at all.
  - Story 0329, `grok-4.6-high`:
    > With both hands she gripped the statue's base and pulled.
    > Muscles strained, roots tore, wires snapped in showers of blue sparks.
    The required action is performed as labour with breakage, so the following restoration is paid for in the story's own currency.
- **C005 — Civilization without dissent:** Both writers display practical imagination in rebuilding Paper-Lantern Cove, but neither shows much social or political intelligence. Institutions appear because the alchemist designs them correctly; newcomers accept the arrangements, markets become fair, and governance becomes collective without disputes over ownership, authority, memory, or unequal sacrifice. The revival is systems-minded but socially frictionless.
  - Story 0210, `grok-4.5-high`:
    > Governance emerged from collective reasoning instead of hierarchical claims.
    A desirable political outcome simply “emerged.” No constituency, procedure, disagreement, or transfer of power gives collective reasoning causal social form.
  - Story 0210, `grok-4.6-high`:
    > Markets reopened with fair trade practices he had outlined.
    Fairness is treated as a design feature one planner can outline rather than a contested arrangement among people with different leverage and needs.
- **C019 — The setting as applause track — a shared limitation:** Both writers resolve tension by having the environment ratify the protagonist rather than by having anything resist. Landscapes agree, hum in sympathy, and applaud; antagonists (conspirators, saboteurs, mistrustful crowds) either never appear onstage or collapse without argument. This shared move is the largest limit on both writers' causality, and it is easy to mistake for lyricism.
  - Story 0103, `grok-4.5-high`:
    > The garden pulsed in agreement, leaves rustling with shared understanding of the discovery.
    Validation comes from the scenery, so the protagonist's success is never tested by anything with its own interests.
  - Story 0103, `grok-4.6-high`:
    > A gentle quake passed through the earth, affirming the discovery, as if time itself applauded the designer's daring geometry.
    Identical move in Grok 4.6 (high), and more explicit: the universe is literally described as applauding, confirming that the drama's pressure is supplied by sympathy rather than opposition.
- **C024 — Machines that pronounce absolution:** Both writers repeatedly make technical or magical systems deliver emotionally final verdicts. Guilt becomes forgiveness, boredom becomes wonder, and exile becomes vindication with little sustained accountability or contested interpretation. This shared closure hunger limits any claim that either writer is consistently more psychologically mature, although both sometimes retain environmental danger after personal resolution.
  - Story 0278, `grok-4.6-high`:
    > Haunted firmware stabilized as baby cries softened into whispers of forgiveness and understanding.
    The apparatus changes accusation into forgiveness as soon as the ritual succeeds. The character does not have to decide how to live with an answer that might remain painful or ambiguous.
  - Story 0278, `grok-4.5-high`:
    > The haunted firmware quieted its screens going dark after one last translation that simply read thank you mother.
    grok-4.5-high makes the absolution still more explicit: the machine supplies a final, authoritative sentence and then removes itself from further questioning.
  - Story 0292, `grok-4.6-high`:
    > In the lingering humidity, remnants of spongey dread lingered like a warning that nature's exile could return if vigilance failed.
    Grok 4.6 (high) does preserve a distinction between personal vindication and continuing ecological risk, preventing complete triumph.
  - Story 0292, `grok-4.5-high`:
    > Yet the spongey dread did not vanish entirely for residual moisture clung and nature remained unpredictable even after the jet stream began stabilizing.
    grok-4.5-high offers the same useful restraint: technological success does not abolish nature’s instability.
- **C056 — Pre-solved symbolism:** Despite their surreal materials, both writers frequently narrow an object to an announced moral equivalent. The result is imaginative décor with limited interpretive resistance. This is an important absence of difference: Grok 4.6 (high)’s stronger integration does not consistently produce greater ambiguity or symbolic openness.
  - Story 0004, `grok-4.5-high`:
    > The dove gray map case serves as both container and symbol for mapping the journey from pain to joy.
    The narration explicitly assigns the case its symbolic meaning and fixes healing as a journey from one named state to another.
  - Story 0180, `grok-4.6-high`:
    > It took root immediately, symbolizing fresh starts after broken deals.
    Grok 4.6 (high) similarly announces the graft’s meaning at the moment it appears, leaving little room for the immediate magical success to complicate the metaphor.
- **C020 — Friction inside the mechanism:** Writer Grok 4.6 (high) more often supplies intermediate operations, bodily cost, feedback, and verification between intention and success. Writer grok-4.5-high can name plausible equipment, but the equipment commonly proceeds straight from activation to large-scale result. The resulting advantage is substantive causal intelligence rather than mere technical vocabulary.
  - Story 0278, `grok-4.6-high`:
    > Following the letters he prepared his tools on the antique desk.
    > He mixed special ink that glowed like distant meteors streaking through black.
    > On his own chest he tattooed a new constellation forming a binding symbol of linked stars.
    The cure becomes a sequence involving preparation, material composition, self-inscription, and a physical tether. The character must alter his body rather than simply possess the correct relic.
  - Story 0292, `grok-4.6-high`:
    > Lightning forked unnaturally close, but then the local drizzle lessened, a pocket of clearer air forming as if exile's grip loosened.
    > Instruments confirmed a micro-shift, reversible conditions emerging that could reconnect the station to mainland supply routes long severed.
    The experiment entails danger, a limited local effect, instrumental confirmation, and a practical consequence. Success is incremental rather than instantly total.
  - Story 0292, `grok-4.5-high`:
    > They inserted the copper nail from the coffin into the central calibration port as the journals directed.
    > Generators whirred to life following the patterned instructions from the stanzas, sending pulses that influenced the upper atmosphere.
    grok-4.5-high provides a coherent action chain, but “sending pulses” immediately becomes atmospheric influence without resistance, measurement, or a clearly bounded test.
- **C038 — Caused marvels versus declared marvels:** Grok 4.6 (high) supplies provenance and mechanism so fantastic events feel caused; grok-4.5-high has the world simply comply with the protagonist (the lens mends itself, knowledge instructs without words). The difference is causal intelligence, not realism: Grok 4.6 (high)'s magic is equally impossible but arrives with reasons and limits.
  - Story 0197, `grok-4.6-high`:
    > It clicked open to reveal not wires for voice but a compact transmitter and slots for data crystals she had carried.
    The mandated key does designed work: the defunct phone company justifies an analog network resistant to digital erasure, and Mira's prior preparation (carrying the crystals) makes the broadcast her achievement rather than a gift of the setting.
  - Story 0100, `grok-4.5-high`:
    > The distress signals from the package and his own need converge here as the lens begins to mend itself under the influence of the watery archives.
    The central task, revitalizing the lens, is performed by the setting on the protagonist's behalf; effort is asserted elsewhere but the decisive event is unearned, a pattern repeated in all five grok-4.5-high stories.
- **C047 — Convergent inference versus parallel enumeration:** Given a decoding task, Grok 4.6 (high) builds one chain with a corroborating cross-check and a consequence in the world; grok-4.5-high produces a catalogue of independent decodings, each colorful, none verified against another, none acted upon. The felt intelligence comes from the presence of a second, confirming source and a downstream action.
  - Story 0064, `grok-4.6-high`:
    > He cross-referenced with a coin from the sovereign case that bore a similar spiral mint mark, confirming the connection through some forgotten family history.
    The object is used as evidence corroborating a reading, and the reading yields a specific act ("Tomorrow he would contact the niece"). Interpretation becomes consequence.
  - Story 0064, `grok-4.5-high`:
    > Another black thread, dark as midnight, untangled to disclose a merchant's greedy scheme, shaped like a grasping claw that sought to clutch all nearby fortunes.
    The fourth in a list of interchangeable decodings; nothing depends on it, nothing tests it, and the gardener merely records the shapes.
- **C052 — Mechanisms with differentiated parts:** Grok 4.6 (high) more often asks what distinct stages a fantastical procedure would require. grok-4.5-high commonly gives an object one asserted causal power and moves directly to the desired result. This produces an impression of stronger procedural and causal intelligence in Grok 4.6 (high), although neither writer offers rigorous science.
  - Story 0143, `grok-4.6-high`:
    > Some used oscillating reactions that would produce color changes at dawn; others employed slow acid-base shifts that would reveal hidden writing on specially treated paper inside the vials.
    Different reactions have different timing and display functions. The treated paper also supplies an intermediate mechanism between chemical change and readable message.
  - Story 0143, `grok-4.5-high`:
    > Dropping the precious grain into the vial started a slow transformation that would produce a luminous timed message.
    The grain initiates timing, transformation, luminescence, and language in a single unexplained leap. The sequence is legible but less causally discriminating.
  - Story 0033, `grok-4.5-high`:
    > The drone rose silently, guided by gaps in the radar that the released mist from the bottle created, flying over the razor wire that marked the disputed line.
    This is a significant reversal: grok-4.5-high gives the storm bottle a specific tactical function and connects it clearly to the drone’s route.
- **C076 — Constraint circuitry:** Grok 4.6 (high) more often turns the assigned elements into a mutually explanatory circuit rather than a sequence of mentions. In 0310, contraction generates reverse-running cosmic history, static carries that history, and distillation extracts its wavelength. grok-4.5-high identifies a correspondence between prophecy and sequence but does not develop an equally specific cosmological logic.
  - Story 0310, `grok-4.6-high`:
    > Gradually the pattern emerged as a backwards prophecy, a recitation of cosmic history spoken from this final moment backward through time.
    > It described the contraction first, then rewound the expansion, galaxies flying apart in reverse, stars unburning into gas, the primordial fire assembling rather than exploding.
    The prophecy is not merely labeled backwards: its direction is concretely embodied in physical processes, giving several prompt elements one shared conceptual mechanism.
  - Story 0310, `grok-4.5-high`:
    > The backwards prophecy matched this sequence perfectly when read from finish to start.
    grok-4.5-high states the fit clearly, but the fit remains an assertion rather than an articulated model of what reversing cosmic history would mean.
- **C079 — Mechanisms carry theme:** Grok 4.6 (high) more consistently makes mechanisms explain thematic language. Chemical clocks preserve an analog night through analog means; the diamond's flaw simultaneously explains its danger, usefulness, and required placement. This is causal intelligence rather than mere technical diction, though the science remains speculative.
  - Story 0143, `grok-4.6-high`:
    > Some used oscillating reactions that would produce color changes at dawn; others employed slow acid-base shifts that would reveal hidden writing on specially treated paper inside the vials.
    The differentiated reactions give the timed messages a plausible procedure and tie the documentation project to slowness, materiality, and dawn.
  - Story 0388, `grok-4.6-high`:
    > The diamond, they revealed, was no mere gem but a focusing lens, flawed by design to contain the volatile energies of the stillpoint.
    > Its curse was the radiation it had absorbed, leaking slowly unless properly seated.
    One physical property accounts for the apparent curse, the engineered flaw, and the gem's function, creating economical causal linkage.
- **C086 — Causal mechanism versus magical adjacency:** Grok 4.6 (high) builds mechanisms that link object, method, and outcome so the reader can reconstruct why events happen; grok-4.5-high places elements next to each other and lets atmosphere carry the causal load. grok-4.5-high 0281 compounds this with timeline muddles (the pill taken "hours before" produces a "recall" surging like an old memory) and an odd plan to schedule future sessions "after potential static shocks."
  - Story 0197, `grok-4.6-high`:
    > It clicked open to reveal not wires for voice but a compact transmitter and slots for data crystals she had carried.
    Key, lock, transmitter, crystals, and broadcasts form a legible chain; the later effects (old radios in attics) follow from equipment the story has physically established.
  - Story 0197, `grok-4.5-high`:
    > Gears clicked deep inside the ancient frame.
    > A low hum rose from the lagoon itself as if the water remembered.
    > Then the revised histories that had smothered the truth began to peel away.
    The mechanism is "the water remembered"; the key's turning and the histories' peeling are adjacent events linked only by sequence and mood, not by any established means.
- **C021 — Abstractions made to misbehave:** Grok 4.6 (high) more frequently converts conceptual phrases into observable consequences. “Spatial mutiny” alters the behavior of architectural relations, while negative curvature solves a particular problem of narrative capacity. grok-4.5-high more often paraphrases the abstraction as generalized twisting, possibility, or infinity. This gives Grok 4.6 (high) an edge in conceptual entailment.
  - Story 0138, `grok-4.6-high`:
    > Walls refused their positions, sliding into new configurations that defied geometry.
    > Floors became ceilings in abrupt rebellion, and doorways led to places that should not connect.
    Mutiny is not only named; the prose asks what rebellion by space would mean for walls, orientation, and adjacency. The personification generates spatial consequences.
  - Story 0138, `grok-4.5-high`:
    > Spatial mutiny erupted fully as dimensions twisted and stretched creating fractures through which unknown possibilities leaked.
    The sentence preserves the cosmic scale but leaves “possibilities” and the dimensions’ altered behavior comparatively unspecified.
  - Story 0331, `grok-4.6-high`:
    > The stories reawakened fully now, revealing themselves as living entities that inhabited the hyperbolic dimensions, where each narrative could branch into infinite variations without colliding, thanks to the negative curvature allowing more "space" between them.
    Hyperbolic geometry is assigned a functional narrative consequence: increased room permits branching stories to coexist without collision.
  - Story 0331, `grok-4.5-high`:
    > Analog memories, unlike their digital counterparts, flowed continuously like rivers of sensation and emotion.
    This is a genuine counter-strength: grok-4.5-high derives continuity from “analog” rather than treating the word as a decorative synonym for old-fashioned memory.
- **C040 — Attributes as engines, not labels:** In Grok 4.6 (high) the mandated attributes generate decisions and persist to the final paragraph; in grok-4.5-high they are stated once and discarded when inconvenient. This is psychological intelligence: character traits that constrain the plot rather than decorate it.
  - Story 0281, `grok-4.6-high`:
    > The skeptic within tabulated possible explanations involving residual current from the shock, tactile suggestion from the sliver, or simple grief transmuted by creativity.
    The affectionate skeptic stays a skeptic at the climax, producing the story's central epistemic tension; the following sentence lets affection validate the work without refuting the doubts, so the attribute does structural work to the end.
  - Story 0281, `grok-4.5-high`:
    > Mira's skepticism melted into pure affection as she saw how the method had worked.
    The required trait is retired the moment it would complicate the resolution, the same pattern as grok-4.5-high's conflicted novelist ending "no longer torn" and the stubbornness that "dissolves into peaceful acceptance" in 0100.
- **C065 — Compromising emotional particulars:** Grok 4.6 (high) more often specifies feelings that threaten the character's preferred self-image. This produces psychological perceptiveness: fear is not just an enemy but is entangled with paralysis, relief, envy, and survivorhood.
  - Story 0077, `grok-4.6-high`:
    > He confessed the envy he felt toward the dead, the relief mixed with horror at being the sole survivor of his group.
    The confession contains incompatible responses rather than a generic buried terror. Elias becomes morally and emotionally implicated in his survival, making “unbosom” consequential.
- **C085 — The assigned character trait survives to the final page:** Grok 4.6 (high) treats the required attribute as a permanent disposition that must persist through the resolution; grok-4.5-high treats it as a defect the plot cures. Grok 4.6 (high)'s skeptic ends still skeptical, still affectionate; grok-4.5-high's skepticism "melted." grok-4.5-high's conflicted novelist ends "no longer torn," his underestimated rebel becomes "the fixed point around which freedom turned." A trait that disappears at the end was decoration, not character.
  - Story 0281, `grok-4.6-high`:
    > The skeptic within tabulated possible explanations involving residual current from the shock, tactile suggestion from the sliver, or simple grief transmuted by creativity.
    Even mid-ecstasy the doubt keeps working alongside the love; the attribute "affectionate skeptic" is dramatized as a stable double exposure rather than a problem to solve.
  - Story 0281, `grok-4.5-high`:
    > Mira's skepticism melted into pure affection as she saw how the method had worked.
    The defining tension of the assigned character is dissolved by success, leaving "pure affection"; the trait existed mainly to be overcome.
- **C029 — Hinge-making: turning the timeframe into the theme:** Grok 4.6 (high) finds structural hinges that fuse arbitrary required elements, most sharply in 0095, where the mandated timeframe "while waiting" becomes the payoff of the mandated motivation "to turn questions into destinations." grok-4.5-high treats the timeframe as scenery and stages the motivation as explanation instead.
  - Story 0095, `grok-4.6-high`:
    > Waiting here was already a destination born of prior questions.
    Two independent required elements (timeframe and motivation) are collapsed into a single earned realization, so the constraint set generates the theme rather than decorating it.
- **C016 — Longing with an address versus longing without one:** On the same prompt, grok-4.5-high's ache has no human referent — the lost thing is the dream itself — while Grok 4.6 (high) attaches it to a specific person, a specific weather event, and a specific interval, then widens it to a collective. Specifying the referent gives Grok 4.6 (high)'s abstraction ("cipher of longing") something to be a cipher of.
  - Story 0332, `grok-4.5-high`:
    > the urgent need to capture a runaway dream which had escaped her grasp and vanished among the whispering shores years earlier
    The loss is circular: the dream is missing because the dream is missing. Nothing in the world is different for its absence, so the "luminous absence" cannot be located.
  - Story 0332, `grok-4.6-high`:
    > That dream contained the cipher of longing, an intricate code woven from memories of a sailor who had vanished in a squall ten years earlier.
    The abstraction is grounded in a person, a cause of death, and an elapsed time, which lets later images (the figure coded in ripples, the empty sea) mean something particular.
- **C068 — Two intelligences about myth:** Grok 4.6 (high) shows structural intelligence by staging the social transmission through which an event becomes myth. grok-4.5-high offers the more surprising conceptual hypothesis: myth may preserve influence precisely by erasing personal memory. Grok 4.6 (high) enacts the process better; grok-4.5-high briefly thinks about it more strangely.
  - Story 0361, `grok-4.6-high`:
    > The tale spread from village to village.
    > Bards added details until the facts blurred.
    > Across the fade from memory to myth the event transformed.
    The required timeframe becomes narrative action: witnesses, reports, bards, children, and elders progressively alter the event.
  - Story 0361, `grok-4.5-high`:
    > Perhaps the mentor had chosen to fade completely into myth so that his influence could germinate freely without the constraints of memory.
    grok-4.5-high proposes a productive opposition between remembered personhood and freely germinating influence, an idea less conventional than simple legendary transmission.
- **C041 — Conceptual honesty versus pseudo-rigor:** Given the most conceptually demanding prompt (the mathematics of mercy), grok-4.5-high decorates with calculus notation that does not survive inspection, while Grok 4.6 (high) answers the premise by reframing it in plain language that actually resolves the story's own setup. This is the cleanest separation in the packet between vocabulary as a proxy for intelligence and intelligence itself.
  - Story 0201, `grok-4.5-high`:
    > Mercy equaled the integral of pain over time divided by the sum of forgiveness variables, or so the lights suggested.
    The formula borrows the prestige of mathematics without content; "the limit as cruelty approaches zero of resistance" later is syntactically mangled math-speak, indicating the target was impressiveness rather than meaning.
  - Story 0201, `grok-4.6-high`:
    > Standing there he understood that mercy defied strict equations yet followed a logic of its own.
    This is a real conceptual position and it closes the story's loop: the torturers believed numbers held secrets of war, so the survivor's acceptance of an incomplete proof is the earned repudiation of their frame, not a dodge.
- **C001 — Evidence before synthesis:** Writer Grok 4.6 (high) better separates material evidence from the narratives imposed on it. The sediment is partial, excavation can destroy information, and the cog creates an ethical problem rather than supplying a verdict. Writer grok-4.5-high acknowledges competing accounts but then announces a precise compromise history without showing how the recovered evidence establishes it. This difference produces an impression of epistemic maturity and controlled causal reasoning.
  - Story 0068, `grok-4.6-high`:
    > Each layer told a partial story of collapse: silt over cobblestones, then ash, then more silt mixed with household trash.
    > He worked slowly, using a scavenged trowel, because haste would destroy the very evidence he sought.
    The concrete sequence of deposits makes interpretation materially constrained, while the danger of damaging evidence gives inquiry a method and an ethical cost.
  - Story 0068, `grok-4.5-high`:
    > He forms his own synthesis with rationally rebellious logic.
    > The plague ended because seafarers timed an escape correctly yet brought toxins.
    > This dual role justifies preserving their tools for future guidance.
    The conclusion is called logical, but the story has not established either precise causal assertion. Complexity here risks becoming a tidy compromise rather than earned inference.
- **C026 — Stating significance versus staging it:** grok-4.5-high's narrator tells the reader what objects mean, duplicating what the scene already shows. Grok 4.6 (high) lets the same object carry meaning through image and use. The matched object in 0068 makes the contrast clean: identical brass cog, opposite allocation of interpretive labor.
  - Story 0068, `grok-4.5-high`:
    > The seafarer's chronometer cog represents all ancient methods he aims to preserve.
    The narrator supplies the symbol's decoding directly, pre-empting the reader's inference and flattening the object into a thesis statement.
  - Story 0068, `grok-4.6-high`:
    > The small brass piece sat in his palm like an accusation.
    Meaning is carried by a single simile that implies guilt and evidence without naming them; the reader completes the thought, which is why the object feels heavier.
- **C032 — Specified evidence versus announced resolution:** When a story turns on discovery, Grok 4.6 (high) states what was discovered and where, creating a small epistemic reversal; grok-4.5-high typically names that a revelation occurred and reports its social effect, leaving the informational content blank.
  - Story 0110, `grok-4.6-high`:
    > Hidden among the margins were contrary marks from the percussionist, revealing his own sabotage through cramped guilty scribbles.
    Location ("margins"), medium ("cramped scribbles") and content (self-incrimination) are specified, so the crowd's earlier belief is demonstrably wrong rather than merely said to be.
  - Story 0110, `grok-4.5-high`:
    > The accused figure stepped forward and responded with matching honest doodles of explanation.
    > Misunderstandings dissolved as transparency spread through the group.
    The explanation itself is never given; the reader is told the misunderstanding dissolved, which is the outcome standing in for the mechanism.
- **C072 — Motivation weighted by cost and history:** Grok 4.6 (high) supplies the required motivation with a backstory that includes failure and consequence, making the abstract drive legible as psychology. grok-4.5-high states the motivation firmly but rarely lets anything be lost because of it.
  - Story 0391, `grok-4.6-high`:
    > Impatience once ruled the mapper's blood, sending scouts too soon and costing lives.
    One clause converts "to sculpt patience from impatience" from a slogan into a history with casualties, so the later waiting carries moral weight. grok-4.5-high's mapper simply "chiseled it away, sculpting pure patience from its rough form," an assertion without cost.
- **C060 — Repairing prompt incoherence by invention versus annotating it and continuing:** Given briefs that combine mutually hostile elements (kelp-drift peace in a desert lagoon; noctilucent reckonings at dawn), Grok 4.6 (high) invents a world-rule that makes the combination legal, while grok-4.5-high states the mismatch as a fact and proceeds regardless. Grok 4.6 (high)'s method buys coherence at the cost of never acknowledging strangeness; grok-4.5-high's produces a deadpan candour that leaves the fiction unbuilt but is oddly the more intellectually exposed move.
  - Story 0006, `grok-4.6-high`:
    > All around her the lagoon held a kelp-drift peace, long dark fronds swaying in currents too slow to name, their motion echoing the clouds that slid from one horizon to the other without hurry or haste.
    Grok 4.6 (high) installs actual kelp in the desert lagoon so the required tone can be literal, and ties its motion to the required timeframe, resolving two constraints with one invention.
  - Story 0006, `grok-4.5-high`:
    > The tone of the day settled into kelp-drift peace as soft as floating fronds in quiet seas even though this was desert.
    The contradiction is named and abandoned in the same sentence; the simile is imported from a sea that the story does not contain.
  - Story 0167, `grok-4.5-high`:
    > He recalled past noctilucent reckonings under actual night clouds that glowed strangely in polar regions of the sky.
    > Though this dawn lacked true noctilucence the mental ones burned bright.
    grok-4.5-high supplies the real-world referent and then concedes the metaphor is only mental — a pedantic honesty about the brief's strain that Grok 4.6 (high), who smooths the same phrase into "thoughts that glowed with an inner light," never risks.
- **C007 — Threshold poetics: staying inside the assigned timeframe and deferring the payoff:** Across 0095, 0313, and 0323 Grok 4.6 (high) ends at the threshold of the promised event rather than staging it, which keeps the story inside the specified timeframe (while waiting; twilight patrol; the interval after contact). The duel, the communal remembering, and the mastery of starlight are all positioned as imminent but unrealized, giving Grok 4.6 (high)'s stories a consistent architecture of poised anticipation that mirrors the prompts' emphasis on waiting and aftermath. grok-4.5-high instead narrates the payoff and its institutional sequel: the challenger arrives and fences in 0095, the community center is built and the label framed in 0313, the curriculum is transformed in 0323. grok-4.5-high's arc is complete where Grok 4.6 (high)'s is suspended.
  - Story 0313, `grok-4.6-high`:
    > Tomorrow he would begin to spin those stories into shared meaning, inviting others to add their own recollections.
    The story's central motivation is fulfilled only prospectively: the entire narrative occupies the twilight patrol of the given timeframe, and the communal meaning-making is deferred to a tomorrow outside the story. The same pattern governs 0095, which ends "The wait itself had become the journey," and 0323, which ends with a vow to master the skill "herself first."
- **C034 — Interior goods: refused literalization (Grok 4.6 (high)) versus staged retrieval (grok-4.5-high):** Given identical elements, Grok 4.6 (high) converts the quest object into a disposition and explicitly declines the physical hiding place; grok-4.5-high builds the hiding place and fills it with an image. The difference is a genuine fork in poetics — Grok 4.6 (high) gains restraint but loses event, grok-4.5-high gains an image but literalizes a metaphor.
  - Story 0266, `grok-4.6-high`:
    > Unused courage, she began to sense, waited not in some distant cave but in the willingness to keep moving without a map.
    Grok 4.6 (high) names the obvious literalization in order to refuse it; the payoff is relocated to the manner of travel, consistent with the story's indirect-routes method.
  - Story 0266, `grok-4.5-high`:
    > Deeper she found a still chamber where reflections showed not her face but visions of bold acts she had never claimed.
    grok-4.5-high takes the literal route but earns a strong image: unclaimed acts as reflections replacing the self, which is more concrete than Grok 4.6 (high)'s aphorism.
- **C028 — Verdict endings versus ongoing practice, plus the self-grading finale:** grok-4.5-high closes by reconciling, thanking, and summarizing, often with a final sentence that assesses the story's own success. Grok 4.6 (high) closes by establishing a practice that continues past the last line, leaving the central question intact. Grok 4.6 (high)'s endings cost or defer something; grok-4.5-high's endings certify that everything worked.
  - Story 0095, `grok-4.5-high`:
    > Thus all elements of the day wove together seamlessly supporting a narrative of growth through challenge.
    The closing sentence evaluates the story's own construction ("all elements... wove together seamlessly"), a self-grading gesture that substitutes certification for resonance.
  - Story 0068, `grok-4.6-high`:
    > Those few became his reluctant students.
    The story ends by opening a continuing social practice around the unresolved question; nothing is settled, but something has begun, which fits a core concept of competing narratives.
- **C043 — Management of reader knowledge: recontextualization versus front-loading:** Grok 4.6 (high) withholds information so that earlier sentences change meaning retroactively; grok-4.5-high discloses everything at first mention, and no grok-4.5-high sentence rewards a second reading. This is a structural intelligence that ordinary judging, which reads each story once, is built to miss.
  - Story 0281, `grok-4.6-high`:
    > It had been a last attempt when Elias's voice grew too weak for conversation.
    Mid-story, the studio session is revealed as solitary grief work for a dead or dying partner, retroactively converting the opening's shared glances into memory and the whole light-painting method into an elegy; the telepathy pill recall becomes bereavement rather than experimentation.
  - Story 0048, `grok-4.5-high`:
    > His motivation remained pure: to collect the shapes of different hopes before they dissolved forever.
    grok-4.5-high's typical move: motivation, conflict, and stakes are stated outright in the opening beats and then illustrated without modulation; nothing is withheld, so nothing can be reweighted.
- **C073 — Sentence-level syntactic control:** grok-4.5-high habitually writes long, comma-free run-ons in which clauses stack without hierarchy, blurring agency and sequence. Grok 4.6 (high)'s sentences are mostly punctuated and subordinated, so cause and timing stay clear.
  - Story 0078, `grok-4.5-high`:
    > Softly he tapped a ripe fruit and sketched resonance vibrated outward rippling the water in perfect circles of sound that bounced back from distant horizons.
    The sentence runs five actions together with no punctuation and a subject-verb collision at "sketched resonance vibrated," a pattern pervasive in grok-4.5-high's 0078 and 0177. Grok 4.6 (high)'s equivalent passages mark each action's relation to the next.
- **C018 — Whether the required object does causal work — inconsistent:** I expected Grok 4.6 (high) to integrate props more functionally, and in the projector-lens story Grok 4.6 (high) does, restoring the object's native function and using the setting's crystal as a screen. But in the water-clock story the pattern reverses cleanly: grok-4.5-high makes the screw the working fastener whose adjustment repairs the clock, while Grok 4.6 (high) has it found offstage and retired to a display case. The difference is real per-story but does not hold as a trait.
  - Story 0110, `grok-4.6-high`:
    > She then positioned the lens from projector to catch lantern glow and throw enlarged versions of the doodles onto a standing crystal slab.
    The lens is used as a lens-from-a-projector — projection, not generic magnification — and the setting supplies the screen, so two required elements interlock mechanically.
  - Story 0110, `grok-4.5-high`:
    > Holding the lens carefully, he directed it toward the vibrating walls to focus the whispers.
    An optical lens is used to focus sound; in a text otherwise this literal-minded, the effect is inattention to what the object is rather than deliberate surrealism.
  - Story 0236, `grok-4.5-high`:
    > With renewed focus she adjusted the midwife’s birthing clamp screw until the water dripped at a perfect rate.
    Here grok-4.5-high makes the required object mechanically load-bearing — the story's one action depends on it — while Grok 4.6 (high)'s version ends "The screw found a new home in a display case, honored for its unique journey."
- **C044 — Tone words treated as endings versus tone words treated as paint:** When a prompt supplies a melancholic or doubtful tone, Writer Grok 4.6 (high) keeps that state alive through the final sentences, integrating it into the resolution; Writer grok-4.5-high applies the tone as adjectival color early and then explicitly cancels it at the close, so the required mood ends up contradicted by the story's own last lines.
  - Story 0310, `grok-4.6-high`:
    > Then stellar doubt returned, cooler than the residual heat, questioning whether any alignment could matter in a universe already decided upon collapse.
    > He accepted the doubt as part of the wavelength, not an enemy but a necessary harmonic.
    The prescribed tone is absorbed into the story's central metaphor and survives the climax; doubt is repositioned rather than removed.
  - Story 0310, `grok-4.5-high`:
    > But the success of the backwards prophecy and the accurate casting of lots dispelled it forever.
    The required "stellar doubt" is eliminated by narratorial fiat, leaving the story's stated tone unrepresented at the point where tone matters most.
  - Story 0205, `grok-4.5-high`:
    > The baroque asteroid continued its eternal rotation, now enriched by a shared vision that softened the edges of visible time with tempered hope amid the burnished sorrow.
    "Burnished sorrow" is retained as a phrase while being functionally overwritten by "enriched," "shared," and "tempered hope."
- **C077 — Doubt as a working part:** Grok 4.6 (high) treats uncertainty as an ingredient of knowledge rather than a temporary obstruction. This produces epistemic maturity: the protagonist can act without converting interpretation into certainty. grok-4.5-high instead makes successful procedure abolish doubt, giving the narrative cleaner closure but flattening the required tone of stellar doubt.
  - Story 0310, `grok-4.6-high`:
    > He accepted the doubt as part of the wavelength, not an enemy but a necessary harmonic.
    The metaphor changes the epistemic structure of the story. Doubt is neither failure nor ornamental mood; it becomes part of the alignment being sought.
  - Story 0310, `grok-4.5-high`:
    > But the success of the backwards prophecy and the accurate casting of lots dispelled it forever.
    The permanent dismissal of doubt resolves the quest decisively but makes doubt less substantive and weakens the tension between divination, random noise, and purpose.
- **C087 — Epistemic restraint: the marvelous stays doubtful:** Grok 4.6 (high)'s narration habitually hedges the supernatural with alternatives, keeping the lucidly-watchful register the prompts often request; grok-4.5-high's narration declares the marvel as public fact. This produces different reading contracts: Grok 4.6 (high) invites interpretation, grok-4.5-high asks only for acceptance.
  - Story 0048, `grok-4.6-high`:
    > The current seemed to lessen, or perhaps he had grown stronger.
    Even at the triumphant turn Grok 4.6 (high) preserves two competing explanations, one external and one psychological; the watchfulness assigned to the character is also practiced by the prose.
  - Story 0247, `grok-4.5-high`:
    > Suddenly, the music burst forth not just in their imagination but as real sound carried on the night breeze.
    The narration forecloses the imaginative reading outright ("not just... but as real sound"), converting what Grok 4.6 (high) keeps as ripples and possible "echoes of old names" into certified public miracle.
- **C002 — Success without canceled paradox:** In the temporal-ferry story, Writer Grok 4.6 (high) allows the goal to succeed without making its central contradiction disappear. The timelines merge, but permanence takes the form of perpetual arrival and departure. Writer grok-4.5-high instead translates merger into stability, completion, harmony, and peace. Grok 4.6 (high) therefore shows stronger conceptual control over the supplied “permanent transient” tension.
  - Story 0321, `grok-4.6-high`:
    > The tone of their existence settled into something permanent transient, a state where the ferry forever approached the spectral grotto under starlight and forever left it behind.
    > Clocks continued to run sideways, marking a time that moved laterally through merged realities without ever settling.
    The paradox becomes the new operating condition rather than decorative wording. Achievement changes how instability is inhabited but does not abolish it.
  - Story 0321, `grok-4.5-high`:
    > The vanishing commuter ferry solidified, its form stable under the eternal starlight of the spectral grotto.
    > Clocks still ran sideways but now in harmonious agreement across the merged timelines.
    “Stable” and “harmonious agreement” neutralize much of the friction promised by permanent transience, even though sideways clocks remain as imagery.
- **C045 — Resolutions that regenerate the problem:** Grok 4.6 (high) occasionally lets a success produce its own successor problem or turn back on the protagonist, which models how contested knowledge actually behaves. grok-4.5-high's resolutions terminate: disputes are settled by unanimous conversion, and the artifact goes dormant on a desk.
  - Story 0205, `grok-4.6-high`:
    > Scholars would soon argue over the authenticity of these fresh echoes, sparking another archaeological dispute that would last generations.
    The hero's fabricated history does not end the archaeological dispute; it manufactures the next one, closing the story on a loop rather than a settlement.
  - Story 0205, `grok-4.5-high`:
    > Awed by the projected scenes, they abandoned their rigid positions and agreed that the civilization embodied a synthesis worthy of emulation.
    Two entrenched academic factions convert instantly and unanimously; the social mechanism of a dispute is replaced by a wish.
- **C071 — Endings that perform the theme versus endings that summarize it:** Grok 4.6 (high) tends to close on an action or image that enacts the story's thesis, while grok-4.5-high tends to close with a summarizing moral using connectives like "Thus" and "In this way."
  - Story 0177, `grok-4.6-high`:
    > He no longer needed to guard it.
    > In that act he began to transcend, his awareness brushing for an instant against the raw now of rain and thunder and trembling earth.
    Transcendence for a character who has foresight and hindsight only is performed as a single instant of present-tense contact, and the release of the seal demonstrates the story's answer about letting go. grok-4.5-high's parallel endings instead recap, as in "Thus the Leeward tide prophet secured his place."
- **C031 — Objects act according to what they are (Grok 4.6 (high)) versus what the plot needs (grok-4.5-high):** Grok 4.6 (high) repeatedly derives events from an object's actual function, so the device and the theme reinforce each other; grok-4.5-high more often grants an object an arbitrary or physically incoherent power, and sometimes uses it to override the story's own premise.
  - Story 0110, `grok-4.6-high`:
    > She then positioned the lens from projector to catch lantern glow and throw enlarged versions of the doodles onto a standing crystal slab.
    A projector lens is used to project, and projection is literally publication — the object's real optics carry the story's theme of public transparency.
  - Story 0110, `grok-4.5-high`:
    > Holding the lens carefully, he directed it toward the vibrating walls to focus the whispers.
    > Suddenly fragments of dialogue became audible despite the era after words become unnecessary.
    A lens is given acoustic powers it cannot have, and the effect cancels the story's stated premise; "despite" flags the contradiction without resolving it.
- **C057 — Apparatus specified to the point of function versus apparatus merely named:** When a story needs an invented device or system, Grok 4.6 (high) tends to state how it works well enough that its output follows from its parts, while grok-4.5-high tends to name the device, declare it complex or effective, and move on. The prose signature is Grok 4.6 (high)'s use of load, contact, and correspondence verbs (hold, strike, press, represented) against grok-4.5-high's classificatory grammar ("the method he employed was," "building a complex diagram").
  - Story 0006, `grok-4.6-high`:
    > The coin's weight would hold the graft steady against the lagoon's gentle surge while the red thread, bright as arterial blood, would remind her that life still pulsed even in ruined places.
    The required object is given a mechanical job (mass as clamp) before it is given a symbolic one, so its later ringing against the root is an event the story has already made possible.
  - Story 0247, `grok-4.6-high`:
    > Low tones represented the heavy ship silences while bright arpeggios echoed the pebble beach.
    Grok 4.6 (high) specifies the actual mapping rule between the catalogued silences and the resulting music, so "translate silence into music" is a procedure rather than a slogan.
  - Story 0247, `grok-4.5-high`:
    > Lira whispered coordinates and Elias signed the corresponding patterns, building a complex diagram of silence.
    The system's complexity is asserted as an adjective; no instance of the diagram, no rule of correspondence, and no differentiated silence is ever supplied.
- **C049 — Premise absorbed into figure versus premise stated then violated:** Both writers are given a world where friction has vanished. Grok 4.6 (high) lets the rule leak into simile and imagery so the premise governs the prose; grok-4.5-high states the rule and then breaks it in the closing image without accounting for the change.
  - Story 0093, `grok-4.6-high`:
    > The revelation washed over him like a tide without friction, smooth and all-encompassing, connecting every element of his life.
    The world-rule becomes the vehicle of a metaphor about understanding, so the premise does interpretive work rather than sitting as set dressing.
  - Story 0093, `grok-4.5-high`:
    > Finally he rose and descended the bluff with sure footing despite the lack of friction, carrying his revelations into the wider world.
    Restoring friction is described as a future capability he has only theorized; the final image grants him traction anyway, so the premise is contradicted at the moment of exit.
- **C048 — Magic that rehearses the act versus magic that performs it for you:** On the apology prompt, Grok 4.6 (high) uses the supernatural as a rehearsal that leaves the real act still to be done, preserving the moral weight of "unsent." grok-4.5-high uses the supernatural to retroactively send the letters, so the protagonist is relieved of the choice the story is about.
  - Story 0153, `grok-4.6-high`:
    > She would leave this place and find him, letters in hand, no longer unsent.
    The vision has changed her disposition, not the past; the apology remains a future action she must still take, which keeps the premise's cost intact.
  - Story 0153, `grok-4.5-high`:
    > The unsent letters transformed in the vision ink flowing free as she mailed them in that reclaimed second.
    The past is literally rewritten and the pack is "empty of those heavy unsent letters"; the required concept is dissolved rather than confronted, and the medium's aphorism "the past is clay when moon guides hand" makes the wish explicit.
- **C037 — Explanatory analogy (Grok 4.6 (high)) versus characterological analogy (grok-4.5-high):** Both writers are simile-heavy, but the figures do different jobs. Grok 4.6 (high)'s best comparisons clarify a concept the story depends on; grok-4.5-high's best comparisons define a temperament from the character's own occupational world. Neither mode is superior, and both writers also produce stock decoration.
  - Story 0331, `grok-4.6-high`:
    > Within its fibers resided analog memories, those pre-digital remnants of lived experiences, emotions, and narratives impressed upon the material through years of use, like vinyl records holding sound in grooves.
    The simile is the definition: it makes the story's central abstraction physically imaginable rather than merely atmospheric.
  - Story 0128, `grok-4.5-high`:
    > He carried a cautious exuberance that tempered his excitement with careful calculation, as if joy itself were a shipment requiring precise docking.
    The comparison derives from the character's trade, so an abstract required attribute becomes a specific habit of mind belonging to this man.
- **C061 — Figurative vehicles drawn from the story's own inventory versus from generic poetic stock:** Grok 4.6 (high)'s similes and metaphors tend to be sourced from materials already present in the fiction or from the character's profession, which makes them do characterizing work; grok-4.5-high's tend to be drawn from a shared lyrical reservoir (starlight, gold, tears, wildfire, rusty hinges) that could be transplanted into any of the packet's stories without loss.
  - Story 0006, `grok-4.6-high`:
    > Lena aligned the kelp shoot against the scarred root, matching cambium to cambium with the same care she used when checking a victim's pulse.
    A correct horticultural term is paired with a simile taken from the character's actual job, so the figure carries technical and biographical information at once.
  - Story 0329, `grok-4.6-high`:
    > At the orchard's center stood the oldest tree, its trunk split by a massive statue fused to it like a parasitic king.
    The vehicle ("parasitic king") encodes the story's political situation — an installed authority feeding on living things — rather than merely decorating the image.
  - Story 0329, `grok-4.5-high`:
    > In the end, beauty, once uprooted and free, would spread like wildfire of the soul.
    A stock vehicle, and one that fights the story's own logic, since fire and machinery are the antagonists elsewhere in the same fiction.
- **C003 — Courage as a way of moving:** Writer Grok 4.6 (high) interprets unused courage psychologically: it is discovered through tolerating uncertainty and accepting only intermittent support. Writer grok-4.5-high literalizes it as a destination inside a cave, making the quest more conventionally legible but less behaviorally exact. Grok 4.6 (high)’s version suggests a more mature account of agency because courage is enacted before it is recognized.
  - Story 0266, `grok-4.6-high`:
    > Unused courage, she began to sense, waited not in some distant cave but in the willingness to keep moving without a map.
    The sentence explicitly reverses the treasure-quest model. Courage resides in sustained conduct under uncertainty rather than in a hidden substance awaiting collection.
  - Story 0266, `grok-4.5-high`:
    > Deeper she found a still chamber where reflections showed not her face but visions of bold acts she had never claimed.
    > Here was the place where unused courage waits, patient for the seeker who arrives through indirect routes of heart and sea.
    The reflections connect courage to unlived possibilities, but the cave still externalizes and localizes the trait as the reward at the end of a route.
- **C009 — Preserved difficulty versus granted solutions:** Grok 4.6 (high) keeps the protagonist's goal partly out of reach and gives the required method real constraints to work against: in 0323 star navigation is a lost art recovered laboriously from "old manuals and simulated skies," and edge geometry must distribute water pressure before any tower can rise. grok-4.5-high tends to have the world hand the goal over: in 0323 the aliens simply display the star knowledge, and in 0095 the rival is disarmed "without causing injury thereby opening dialogue anew," converting conflict to friendship in one stroke. grok-4.5-high's communities, scholars, and pupils all agree and unify on first invitation, so the stories carry little causal or interpersonal friction. Grok 4.6 (high)'s worlds retain residue — erased town names, neighbors turned hostile, lonely aliens — that the ending does not dissolve.
  - Story 0323, `grok-4.5-high`:
    > His motivation remained pure to learn to navigate by starlight which the aliens had shown through glowing maps of distant skies.
    The assigned motivation is satisfied at the premise level: the skill the instructor wants to learn has already been demonstrated by the aliens, leaving no epistemic obstacle for the story to work against. Grok 4.6 (high)'s version of the same prompt makes the skill unattained and the aliens' message a source of difficulty rather than answers.
- **C036 — Higher ceiling and lower floor (grok-4.5-high) versus flat consistency (Grok 4.6 (high)):** grok-4.5-high produces the packet's single best-built sequence and also its most degraded prose, while Grok 4.6 (high)'s five pieces sit at a nearly identical level. Decisions based on average quality and decisions based on best work would diverge here.
  - Story 0128, `grok-4.5-high`:
    > The librarian in turn described a cargo broker who had quietly paid a boy's school fees after finding him asleep among crates.
    > Elias felt the locket photo grow warm against his chest and realized the broker mentioned was himself years ago
    A closed loop of obligation is enacted rather than asserted, and the protagonist learns it from outside himself — the strongest causal structure in either writer's work here.
  - Story 0266, `grok-4.5-high`:
    > There they paused so Mara could rest and consider all she had left behind after the leash breaks her free.
    The required phrase is jammed in without grammatical adaptation, producing a tense and sense collision; 0385 similarly loses comma control for long stretches.
  - Story 0128, `grok-4.6-high`:
    > Clara added that her father's locket photo had once motivated a young clerk to stay honest during hard times, closing another loop.
    Facing the same prompt, Grok 4.6 (high) reports the loop in summary and labels it, illustrating Grok 4.6 (high)'s steady mid-level rather than a peak.
- **C070 — Earned causal resolution versus element parade:** Grok 4.6 (high) builds chains in which the required method does mechanical work on a real threat, so the outcome follows from the setup. grok-4.5-high lists elements in sequence and absorbs obstacles instantly, with no resistance between threat and triumph.
  - Story 0078, `grok-4.6-high`:
    > Waves that might have broken the circle instead struck the fractal-tuned wood and produced chords of astonishing complexity.
    The cyclone's destructive force is converted by the specific method established earlier; the survival of the orchard is caused, not asserted. grok-4.5-high's version has obstacles "arrived first as floating crates then as uprooted mangroves" and, "Without hesitation," they join the orchestra, so nothing is ever at stake.
- **C030 — grok-4.5-high's under-credited systems imagination:** When the tone slot is empty, grok-4.5-high relaxes into concrete civic engineering that Grok 4.6 (high) only sketches. grok-4.5-high's reimagined civilization has logistics, while Grok 4.6 (high)'s remains at the level of contrasting slogans. This is substantive causal and social intelligence from the writer who elsewhere underperforms.
  - Story 0210, `grok-4.5-high`:
    > He mapped out systems for water collection using the natural cliffs, methods for cultivating resilient crops in the salty soil, and designs for workshops that taught craft over dependence.
    The revival is specified at the level of water, soil, and pedagogy; the civilization is conceived as functioning infrastructure rather than asserted as renewal.
- **C062 — Solitary interiority versus populated diffusion:** Grok 4.6 (high)'s stories reliably empty the frame until one figure faces an object, and locate meaning in unwitnessed inner residue; grok-4.5-high's reliably populate it and push the meaning outward into other people, institutions and future campaigns. Each writer's characteristic strength is the other's characteristic gap: Grok 4.6 (high) can render moral interiority but has no society to test it against; grok-4.5-high can stage social consequence but usually asserts rather than dramatizes it.
  - Story 0247, `grok-4.5-high`:
    > Shopkeepers once greeted him by name, but now their gazes slid past him without recognition.
    > Sailors who shared countless tales with him turned away as if facing empty air.
    grok-4.5-high converts the abstract timeframe "when no one remembers you" into observable social behaviour, something Grok 4.6 (high)'s version, which simply reports that Elias felt "utterly alone," never attempts.
  - Story 0167, `grok-4.5-high`:
    > Noctilucent reckonings solidified into plans for a community glass workshop.
    Private epiphany is turned into a transmissible institution — a move absent from every Grok 4.6 (high) story in the packet, which end with the insight retained by one person.
  - Story 0247, `grok-4.6-high`:
    > No one would remember Elias come morning but the music born from mapped silences would echo in the glow.
    Grok 4.6 (high) keeps the premise's cruelty intact and locates value in an unwitnessed artefact, refusing the social validation grok-4.5-high grants.
- **C035 — Endings shaped as stewardship-at-a-distance (Grok 4.6 (high)) versus absorption into community (grok-4.5-high):** Across prompts, Grok 4.6 (high)'s protagonists remain unnoticed custodians who resume their rounds; grok-4.5-high's protagonists dissolve into a group, a circle, or the place itself. This is a stable difference in the shape of desire rather than in competence, and it changes which tone words each writer can honor.
  - Story 0331, `grok-4.6-high`:
    > The observed solitude remained intact; the librarian's inner journey continued unseen by the browsing patrons, who pursued their own analog or digital paths to knowledge.
    Grok 4.6 (high) makes the required tone into the story's structural end-state: the discovery is deliberately not shared, preserving separateness.
  - Story 0110, `grok-4.5-high`:
    > Freed by honesty, the quiet night registrar felt integrated into the very essence of the place.
    grok-4.5-high resolves individuation into merger with setting and community, the recurring shape of grok-4.5-high's closes in 0110, 0128 and 0266.
- **C055 — Motifs that return as actions:** Grok 4.6 (high) more consistently reuses setting and objects as late actions that alter their meaning. An abandoned arcade game becomes a private fulfillment of absence; an hourglass grain physically enacts “the last.” grok-4.5-high often explains motifs instead, though grok-4.5-high’s blank envelope is an excellent exception.
  - Story 0033, `grok-4.6-high`:
    > One screen displayed a high score from years ago, a name he recognized as another absence, another unkept vow to come back and beat it.
    The arcade ceases to be atmospheric décor. Its obsolete score becomes another broken promise, and the mailman’s subsequent game turns his public vocation into a small personal rite.
  - Story 0143, `grok-4.6-high`:
    > He wound the hourglass once more, watching the special sand grain fall last of all, as if it too wished to linger in the dawning hush.
    The grain’s motion embodies the mission to photograph “the last” and joins timekeeping, loss, and reluctance to depart in one image.
  - Story 0033, `grok-4.5-high`:
    > Before departing, he paused to leave a single blank envelope on a counter, an invitation for more absences to be filled next time.
    This is grok-4.5-high’s strongest counterinstance: blankness simultaneously represents absence, possibility, and the next iteration of the mail route without requiring a large plot event.
- **C066 — Local pressure before explanation:** Grok 4.6 (high) more regularly turns a decorative image into a sequencing device. The resulting plots have better local pressure even when their supernatural premises remain arbitrary. grok-4.5-high more often explains that steps are deliberate or flawless rather than giving the scene an independent constraint.
  - Story 0038, `grok-4.6-high`:
    > That delicate construction would serve as her clock, for she must finish before the last thread was placed.
    The spider directly governs pace, later marks intermediate progress, and completes its web at the vault's opening. The timeframe therefore organizes the scene rather than remaining a repeated simile.
- **C022 — Compassion as a public protocol:** In 0128, grok-4.5-high understands “cycles of compassion” structurally: recipients become narrators and future givers, and no central benefactor can fully audit the network. Grok 4.6 (high) offers sharper ethical caution and more specific recognition, but its compassion remains largely an initiative designed by Marcus and Clara. grok-4.5-high’s version therefore shows stronger social imagination in this instance.
  - Story 0128, `grok-4.5-high`:
    > He explained how each person would recount one quiet favor they had received, then promise one they would give, creating a living loop that no ledger could fully track.
    The cycle is embodied in a repeatable rule that redistributes agency. The phrase about the ledger also productively limits the cargo broker’s habitual mode of control.
  - Story 0128, `grok-4.5-high`:
    > As the wind toyed with their hair and the stars wheeled overhead, a dockhand named Tomas spoke first of a librarian who had once fed him when storms closed the port.
    A supposedly “silent contributor” receives a name, a voice, and possession of the story rather than appearing only as the object of praise.
  - Story 0128, `grok-4.6-high`:
    > With cautious exuberance they greeted each other, aware that grand plans required careful steps to avoid overwhelming the humble recipients.
    Grok 4.6 (high) notices a subtle ethical danger that grok-4.5-high largely misses: public uplift can burden or patronize the people it intends to honor.
- **C078 — Epiphany wants a civic body:** grok-4.5-high more often pushes private perception toward institutions or shared material consequences. The glazier's insight becomes a workshop, while the debunker's discovery becomes a proposed technology for reclaiming communal land. This is projective social intelligence, although grok-4.5-high usually announces the public future rather than dramatizing the difficult work of creating it.
  - Story 0167, `grok-4.5-high`:
    > Noctilucent reckonings solidified into plans for a community glass workshop.
    > There people might learn to see beauty too.
    The revelation produces a concrete social form rather than remaining solely an enriched state of consciousness.
  - Story 0388, `grok-4.5-high`:
    > This power if shared would allow communities to reclaim the wastes and live free of lies.
    grok-4.5-high imagines knowledge as distributable infrastructure with consequences beyond the solitary discoverer.
- **C017 — Applying the theme back onto the protagonist's own method:** Given a story about transparency built on eavesdropping, grok-4.5-high notices the contradiction and makes the protagonist disclose his own surveillance as part of the cure; Grok 4.6 (high) notices nothing and pre-absolves her heroine. This is structural moral reasoning, and it appears in the rougher, more repetitive text — a reversal of the polish ordering.
  - Story 0110, `grok-4.5-high`:
    > These new drawings openly admitted his own eavesdropping actions and outlined the discovered secrets without filter.
    The theme (transparency frees) is applied reflexively to the investigator's own compromised method, so the resolution costs him something and the concept is tested rather than illustrated.
  - Story 0110, `grok-4.6-high`:
    > With the lens she could continue to eavesdrop responsibly, never for gossip but for healing.
    Grok 4.6 (high) states the exemption instead of dramatizing the problem; the surveillance is retroactively rebranded rather than disclosed, and Mira ends the story admired by the narration.
- **C004 — The cure leaves residue:** Story 0035 reverses the broader pattern. Writer grok-4.5-high more carefully tracks what subsuming contagious remorse costs the chef: the acquired memories remain bodily lodged and require continued isolation and processing. Writer Grok 4.6 (high) lets a touch of the bowl mark the contagion’s disappearance without establishing why that contact should end it. Here grok-4.5-high shows stronger causal aftercare.
  - Story 0035, `grok-4.5-high`:
    > Lira herself felt the weight of the subsumed remorse settle in her bones, a permanent addition to her collection of tasted memories.
    The communal cure does not erase conservation of emotional burden. Someone retains what has been removed or softened for others.
  - Story 0035, `grok-4.6-high`:
    > Touching the bowl he felt the last of the contagion fade, replaced by a fragile peace.
    The bowl provides a clean transition from contagion to peace, but the mechanism is asserted rather than developed from the established rules of touch transmission.
- **C011 — Sporadic conceptual daring at the edge of incoherence:** grok-4.5-high produces the packet's boldest conceit: a timekeeper who rediscovers the capsule by following messages he planted himself, so that method, object, and timeframe collapse into a loop. Read generously this is a bootstrap paradox perfectly matched to a story about time; read skeptically it is a causal muddle in which a character uses his own clues to find something he must already have located in order to plant the clues. grok-4.5-high pairs this with genuinely tactile imagination (time as woven strands, a map "sketched in ash from the urn"). Grok 4.6 (high)'s competing conceptual move in the same story — the catastrophe was perceptual rather than physical — is smaller but fully coherent, and Grok 4.6 (high) never risks a comparable leap anywhere in the packet. Originality and control each show up here, but not in the same writer.
  - Story 0216, `grok-4.5-high`:
    > As the borrowed-time timekeeper dug near the silo's foundation guided by his own planted words he unearthed the damaged time capsule.
    The sentence is either the packet's most original structural idea — a self-consulting message trail that turns the required method into a time loop — or its largest logic hole, and the surrounding text does not resolve which. The ambiguity itself is the datum: grok-4.5-high will risk incoherence for a conceit; Grok 4.6 (high) never does.
- **C081 — The object learns its own grammar:** In 0195, grok-4.5-high produces the packet's most convincing piece of relational surrealism. The marionette program does not merely provide generic magical instructions: it releases strings, and puppet manipulation becomes the physical grammar for sculpting possible futures. The invention feels motivated rather than random because object, action, method, and goal share one vocabulary.
  - Story 0195, `grok-4.5-high`:
    > With a soft click, he unsnapped the clasp, unleashing a cascade of ethereal strings that floated free.
    > Guided by the forgotten patterns, the knight manipulated the strings as if controlling invisible marionettes of potential.
    The literal strings convert an archival theater object into an operative model of agency and possibility.
  - Story 0195, `grok-4.6-high`:
    > He located an ornate lock on a cabinet of rare seeds and chose to unsnap it.
    > The unsnap released a puff of pollen that formed swirling images.
    Grok 4.6 (high) supplies a clear magical trigger, but the seed cabinet and pollen are less specifically connected to the marionette program's formal logic.
- **C010 — Relational particularity versus emblematic aggregates:** Grok 4.6 (high) populates the stories with named individuals (Lena, Elias, Mara Kane), inherited objects with working histories, and one-to-one encounter beats, including the packet's only direct question from a minor character ("One apprentice asked how they could ever see stars from so far below"). grok-4.5-high's figures remain generic titles — the philosopher, the timekeeper, the warden, the instructor, the scholar — and grok-4.5-high's social scenes involve aggregates that marvel, gather, and listen in unison rather than individuals with distinct positions. Grok 4.6 (high)'s objects arrive with lineage that encodes family time and gives the required item a job inside the scene; grok-4.5-high's objects function as tools or symbols introduced at the moment of use.
  - Story 0258, `grok-4.6-high`:
    > She retrieved the measuring tape from an old wooden drawer, an antique brass instrument that her grandmother had used decades ago to lay out ritual spaces with absolute precision.
    The required object carries provenance, material specificity, and a prior use that explains its present function in organizing the card spread. No comparable layering attaches to grok-4.5-high's version of the same object, which is introduced bare as "a weathered measuring tape."
- **C069 — Mathematics without constraint:** Both asylum stories use mathematical language as an authority signal rather than substantive reasoning. No equation constrains a decision, reveals an unfair distribution, or forces the protagonist to confront incommensurable values. “Fair trade” is effectively the desired verdict dressed as calculation.
  - Story 0139, `grok-4.6-high`:
    > As she wrote the petition for political asylum, she simultaneously solved for the variables in her fairness equation: time invested versus lives potentially saved.
    The variables are named, but no values, uncertainty, weighting principle, or conflict between them enters the plot.
  - Story 0139, `grok-4.5-high`:
    > His deepest motivation remained to find the mathematics of a fair trade that could balance truth for safety in perfect equity.
    “Mathematics” and “perfect equity” confer confidence without specifying what truth is traded, who bears the risk, or how equity could be demonstrated.
- **C050 — Social and political concreteness is present in both and stable in neither:** A conventional read would credit grok-4.5-high with richer world-building because grok-4.5-high stages factions, exploitation risk, and knowledge distribution. But Grok 4.6 (high) supplies the sharpest political image in the packet, and on another prompt the positions reverse: Grok 4.6 (high)'s protagonist acts on his discovery while grok-4.5-high's merely files it. The difference is not consistent enough to attribute to either writer.
  - Story 0205, `grok-4.6-high`:
    > He had once rallied the miners and artisans against the Time Lords who rationed the newly visible chronology, but the revolt crumbled when the lords unleashed storms of raw time.
    Named class actors plus a concrete mechanism of domination (rationing a newly material resource) — more specific political imagination than grok-4.5-high's "a grand revolution that sought equality among the stellar outposts."
  - Story 0093, `grok-4.5-high`:
    > His elusiveness came from years of avoiding those who would exploit the changed physics for conquest.
    grok-4.5-high motivates the character attribute through a political hazard and later raises the distribution question ("share the knowledge selectively, teaching those pure of intent") — a dimension Grok 4.6 (high)'s version of the same character omits.
- **C027 — Ideas given social addresses:** Grok 4.6 (high) embeds beliefs in groups with interests, so the prompt's abstract "competing narratives" acquire political causality: an elite narrative of purification versus a working-class narrative of cover-up. grok-4.5-high's narratives are unattributed, spoken by nobody, which makes the conflict conceptual rather than social.
  - Story 0068, `grok-4.6-high`:
    > A competing narrative circulated among the remaining dockworkers, claiming that seafaring merchants had opened floodgates to cover their own infections and thefts.
    The narrative has a bearer, a motive, and a class position; belief becomes sociologically caused rather than decoratively present.
  - Story 0068, `grok-4.5-high`:
    > Some say the sea rose in punishment; others claim engineered flood to end the plague.
    "Some" and "others" are anonymous voices; the competing narratives exist as required content but explain nothing about who needs which story and why.
- **C074 — Metabolizing required elements versus displaying them:** Grok 4.6 (high) often converts an abstract required action into a concrete practice with mechanics, while grok-4.5-high often satisfies the element by naming it. The difference is inconsistent and reverses in at least one story.
  - Story 0078, `grok-4.6-high`:
    > He took the raw noise of rising gale and overlaid it with the resonant frequencies he had awakened, like a sailor overdubbing a shanty upon the crash of surf.
    The action "dub" becomes actual overdubbing that fuses storm noise with tuned resonance, driving the climax. grok-4.5-high's treatment is "He chose to dub this new composition the Eternal Tide Song," reducing the action to giving the piece a title.

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0004 | +2.900 | 685 | 794 | 3 | 1.800 |
| 0006 | +3.583 | 740 | 763 | 3 | 0.833 |
| 0033 | +1.250 | 722 | 704 | 3 | 1.500 |
| 0035 | -2.167 | 669 | 785 | 3 | 0.333 |
| 0038 | +2.250 | 675 | 761 | 3 | 0.500 |
| 0048 | +2.750 | 627 | 791 | 3 | 0.833 |
| 0064 | +1.333 | 680 | 728 | 3 | 1.667 |
| 0068 | +4.217 | 641 | 765 | 3 | 0.567 |
| 0077 | -0.167 | 768 | 656 | 3 | 3.200 |
| 0078 | +3.500 | 666 | 643 | 3 | 0.333 |
| 0093 | +1.717 | 697 | 750 | 3 | 0.567 |
| 0095 | +1.667 | 606 | 733 | 3 | 1.000 |
| 0100 | +2.750 | 667 | 628 | 3 | 0.500 |
| 0103 | +2.417 | 754 | 752 | 3 | 1.500 |
| 0110 | +3.050 | 718 | 773 | 3 | 1.233 |
| 0128 | -2.817 | 697 | 763 | 3 | 1.700 |
| 0138 | +3.133 | 698 | 731 | 3 | 1.733 |
| 0139 | +2.417 | 774 | 722 | 3 | 0.167 |
| 0143 | +3.717 | 786 | 744 | 3 | 1.567 |
| 0153 | +2.750 | 686 | 737 | 3 | 0.500 |
| 0167 | +2.433 | 659 | 689 | 3 | 0.667 |
| 0177 | +3.300 | 610 | 640 | 3 | 0.733 |
| 0180 | +1.917 | 693 | 725 | 3 | 1.500 |
| 0195 | -2.000 | 658 | 737 | 3 | 0.333 |
| 0197 | +1.633 | 722 | 738 | 3 | 1.600 |
| 0201 | +1.467 | 713 | 732 | 3 | 1.933 |
| 0205 | +2.833 | 615 | 707 | 3 | 0.667 |
| 0210 | -2.000 | 763 | 777 | 3 | 0.333 |
| 0216 | -2.700 | 721 | 797 | 3 | 0.400 |
| 0236 | -2.717 | 669 | 783 | 3 | 0.900 |
| 0247 | -0.050 | 744 | 716 | 3 | 2.433 |
| 0249 | +2.000 | 704 | 728 | 3 | 0.000 |
| 0258 | +3.000 | 740 | 730 | 3 | 1.333 |
| 0266 | +2.967 | 623 | 791 | 3 | 0.600 |
| 0278 | +2.133 | 603 | 736 | 3 | 0.400 |
| 0281 | +4.417 | 646 | 722 | 3 | 0.833 |
| 0292 | +3.167 | 695 | 793 | 3 | 0.667 |
| 0295 | +2.667 | 688 | 734 | 3 | 1.000 |
| 0310 | +4.333 | 659 | 702 | 3 | 0.667 |
| 0313 | +2.500 | 739 | 765 | 3 | 0.667 |
| 0321 | +2.833 | 662 | 724 | 3 | 0.533 |
| 0323 | +3.667 | 769 | 746 | 3 | 2.000 |
| 0329 | +2.967 | 643 | 717 | 3 | 0.600 |
| 0331 | +1.750 | 668 | 740 | 3 | 1.500 |
| 0332 | +3.667 | 709 | 634 | 3 | 0.667 |
| 0350 | +3.217 | 665 | 776 | 3 | 0.900 |
| 0361 | +3.583 | 650 | 790 | 3 | 0.500 |
| 0385 | +1.700 | 710 | 733 | 3 | 1.933 |
| 0388 | +2.300 | 766 | 751 | 3 | 0.933 |
| 0391 | +2.417 | 746 | 791 | 3 | 0.633 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-xhigh`, `gpt-5.6-high`, `kimi-k3`.
Synthesis editor: `kimi-k3`. Verified subjective claims: 87.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
