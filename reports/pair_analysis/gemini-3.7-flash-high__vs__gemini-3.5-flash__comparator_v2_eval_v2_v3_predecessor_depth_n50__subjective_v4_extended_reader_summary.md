# Gemini 3.7 Flash (high) vs. Gemini 3.5 Flash: comparative writing analysis

Focus model: `gemini-3.7-flash-high`. Comparison model: `gemini-3.5-flash`. Direct-comparison scope: `comparator_v2_eval_v2_v3_predecessor_depth_n50`.

## In one paragraph

Given the same short-fiction prompts, Gemini 3.7 Flash (high) and Gemini 3.5 Flash write in nearly the same lush, allegorical voice, but they do different work with the required ingredients. Gemini 3.5 Flash sets each assigned object out like a labeled exhibit and has the narrator pronounce its meaning; Gemini 3.7 Flash wires the same objects into the plot's machinery, so a grain of hourglass sand starts a chemical timer and a mending ribbon is designed to fray on schedule [C007]. The sharpest contrast is what each does with loss: asked to resolve a death hidden in an archive, Gemini 3.7 Flash scatters the dead engineer's confession through thousands of forgotten songs where no purge would think to look, while Gemini 3.5 Flash clicks "restore" and brings the lost sister home [C001]. That reflex repeats at endings — Gemini 3.5 Flash certifies peace, mastery, and reunion, once flatly contradicting its own premise of impermanence, while Gemini 3.7 Flash keeps the cost on the books and lets consequences travel outward to strangers [C014]. Gemini 3.5 Flash does sometimes land the bolder single concept, such as a mind that sees past and future but not the present [C080]. The everyday difference, though — parable announced versus mechanism watched turning — recurred across fifty shared prompts, and it favors Gemini 3.7 Flash.

## Quantitative context

Across 50 matched prompts, the focus model recorded 40 wins, 6 ties, and 4 losses at the ±0.5 tie threshold. Its mean signed margin was +1.586 ± 0.346 (95% normal half-width).

Mean lengths were 706.2 and 668.5 words; the correlation between length difference and margin was +0.142.

## Comparative portrait

All three panel analysts, across fourteen blinded packets, describe the same starting point: these are two writers working one house idiom — lush allegorical fantasy, long declarative paragraphs, every required element visibly seated, a closing benediction. Surface differentials are small (mean 706 vs 669 words; polish, vocabulary, and confidence repeatedly rated comparable), and image-level invention is essentially a wash — one packet analyst found both writers independently reaching for the same props on the same prompts (velvet coin pouches, grandfather keepsakes, crystalline ferns, hedgehog vigils), and the per-story evaluator records echo this with near-identical scaffolding in pairs like 0006 and 0329. Both writers paste prompt language verbatim and both gloss their own symbols after dramatizing them [C017][C024][C083].

The recurring, panel-supported difference is what the prose does in the second and third sentences after an element arrives. Gemini 3.7 Flash (high) operationalizes: required objects become triggers, prerequisites, and jobs inside a causal chain [C007][C026][C039][C046][C055][C065][C071]. Gemini 3.5 Flash interprets: the same elements arrive as emblems whose significance the narration announces [C034][C065]. The newer model's objects carry provenance and obey the story's own stated doctrine [C011][C027]; the older model's objects are keepsakes rooted in family transmission, with meaning narrated rather than enacted [C018][C057]. One analyst's compressed formula — one writer builds small machines that produce parable as a byproduct, the other tells parables with the elements placed like labeled exhibits — is corroborated by every other reader.

The divergence extends to endings and social topology. The newer model's endings tend toward custody rather than recovery, resumed work rather than sealed verdicts, costs kept on the books rather than refunded [C001][C008][C014][C029][C036][C043][C090]; its worlds contain second parties who refuse, object, and act on their own reasons [C023][C032][C037][C070][C075], and its wounds have identifiable institutional content [C020][C059]. The older model more often restores the lost thing, certifies the emotional settlement, and ministers to passive recipients — with a narrator that pre-rates its own material [C074]. This is corroborated independently: the evaluator notes for the largest focus wins (0231, 0271, 0283, 0395) repeatedly cite element integration and earned closure as the deciding factor.

Cohort check: the portrait formed in the original cohort (18/2/0, mean margin +1.961) replicates in direction in the extension (22/4/4, +1.337). The material change is attenuation, not reversal: the margin shrank by roughly a third, and all four comparison wins appear in the extension. Those four wins map one-to-one onto documented claim-level reversals [C052][C062][C068][C080], so the extension qualifies the original portrait's edge rather than overturning its center.

## Does either model seem smarter?

Treated strictly as a reader impression manifested through writing choices — never as a measurement of general intelligence — the answer from the panel is yes, and it is unusually specifiable. Twelve of fourteen packet readings land on the newer model, and they name mechanisms rather than vibes:

- **Causal and structural foresight.** Events have prerequisites; methods exist because the world first presented an obstacle; intermediate states are shown, not skipped [C007][C003][C046][C085]. Risk is enacted and corrected on the page rather than announced in the abstract [C073].
- **Relevant-detail selection.** The newer model repeatedly chooses the one detail that discharges several obligations at once — a planted absence later filled, a final image whose materials gather several story systems, component nouns that turn out to be load-bearing [C016][C006][C077].
- **Constraint synthesis.** Two or three required elements collapse into a single functioning image, so the brief disappears into event [C071][C046].
- **Epistemic conduct.** Doubt has procedural consequences; skepticism survives contact with evidence as a revised position rather than dissolving into wonder; the narration distinguishes what a character proved from what a character felt [C047][C019][C081]. The older model's narration certifies with absolutes ("absolutely undeniable") where the newer model leaves a live disjunction [C086].
- **Reader trust.** The newer model more often ends on a consequence in the world and lets the state be inferred; the older model pre-rates its images and pronounces the settlement [C014][C074][C090].

What does *not* drive the impression: verbosity (the word-count gap is +37.7 and its correlation with margin is only +0.142), polish (rated matched by all three analysts), or technical diction, which every analyst flags as a proxy risk precisely because the newer model's mechanisms are sometimes pseudo-physics [C035][C056][C077].

Psychological inference is genuinely split, and this is where the minority readings live. The newer model shows the stronger social-moral psychology — implicated protagonists, reciprocal blame, care that permits refusal [C020][C032][C059][C023] — but the older model shows the sharper somatic psychology and a distinctive willingness to plant impure, self-interested motives inside pious projects [C088][C040][C053]. Conceptual compression also cuts both ways: the older model owns several of the boldest single conceptions in the entire evidence set [C080][C068], while the newer model's compression is steadier and structural [C071][C012].

Two minority positions are well supported and must be preserved. One analyst (read_09) found no aggregate winner at all: different intelligences, with the packet ranking flipping per prompt — the older model reflexive and paradox-holding, the newer model procedural and institutional [C053][C058]. Another (read_03) found the newer model's material-literacy advantage concentrated in the naturalistic premises and near zero in the frankly magical ones, where both hand-wave [C013][C035]. A third (read_12) found no stable maturity difference, because the newer model's competence-endings sometimes cure the very tension the prompt requested [C076].

Cohort check: the impression replicates but weakens — extension margin +1.337 versus +1.961 — and the extension was *less* noisy, not more (evaluator disagreement 0.606 vs 0.806; order sensitivity 0.687 vs 1.052). The smaller extension gap is therefore not an artifact of more contentious judging; it is a genuinely narrower, still-clear advantage.

## Narrative reasoning and aesthetic judgment

The newer model's narrative reasoning shows four checkable behaviors. First, causal joints: mechanisms pass through visible intermediate states — liquid shifts a cradle, a catch releases — rather than leaping from trigger to wished-for revelation [C003]. Second, premise-to-operation derivation: a speculative rule yields a specific, counterintuitive action that could only follow from that rule, and the rule then constrains behavior consistently [C085][C072]. Third, setup discipline: a specified vacancy planted early is filled structurally at the climax, so required concepts arrive as payoff rather than exposition [C016]. Fourth, doctrine-object alignment: the props enact the story's own philosophy, where the older model's props sometimes contradict it within paragraphs [C027]. Metaphor auditing — checking whether an assigned image's real formation process supports its meaning — is the subtlest version of the same behavior [C013].

Aesthetic judgment diverges most consequentially at the ending. The newer model's ethic is custodial: testimony is distributed and witnessed rather than the dead restored; healing is tempering rather than erasure; compromised machinery is jammed and rerouted rather than shattered; wisdom is purchased by self-revision instead of delivered intact [C001][C009][C021][C010][C028]. The older model's aesthetic is restorative and declarative: recovery equals reunion, the final sentence announces the settlement — twice contradicting the story's own premise, as when "temporary eternity" ends "forever preserved" [C014]. Both models' aesthetic failures are also shared and real: asserted rigor standing in for content [C038][C056], metaphors promoted into verdicts [C083], and totalizing finales that scale one victory into world renewal [C051][C064].

On opposition, the newer model's antagonists act on traceable incentives [C066] and its institutions behave like institutions [C054] — but with two documented reversals: the older model once persuades with political reasons where the newer model shortcuts with a mind-altering vapor [C082], and the older model is the only one that builds jeopardy architecture at all, even though its threats never engage [C089].

Cohort check: every one of these behaviors is documented across multiple packets and all three analysts, and the story-level judging in both cohorts independently rewards them; nothing in the extension record contradicts them. The extension's four losses instead confirm the panel's reversal notes — see the next two sections.

## Range, recurring habits, and floor versus ceiling

**Range.** No supportable difference exists in genre, realism, humor, or formal ambition. Both writers are conventional — no fragmentation, no unreliability, no formal experiment from either (panel consensus, all three analysts); both domesticate absurd premises into solemn cosmology; the comic register appears essentially once per writer. Shared attractors are striking: both independently invented a lost sister's laughter for the same prompt, and both closed a matched pair with a near-identical sentence about a brook's eternal journey. This is a prompt-dependent, checklist-saturated mode that suppresses whatever range either model might otherwise have.

**Recurring habits, newer model:** thesis-statement endings that summarize rather than add information [C058]; gadgetry and pseudo-precision that can be costume rather than thought [C003][C077]; a formulaic "not X, but Y" negation aphorism [C019]; dense unbroken paragraphs that flatten climaxes; and attribute migration — relocating a required trait onto an object or surveillance agent, gaining irony while weakening literal compliance [C005].

**Recurring habits, older model:** certainty markers that forbid doubt by fiat [C086]; narration that pre-rates its own material [C074]; prompt seams — tense wobble and an unabsorbed slot label — exactly where required text enters the sentence [C031][C026]; required tones named as tones [C034]; and a terminal gesture of keeping, pocketing, possessing where the newer model releases, circulates, or discards [C057][C084].

**Floor versus ceiling.** The evidence supports a lopsided conclusion, stated plainly: the newer model has the clearly higher floor, and its median margin (+2.083) is larger than its mean, meaning the typical pair is more decisive than the average. The older model's four wins are real but concentrated and explicable — each is a prompt-fit case involving epistemological doubt, an unresolvable condition, or ecological revelation [C052][C062][C068][C080]. One analyst (read_11) described the older model as owning its packet's highest single peak while the newer model owned the higher floor across all five; the full record supports the floor claim robustly and the peak claim only locally — the four wins are documented successes, not evidence of a generally higher ceiling, and the record does not justify manufacturing one. This pattern is a **new, extension-cohort finding**: the original cohort contained zero comparison wins, so the earlier portrait understated how often the older model can simply be better on a given prompt.

## What each model still does better

**Gemini 3.5 Flash, recurring and corroborated:** somatic embodiment — load, torque, posture, a spine matched to bent wood [C088][C040]; verb-slot fusion, collapsing required act and method into one gesture [C030]; finding and keeping the friction between two contradictory assigned elements [C015]; constructing genuinely alien cognitive premises [C080]; holding assigned dissonance open to the last line [C052]; keeping an unresolvable attribute operative at the end where the newer model cures it [C076]; refusing absolution while permitting action [C048]; and noticing that forced intimacy need not culminate in self-annihilation [C050]. **One-story observations (labeled as such):** the premise-selection coup of a terrestrial crater about to be bulldozed into a fake moon [C091]; the ecological revelation where human apparatus fails and the nonhuman world supplies the pattern [C062]; the inquiry actually dramatized in real time rather than reported [C022]; persuasion through incentives rather than enchantment [C082]; and the single best figure for absence in either body of work, a room where a grandfather clock had recently stopped [C033].

**Gemini 3.7 Flash (high), recurring and corroborated:** the structural complex detailed above, plus institutional and logistical imagination [C054][C079]; trade-accurate domain retrieval [C077]; reciprocal blame geometry [C059]; custody ethics for dangerous testimony [C001]; worlds populated with agents who resist [C037][C075][C070]; gifts that recipients may decline [C023]; bodily symptoms that alter the route [C078]; empathy as diagnosis and repair rather than soothing [C063]; rest imagined as a durable address rather than expulsion [C060]; counterfactual hospitality toward minor lives [C061]; and explanatory closure about why legends self-seal [C042].

**Prompt-dependent qualification:** the newer model's material-auditing edge is concentrated in naturalistic premises and shrinks sharply in frankly magical ones, where both hand-wave equally [C013][C035]; the older model's verb-fusion and embodiment edges appear only where the prompt supplies actions and bodies [C030][C088].

## Findings beyond the existing judging

The supplied per-story judging mostly rewarded integration and craft; the packet analyses surfaced dimensions for which ordinary rubrics have no vocabulary:

1. **Who is permitted to possess closure.** The newer model's protagonists recede behind what they preserve; the older model's receive confirmation and keep the relic. Custody-versus-recovery is an ethics of information afterlife, not a plot preference [C001][C036][C043].
2. **Compliance temperament.** Both writers paste required phrases, but the newer model migrates attributes onto objects (thematic irony, weakened literal compliance) while the older model keeps the trait on the protagonist and exposes the seam [C005][C031][C026]. A checklist judge scores both compliant and misses the trade.
3. **Terminal gestures.** Pocketing versus releasing; securing versus circulating [C057][C084].
4. **Reveal semantics.** For the older model a reveal is a verdict about moral character; for the newer model it is a function or a roster — verdicts end conversations, rosters start them [C067].
5. **Countable tells.** Certainty adverbs and an installed admiring audience in the older model's narration [C086][C074]; a permitted gap between narrator and protagonist, where virtue is characterized as a tic, in the newer [C087].
6. **Provenance split.** Objects inherit from grandfathers in the older model, from strata and defunct infrastructure in the newer — one habit generating most of what readers would otherwise call "voice" [C018].
7. **Shared substitute epistemology.** Both writers let texture — moss, mica, vibration — stand in for proof, and both convert suggestive absences into unearned certainty [C024][C083][C002].
8. **A synthesis-level finding enabled by the cohort data:** the extension's four comparison wins correspond exactly to the four stories where claim-level reversals were documented [C052][C062][C068][C080]. The earlier portrait's minority notes were predictive, not noise.

Two further observations are **speculative (low-confidence)**: that the newer model inverts prompt images rather than illustrating them [C044], and that its payoffs radiate outward as a values difference [C045] — each rests on few instances and is preserved here as a hypothesis, not a finding.

## Disagreements and limitations

**Panel disagreement.** The strongest minority position (read_09) rejects any aggregate winner, locating the older model's intelligence in reflexive endings and impure motives and the newer model's in procedure, with rankings flipping per prompt [C053][C058]. Read_03 limits the newer model's edge to naturalistic premises [C013]. Read_12 finds no stable maturity difference and documents the newer model's competence-endings canceling requested tension [C076]. These are preserved as live minority readings, not resolved away.

**Story-level disagreement.** Story 0241 is contested: one packet found the older model's real-time traversal structurally superior [C022], while the evaluator and another packet favored the newer model's conceptual distinction between expected loss and purchased agency [C025]. Story 0035 splits the record: the evaluator preferred the older model's character-bound contagion constraint while the packet favored the newer model's tempering ethic [C009]. Story 0047 was judged a near-tie despite two strong packet claims favoring the newer model [C020][C023]. In 0139, neither writer dramatized the persuasion both required [C069].

**Taste-dependence.** The preference for open endings, distributed consequence, and visible cost is itself a literary taste; a judge favoring parable closure or mythic clarity could reasonably score the same evidence for the older model, and grimness is a known maturity proxy [C008][C029][C043][C021].

**Surface-cue sensitivity.** Several findings are explicitly proxy-adjacent: technical lexicon [C035][C056][C077], hedging vocabulary [C086], and length all risk masquerading as thought; the claims survive only where a mechanism demonstrably constrains an outcome. The newer model's own physics is documented as wrong in places [C085][C077].

**Shared failure modes cap every comparative claim:** both over-explain [C024], both totalize their finales [C051][C064], both assert rigor they do not demonstrate [C038], both leave prompt phrases grammatically stranded [C017], and neither produces supportable humor, ambiguity, or formal experiment.

**Statistical limits.** The cohort attenuation is suggestive, not proven — the 95% intervals overlap (original 1.53–2.39; extension 0.85–1.82). Order sensitivity (0.833) is about half the mean margin, so presentation order moves scores materially. Several packet-level claims rest on single stories and are labeled as such [C068][C091][C062]; one analyst's largest "smartest" claim depended heavily on one story with dialogue.

## Representative case studies

**Story 0395 (focus +2.667) — the central pattern in one pair.** Facing a surveilled archive, the newer model's archivist duplicates a dead engineer's confession across three thousand forgotten songs, making testimony harder to erase without pretending the loss is reversed; the older model's protagonist clicks "restore" and brings his sister home, bypassing every problem the premise raised [C001][C036]. The same pair shows attribute migration (the required brightness assigned to the corporate surveillance avatar) and the implicated-versus-innocent protagonist split [C005][C032]. The evaluator's notes independently confirm the tonal collapse of the restore ending.

**Story 0180 (focus +2.417) — doctrine obeyed versus doctrine contradicted.** Both stories preach that vows should be deciduous. Only the newer model's repair is designed to fray, and its wisdom is generated by the daughter's opposition — the father is wrong for most of the story and is corrected — while the older model's narration praises its ribbon as unyielding moments after the letting-go lecture and labels a prepared speech "accidental wisdom" [C027][C010][C028].

**Story 0231 (focus +2.917) — two architectures of absence.** Instructed to investigate by observing gaps, the newer model renders social non-events across a lifetime (an untouched shoulder at a festival, an empty wedding chair) and makes the central object an ungiven gift; the older model finds forensic traces of presence and then abandons the method for an announced psychic talent [C033]. This pair is the panel's length control — the stories are close in length, so the difference cannot be attributed to room [C033]. The older model's boot-print interval is genuinely sharper clue-reading, a preserved minority point [C002].

**Story 0177 (−1.617, extension cohort) — the older model's cleanest win.** "Foresight hindsight only" becomes a mind that perceives past and future but not the present — a constraint that governs the plot and earns its resolution — while the newer model reads the same phrase as ordinary belated insight [C080]. The evaluator agreed. This is a one-pair observation but corroborated by two independent readers.

**Story 0098 (−1.400, extension cohort) — doubt kept open.** Only the older model honors the assigned luminous doubt past the climax, ending on a self-undermining pragmatism about functional truth; the newer model raises the doubt and discharges it into affirmation [C068]. One analyst called this the packet's highest peak; it is also evidence for the minority "flips per prompt" position.

**Story 0241 (+2.083) — the live disagreement.** The packet record says the older model's enacted, real-time investigation is the better structure [C022]; the evaluator record and a cross-read say the newer model's retrospective account contains the more discriminating concept — agency knowingly purchased at negative expectation [C025]. The margin favors the newer model; the structural argument favors the older. Unresolved.

**Story 0283 (+2.750) — transformation versus rupture, with a taste caveat.** The newer model jams the deterministic hourglass into plural, irregular streams; the older model shatters it [C021]. The panel judged transformation the more structurally intelligent response while explicitly noting that shattering may be the more honest answer to a coercive order — a preference a different reader could reverse [C021].

**Story 0146 (+1.917) — a sub-dimension reversal inside a focus win.** The older model found the friction the prompt offered — colliding "infinitely patient" with a live deadline — while the newer model relocated the collapse into backstory and dissolved the tension [C015]; the evaluator credited the timeframe framing too, yet the newer model won the pair on other axes. Useful precisely because it shows the aggregate pattern coexisting with prompt-local older-model victories.

## Cited claim ledger

- **C017 — Prompt-phrase assimilation failures are symmetrical:** Both writers must absorb present-tense required phrases into past-tense narration, and both solve it once by writing the whole story in present tense and fumble it once by leaving the phrase grammatically stranded — on opposite stories. This blocks any competence-level claim about formal control and suggests attention allocation rather than skill difference.
  - Story 0228, `gemini-3.5-flash`:
    > This morning, after the mirror cracks in his dilapidated studio, he knows the designated hour has finally arrived.
    Gemini 3.5 Flash writes 0228 entirely in present tense, so the required phrases "after the mirror cracks" and "a wrong turn leads to a hidden oasis" become grammatical rather than intrusive.
  - Story 0228, `gemini-3.7-flash-high`:
    > His routine had shifted irrevocably only after the mirror cracks in his seaside attic, shattering during a sudden autumn gale
    Gemini 3.7 Flash (high) keeps past narration and the borrowed present-tense clause sits unassimilated inside a pluperfect sentence — an audible seam.
  - Story 0263, `gemini-3.5-flash`:
    > Because she hears unspoken words, she captured the silent, desperate thoughts of the village sleeping below.
    Here Gemini 3.5 Flash commits the mirror-image error — present-tense attribute welded to a past-tense main verb in one sentence — while Gemini 3.7 Flash (high)'s 0263 is written in present tense throughout ("Here stands Kaelen, a moonstruck dreamer...") and absorbs the phrase cleanly.
- **C024 — Meaning is pre-chewed:** Both writers frequently explain an image after the action has already made its intended significance clear. Their narrators convert metaphor into an endorsed thesis, reducing ambiguity and limiting the reader’s interpretive participation. This shared habit is more consistent than most differences between them.
  - Story 0256, `gemini-3.5-flash`:
    > By challenging her belief that unity required perfection, his powerfully gentle intervention had guided her to the raw, beautiful truth of human existence.
    The sentence restates the preceding dialogue, bell strike, bodily vibration, and change in Mara’s posture. It supplies a universal conclusion where the scene had already conveyed a more particular experience.
  - Story 0256, `gemini-3.7-flash-high`:
    > She had dismantled the illusion of distance by proving that harmony was a shared physical skin, tactile and alive.
    Gemini 3.7 Flash (high) likewise declares what the experiment proved, converting a suggestive collective sensation into a closed doctrine of harmony.
- **C083 — Metaphors promoted into verdicts:** Both writers repeatedly turn an organizing metaphor into conclusive evidence. Love acquires an exact frequency; mercy becomes an equation that resolves to zero. This produces clean thematic architecture but weakens ambiguity, especially where trauma or intimacy should exceed the model used to describe it. The shared habit prevents a strong claim that either writer is consistently more mature or restrained.
  - Story 0281, `gemini-3.5-flash`:
    > The image proved that even without the telepathy pills, their bodies had remembered the exact frequency of their love, mapping it in the air with absolute clarity.
    Physiological synchrony is elevated from suggestive artwork to definitive proof, bypassing alternative explanations and the skeptic’s legitimate reservations.
  - Story 0201, `gemini-3.7-flash-high`:
    > In that quiet realization, the heavy accounting of his torment resolves into zero, canceling the systemic ledger of his torturers forever.
    Gemini 3.7 Flash (high) converts a moment of endurance into total psychic and moral cancellation, giving a single insight implausibly complete authority over systemic trauma.
- **C007 — Required elements as machinery rather than inventory:** In Gemini 3.7 Flash (high), mandated elements become causal prerequisites of one another: the silence between lightning and thunder is the reason the encoded signal reaches the ghost; gravity pockets are the physical mass of deleted memories; the binary stars' mutual dimming is the decoding principle. In Gemini 3.5 Flash the same elements are present and vividly rendered but discrete — the lightning-thunder hush is merely when Pip happens to move, and the thunder afterward decoratively seals "the magical circuit forever." The difference recurs across all five prompts and is the strongest single separator.
  - Story 0034, `gemini-3.7-flash-high`:
    > That lingering hush between flash and detonation created an atmospheric vacuum where light signals could penetrate deep into the foundation channels without interference.
    The required timeframe is made load-bearing: without the hush, the method fails. Gemini 3.5 Flash's version of the same beat — "In the suspended pocket of absolute silence between lightning and thunder, Pip moved with breathless, rhythmic precision" — uses the interval as stage lighting. Likewise Gemini 3.7 Flash (high)'s 0380 makes the required gravity anomalies identical to the core concept: "The excised memory had not vanished into oblivion; it had simply gathered mass, sinking under its own unresolved sorrow into the salt below the town."
- **C026 — Load-bearing elements versus label compliance:** Gemini 3.7 Flash (high) assigns required elements causal jobs while Gemini 3.5 Flash more often pastes them in as narration, once leaking the prompt's own field label. Gemini 3.7 Flash (high)'s objects come with provenance, deadlines drive scenes, and required actions occur inside mechanisms. Gemini 3.5 Flash's elements are frequently announced rather than used, and the required action can be outsourced to scenery.
  - Story 0180, `gemini-3.5-flash`:
    > The bitter timeframe after the breach of contract had left the valley below hostile and suspicious
    The prompt's slot label timeframe survives unabsorbed into the prose, a direct artifact of slot-filling rather than assimilation into scene logic.
  - Story 0379, `gemini-3.7-flash-high`:
    > Between her fingers, Mara turned an aged locket of tarnished silver, recovered from an estate trunk sold to her shop three days prior.
    The crucial object's presence is explained by the protagonist's own profession; Gemini 3.5 Flash's parallel locket arrives unexplained even though the curator trade would explain it for free.
  - Story 0317, `gemini-3.5-flash`:
    > Through the open window, he watched the brook flow over smooth stones, its steady current reflecting the starlight.
    The required action flow is fulfilled by background scenery, whereas Gemini 3.7 Flash (high) places flow inside the lock mechanism itself as oil shifting a counterweight, making the element functional.
- **C039 — Required objects are load-bearing parts, not emblems:** Across the packet Gemini 3.7 Flash (high) more often wires the furnished object into the story's causal skeleton, so the plot could not run without it, while Gemini 3.5 Flash sometimes parks the object as a symbol whose meaning is narrated rather than enacted. In 0143 Gemini 3.5 Flash's hourglass grain sits in a locket as a silent anchor in a world racing toward the stars; Gemini 3.7 Flash (high)'s grain physically starts the timer. In 0006 Gemini 3.5 Flash's coin merely tensions the graft while wind makes the song; Gemini 3.7 Flash (high)'s coin becomes the striker that lets the scar sing.
  - Story 0143, `gemini-3.7-flash-high`:
    > Coated in reactive silver salts, that quartz particle broke the meniscus of the reagent when dropped into the chamber, initiating the timed countdown for the shutter mechanism.
    The required sand grain is the trigger of the chemical timing method; remove it and the photograph cannot happen. Causality, not ornament.
  - Story 0006, `gemini-3.7-flash-high`:
    > Fire had carved an acoustic chamber out of agony, and the willow shoot had become its tuning fork.
    Object, wound, and method fuse into one mechanism that literally produces the required singing scars; the element generates the payoff image.
- **C046 — Constraint metabolism:** Gemini 3.7 Flash (high) more consistently turns required elements into mutually necessary causes. A method exists because the world has first presented a particular physical obstacle. Gemini 3.5 Flash usually connects the elements locally, but some connections function mainly as prompt acknowledgment rather than a navigable chain.
  - Story 0044, `gemini-3.7-flash-high`:
    > Linear scribing was useless in this altered age, as open incisions merely leaked potential into the thin mountain air.  True containment could only be achieved by closing loops.
    The altered physics produces a failure mode, and that failure mode necessitates the required loop-closing method. The strangeness is therefore functional rather than merely ornamental.
  - Story 0087, `gemini-3.7-flash-high`:
    > Whenever the fog blinded him completely, he paused to listen for the faint hum of high voltage transformers and the metallic rattle of porcelain insulators.
    The utility poles provide multiple usable signals when sight fails, making the unconventional navigation method physically intelligible.
  - Story 0087, `gemini-3.5-flash`:
    > Using the tall utility poles along the shore as her only guideposts, she paddled away from the land, their yellow streetlamps casting long, shimmering trails across the black water.
    The image is attractive, but the route has no specified destination or geometry. Shore lights might maintain a bearing, yet the story does not establish how paddling away from them leads Maeve home.
- **C055 — Required elements as machinery versus as weather:** Faced with identical constraint lists, Gemini 3.7 Flash (high) more often converts an element into a proximate cause with timing — the frost that cracked the tube last night, the power surge that makes the scan possible, the static clearing that makes the corrupted telemetry visible. Gemini 3.5 Flash more often converts the same element into ambience, so scenes proceed by montage rather than trigger.
  - Story 0326, `gemini-3.7-flash-high`:
    > For months, the receiver had droned with blizzard interference, but the air settled into breathless silence after the radio static clears.  In the sudden quiet, Elena's scattered telemetry flickered across the glass terminal in broken, frantic loops.
    The assigned timeframe becomes the reason the problem is now perceptible and actionable; the plot cannot begin before it.
  - Story 0326, `gemini-3.5-flash`:
    > A comforting sense of midnight solace fills the glass dome after the radio static clears from the main receiver.
    The same element is used as mood-setting; nothing in the subsequent action depends on the static having cleared.
- **C065 — Objects with jobs vs. objects with meanings:** Across the packet, Gemini 3.7 Flash (high) assigns the required object a function in the causal chain while Gemini 3.5 Flash assigns it a meaning. In Gemini 3.7 Flash (high)'s silo story, the sovereign case hides a cipher-locked reed that completes the silo's purpose, so object, method, and the required echoes interlock into one mechanism. Gemini 3.5 Flash's matching case is a memento holding a tool; the aquifer reveal does not need it. The pattern recurs: Gemini 3.7 Flash (high)'s ink stamps the treaty and alters the stamper (139), Gemini 3.7 Flash (high)'s lagoon sediment hides the swimmer (197), while Gemini 3.5 Flash's lagoon is held up as an emblem, "a silent, glowing archive of the heavens" (Gemini 3.5 Flash, 197). Gemini 3.7 Flash (high)'s prompts feel engineered; Gemini 3.5 Flash's feel annotated.
  - Story 0064, `gemini-3.7-flash-high`:
    > When Julian held it up against the lamp, he realized it was an acoustic reed meant to fit the silo's draft flue.
    The required object turns out to be the missing part of the setting's hidden function; nothing in Gemini 3.5 Flash's version of the same prompt performs equivalent causal work, so the difference is structural rather than decorative.
- **C071 — Elements fused into one image versus elements cited in apposition:** Gemini 3.7 Flash (high) tends to collapse two or three required elements into a single functioning image, so the brief disappears into event. Gemini 3.5 Flash more often names an element and then defines it in apposition, leaving the assembly seam visible and turning the story into an annotated checklist.
  - Story 0051, `gemini-3.7-flash-high`:
    > Sola tilted the kerosene lamp burner seven degrees toward the highest zenith, aligning its pierced collar with the constellation of the Baleen.
    One sentence discharges the object, the method ("by orienting properly"), the starlit setting, and the "whalebone reverie" tone, which becomes a named constellation instead of a mood label.
  - Story 0247, `gemini-3.5-flash`:
    > This core concept of silent, gestural communication was his chosen instrument, a beautiful, physical choreography of the air.
    "This core concept" is the prompt's own category word surfacing inside the fiction; the sentence explains an element rather than using it.
  - Story 0051, `gemini-3.5-flash`:
    > The thread vibrated with a low, oceanic moan, evoking a deep whalebone reverie that seemed to stretch back to the dawn of the world.
    The tone word is inserted as a thing the prose "evokes" — the requirement is quoted rather than embodied.
- **C034 — Naming the required tone versus staging it:** Gemini 3.5 Flash frequently satisfies the tone and attribute requirements by declaring them as states of the scene or as inventoried character traits; Gemini 3.7 Flash (high) more often builds an image whose consequences produce the tone. The difference is between a caption and a demonstration.
  - Story 0231, `gemini-3.5-flash`:
    > The heavy tone of witnessed isolation settled over the lonely lighthouse spit, thick and unyielding.
    The story names its own required tone and even calls it a "tone," which briefly breaks the fiction into a checklist. The line performs no dramatic work.
  - Story 0231, `gemini-3.7-flash-high`:
    > He knew no vessel would steer by that shadow, and no sailor would recognize the alpine blossom thrown against the sea.
    Isolation-with-a-witness is produced by an action and its acknowledged futility: he makes a signal that will not be read, and keeps it anyway. The tone is an outcome rather than a label.
- **C011 — Objects carry provenance and rhyme with recovered memory:** Gemini 3.7 Flash (high)'s required objects have histories that characterize their owners and that lock into the plot: the exhumed wildflowers in 0380 are the same bouquet inside the recovered memory, and the erasure has a specified motive (grief paid away to surgeons after a drowning). Gemini 3.5 Flash's 0380 hero already possesses the flower envelope despite total memory erasure — an unexplained residue — and the recovered memory (a woman, a meadow, a promise) never connects back to the flowers. Gemini 3.7 Flash (high)'s 0180 ribbon was hoarded for years "intending to return it," a micro-history that indicts the father; Gemini 3.5 Flash's ribbon is simply "exactly what we need."
  - Story 0380, `gemini-3.7-flash-high`:
    > the laughter of a sister whose name he had surrendered to the surgeons after her drowning, and the bouquet they had gathered before the storm broke
    The remembered bouquet and the exhumed pressed flowers are the same object, closing a logical and emotional loop, and the deletion's voluntariness ("surrendered") gives the recovery moral weight. Gemini 3.5 Flash's equivalent passage restores "a woman with laugh lines around her eyes, a sunlit meadow, and a promise" — generic content with no causal tie to the object that triggered it.
- **C027 — Whether objects obey the story's own thesis:** Both 0180 stories preach deciduous vows, promises meant to fall away, but only Gemini 3.7 Flash (high) makes the physical fix behave accordingly. Gemini 3.7 Flash (high)'s ribbon is explicitly temporary so the tree learns independence; Gemini 3.5 Flash's narration praises its ribbon as unyielding immediately after delivering the letting-go doctrine, splitting theme from thing. The impression of intelligence comes from whether a story's props enact its philosophy.
  - Story 0180, `gemini-3.7-flash-high`:
    > The ribbon will fray before the fruit ripens
    The repair is deliberately impermanent, so the object performs the theme of vows designed to shed; the daughter adds that by then the wood will know how to stand on its own.
  - Story 0180, `gemini-3.5-flash`:
    > The scarlet ribbon held remarkably firm, damp but unyielding under the steady pressure of the cool stream.
    After a speech about promises that shed old forms, the story's final image praises unyieldingness, quietly contradicting the stated moral.
- **C018 — Object provenance: kinship versus strata:** Gemini 3.5 Flash roots required objects in family transmission, which gives motive a biography; Gemini 3.7 Flash (high) roots them in geological or civilizational deep time, which gives them scale but leaves protagonists motivated by curiosity or vocation alone. Neither is superior, but this single habit generates most of the packet's tonal difference and explains why Gemini 3.5 Flash feels warmer and Gemini 3.7 Flash (high) feels larger.
  - Story 0374, `gemini-3.5-flash`:
    > She remembered how her grandfather always tasted of petrichor before a storm, his very presence bringing a cool humidity to their living room.
    One domestic image makes the sci-fi premise personal and simultaneously explains the heroine's inherited palate — the object's history and her motive are the same fact.
  - Story 0146, `gemini-3.7-flash-high`:
    > this dark wood held the memory of the forest before the collapse, when tree roots and bedrock shared a single, unbroken pulse
    Gemini 3.7 Flash (high) gives the fork a cosmological pedigree instead of a familial one; it enlarges the world but supplies no personal reason for this man to be doing this work.
- **C057 — Damage as instrument versus damage as defect:** A consistent symbolic economy separates the writers without either being obviously better. Gemini 3.5 Flash treats a flaw as the thing that makes the instrument work, and keeps the wounded object; Gemini 3.7 Flash (high) treats a flaw as a fault to be mended or discarded, and disposes of the wounded object at the end. Same props, opposite metaphysics of injury.
  - Story 0159, `gemini-3.5-flash`:
    > The cracked bamboo warbled, its compromised tone carrying a ghostly, dual resonance that perfectly matched the song's lost frequency.
    The crack is not a problem but the precise reason the ritual functions — damage as tuning, reinforced by the gold-lacquer seal earlier in the story.
  - Story 0159, `gemini-3.7-flash-high`:
    > His fingers moved with steady care, binding the split wood and sealing the fissure with resin so that the hollow chamber could once more hold air.
    Gemini 3.7 Flash (high) makes the crack the story's obstacle and the repair its first act; restoration, not incorporation, is the governing idea, matching Gemini 3.7 Flash (high)'s later release of the mask strap and disposal of the dice.
- **C001 — Custody instead of recovery:** Writer Gemini 3.7 Flash (high)’s strongest endings preserve evidence without pretending loss has been reversed. Information is dispersed, witnessed, or kept in circulation. Writer Gemini 3.5 Flash more often equates discovery with restoration, giving the protagonist an emotionally gratifying endpoint. Gemini 3.7 Flash (high)’s pattern creates an impression of mature archival intelligence because it separates survival of testimony from recovery of the person.
  - Story 0395, `gemini-3.7-flash-high`:
    > Instead, Silas duplicated the confession across three thousand unmonitored musical archives, letting Thorne's voice slip into the everlasting stream of forgotten songs where no algorithm would think to look.
    Silas responds to institutional danger by changing the confession’s mode of existence. Redundancy and obscurity become ethical safeguards; the dead engineer is not restored, but his testimony is made harder to erase.
  - Story 0395, `gemini-3.5-flash`:
    > He clicked restore, watching the progress bar fill as her code reassembled.
    Gemini 3.5 Flash converts the archive mystery into direct familial recovery. The emotional payoff is clear, but the action bypasses the security, identity, and embodiment problems raised by the discovery of stored consciousness.
- **C008 — Sealed verdict endings versus resumed-work endings:** Gemini 3.5 Flash closes each story with a completed-state verdict that summarizes the meaning, while Gemini 3.7 Flash (high) ends mid-motion, returning characters to ordinary labor with the change still propagating. Gemini 3.5 Flash's closures state that the problem is solved; Gemini 3.7 Flash (high)'s imply the world will keep needing the work. This produces Gemini 3.7 Flash (high)'s impression of maturity: trust that the reader does not need the moral pronounced, and realism about change being ongoing.
  - Story 0034, `gemini-3.5-flash`:
    > The ghost was no longer a silent captive of the stones, and the seldom-heard balladeer had finally found a song worth sharing with the universe.
    Total resolution plus thematic summary in one sentence; compare Gemini 3.7 Flash (high)'s 0295 close, "Elias extinguished the brass desk lamp, tightened his cloak against the morning chill, and stepped out toward the winding mountain path," which ends before the reconciliation the whole story pointed toward, and Gemini 3.7 Flash (high)'s 0034 close, where citizens simply step onto balconies as Orlo packs his brushes.
- **C014 — Endings that cause a state versus endings that announce one:** Gemini 3.5 Flash's closes typically assert the protagonist's final emotional settlement in summary language, sometimes contradicting the story's own concept; Gemini 3.7 Flash (high)'s closes more often report a consequence in the world and let the state be inferred. The difference is causal, not tonal: Gemini 3.5 Flash claims a change the middle did not produce.
  - Story 0228, `gemini-3.5-flash`:
    > Julian watches it settle onto the white sand of the pool floor, forever preserved in the stillness of the cave.
    The required core concept is "temporary eternity," but Gemini 3.5 Flash's climactic act achieves permanence; the following hedge, "one day the sea might reclaim this sanctuary, but for now," concedes the contradiction rather than resolving it.
  - Story 0146, `gemini-3.7-flash-high`:
    > In the distance, the first travelers appeared on the horizon, drawn unwittingly toward the restored song of the valley.
    Instead of naming the hero's satisfaction, Gemini 3.7 Flash (high) gives an external effect that verifies the work succeeded; "unwittingly" quietly extends the mechanism to people who never learn of it.
  - Story 0271, `gemini-3.5-flash`:
    > As the automated lighthouse beam began its evening rotation outside, Layla smiled faintly, knowing she had weathered another storm.
    The final clause tells the reader the meaning of the episode in received phrasing, closing off the more difficult implication that the freeze will recur.
- **C029 — Endings that spend the protagonist versus endings that refund them:** Gemini 3.7 Flash (high)'s resolutions accept cost, temporariness, or pending tests, while Gemini 3.5 Flash's consolidate mastery, belonging, or comfort. The difference is an emotional geometry: Gemini 3.7 Flash (high) opens loops, Gemini 3.5 Flash closes them cozily. This reads as maturity because the story's world is allowed to remain larger than the hero's comfort.
  - Story 0103, `gemini-3.7-flash-high`:
    > His boots, his pruning shears, and the heavy skin of his hands began to disintegrate into shimmering strands of particulate memory.
    Transcendence costs the protagonist his body and identity; knowledge is purchased with selfhood.
  - Story 0103, `gemini-3.5-flash`:
    > finding solace not by escaping the maze of time, but by becoming its ultimate architect.
    The same premise resolves into promotion and solace; the hero is preserved, stilled, and crowned.
  - Story 0317, `gemini-3.7-flash-high`:
    > Tomorrow, when the financiers arrived with their standardized contracts and predatory offers, he would guide them into this dark room and let the silence speak.
    The story ends before the confrontation, leaving the victory untested, whereas Gemini 3.5 Flash's parallel ending certifies that the innovation was alive and closes with a smile.
- **C036 — Endings that keep a cost versus endings that undo the wound:** Gemini 3.5 Flash tends to resolve by cancellation — the dead are alive, the file is restored, the wound is covered over — while Gemini 3.7 Flash (high) more often converts the problem into a durable but partial arrangement whose cost stays visible. This is a tendency with real exceptions on Gemini 3.7 Flash (high)'s side.
  - Story 0395, `gemini-3.5-flash`:
    > He clicked restore, watching the progress bar fill as her code reassembled.
    The premise's grief is retroactively voided: the crew were never dead, and the sister comes home. The story's own constraint (a surveilling corporation with purge authority) is simply dropped at the moment of payoff.
  - Story 0395, `gemini-3.7-flash-high`:
    > Instead, Silas duplicated the confession across three thousand unmonitored musical archives, letting Thorne's voice slip into the everlasting stream of forgotten songs where no algorithm would think to look.
    The victory is tactical and incomplete: the engineer stays dead, the truth stays unheard, and the ending is a preservation strategy that respects the surveillance system established earlier.
- **C043 — Endings keep the cost on the books rather than refunding it:** Both writers use the same success-declaration grammar at endings, but Gemini 3.5 Flash's version negates the cost while Gemini 3.7 Flash (high)'s concedes it. Gemini 3.5 Flash's Karen survives and keeps the prize, with the narration doubly assuring the reader; Gemini 3.7 Flash (high)'s Kira dies and converts her distress beacon into a delivery system for someone she will never meet. The same pattern recurs in 0143, where Gemini 3.7 Flash (high) lets the precious ice sublime during its own photograph while Gemini 3.5 Flash's varnish dies safely offscreen.
  - Story 0147, `gemini-3.7-flash-high`:
    > She affixed the crystal perfume vial directly to the transmitter housing so that whatever expedition followed her signal would find the prize intact.
    The required character element is redefined: the signal outlives the sender and becomes the artifact's courier, an ending built on unreimbursed loss.
  - Story 0147, `gemini-3.5-flash`:
    > She climbed into the decompression chamber, knowing she had not only survived, but had successfully captured the fleeting essence of her sister's smile inside the vial.
    The stacked assurances (survived, captured) over-certify the outcome, closing the books with no outstanding debt.
- **C090 — Endings: held gesture vs. delivered verdict:** Gemini 3.7 Flash (high)'s final sentences are usually a physical action or a sustained image with residue; Gemini 3.5 Flash's are usually an evaluative summary that tells the reader what the story meant, often restating the prompt's own motivation as achieved. This is a closural habit rather than a quality of sentence.
  - Story 0143, `gemini-3.7-flash-high`:
    > She retrieved her spent chemical timers, packed her case, and began the long descent toward the noise of humanity.
    Ends on housekeeping plus one turned word — "noise," which inverts the story's hush without explaining itself.
  - Story 0143, `gemini-3.5-flash`:
    > That single grain of sand had survived centuries of ocean spray, just as these photographs would survive the violent onset of the space age.
    The symbolic equation is spelled out as a simile with "just as," leaving the reader nothing to assemble.
  - Story 0205, `gemini-3.5-flash`:
    > This chronicle would survive even if he did not, serving as a beacon of hope for future generations who dared to dream of liberty.
    Gemini 3.5 Flash's emotional peaks recruit inspirational-poster phrasing at precisely the load-bearing moment, where Gemini 3.7 Flash (high)'s tend to end on an object or a look.
- **C023 — Care permits refusal:** Gemini 3.7 Flash (high) shows unusual relational perception in Story 0047 by allowing Jonas to refuse Kira’s symbolic gift and initiate his own form of participation. The proffer does not automatically authorize the giver’s interpretation. Gemini 3.5 Flash makes Silas receive the amber exactly as Maeve intends, so care succeeds as symbolic transmission rather than negotiation.
  - Story 0047, `gemini-3.7-flash-high`:
    > He did not take the stone, but instead reached into his pocket, retrieved a handful of damp moss seeds, and knelt beside her on the metal floor.
    Jonas neither rejects reconciliation nor passively accepts its prescribed token. He translates it into an action of his own, preserving the recipient’s autonomy.
  - Story 0047, `gemini-3.5-flash`:
    > Silas closed his fingers around the warm stone, the physical weight of her quiet, proactive care grounding him in the present moment.
    The recipient’s psychological change immediately confirms Maeve’s symbolism. This is emotionally legible but less socially complex because the gift’s intended meaning encounters no resistance.
- **C032 — Implicated protagonists versus ministered-to victims:** Given the same prompt about a viral confession, Gemini 3.5 Flash constructs a clean helper/sufferer dyad in which the sufferer has done nothing wrong and speaks no dissent, while Gemini 3.7 Flash (high) makes the confessor herself culpable and gives the second character a grievance he voices. The difference produces moral friction in Gemini 3.7 Flash (high) and pure consolation in Gemini 3.5 Flash.
  - Story 0047, `gemini-3.7-flash-high`:
    > He had been her partner in designing the predatory data architecture, and he had fled when she chose transparency over silence.
    Both principals are compromised: she built the harmful system, he abandoned her. The scene therefore has stakes beyond comfort, and the later reconciliation has to be earned across an actual breach.
  - Story 0047, `gemini-3.5-flash`:
    > Silas sat shivering on a plastic crate nearby, his shoulders hunched as he tried to block out the memory of how quickly his private pain had been turned into public entertainment.
    Gemini 3.5 Flash's sufferer is wholly innocent and wholly passive; he never speaks in the story. The emotional problem is external (the internet), so nothing between the two characters needs resolving.
- **C037 — Worlds populated by people with their own reasons:** Gemini 3.7 Flash (high) routinely admits third parties who exert independent pressure — a colleague's verdict, a fled accomplice's counter-gesture, a cheerfully bureaucratic monitor — so that protagonists are situated inside a social field. Gemini 3.5 Flash's protagonists tend to operate alone or with a silent recipient, and even Gemini 3.5 Flash's obstacles resolve at once.
  - Story 0047, `gemini-3.7-flash-high`:
    > He did not take the stone, but instead reached into his pocket, retrieved a handful of damp moss seeds, and knelt beside her on the metal floor.
    The required action "proffer" is fulfilled and then declined; the other character answers with an equivalent of his own. He is an agent, not a recipient, and the reconciliation is his act too.
  - Story 0241, `gemini-3.7-flash-high`:
    > Her colleagues called her models dangerously poetic, but she considered her theoretical rebellion a necessary correction to bloodless econometrics.
    One clause supplies a professional community with a hostile opinion, which converts "theoretically rebellious" from a label into a position held against opposition. Gemini 3.5 Flash's version of this prompt contains no other living character at all.
- **C070 — Stories built as exchanges vs. solitary errands:** Gemini 3.7 Flash (high) recurrently constructs plot as a transaction between minds: a dead man's riddle answered in dialogue ("You never did trust plain speech, old man," Gemini 3.7 Flash (high), 64), a negotiated price for treason, an archivist won over, a broadcast answered by windows lighting one by one. Gemini 3.5 Flash more often sends a solitary protagonist to collect a revealed meaning; the climax is a verdict delivered to the reader rather than knowledge received by a second consciousness.
  - Story 0064, `gemini-3.5-flash`:
    > Alistair's intentions were profoundly beautiful, a legacy of life hidden beneath the veil of death.
    The mystery resolves as a private moral verdict that no other character contests, receives, or uses; Gemini 3.7 Flash (high)'s equivalents end in reception — Kallis "recording the translated lines into her official ledger" (Gemini 3.7 Flash (high), 205), the city's windows answering Mara's broadcast (Gemini 3.7 Flash (high), 197).
- **C075 — A second consciousness to push against:** Gemini 3.7 Flash (high) typically invents an unrequired second presence that resists or comments — an advisor, a wry machine, a vanished sister, dead companions — which converts exposition into interaction. Gemini 3.5 Flash's protagonists are almost always alone with their objects, so change happens inside description rather than between people.
  - Story 0247, `gemini-3.7-flash-high`:
    > "You cannot awaken the departed with gestures, Julian," she whispered urgently.  "Their stories are over, and they must fade into peace."
    The required "whispering advisor" is split off from the protagonist to create opposition, giving the story an argument to win rather than a mood to sustain.
  - Story 0247, `gemini-3.7-flash-high`:
    > He did not argue with words, but used the empty viewfinder to frame her face, capturing the precise beat of her hesitation.
    The objection is answered through the required object, so the interpersonal beat and the prop are the same move.
- **C020 — Consequence has an address:** Gemini 3.7 Flash (high) more often specifies the causal and institutional content of a wound. In Story 0047, the viral confession concerns participation in a predatory system and creates a conflict between transparency, complicity, and loyalty. Gemini 3.5 Flash supplies protected suffering but leaves the confession’s substance almost entirely blank. Gemini 3.7 Flash (high) therefore makes restoration answer an identifiable ethical history rather than generalized exposure.
  - Story 0047, `gemini-3.7-flash-high`:
    > He had been her partner in designing the predatory data architecture, and he had fled when she chose transparency over silence.
    The sentence establishes what Kira did, what she confessed, why Jonas fled, and what their relationship has at stake. Those linked consequences produce causal and social density.
  - Story 0047, `gemini-3.5-flash`:
    > Silas sat shivering on a plastic crate nearby, his shoulders hunched as he tried to block out the memory of how quickly his private pain had been turned into public entertainment.
    Gemini 3.5 Flash clearly renders injury, but “private pain” supplies no comparable account of conduct, responsibility, or disagreement. The public is simply cruel, so the moral field is already settled.
- **C059 — Two-sided blame geometry:** Gemini 3.7 Flash (high) gives reconciliation a psychologically reciprocal structure. Each party's damaging act arose from a different fear and interpretation, so the vows answer actual epistemic failures rather than merely supplying virtuous sentiments. Gemini 3.5 Flash names plausible academic offenses, but the prior relationship remains less causally reconstructed.
  - Story 0016, `gemini-3.7-flash-high`:
    > "I hid the ledger because I feared you would destroy it," he confessed, his voice trembling as he touched the dry border of the parchment.  The ink flared a warm, resonant bronze.  "And I abandoned the dig because I believed you valued the discovery more than our lives," Mira countered
    The paired confessions reveal opposed fears about evidence and safety. Their conflict therefore has intelligible symmetry without making the parties identical or assigning all fault to one side.
  - Story 0016, `gemini-3.5-flash`:
    > "I promise to record your brilliant discoveries without ever taking the credit," he whispered, tracing the first glowing rune on the slate.
    This is ethically specific, but it functions primarily as a prospective pledge. The story gives less dramatic evidence of how the original breach occurred or how the two perceptions interacted.
- **C074 — The narrator as its own admiring audience:** Gemini 3.5 Flash's narration pre-rates its material with evaluative adjectives, telling the reader the experience is beautiful, stunning, or magnificent. Gemini 3.7 Flash (high) more often withholds evaluation and lets consequence or a character's reaction supply the verdict. The effect is that Gemini 3.5 Flash's emotional peaks arrive already spent.
  - Story 0247, `gemini-3.5-flash`:
    > His chosen method was strange yet profoundly beautiful: he would disrupt this crushing stagnation specifically by mapping silence.
    The sentence grades its own conceit before demonstrating it, and simultaneously flags the required action and method — self-praise and prompt-recital in one breath.
  - Story 0247, `gemini-3.7-flash-high`:
    > Every shutter click was hollow, but each mechanical snap framed a distinct interval of stillness in his mind.
    The same conceit is delivered as a mechanism with no adjective of approval; the reader is left to judge it.
- **C052 — Dissonance held open versus dissonance dissolved:** Given a deliberately contradictory assigned tone ("foxglove regret," "displaced rooted"), Writer Gemini 3.5 Flash keeps both poles active through the final sentence, treating the contradiction as the story's meaning. Writer Gemini 3.7 Flash (high) converts the dysphoric half into resolved comfort, usually in the closing paragraph, so the assigned tone survives only as decoration en route to relief.
  - Story 0159, `gemini-3.5-flash`:
    > Yet, the foxglove regret remained, a beautiful, toxic reminder that these names existed now only as light and resonance, devoid of flesh.
    The tone is not merely named but given a cost — resonance without flesh — and explicitly refused resolution ("remained").
  - Story 0159, `gemini-3.7-flash-high`:
    > Vael stepped down from the ladder, feeling the sharp sting of foxglove regret ease into a quiet, enduring satisfaction.
    The same assigned tone is administered and then dispelled; the story's final position is satisfaction, not regret. Compare Gemini 3.7 Flash (high)'s 0201 ending, "fully restored to himself and free at last," which resolves "displaced rooted" into unmixed freedom.
- **C062 — Darkness corrects the apparatus:** Gemini 3.5 Flash's story 0163 has the packet's strongest symbolic convergence. The astrologer's inverted constellations prepare the deep-sea lights, and the failure of artificial illumination reveals the living pattern he seeks. The revelation therefore grows from reversal rather than from a newly announced magical property. Gemini 3.7 Flash (high) reaches a similar image, but its burnt feather becomes an expedient technical component through unsupported atmospheric memory.
  - Story 0163, `gemini-3.5-flash`:
    > To him, the abyssal trenches were not empty voids but inverted constellations, dark valleys where massive geothermal vents burned like cold blue stars.
    The central metaphor joins occupation, landscape, and setting before the plot's revelation, making the later bioluminescence feel prepared rather than decorative.
  - Story 0163, `gemini-3.5-flash`:
    > As the artificial lights died, the natural world of the abyss awoke.
    This concise reversal makes technological failure perceptually productive. Orin learns belonging because loss of control permits him to see an existing ecology.
  - Story 0163, `gemini-3.7-flash-high`:
    > "The focal cradle needs an organic filament with atmospheric memory to bridge the electrical gap between the mirrors," she explained softly.
    Gemini 3.7 Flash (high) integrates the feather into the action, but its special property arrives when required and has little prior causal basis. The mechanism is functional yet less conceptually earned.
- **C068 — One story where Gemini 3.5 Flash keeps the knife open:** In 98, the prompt's luminous doubt is the whole assignment, and only Gemini 3.5 Flash honors it past the climax. Gemini 3.5 Flash's reality checker saves the memory while doubting the saved material is true, ending on a pragmatist compromise that undercuts her own profession; Gemini 3.7 Flash (high) raises the doubt mid-story, then discharges it into affirmation ("Their cultural memory was saved, rooted deeply enough to outlast any deluge," Gemini 3.7 Flash (high), 98). This is the packet's most conceptually risky ending.
  - Story 0098, `gemini-3.5-flash`:
    > she wondered if she had merely constructed a prettier prison for their illusions
    The preserved history may be collective fabrication and the story refuses to settle it; the closing position that realities are measured "by their power to keep the storm at bay" (Gemini 3.5 Flash, 98) is an earned, uneasy stance rather than a mood.
- **C080 — A present-shaped blind spot:** Gemini 3.5 Flash produces the packet’s most substantive conceptual invention in 0177. “Foresight hindsight only” becomes a mind that perceives past and future but cannot perceive the present, and the climax briefly repairs exactly that missing temporal faculty. Gemini 3.7 Flash (high) interprets the phrase as insight arriving only after events, which is psychologically legible but much closer to ordinary hindsight.
  - Story 0177, `gemini-3.5-flash`:
    > She could see the pristine facility of eighty years ago, and she could see the overgrown mound it would become in a century, but the ticking present remained an invisible void.
    This is a precise cognitive constraint rather than decorative mysticism. It governs her inability to operate the console directly and gives the eventual sensation of “now” structural force.
  - Story 0177, `gemini-3.7-flash-high`:
    > He could see the intricate geometry of fate clearly, but solely in the immediate wake of its occurrence, forever mourning choices that felt predetermined.
    Gemini 3.7 Flash (high)’s version yields recognizable regret, but “foresight” no longer contributes much beyond naming hindsight as belated pattern recognition.
- **C003 — Intermediate-state thinking:** Gemini 3.7 Flash (high) more often shows a mechanism passing through consequential intermediate states rather than merely naming an ingenious method and presenting its result. This produces substantive causal intelligence when the parts genuinely alter one another. Gemini 3.5 Flash frequently has an evocative premise but moves quickly from trigger to desired revelation.
  - Story 0317, `gemini-3.7-flash-high`:
    > He introduced a thin glass pipette filled with mineral oil and watched the amber liquid flow smoothly into the lower chamber.  The shifting center of mass tilted the brass cradle by exactly three degrees, disengaging a hidden magnetic catch.
    The liquid changes mass distribution, the cradle tilts, and the catch releases. Whatever the larger mechanism’s plausibility, this local sequence has visible causal joints.
  - Story 0395, `gemini-3.5-flash`:
    > He clicked restore, watching the progress bar fill as her code reassembled.
    The decisive action produces its wished-for result without confronting the purge risk, corporate response, or problem of what restored consciousness would inhabit. The progress bar substitutes for a causal and ethical transition.
- **C085 — Premise yields an operation (Gemini 3.7 Flash (high)) vs. premise yields a mood (Gemini 3.5 Flash):** Given the same speculative conceit, Gemini 3.7 Flash (high) extracts a specific, counterintuitive action that follows from the rule; Gemini 3.5 Flash restates the conceit at higher intensity and calls the resulting vagueness a plan. This is causal intelligence, not vocabulary: both writers use comparable diction, but only Gemini 3.7 Flash (high)'s premise constrains what the character must do next.
  - Story 0310, `gemini-3.7-flash-high`:
    > To wavelength align with purpose, they did not need to ignite their propulsion engines; they had to extinguish the primary reactor and coast backward into the gravitational pocket.
    The reversed-time premise produces a concrete, falsifiable, counterintuitive instruction — do less, not more — which could only be derived from the rule, not decorated onto it.
  - Story 0310, `gemini-3.5-flash`:
    > He knew they had to distill their physical bodies and the ship's titanium hull into a single, concentrated stream of pure, harmonious energy.
    Same prompt, same required verb "distill," but the output is unconstrained by the backwards-prophecy premise; any transcendent conceit would produce this sentence.
  - Story 0143, `gemini-3.5-flash`:
    > the changing colors would project faint, brief pinpricks of light onto the opposite canyon wall, signaling him when the guards shifted patrols
    A pre-set chemical timer cannot report a contingent human event; the mechanism is asked to carry information it has no way of acquiring.
- **C073 — Risk executed on the page versus risk announced in the abstract:** Both writers identify the same hazard in matched stories, but Gemini 3.7 Flash (high) stages a near-failure and its correction as an event, which also makes the character's attribute do plot work; Gemini 3.5 Flash states the hazard as a fact about the world and never tests it.
  - Story 0093, `gemini-3.7-flash-high`:
    > A second premonition struck his consciousness, showing the fifth stone slipping two millimeters wide under the rising tide of ether.  Armed with the cursed knowledge, Kael adjusted his grip before the error could manifest, anchoring the stone precisely into the spiral node.
    The precognition attribute becomes the instrument of the method; the risk is realized, sensed, and averted in sequence, producing causality rather than atmosphere.
  - Story 0093, `gemini-3.5-flash`:
    > Even a millimeter of error would send the stones sliding off the edge of the cliff forever.
    Identical hazard, declared and then dropped; Gemini 3.5 Flash's precognition never intervenes, and the attribute only resolves retroactively when "the chaotic visions of the future aligned perfectly."
- **C016 — Planted absence, later filled:** Gemini 3.7 Flash (high) sets up a specific lack early and satisfies it structurally at the climax, so the required "core concept" arrives as a payoff rather than an announcement. Gemini 3.5 Flash states the same concept as inherited lore up front and then confirms it, which is exposition rather than structure.
  - Story 0374, `gemini-3.7-flash-high`:
    > Its original brass spindle had rusted away generations ago, leaving the hollow tin bezel completely empty of magnetic guidance.
    Gemini 3.7 Flash (high) creates a specified vacancy in the object early.
  - Story 0374, `gemini-3.7-flash-high`:
    > Ionized droplets and pale sparks leaped into the empty circle of metal, weaving together to fashion an emergent compass out of the swirling atmospheric vortex.
    The emergence happens in the exact space Gemini 3.7 Flash (high) emptied, so "emergent compass" is produced by the story's own architecture rather than asserted.
  - Story 0374, `gemini-3.5-flash`:
    > Her late grandfather had been one such storm walker, and he had left her the ring, claiming it was an emergent compass.
    Gemini 3.5 Flash installs the concept as prior testimony; the later confirmation adds information but no structural surprise, since nothing was withheld or prepared.
- **C006 — Material convergence of motifs:** Gemini 3.7 Flash (high) more often selects final images whose materials gather several story systems at once. Botanical fibers, curved space, relics, light, and memory continue interacting rather than becoming interchangeable symbols. Gemini 3.5 Flash usually states the thematic synthesis more abstractly. This is selective intelligence: choosing which images to repeat and transform, not merely producing more imagery.
  - Story 0103, `gemini-3.7-flash-high`:
    > It possessed a coarse, fibrous weave, like dried palm cordage interwoven with cold river silt and powdered stone.  It snagged against his flesh with the dry friction of countless layered epochs rubbing against one another in the curved fold.
    The answer to time’s texture remains materially continuous with the living bridge, pruning labor, canyon, and geometric folding. The metaphor does several structural jobs rather than merely decorating the revelation.
  - Story 0103, `gemini-3.5-flash`:
    > This was the texture of time, a rugged tapestry woven from gravity, memory, and the inevitable decay of physical form.
    Gemini 3.5 Flash delivers a clear conceptual summary, but its components are abstractions. “Tapestry” names synthesis without retaining as much of the garden’s particular matter.
  - Story 0231, `gemini-3.7-flash-high`:
    > As the lamp spun, the beam passed through the brittle petals, projecting a faint, starry shadow far out across the misty water.
    The alpine flower becomes part of the lighthouse apparatus, and its star shape is projected into the maritime setting. Mountain memory, sea, vigil, and the keeper’s occupation converge in one transformed object.
- **C077 — Load-bearing specificity: component nouns, numerals, and stated non-events:** Gemini 3.7 Flash (high)'s concreteness tends to be functional — correct part names for the object, quantities that specify an operation, and explicit statements of what did not occur. Gemini 3.5 Flash's concreteness is scalar and approximate. This produces authority without any assertion of authority, but it is also the difference most vulnerable to being fake rigor.
  - Story 0051, `gemini-3.7-flash-high`:
    > Its brass thumbwheel was notched with age, and its perforated gallery smelled of historic combustions.
    "Thumbwheel" and "gallery" are actual kerosene burner components used correctly; this is retrieval of domain structure, not adjectival dressing, and it is later repurposed when the wick-sleeve is fed silver filament instead of fuel.
  - Story 0391, `gemini-3.7-flash-high`:
    > The immense iron rails shifted four inches out of alignment, decoupling cleanly from the terminal buffers without shearing a single rivet.  No catastrophic explosion illuminated the night sky, and no sentries shouted in sudden panic.
    The exact displacement defines the sabotage's political character (untraceable, no martyrs), and the negative clauses model the alternative outcomes the writer rejected.
- **C047 — Provisional belief under pressure:** Gemini 3.7 Flash (high) more often lets uncertainty modify the procedure rather than merely decorating a triumphant decision. This creates an impression of epistemic intelligence: the character asks what else could explain a signal and seeks an additional test. Gemini 3.5 Flash raises doubt but is readier to convert a spectacular coincidence into absolute proof.
  - Story 0310, `gemini-3.7-flash-high`:
    > Was this really the signature of the backward-flowing time stream, or just the deaf hiss of entropy?  To resolve the ambiguity, Marek prepared the cast.
    Marek names a competing explanation and changes his next action in response. Doubt has procedural consequences.
  - Story 0310, `gemini-3.5-flash`:
    > They clattered in a perfect, glowing circle around the central tuning dial.  The mathematical alignment was absolutely undeniable.
    The prose declares certainty without explaining why a circle formed by cast coins has decisive mathematical force. Confidence replaces an articulated inference.
- **C019 — Refusing the conversion arc:** Where a prompt invites the standard epiphany (skeptic becomes believer, survivor is healed), Gemini 3.7 Flash (high) modifies rather than reverses the character's position and states the modification precisely; Gemini 3.5 Flash delivers the default reversal. This is conceptual discipline about what evidence can actually change in a mind.
  - Story 0374, `gemini-3.7-flash-high`:
    > Her luminous skepticism did not shatter under the revelation, but expanded into a richer, humbler science that welcomed mystery as a partner.
    Gemini 3.7 Flash (high) keeps the character's epistemic identity intact while enlarging it, which is both more plausible and more interesting than conversion, and it preserves the required attribute instead of spending it.
  - Story 0374, `gemini-3.5-flash`:
    > the luminous skeptic found her doubts dissolving into wonder
    Gemini 3.5 Flash takes the default arc; the required attribute is annulled by the ending, so the character trait functions as an obstacle to be removed rather than a lens that survives contact with evidence.
  - Story 0271, `gemini-3.7-flash-high`:
    > He understood that true recovery did not promise an absence of fear, but rather a capacity to endure truth without shattering.
    The same discipline applied to trauma: the outcome is capacity, not cure, which is the harder and truer proposition.
- **C081 — Skepticism that survives revision:** Gemini 3.7 Flash (high)’s affectionate skeptic in 0281 is not simply defeated. Julian distinguishes synthetic intimacy from embodied attention, so the experiment confirms a modified version of his original criticism. Gemini 3.5 Flash gives Maya charm and participation, but ultimately treats her skepticism as something an image can sweep away. Gemini 3.7 Flash (high) therefore shows greater interpersonal and epistemic maturity in this story.
  - Story 0281, `gemini-3.7-flash-high`:
    > "I thought they were overpriced shortcuts," Julian corrected gently, stepping closer to rest a warm hand on the shoulder of his companion.  "Real minds are messy, darling, and no laboratory was ever going to compress your glorious chaos into a two milligram tablet."
    Julian combines affection, humor, and a conceptual distinction: he rejects chemical compression without rejecting intimacy or Kael’s grief.
  - Story 0281, `gemini-3.5-flash`:
    > She looked at Leo, her affectionate skepticism entirely swept away by the undeniable, glowing proof of their enduring connection.
    The narration declares the evidence undeniable and removes Maya’s doubt wholesale, narrowing a potentially complex dispute about what physiological synchrony can prove.
- **C086 — Certainty markers as a tell:** Gemini 3.5 Flash's narration repeatedly certifies its own outcomes with absolutes, which substitutes assertion for demonstration and flattens tension. Gemini 3.7 Flash (high) more often leaves a live disjunction on the page and distinguishes proof from feeling. The difference is at the level of individual modifiers, not argument.
  - Story 0310, `gemini-3.5-flash`:
    > They clattered in a perfect, glowing circle around the central tuning dial.  The mathematical alignment was absolutely undeniable.
    The universe cooperates geometrically and the narration then forbids doubt by fiat, using "absolutely undeniable" in place of any shown reasoning.
  - Story 0310, `gemini-3.7-flash-high`:
    > Did the cosmic remnants genuinely retain intent, or was he merely reading geometry into the meaningless spasms of a ruined void?
    Gemini 3.7 Flash (high) states the apophenia problem precisely and does not dissolve it; the eventual settling comes from a bodily sensation, which the prose declines to upgrade into evidence.
- **C035 — Causal ambition traded against causal soundness:** Gemini 3.7 Flash (high) habitually invents a mechanism to justify arbitrary prompt constraints, which reads as rigor but frequently rests on invented physics; Gemini 3.5 Flash leaves such constraints as atmosphere while keeping its own literal chain simple and internally consistent. Neither behavior is straightforwardly smarter, and each writer's weakness is the mirror of its strength.
  - Story 0034, `gemini-3.7-flash-high`:
    > That lingering hush between flash and detonation created an atmospheric vacuum where light signals could penetrate deep into the foundation channels without interference.
    Gemini 3.7 Flash (high) explains why the required timeframe matters, but the explanation is pseudo-physical: acoustic silence cannot create an optical vacuum. The gesture toward causality is more visible than the causality.
  - Story 0034, `gemini-3.5-flash`:
    > The conductive paint seeped into the microscopic fissures of the stone, instantly completing a long broken circuit that ran deep into the heart of the sky keep.
    Gemini 3.5 Flash does not justify the timing at all, using the lightning pause purely for mood, yet its actual causal link — conductive pigment closing a broken circuit — is coherent and does the plot work cleanly.
- **C056 — Mechanistic bluffing and the false-precision proxy:** Both writers handwave their central mechanisms, but they bluff differently. Gemini 3.5 Flash reaches for checkable specificity — numbers, physics, engineered probability — and the specifics are wrong or inert, so the appearance of rigor evaporates on inspection. Gemini 3.7 Flash (high) stays inside unfalsifiable in-world vagueness, which never claims rigor but also never earns it. The lesson is that Gemini 3.5 Flash's technical texture is a surface proxy readers may mistake for causal intelligence.
  - Story 0038, `gemini-3.5-flash`:
    > They settled on double sixes, a statistical impossibility that she had engineered by subtly altering the magnetic field in the chamber.
    The dice were established as ivory, which a magnetic field cannot move, and the rigged roll changes nothing in the plot; the sentence buys an impression of cunning with no mechanism and no consequence.
  - Story 0201, `gemini-3.7-flash-high`:
    > As the radiant storm envelops him, a violent visceral memory flares across his solar plexus, unlocking the final variable in his long calculation.
    Gemini 3.7 Flash (high)'s climax has a weather event deliver a mathematical proof by fiat; the story's stated project — quantifying mercy — is completed without any quantification, so Gemini 3.7 Flash (high)'s causal chain fails exactly where it matters most.
- **C088 — Gemini 3.5 Flash is better at what a body is doing:** Where a prompt requires embodied action, Gemini 3.5 Flash writes load, torque and posture; Gemini 3.7 Flash (high) writes attunement and abstraction. This is a genuine reversal against the general Gemini 3.7 Flash (high)-favoring pattern, and it is invisible to any single "vividness" score because both writers are vivid — about different things.
  - Story 0353, `gemini-3.5-flash`:
    > Thalo leaned his entire weight against the sculpture, matching the curve of his spine to the bent wood, feeling the intense torque of the trunk through his own bones.
    "Empathy in motion" is realized as a specific mechanical relationship between two bodies under strain, with a describable posture.
  - Story 0353, `gemini-3.7-flash-high`:
    > she shifted her body with the subtle sway of the boughs, matching the tension of the string to the living pulse of the wood
    Gemini 3.7 Flash (high)'s version of the same element stays in the register of attunement; "living pulse of the wood" is a metaphor, not a thing a spine does.
- **C040 — Abstract concepts get literal, embodied readings:** Gemini 3.5 Flash's distinctive move is to take an abstract required phrase and enact it physically, committing to the strangest available literal reading. Empathy in motion becomes actual load-sharing with a tree, and overriding instinct becomes paced breath against panic. Gemini 3.7 Flash (high) tends to translate the same abstractions into calibration and procedure, which reads cleaner but is less daring.
  - Story 0353, `gemini-3.5-flash`:
    > He had to physically embody the strain of the tree, moving with its silent, rigid suffering until they shared a single pulse.
    The required concept empathy in motion is interpreted as kinesthetic torque-sharing, an unconventional, fully committed reading rather than a decorative label.
- **C053 — Piety with a private stake:** Writer Gemini 3.5 Flash repeatedly plants self-interest inside apparently devotional projects: filial repair is motivated by self-preservation, penance is motivated by the need to be forgiven for having talked, and the archivist of other people's names turns out to be saving his own. Writer Gemini 3.7 Flash (high)'s protagonists are motivated outward — toward apprentices, prisoners, the dead partner's meaning — which is warmer but psychologically flatter.
  - Story 0326, `gemini-3.5-flash`:
    > The sole motivation of Maeve is to fetch wisdom from failure; she must understand the structural calculations that doomed his final, grand project.  To prevent his tragic destiny from becoming her own, she has to repair his broken digital mind.
    Mourning is reframed as risk management for the survivor. The daughter repairs her father partly to avoid inheriting his fate — an unsentimental motive the story does not flinch from.
  - Story 0038, `gemini-3.7-flash-high`:
    > Her intention was not merely to save herself, but to liberate every worker, diver, and researcher suffering in the iron belly of the trench.
    Gemini 3.7 Flash (high) explicitly upgrades the motive from self to collective; the sentence's structure ("not merely… but") shows the story correcting toward altruism rather than complicating it.
- **C012 — Form enacts the stated theme:** In Gemini 3.7 Flash (high)'s 0295 the decoding mechanism itself requires partnership — the inscription is a two-voice liturgy derived from mutually dependent stars — so "shared burdens" is demonstrated by the plot's logic, and the mentor's collapse is the theme's negative proof. In Gemini 3.5 Flash's 0295 the theme is stated ("We are all lanterns in the same dark") while the actual decoding is solitary and arbitrary: temple lines "perfectly matched the light curves of the variables," a visual coincidence with no interpretive necessity. Gemini 3.7 Flash (high) aligns structure with message; Gemini 3.5 Flash appends message to structure.
  - Story 0295, `gemini-3.7-flash-high`:
    > Every stanza required two complementary voices to complete its meter, just as the variable stars required one another to maintain their equilibrium.
    The required method (variable stars) generates the interpretation rather than merely resembling the cipher, and it dictates the ending: Elias must carry half the song to Mara. Gemini 3.5 Flash's match between inscriptions and light curves explains nothing about why matching equals meaning, and the villagers function as instruments of Jeremy's solo insight rather than as co-decoders.
- **C058 — Endings that turn back versus endings that summarize:** Gemini 3.5 Flash's strongest endings do work the body of the story did not: a reflexive reveal, an artifact that erases itself at the moment of success, a counter reset to one. Gemini 3.7 Flash (high)'s endings more often restate the theme as a portable proposition, adding articulation rather than information. This is a difference in what an ending is for.
  - Story 0159, `gemini-3.5-flash`:
    > He gasped, realizing his own name was indeed the last to be preserved, forever held in the custody of his glass creations.
    The reveal retroactively reinterprets the caretaker's entire routine and his relation to the museum's dead; the ending changes the meaning of what preceded it.
  - Story 0201, `gemini-3.7-flash-high`:
    > Mercy is not the passive subtraction of suffering, but the exact equilibrium where force meets endurance and refuses to perpetuate violence.
    An articulate thesis delivered as narration; it summarizes an idea the story has asserted rather than dramatized, and nothing in the preceding scene tested it.
- **C013 — Auditing the physics of a given metaphor:** Given the same abstract object-concepts, Gemini 3.7 Flash (high) derives the image's meaning from how the thing actually forms or behaves, so the metaphor carries argument; Gemini 3.5 Flash treats the same image as ornament and sometimes inverts its properties without noticing. This is a reasoning behavior, not a diction advantage — both writers have equal access to the vocabulary.
  - Story 0271, `gemini-3.7-flash-high`:
    > Deep behind the alarm rattling his ribcage, he located a pearl of stillness that he had spent years forming from sedimented grief.
    A pearl is literally an accretion around an irritant; Gemini 3.7 Flash (high) makes the calm object be built out of the wound, so the required phrase becomes a claim about how recovery works.
  - Story 0271, `gemini-3.5-flash`:
    > It was a mental space she had carefully cultivated over years of recovery, a tiny, frictionless sphere of pure awareness unaffected by the panic of her blood and nerves.
    Same required phrase, but "frictionless" and "unaffected" strip the pearl of its origin in irritation; the image becomes generic meditation language that contributes nothing the abstract noun didn't already say.
  - Story 0228, `gemini-3.7-flash-high`:
    > In a matter of hours, the rising tide would sweep through the lower channels, submerging the ledge beneath ten feet of foaming brine.
    Gemini 3.7 Flash (high) secures "temporary eternity" with a measured physical fact that guarantees destruction, making both halves of the paradox literally true.
- **C076 — Closure that cures the premise versus closure that keeps it standing:** A reversal of the control impression. Gemini 3.7 Flash (high)'s habitual ending is completed mastery, which often dissolves the tension the prompt specified; Gemini 3.5 Flash more often ends with the condition still operative or the payoff deliberately deferred, which better honors briefs built on unresolvable states or slowness.
  - Story 0051, `gemini-3.5-flash`:
    > She was boundary-lessly trapped within this task, an eternal spectator to the sorrows of a world she could no longer touch.
    The required attribute is still true at the end and has been deepened into a cost; the labor continues past the last line.
  - Story 0051, `gemini-3.7-flash-high`:
    > The weights were gathered, the geometric bones were set, and the cavern held its silence once more.
    Everything is inventoried and neutralized; the trapped, boundary-less quality has been eliminated rather than inhabited, and no residue remains.
  - Story 0391, `gemini-3.5-flash`:
    > The frozen lake remained intact for now, but beneath the ice, the revolution had begun.
    Deferred, incomplete payoff matches "a patient revolution" better than Gemini 3.7 Flash (high)'s same-night sabotage that has already stranded the enemy fleet.
- **C072 — Speculative rules that constrain behavior versus rules that decorate it:** Given identical premises, Gemini 3.7 Flash (high) derives consequences and keeps them consistent; Gemini 3.5 Flash states the premise vividly and then narrates actions the premise forbids. This is a causal-consistency difference, not a plausibility-of-magic difference.
  - Story 0093, `gemini-3.7-flash-high`:
    > This dense substance generated localized microgravitational wells, creating points of artificial drag where natural friction had failed.
    The invented substance is defined precisely as the missing physical property, so the object, the method, and the world-rule are one causal system.
  - Story 0093, `gemini-3.5-flash`:
    > Because there was no friction to hold the stones in place, Kaelen had to slide them with absolute precision, letting their own momentum lock them into the sequence.
    The clause correctly identifies the problem and then solves it with the one thing that cannot work without friction; two sentences later a rock "clicked into the spiral." The rule is scenery.
- **C009 — Healing modeled as distributed tempering rather than solitary ingestion:** In Gemini 3.5 Flash's 0035 the healer absorbs the community's remorse into his own body alone and re-seals himself behind gloves; the beneficiaries are abstract "descendants." In Gemini 3.7 Flash (high)'s 0035 the healer cooks the same remorse into a broth served to the whole garrison, and the closing image is two soldiers touching without contagion. Gemini 3.7 Flash (high) explicitly distinguishes tempering from erasure, an ethical nuance Gemini 3.5 Flash's sin-eater model lacks, and the resolution removes the need for the barrier rather than restoring it.
  - Story 0035, `gemini-3.7-flash-high`:
    > He did not seek to erase what these men had done or suffered, only to buff down the serrated edges until their sorrow became sturdy and bearable.
    The stated ethic preserves memory while changing its texture, and the plot enacts it communally: "A guard reached out to steady his trembling companion, and for the first time in months, no panic flared across their touching fingers." Gemini 3.5 Flash's parallel passage — "he had to fully subsume the essence of their shame into his own consciousness" — concentrates all cost in one sealed-off body and ends with the gloves going back on.
- **C021 — Friction instead of cleansing:** Gemini 3.7 Flash (high)’s strongest transformations interfere with deterministic systems without pretending that history can be cleanly removed. In Story 0283, the hourglass continues operating, but its single stream becomes plural and irregular. Gemini 3.5 Flash resolves the same conflict by shattering the governing object. Gemini 3.7 Flash (high)’s version manifests structural intelligence: agency emerges through changed constraints, not merely the disappearance of constraint.
  - Story 0283, `gemini-3.7-flash-high`:
    > The iron sand did not empty, nor did the mechanism fully stop; instead, the stream divided into dozens of chaotic, dancing trickles that drifted sideways through the amber light.
    The altered mechanism retains sand, time, and inherited machinery while producing multiple trajectories. The physical operation embodies plural possibility rather than merely naming it.
  - Story 0283, `gemini-3.5-flash`:
    > Instead of turning it to reset the old cycle of destiny, he tilts it on its side, shattering the glass.
    Gemini 3.5 Flash’s action is vivid and decisive, but it equates freedom with total rupture. That supplies mythic release rather than Gemini 3.7 Flash (high)’s more complicated model of living within altered historical machinery.
- **C010 — Wisdom priced in self-revision instead of transmitted intact:** In Gemini 3.7 Flash (high)'s 0180 the father is wrong for most of the story — paralyzed by doctrine — and is corrected by his daughter's impatience, so the central insight is purchased by abandoning a held belief; even his knot changes, a fisherman's knot replacing the "forbidden liturgical seal." In Gemini 3.5 Flash's 0180 the father begins wise and delivers a finished lecture while the narration labels it "accidental wisdom" although nothing accidental occurs. Gemini 3.7 Flash (high) dramatizes the required tone; Gemini 3.5 Flash annotates it.
  - Story 0180, `gemini-3.7-flash-high`:
    > He had spent decades believing fidelity meant constructing unbreakable cages, yet nature survived entirely on deciduous vows.
    The aphorism is earned because the plot first shows the cost of the discarded belief and gives the daughter the corrective line, "No tree wants an eternal bind, you stubborn old fossil." Gemini 3.5 Flash's counterpart — "Contracts are like iron, Maeve; they are rigid, and when the cold wind blows or the earth shifts, they snap completely" — is a fine metaphor delivered by a character who never risks being wrong.
- **C028 — Wisdom produced by opposition versus delivered by question-and-answer:** Gemini 3.7 Flash (high)'s accidental wisdom is generated by a genuine hierarchy inversion: the feisty daughter's pragmatic retort teaches the father, so the accident is diegetically real and the generational bridge runs upward. Gemini 3.5 Flash's wisdom is a prepared lecture triggered by a feed line, while narration asserts the accidental tone the scene contradicts.
  - Story 0180, `gemini-3.7-flash-high`:
    > No tree wants an eternal bind, you stubborn old fossil
    The daughter's impatient practicality, capped by it just needs to hold until spring, is the actual source of the father's revelation, making the wisdom genuinely accidental.
  - Story 0180, `gemini-3.5-flash`:
    > What are deciduous vows?
    The daughter kneels closer and supplies a prompt so the father can explain; narration then labels his prepared speech with the quiet warmth of accidental wisdom, asserting a tone the scene does not produce.
- **C038 — Shared failure mode: asserted rigor as a stand-in for thought:** Both writers decorate intellectual subject matter with unearned authority, describing arguments as elegant, paradoxical or rigorous without producing content. The tic is more conspicuous in Gemini 3.7 Flash (high) because Gemini 3.7 Flash (high) claims more, but Gemini 3.7 Flash (high) is also the only one that converts an abstraction into observable data, so the behavior is not evenly diagnostic.
  - Story 0241, `gemini-3.7-flash-high`:
    > He had proven, with astonishing elegance, that love was the only bet where the expected loss never diminished the player's intrinsic worth.
    A theorem is announced as elegant and proven while being mathematically vacuous. The reader is asked to accept a display of rigor as its own payoff.
  - Story 0241, `gemini-3.5-flash`:
    > she had sketched the paradoxical equations of lucid contradictions, those mathematical proofs where opposing truths could exist in perfect, shimmering harmony.
    Identical move on Gemini 3.5 Flash's side: an appeal to nonexistent proofs plus aesthetic adjectives. Neither writer's mathematics survives inspection, so polish and jargon should not be read as conceptual strength for either.
- **C051 — Totalizing finales:** Neither writer consistently resists inflated closure. Both often scale one character’s symbolic victory into world renewal and certify internal completion in the final sentences. This shared habit reduces ambiguity and makes their endings less discriminating than their middle passages.
  - Story 0329, `gemini-3.7-flash-high`:
    > The tarnished world had begun to breathe again, its mechanical slumber broken by the irrepressible pulse of art and life intertwined.  She tucked her bow beneath her arm and smiled, ready to play for an empire reborn.
    A single performance is immediately promoted into the rebirth of an empire, with little attention to political or material aftermath.
  - Story 0329, `gemini-3.5-flash`:
    > The tarnished world was washing away, replaced by the vibrant, messy splendor of true life.  Lyra closed her eyes, her bow still dancing to her heartbeat, finally whole.
    Gemini 3.5 Flash similarly declares both systemic purification and total personal integration, resolving the story at maximum thematic amplitude.
- **C064 — Closure without residue:** Neither writer consistently demonstrates greater emotional maturity in endings. Both often equate truthful expression with complete dissolution of distrust, compressing recovery into a single beautiful phenomenon. The high lyric finish can obscure how little resentment, uncertainty, or renegotiation survives the climax.
  - Story 0016, `gemini-3.7-flash-high`:
    > The chord resonated with radiant clarity, washing away the bitter sediment of five wasted years in an overwhelming surge of harmony.
    Gemini 3.7 Flash (high)'s carefully specified conflict is resolved by total emotional cleansing, reducing the durable consequences of five years of estrangement.
  - Story 0016, `gemini-3.5-flash`:
    > Lyra looked at Elian, her eyes shimmering with unshed tears, the heavy wall of distrust completely dissolved by the magical, honest harmony.
    Gemini 3.5 Flash uses almost the same absolute model: magical verification leaves no meaningful remainder of mistrust.
- **C066 — Opposition that runs on reasons:** Gemini 3.7 Flash (high)'s antagonists and obstacles act on traceable causes: surveillance detects a power surge, a captain weighs bearer bonds against a firing squad, an archivist argues a position. Gemini 3.5 Flash's opposition more often dissolves on schedule or behaves as the theme requires. The textual signature is whether the story supplies the opponent's reason at the moment it acts, before the effect it explains.
  - Story 0197, `gemini-3.7-flash-high`:
    > They had registered the analog power surge on their monitors.
    The pursuit is triggered by the protagonist's own necessary action, closing a cause-effect loop; in Gemini 3.5 Flash's matching story the soldiers abandon the hunt because "They believed she had drowned, or perhaps she had never existed at all" (Gemini 3.5 Flash, 197), a whim that serves the invisibility theme instead of logic.
- **C054 — Bureaucratic and logistical imagination:** Writer Gemini 3.7 Flash (high) consistently populates its worlds with institutions that behave like institutions — agencies, recalls, registries, evacuation crowds with injured people in them — and draws thematic conclusions from that machinery. Writer Gemini 3.5 Flash registers the same institutions as atmosphere or as sudden violence, without procedure.
  - Story 0281, `gemini-3.7-flash-high`:
    > He had been proven right when the federal agency announced the telepathy pill recall, pulling the neural capsules from every pharmacy shelf after thousands of users suffered cognitive feedback loops.
    A recall is given the correct actors, mechanism, and adverse-event rationale in one sentence, making the science-fiction premise institutionally legible.
  - Story 0326, `gemini-3.7-flash-high`:
    > The clerical error on his death certificate had taught him that life could not be verified by bureaucratic consensus, just as her dispersion proved consciousness could not be hoarded without loss.
    Gemini 3.7 Flash (high) extracts a conceptual proposition from the bureaucratic premise rather than using it as backstory colour, linking the civic and digital deaths through a shared logic of verification.
- **C082 — Persuasion before enchantment:** Story 0139 reverses Gemini 3.7 Flash (high)’s usual causal advantage. Gemini 3.5 Flash gives the officer political and personal reasons to cooperate: regime instability, elite realignment, and danger to himself. Gemini 3.7 Flash (high) instead makes an enchanted pigment directly dissolve obstinacy. Gemini 3.5 Flash’s negotiation is still compressed, but it grants the antagonist more psychological agency.
  - Story 0139, `gemini-3.5-flash`:
    > She detailed the imminent collapse of the regime, the shifting alliances of his superiors, and the exact probability of his execution should he return with the scientist alive.
    Vance’s decision responds to incentives embedded in the political situation rather than to Clara’s charisma alone.
  - Story 0139, `gemini-3.7-flash-high`:
    > The officer suddenly paused, his fierce glare fracturing into open contemplation as the vapor acted upon his stubborn mind.
    The literal mind-altering vapor shortcuts the difficult work of changing an ideologue’s judgment and compromises the apparent fairness of the bargain.
  - Story 0139, `gemini-3.5-flash`:
    > She presented Vance with a meticulously forged death certificate, but as she spoke, she laid out the stark, mathematical reality of his own position.
    This exposes Gemini 3.5 Flash’s own control problem: a protagonist defined by non-deception still relies on a forgery, and the story does not examine that contradiction.
- **C089 — Gemini 3.5 Flash builds jeopardy machinery that never engages; Gemini 3.7 Flash (high) builds none:** Gemini 3.5 Flash is the only writer who supplies external opposition, but in every instance the threat is offstage, retreating, or deferred past the last sentence, so the machinery adds nomenclature rather than pressure. Gemini 3.7 Flash (high) mostly declines opposition entirely, substituting interpretive or thermal difficulty. These are opposite structural weaknesses, not a hierarchy.
  - Story 0143, `gemini-3.5-flash`:
    > The chemical reaction was progressing exactly as planned, signaling that the final patrol had retreated to the base camp.
    Patrols, spotlights and a lockdown are established, then dismissed in one clause; the vigil proceeds unobstructed, so the security apparatus functions as set dressing.
  - Story 0143, `gemini-3.7-flash-high`:
    > She had to outlast the numbing freeze just long enough to catch the first sliver of solar dawn across the crevasse.
    Gemini 3.7 Flash (high)'s sole antagonist is temperature, and it never actually endangers her; the story is an uninterrupted competent procedure. Gemini 3.7 Flash (high) avoids Gemini 3.5 Flash's failure only by not attempting the thing.
- **C005 — Attribute migration and visible scaffolding:** Gemini 3.7 Flash (high) often metabolizes prompt language by relocating it into the story world, which can create irony but sometimes assigns the required attribute to the wrong entity. Gemini 3.5 Flash preserves literal character compliance, yet occasionally repeats the supplied phrase so explicitly that the prompt seam remains visible. This is a tradeoff between transformation and fidelity, not simple control versus clumsiness.
  - Story 0395, `gemini-3.7-flash-high`:
    > She was brightly attentive, her synthetic gaze radiating a polished enthusiasm designed to mask the cold severity of corporate oversight.
    The required brightness becomes the surveillance avatar’s weaponized corporate friendliness. That is conceptually productive, but the designated character is Silas, not Iris.
  - Story 0231, `gemini-3.7-flash-high`:
    > A softly persistent hum rose from the desiccated stem, vibrating against his skull like a distant cello string.
    Gemini 3.7 Flash (high) again transfers an adjectival attribute from protagonist to object. The phrase becomes sensory and atmospheric, but literal character specification is weakened.
  - Story 0231, `gemini-3.5-flash`:
    > Instead, he had to employ his softly persistent nature.  His softly persistent curiosity was not one of loud demands or frantic searching, but a quiet, patient wait for the truth to seep through.
    Gemini 3.5 Flash unambiguously assigns the attribute to Barnaby and defines it behaviorally, but the immediate repetition reads as requirement management rather than discovered characterization.
- **C031 — Grammatical control where prompt text meets prose:** Gemini 3.5 Flash shows repeated tense wobble and a misfitted connective precisely at the seams where prompt phrasing enters the sentence, indicating transplant rather than rewriting. Gemini 3.7 Flash (high), though denser and sometimes purple, keeps syntax under control. This is low-order evidence, useful mainly as corroboration of the paste-versus-rewrite process behind the deeper integration gap.
  - Story 0379, `gemini-3.5-flash`:
    > the peace began to fracture when the outside world intrudes, bringing the distant screech of commuter trains
    Past-tense narration collides with the prompt's present-tense timeframe phrasing, preserved unconjugated at the exact point of insertion.
  - Story 0263, `gemini-3.5-flash`:
    > Because she hears unspoken words, she captured the silent, desperate thoughts of the village sleeping below.
    The present-tense attribute is followed by a past-tense main clause in the same breath, a seam visible only because the attribute slot was copied rather than recast.
- **C084 — Props that undergo conversion:** Gemini 3.7 Flash (high) more often lets a required object undergo a state change that records the story’s moral or psychological transition. The hangman’s dice leave the prison’s economy of terror; the mask strap is deliberately released after Kaelen rejects his captors’ accounting. This “prop metabolism” gives objects structural work beyond serving as repeatedly explained symbols.
  - Story 0038, `gemini-3.7-flash-high`:
    > The hangman's dice bounced from the tilting copper desk, falling down a drainage conduit into the abyss where their morbid authority could hold sway no longer.
    The object’s physical removal coincides with the collapse of the wardens’ arbitrary power, completing a plot-level transformation.
  - Story 0201, `gemini-3.7-flash-high`:
    > He uncurls his fingers and releases the pewter mask strap into the howling violet updraft, watching the remnant of his captivity dissolve into the light.
    The changed handling of the strap makes Kaelen’s altered relation to captivity visible without requiring another explanation of what the strap represents.
- **C030 — Verb-slot fusion: Gemini 3.5 Flash's distinctive inventive strength:** When the required element is an action, Gemini 3.5 Flash shows a talent Gemini 3.7 Flash (high) lacks for collapsing act and method into a single gesture, so the means becomes the end. Gemini 3.7 Flash (high) performs the same elements sequentially, work first, reward after. This is a real structural virtue that pairwise plot-checking would miss because both versions technically include the elements.
  - Story 0263, `gemini-3.5-flash`:
    > She sought this rest by tracing the path of falling stars across the velvet sky.
    Rest is not a reward after the task but is produced by the required method itself; tracing the meteors quiets her mind, one motion satisfying two prompt slots with causal elegance.
  - Story 0263, `gemini-3.7-flash-high`:
    > Having completed his solitary vigil across the uncounted nights, he finally permits himself to rest beside the quiet portal.
    Gemini 3.7 Flash (high)'s rest arrives only after the work is finished, a conventional sequence; competent, but the action and method remain separate parts bolted together.
- **C015 — Finding the friction between required elements:** Gemini 3.5 Flash more often notices when two assigned elements contradict each other and keeps the contradiction as the story's pressure; Gemini 3.7 Flash (high) more often resolves the contradiction offstage so nothing is at stake. This is a reversal of the general pattern and matters because it concerns plot tension rather than texture.
  - Story 0146, `gemini-3.5-flash`:
    > Time was running out, yet Silas remained infinitely patient, knowing that the slightest rush would shatter the fragile equilibrium of the valley.
    Gemini 3.5 Flash reads "before the collapse" as a deadline and collides it with "infinitely patient," so patience becomes a costly discipline rather than a temperament.
  - Story 0146, `gemini-3.7-flash-high`:
    > Decades had passed since the catastrophe, yet Sylvan remained infinitely patient, moving with the measured deliberation of deep water.
    Gemini 3.7 Flash (high) relocates the collapse into backstory; with no clock running, the "yet" is rhetorical and patience costs the hero nothing. Gemini 3.7 Flash (high) compensates with etiology and risk elsewhere, but the central tension is dissolved.
  - Story 0271, `gemini-3.5-flash`:
    > It was merely an automated research drone monitoring coastal erosion, but Layla's body did not make the distinction.
    Gemini 3.5 Flash selects the one stimulus that is physically identical to the original trauma agent, which sharpens the point about somatic markers; Gemini 3.7 Flash (high)'s chosen trigger, "a maritime patrol aircraft," is plausible but generic.
- **C048 — Repair without absolution:** In the navigator pair, Gemini 3.5 Flash distinguishes renewed action from complete self-forgiveness. Gemini 3.7 Flash (high) makes the rescue journey more causally robust, but then converts it into permanent faith and total dissolution of regret. Gemini 3.5 Flash’s smaller emotional claim produces the more mature psychology.
  - Story 0087, `gemini-3.5-flash`:
    > She did not know if she could ever fully forgive herself, but she knew she could no longer live in this state of suspended animation.
    Maeve can choose movement while remaining morally and emotionally unresolved. Action is not treated as automatic absolution for deaths in her past.
  - Story 0087, `gemini-3.7-flash-high`:
    > The flickering faith that had sustained his journey across the fog began to steady into something permanent.  As he climbed onto the dock, the backlash of regrets finally dissolved into the clean, cold Atlantic wind.
    The atmospheric metaphor abruptly certifies a permanent cure. It compresses guilt, courage, rescue, and self-forgiveness into one successful crossing.
- **C050 — The ethics of merged selves:** In the entangled-memory pair, Gemini 3.7 Flash (high) imagines liberation as perfect fusion and the surrender of individual identity. Gemini 3.5 Flash leaves Lyra embodied, depleted, and vulnerable after freeing Caleb. Gemini 3.5 Flash’s version is conceptually more attentive to the possibility that intimacy and shared dreaming need not culminate in self-annihilation.
  - Story 0249, `gemini-3.7-flash-high`:
    > With one final, decisive blow against the stone, Kael surrendered the last piece of his isolated identity to the sound wave garden.
    The triumphant diction treats the extinction of separateness as an uncomplicated completion of freedom, despite the story beginning with coerced neural fusion.
  - Story 0249, `gemini-3.5-flash`:
    > The scientists would find her here in the morning, exhausted and silent, but they would never be able to reclaim the boy she had sung back to life.
    Lyra pays a bodily cost but remains a distinct person facing future consequences. The shared dream produces release rather than permanent absorption.
- **C091 — Gemini 3.5 Flash's one act of premise-selection outperforms Gemini 3.7 Flash (high)'s whole approach in that prompt:** Faced with "crater inspector," "moonlit summit," "space age," Gemini 3.5 Flash declines the literal lunar reading and sets the story at a terrestrial impact crater about to be bulldozed into a simulated moon for astronaut training — a real historical practice, and an irony that makes every required element do double duty. Gemini 3.7 Flash (high), who clearly holds the same Apollo-era knowledge, spends it as set dressing.
  - Story 0143, `gemini-3.5-flash`:
    > Tomorrow, the government would hand this pristine geological marvel over to the military to train astronauts, churning the ancient basin into a simulated lunar wasteland.
    The premise converts "moonlit summit" into an irony (a real crater destroyed to imitate the moon) and makes the loss historically specific rather than generic; desert varnish is also a genuinely slow-forming thing, which earns "last of something precious."
  - Story 0143, `gemini-3.7-flash-high`:
    > Now, she stood upon the moonlit summit of Mount Marilyn, where Earth's blue radiance washed over the jagged regolith
    Mount Marilyn is an Apollo landmark, so Gemini 3.7 Flash (high) has the same reference pool, but uses it as a name only; the phrase "moonlit summit" on the moon is left as an unresolved contradiction that Earthlight only partly patches.
- **C022 — Inquiry actually traveled:** Story 0241 is an important reversal. Gemini 3.5 Flash dramatizes the required traversal as a sequence of discoveries, transfers, calculations, and changed interpretations. Gemini 3.7 Flash (high) places Elena in the library after the transit work and reports most of the investigation retrospectively. Gemini 3.5 Flash therefore displays better local structural control: the method becomes plot rather than résumé.
  - Story 0241, `gemini-3.5-flash`:
    > On the next train, she found another clue scrawled on a corner seat: a formula for calculating ruin, juxtaposed with a quote about infinite hope.
    The clue appears during movement and changes Maeve’s understanding while the reader accompanies her. Required objects and concepts participate in an unfolding investigation.
  - Story 0241, `gemini-3.7-flash-high`:
    > To traverse those subterranean lines by interpreting cryptic scrawls on subway seats had not been an act of grief-stricken madness, but a rigorous fieldwork of empathy.
    Gemini 3.7 Flash (high) gives the journey a sophisticated interpretation, but the retrospective declaration replaces much of the journey’s dramatic and causal labor.
- **C033 — Absence built as structure versus absence asserted as mood:** Instructed to "investigate by observing gaps," Gemini 3.7 Flash (high) renders absence as a series of social non-events across a life and makes the central object an ungiven gift; Gemini 3.5 Flash converts gaps into forensic traces of presence and then switches to an announced psychic gift, so the method stops determining the discovery.
  - Story 0231, `gemini-3.7-flash-high`:
    > In the stranger's recollection of a crowded alpine festival, there were laughing faces, raised earthenware mugs, and fiddle tunes, yet no hands touched the traveler's shoulders.
    The gap is a specific missing behavior inside a fully rendered scene. The method named by the prompt is what actually yields the information, and the technique repeats with an empty chair, a bare mantle, one teacup.
  - Story 0231, `gemini-3.5-flash`:
    > He noted the blank patch on the wooden railing where the ocean spray had been brushed away by a gripping hand.
    This is evidence of presence, not absence — a smudge left by a hand. Gemini 3.5 Flash's "gaps" are ordinary clues relabeled, and the real revelation arrives via an unearned faculty announced as "a strange talent he possessed."
- **C079 — Liberation as coordinated labor:** Gemini 3.7 Flash (high) has the stronger social imagination in 0038. Liberation requires a dancer, an apprentice who remembers instructions, vulnerable prisoners, and evacuation infrastructure. Gemini 3.5 Flash constructs a more private alliance between Lyra and a machine mind. That intimacy is valid, but Gemini 3.7 Flash (high) better understands escape as distributed labor rather than a gifted protagonist’s singular masterpiece.
  - Story 0038, `gemini-3.7-flash-high`:
    > Her intention was not merely to save herself, but to liberate every worker, diver, and researcher suffering in the iron belly of the trench.
    The widened constituency is subsequently supported by Julian operating the manifold and by the evacuation of elderly and injured prisoners, so it is more than a declaration of benevolence.
  - Story 0038, `gemini-3.5-flash`:
    > Lyra knew she must liberate both herself and this ancient intelligence before the facility collapsed under the immense ocean pressure.
    Gemini 3.5 Flash’s stakes remain focused on two exceptional beings, and the machine’s understanding largely substitutes for the difficult coordination among captives that Gemini 3.7 Flash (high) stages.
- **C078 — Symptoms that alter the route:** Gemini 3.7 Flash (high) more consistently converts an unusual bodily attribute into consequential navigation. In 0201, trauma responses identify hazards and proprioception governs the act of bracing. Gemini 3.5 Flash renders the same body through an evocative mathematical vocabulary, but most reactions are catalogued rather than used to change an external situation.
  - Story 0201, `gemini-3.7-flash-high`:
    > A sudden phantom spasm in his left quadricep recalls the cold iron bench set at thirty degrees, directing him away from a hidden chasm.  A reflexive tightness in his thoracic cage mirrors the old airless isolation tubes, warning him of a deadly pocket of concentrated gas between two phosphorescent trunks.
    Each trauma response supplies specific information, changes Kaelen’s route, and makes damaged embodiment into practical intelligence rather than atmosphere alone.
  - Story 0201, `gemini-3.5-flash`:
    > Every flinch was a vector; every shudder was a coefficient in his grand equation.
    Gemini 3.5 Flash establishes a strong conceptual lexicon, but the vectors and coefficients remain metaphorical; the story never demonstrates what they calculate as concretely as Gemini 3.7 Flash (high)’s chasm and gas pocket do.
- **C063 — Empathy with a wrench:** In story 0350, Gemini 3.7 Flash (high) makes empathy diagnostic rather than merely soothing. Thomas hears loneliness, identifies a frayed governor cable, repairs the throttle, and restores the elevator's useful circulation. Gemini 3.5 Flash creates a persuasive acoustic dialogue and changes the town's perception, but the abandoned machine is primarily pacified into silence rather than materially rehabilitated.
  - Story 0350, `gemini-3.7-flash-high`:
    > He tied off the shuddering cable and hooked the cuckoo clock weight directly onto the intake valve lever.  Instantly, the pendulum physics of the clockmaker's art pulled the thrashing throttle into a smooth, measured rhythm.
    The weight has a legible mechanical role, and compassionate listening leads to a targeted intervention rather than serving as the entire cure.
  - Story 0350, `gemini-3.7-flash-high`:
    > Thomas rested his palm against the warm, vibrating concrete wall and felt the steady, peaceful pulse of wheat moving through restored elevators.
    Rehabilitation includes renewed function. The metaphorical bridge is supported by restored material circulation between agricultural labor and the scholarly tower.
  - Story 0350, `gemini-3.5-flash`:
    > Below, in the darkened town, lights began to flicker on as residents leaned out of windows, no longer afraid of the giant structure.
    Gemini 3.5 Flash does provide a genuine social consequence: the song revises communal perception. What remains less developed is the silo's practical relation to that community after the performance.
- **C060 — Rest becomes an address:** In story 0100, Gemini 3.7 Flash (high) understands the motivation as a design problem: wandering signals require not only removal but a durable destination. The lens gathers them, the ledger translates them, and inscription gives them permanence. Gemini 3.5 Flash's lens removes the disruptive signals effectively, but sending them into the upper ocean is less closely aligned with giving rest an address.
  - Story 0100, `gemini-3.7-flash-high`:
    > He opened the master mortuary ledger, an ancient folio bound in cured leather, and angled the primary prism directly down onto its vellum pages.  The concentrated beam burned each chaotic frequency into the paper, transcribing every frantic signal into quiet, permanent script.
    The object, action, setting, and motivation converge in one operation: an undertaker working in a library converts homeless cries into catalogued, lasting entries.
  - Story 0100, `gemini-3.5-flash`:
    > The beam shot straight upward through the library's glass dome, carrying the desperate cries of the living away into the empty, black void of the upper ocean.
    Gemini 3.5 Flash supplies a clear solution to the noise, but the cries are displaced into a void rather than housed. The semantic connection to a permanent address is consequently weaker.
- **C061 — Counterfactual hospitality:** Gemini 3.7 Flash (high) treats minor unrealized desires as morally significant alternatives to plot. The novelist's restraint is not passivity: he refuses to revise outcomes but notices the small lives that canonical drama suppresses. This is selective intelligence, shown by choosing hopes that contradict each character's assigned genre function.
  - Story 0048, `gemini-3.7-flash-high`:
    > The story demanded blood and neat resolutions, but he sought to honor the quiet longings that canonical endings always crushed.
    The sentence establishes a conceptual conflict between plot efficiency and humane attention rather than simply opposing tragedy and happiness.
  - Story 0048, `gemini-3.7-flash-high`:
    > There, a rebellious debutante dreamed not of the grand marriage the chapter demanded, but of a quiet studio full of unfinished canvases.
    The hope is concrete and revisionary: it opposes both the marriage plot and the simplified identity of the stock rebel, replacing triumph with unfinished private work.
- **C042 — Belief systems are given causal mechanisms, not just debunked:** Where a legend appears, Gemini 3.7 Flash (high) explains why the legend survives in physical terms, closing the loop between folklore and fact. Gemini 3.5 Flash debunks by attribution alone: the curse is propaganda spread to deter thieves, which leaves the reported sicknesses unexplained. Gemini 3.7 Flash (high)'s version shows explanatory intelligence about how myths self-seal.
  - Story 0388, `gemini-3.7-flash-high`:
    > The sickness attributed to the curse was merely the unshielded ionizing discharge emitted whenever the casing was opened without the proper grounding shunt.
    The myth's evidence is given a mechanism, so the superstition becomes an inevitable byproduct of the machine, a genuinely perceptive piece of social-causal reasoning.
- **C067 — Verdict reveals vs. evidence reveals:** Both 205 stories must settle an archaeological dispute about a lost civilization. Gemini 3.5 Flash's projection delivers a total verdict — "no chains," harmony with the cosmos — and the narration certifies it as "undeniably real," foreclosing the doubt a one-sided projection should raise. Gemini 3.7 Flash (high)'s projection delivers data the size of real archaeology and must survive a skeptic onstage ("You romanticize a slaughterhouse," Gemini 3.7 Flash (high), 205); Gemini 3.5 Flash's skeptic is an offstage Ministry that never gets a sentence. Gemini 3.7 Flash (high)'s reveal persuades; Gemini 3.5 Flash's announces.
  - Story 0205, `gemini-3.7-flash-high`:
    > Instead, they mapped the names of common gardeners, weavers, and children who had tended the asteroid's hanging orchards while the stars grew cold.
    Domestic, modest evidence is what could actually settle a dispute, and it visibly converts the present opponent ("her clinical certainty faltering"); the conclusion is earned rather than asserted.
- **C087 — Gemini 3.7 Flash (high) permits a gap between narrator and protagonist; Gemini 3.5 Flash closes it:** Gemini 3.7 Flash (high) occasionally characterizes its heroes' virtues as tics or compulsions, and lets an ending register that a position was chosen rather than proved. Gemini 3.5 Flash's protagonists are ratified by events: the world shows them exactly what they hoped to see. This is a stance difference, not a skill difference in sentence-making.
  - Story 0205, `gemini-3.7-flash-high`:
    > He retained only his notebooks, his elegies, and the incurable habit of framing catastrophe as meter.
    "Incurable habit" treats the required attribute "poetically inclined" as a symptom, creating distance between the telling and the told.
  - Story 0205, `gemini-3.5-flash`:
    > There were no chains, no tyrannical overseers as the Ministry claimed, only a society that lived in harmony with the cosmos.
    The recovered evidence is precisely the protagonist's wish, with no residue or friction; the narration underwrites his hope as fact rather than dramatizing the risk of motivated reading. Gemini 3.7 Flash (high)'s counterpart evidence — a list of gardeners, weavers and children — is the kind of thing archives actually contain.
- **C002 — Two architectures of absence:** Both writers make “gaps” operative, but Gemini 3.7 Flash (high) reads socially structured omissions inside memories, while Gemini 3.5 Flash reads measurable discontinuities in physical space. Gemini 3.7 Flash (high)’s mode is relational and curatorial; Gemini 3.5 Flash’s is forensic and spatial. These are distinct kinds of perceptiveness, and neither is consistently superior.
  - Story 0231, `gemini-3.7-flash-high`:
    > In the vivid memory of an ornate wedding banquet, a chair beside the traveler remained completely empty, carved into the air like a hollow phantom.
    The absent chair is not merely missing data; its conspicuous placement reveals a relationship organized around exclusion or bereavement. Gemini 3.7 Flash (high) treats omission as a composed social fact.
  - Story 0231, `gemini-3.5-flash`:
    > He measured the exact distance between the last wet boot print and the edge of the drop, finding a sudden, empty interval that suggested a deliberate step rather than a slip.
    Gemini 3.5 Flash turns negative space into a physical inference about agency. The clue is more concrete than Gemini 3.7 Flash (high)’s psychic evidence and carefully limits itself, at first, to what the interval “suggested.”
- **C044 — Prompt images get inverted rather than merely illustrated:** Gemini 3.7 Flash (high) is willing to bend a prompt's literal image into a fresher configuration while quietly solving the technical problem the bend creates. A moonlit summit becomes a summit on the moon, lit by Earth; a crater inspector inspects lunar craters. Gemini 3.5 Flash reads prompts at face value, Earth settings, conventional stakes, which is safer and sometimes more faithful.
  - Story 0143, `gemini-3.7-flash-high`:
    > Now, she stood upon the moonlit summit of Mount Marilyn, where Earth's blue radiance washed over the jagged regolith in pale, lonely ripples.
    The required phrase is honored by inversion: the summit is the moon's, and the illumination problem is solved with earthlight, showing conceptual agility rather than compliance.
- **C045 — Payoffs radiate outward instead of returning to the protagonist:** Gemini 3.7 Flash (high)'s climaxes tend to enlarge the beneficiary: one grafted tree becomes a chorus of tuned trunks, one strummed chord turns the whole grove into an instrument, one debunking becomes a teachable, replicable technology. Gemini 3.5 Flash's payoffs more often return to the protagonist's own peace, keepsake, or private chord. This directionality of benefit is something standard rubrics have no vocabulary for.
  - Story 0353, `gemini-3.7-flash-high`:
    > The grove had become an immense, living instrument, holding a sustained chord that defied the mute centuries.
    The achievement belongs to the whole grove, converting a personal performance into a communal, persisting condition of the world.
- **C025 — Agency priced, not merely praised:** At its best, Gemini 3.7 Flash (high)’s conceptual intelligence distinguishes the irrationality of gambling from the genuine psychological good the gambler may be purchasing. This is more discriminating than simply opposing order and chaos: a choice can be mathematically losing while still supplying a temporary experience of agency. Gemini 3.5 Flash’s corresponding formulation remains broad and inspirational.
  - Story 0241, `gemini-3.7-flash-high`:
    > Yet her research refused to dismiss the gambler as merely foolish; instead, she explored lucid contradictions where an agent willingly accepts negative expectation to purchase fleeting moments of agency.
    The passage models contradictory behavior without either endorsing addiction or reducing it to stupidity. Its intelligence lies in separating financial outcome from experienced agency, not merely in using technical terms.
  - Story 0241, `gemini-3.5-flash`:
    > Instead, she sought to widen perspectives responsibly, teaching her students that chaos was not an enemy to defeat, but a partner to understand.
    Gemini 3.5 Flash offers a humane stance, but “chaos” and “partner” do not identify what the gambler gains, what it costs, or why a rationally informed person might still choose it.
- **C069 — Attribute as chemistry vs. attribute as character:** Required to make something liquefy rigid thinking, the writers split: Gemini 3.7 Flash (high) literalizes the attribute into the ink's fumes so the plot can turn on a chemical; Gemini 3.5 Flash metaphorizes it into Clara's voice so the plot must turn on persuasion. Both then assert the effect rather than fully dramatize a mind changing. Gemini 3.7 Flash (high)'s move is more integrated but purchasable as gimmick; Gemini 3.5 Flash's is more realistic but replaces the hardest scene with a summary of the argument.
  - Story 0139, `gemini-3.7-flash-high`:
    > a rare distillation that liquefies rigid thinking whenever an ideologue breathes its fumes
    The abstract attribute becomes a property of the required object, an elegant compliance trick that also conveniently removes the need to write the persuasion; Gemini 3.5 Flash's matching line, "a true frequency that liquefies rigid thinking" (Gemini 3.5 Flash, 139), keeps the burden on character but discharges it in narration.

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0006 | +2.083 | 716 | 693 | 3 | 0.167 |
| 0016 | +2.517 | 722 | 687 | 3 | 0.300 |
| 0034 | +2.783 | 787 | 686 | 3 | 0.233 |
| 0035 | +1.617 | 738 | 710 | 3 | 1.433 |
| 0038 | +1.967 | 748 | 617 | 3 | 0.600 |
| 0044 | +2.117 | 722 | 648 | 3 | 0.567 |
| 0047 | -0.117 | 669 | 667 | 3 | 1.433 |
| 0048 | +0.917 | 710 | 660 | 3 | 2.033 |
| 0051 | +2.350 | 692 | 673 | 3 | 0.500 |
| 0064 | +2.467 | 676 | 678 | 3 | 0.733 |
| 0087 | +2.717 | 749 | 726 | 3 | 0.100 |
| 0093 | +1.800 | 686 | 626 | 3 | 0.400 |
| 0098 | -1.400 | 670 | 699 | 3 | 0.667 |
| 0100 | +2.233 | 686 | 663 | 3 | 0.267 |
| 0103 | +2.583 | 736 | 638 | 3 | 0.167 |
| 0139 | +1.883 | 705 | 651 | 3 | 0.433 |
| 0143 | +2.800 | 711 | 702 | 3 | 0.400 |
| 0146 | +1.917 | 685 | 624 | 3 | 1.833 |
| 0147 | +2.083 | 684 | 650 | 3 | 0.500 |
| 0159 | -0.700 | 713 | 706 | 3 | 1.733 |
| 0163 | -0.800 | 661 | 693 | 3 | 0.733 |
| 0177 | -1.617 | 675 | 664 | 3 | 0.233 |
| 0180 | +2.417 | 678 | 760 | 3 | 0.167 |
| 0197 | +1.783 | 693 | 647 | 3 | 0.433 |
| 0201 | +2.550 | 643 | 730 | 3 | 0.767 |
| 0205 | +2.300 | 726 | 661 | 3 | 0.400 |
| 0213 | +2.117 | 692 | 667 | 3 | 1.567 |
| 0228 | +2.417 | 726 | 643 | 3 | 0.500 |
| 0231 | +2.917 | 683 | 668 | 3 | 0.300 |
| 0241 | +2.083 | 735 | 678 | 3 | 1.500 |
| 0247 | +2.467 | 741 | 749 | 3 | 0.933 |
| 0249 | -0.167 | 678 | 648 | 3 | 2.000 |
| 0256 | +2.667 | 705 | 627 | 3 | 0.333 |
| 0263 | +0.100 | 707 | 637 | 3 | 2.333 |
| 0271 | +2.750 | 666 | 653 | 3 | 0.500 |
| 0281 | +0.833 | 699 | 750 | 3 | 0.333 |
| 0283 | +2.750 | 716 | 632 | 3 | 0.833 |
| 0295 | +0.550 | 703 | 669 | 3 | 2.900 |
| 0310 | +2.083 | 715 | 720 | 3 | 0.167 |
| 0317 | +0.750 | 722 | 624 | 3 | 3.167 |
| 0326 | +2.217 | 674 | 685 | 3 | 0.100 |
| 0329 | -0.500 | 702 | 667 | 3 | 1.467 |
| 0350 | +1.967 | 741 | 680 | 3 | 0.267 |
| 0353 | -0.300 | 688 | 631 | 3 | 1.067 |
| 0374 | +2.667 | 702 | 666 | 3 | 0.667 |
| 0379 | +0.917 | 695 | 620 | 3 | 0.167 |
| 0380 | +2.667 | 730 | 643 | 3 | 0.667 |
| 0388 | -0.383 | 712 | 607 | 3 | 1.967 |
| 0391 | +1.833 | 737 | 671 | 3 | 0.333 |
| 0395 | +2.667 | 760 | 630 | 3 | 0.333 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-xhigh`, `gpt-5.6-high`, `kimi-k3`.
Synthesis editor: `kimi-k3`. Verified subjective claims: 91.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
