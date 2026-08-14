# Qwen 3.8 Max vs. Qwen 3.7 Max: comparative writing analysis

Focus model: `qwen3.8-max`. Comparison model: `qwen3.7-max`. Direct-comparison scope: `comparator_v2_eval_v2_v3_combined_public`.

## In one paragraph

Give both models the same short-fiction prompt and the difference shows up in what the required ingredients are made to do. Qwen 3.7 Max names them and then reassures you about them; Qwen 3.8 Max puts them to work and lets them cost something. In a story about a hidden government weather program, Qwen 3.7 Max's investigator seals his one incriminating ledger under a loose cobblestone in a courtyard he knows is watched, and the narration treats this as an unassailable triumph, while Qwen 3.8 Max's protagonist reasons that a single accusation can be erased and a widely shared record cannot, and sends it out to many hands [C022]. The habit extends to people. In Qwen 3.7 Max's stories nobody speaks aloud or asks the protagonist anything, so no one is ever corrected, and the threat is usually reported as already defeated; Qwen 3.8 Max's secondary characters bargain, testify, and ask the question that turns the scene [C002]. Endings follow from that: peace, home, and mastery on one side, and on the other a gain that names what it did not fix [C038]. Across twenty shared prompts the pattern held without exception. Qwen 3.7 Max remains the better writer of hands, tools, and physical procedure [C012].

## Quantitative context

Across 20 matched prompts, the focus model recorded 20 wins, 0 ties, and 0 losses at the ±0.5 tie threshold. Its mean signed margin was +3.393 ± 0.365 (95% normal half-width).

Mean lengths were 688.4 and 728.6 words; the correlation between length difference and margin was -0.506.

## Comparative portrait

Six blinded readings by three analysts (claude-opus-5-xhigh, gpt-5.6-high, kimi-k3) converged on one description of the pair, stated in three different vocabularies. Qwen 3.7 Max treats the prompt's required elements as items to be introduced, named, and explained; Qwen 3.8 Max treats them as material to be re-defined and put to work. Qwen 3.7 Max inserts tokens in semantically empty positions and then certifies their fit, while Qwen 3.8 Max re-reads a token so its second appearance means something its first did not [C001]; it typically spends each token once, altered in grammar or function, where Qwen 3.7 Max reproduces prompt phrases verbatim, sometimes twice in one story [C015]; and it will re-tense an entire story so an awkward imported phrase reads as native narration, where Qwen 3.7 Max leaves a visible grammatical seam [C020].

Three further recurring splits:

- **Population.** Across the five-story windows examined by two of the three analysts, no character in Qwen 3.7 Max's stories speaks aloud or asks the protagonist a question, so the protagonist ends with the understanding he began with, amplified [C002]; Qwen 3.8 Max stages guardians, couriers, followers and witnesses who argue, bargain, testify and decide, and their speech changes outcomes [C016][C034].
- **Consequence and endings.** Qwen 3.7 Max's threats are frequently reported as already neutralized in the clause that introduces them [C023], and its closures certify a finished inner state — peace, home, mastery [C018][C025]. Qwen 3.8 Max more often ends on a conditional or diminished gain that names what remains unfixed [C006][C038].
- **Objects and social address.** Qwen 3.8 Max's relics acquire practical agency and pass beyond private ownership [C011], recur with re-keyed function [C037], and its plots reason about who else is served, excluded or endangered [C009][C022][C027]. Qwen 3.7 Max's objects more often confirm a personal transformation already chosen.

The shared floor matters too: both writers gloss their own images and replace one definition with another as a wisdom reflex [C007][C032]; both resolve central impossibilities by fiat, one in imagery and one in pseudo-technical exposition [C026]; and premise invention is roughly equal, with both independently making a quarantine a cover for weather engineering [C039].

Quantitatively the direction is unbroken. Across 20 matched pairs judged by three evaluator models, the focus model wins 20, ties 0, loses 0 at ±0.5, mean margin +3.393 (story-level 95% CI half-width 0.365), median +3.517. The narrowest pair is 0229 (+1.150) and the widest 0119 (+4.867).

## Does either model seem smarter?

Read as a reader impression produced by writing choices — not as any measurement of general capability — Qwen 3.8 Max seems the more perceptive writer in all six packet readings, and each analyst independently reported that the impression is *not* built from vocabulary, register or polish. By those proxies Qwen 3.7 Max often leads: it owns the more elevated and technical lexicon, and its diction is arguably richer on the same prompt [C021], while its pseudo-technical vocabulary decorates devices that are never constrained [C003] and its fancier terminology coexists with cruder epistemics [C035]. Nor is the impression volume: the focus model averages 688.4 words against 728.6, and the word-count difference correlates negatively with margin (-0.506), i.e. its wins tended to come when it was relatively *shorter*.

The behaviors that do produce the impression are separable:

- **Constraint synthesis.** Abstract tokens become operational rules the plot then uses [C001][C015]; awkward phrasing is naturalized rather than pasted [C020]; a required attribute becomes a limiting condition that forces the climax rather than a label routed around [C033].
- **Causal and structural foresight.** Planted phrases and objects return with changed function and close causal loops [C037]; transmission is designed against an adversary who might act [C022][C027]; crises are resolved by reusing what was already shown, often demoting the magical object to a mundane instrument [C003].
- **Psychological inference.** Emotion is converted into usable evidence through depicted regulation rather than named as a stable virtue [C010]; and where Qwen 3.7 Max asserts interior facts that its own staged action contradicts — a deliberate orchestrator who is "accidentally prophetic," an illiterate hound who instantly reads a map — Qwen 3.8 Max resolves the same contradictory element pair by giving the trait a psychological source the plot confirms [C005].
- **Conceptual compression.** Supplied binaries are reorganized rather than merely chosen between [C008]; particular discoveries are accumulated before a conclusion is announced [C013]; and an artifact's evidentiary reach is explicitly bounded — proof that change can be made audible, not proof of innocence [C029].
- **Relevant-detail selection.** Invented culture arrives as particulars implying an unwritten social world, and details are chosen for what they let characters know or do [C024][C011].
- **Restraint and reader trust.** The tone word becomes a refusal enacted at cost — a blank last page, one line per listener, staying an assistant — rather than a glow attached to an object [C021][C025]; interpretive labor sits in arrangement rather than in a concluding lecture [C014].

What the impression is *not*: it is not conceptual novelty, since premises are near-parity [C039]; not speculative rigor, since neither model earns its magic [C026]; and not implicitness, since Qwen 3.8 Max also aphorizes on schedule [C007][C032].

## Narrative reasoning and aesthetic judgment

The panel's most useful distinction is between reasoning *about the world of the story* and reasoning *in exposition*. Qwen 3.7 Max is genuinely capable of the latter: it stages method as an ordered sequence of bodily actions, in forensics and in ritual preparation, giving procedural legibility and forward rhythm [C012]; it can operationalize an assigned technical method into outcome-selection with a consequence, and in one story respects its own constraint (an irreplaceable mainspring must be braced, not swapped) where Qwen 3.8 Max quietly cancels its own thesis by installing a new spring [C019]; and it can build a valid eliminative argument for why a strange channel is the only channel available [C022, counterexample]. The accurate limitation, as one analyst insisted, is narrower than "Qwen 3.7 Max asserts causality": its causality is argued in exposition and then never tested against an opponent [C022][C023].

Aesthetic judgment — where to end, what to withhold, which image to trust — is where the gap widens. Evaluators independently credited the focus stories with line-level compression and varied cadence against the comparison's monotone in 0148, 0289, 0298 and 0392, and with turning required elements into functioning motifs rather than named props in 0014, 0089, 0209 and 0264. But this is not uniform: at 0229, the narrowest pair, the evaluator credited the *comparison* with wider syntactic range and better scene construction while flagging the focus story's repetitive subject-verb openings and tell-heavy summary — consistent with the panel finding that Qwen 3.8 Max's advantage is selective and structural rather than stylistic superiority per se [C021, low surface-cue risk]. Both models share the same aesthetic vice: explaining an image's meaning immediately after presenting it [C032][C007][C013].

## Range, recurring habits, and floor versus ceiling

Both models are formula writers. Qwen 3.8 Max's signature is antithetical redefinition arriving on a predictable schedule; Qwen 3.7 Max's is affirmational summary; only Qwen 3.8 Max's version is ever load-bearing, but both are automatic [C007]. Both reuse protagonist names — one analyst initially read Qwen 3.7 Max's four Eliases as default-setting and withdrew the claim on discovering Qwen 3.8 Max's repeated Maras, so naming supports no verdict (panel observation, not carried into the ledger). Panel-level tallies of Qwen 3.7 Max's intensifiers ("profound," "perfect") were likewise reported but not elevated to verified claims; treat them as suggestive only.

Floors. Qwen 3.7 Max's floor is requirement-satisfaction seams: tense collisions [C020], attributes contradicted by action [C005], obstacles retired offstage or by weather [C023], and closure exceeding earned stakes [C025]. Qwen 3.8 Max's floor is thinness under attractive layout: one analyst found an event-poor story with no obstacle, antagonist or reversal, distinguishable from "restraint" only by a small allocative logic at the ending; and 0229's fable-summary mode drew explicit evaluator criticism. It also has its own unearned grants — a father's voice through a pipe [C003, counterexample], an outright apotheosis ending [C025, counterexample], antagonists conceding to a child's paper crown [C004, counterexample].

Ceilings. Qwen 3.7 Max's best passages are real and specific: the rope as stratified history and the friction third option in 0125 [C008][C011], the brace as managed rather than erased damage in 0393 [C019][C029, counterexample], the bodily suspense of the reef approach in 0229 [C031], the forensic sequence in 0392 [C012]. Qwen 3.8 Max's ceilings are structural: the consent hinge and graded source reliability in 0230 [C001][C033][C035], the fortune-as-password loop in 0119 [C037], the lantern that is symbol, test and key at once in 0392 [C011]. The decisive asymmetry is that Qwen 3.7 Max's ceiling never converted: even the pairs containing its strongest work went to the focus model (0229 +1.150, 0125 +2.917, 0393 +3.483). A minority reading from kimi-k3 holds that Qwen 3.7 Max has slightly wider formal range — it took the packet's only point-of-view gamble, second person in 0148 — a range-versus-depth trade that pairwise scoring flattens; the evaluator on that pair, however, read the same device as mechanical and instruction-like.

## What each model still does better

Qwen 3.7 Max, on evidence, is better at:

- hands, tools and process — burnisher, adhesive size, heated brass plates, ordered spice preparation [C012][C024];
- bodily pressure in a crisis scene, where uncertainty is briefly held in posture and breath [C031];
- local mechanism discipline when a prompt supplies a technical method, including respecting a stated irreplaceability [C019];
- eliminative argument and expository clarity about immediate stakes [C022, counterexample][C026, counterexample];
- one instance each of genuine binary-refusal [C008] and genuine withholding — the unopened lockbox at 0220, though the narration then claims the closure the scene declined [C006].

Evaluators additionally credited it with sustained single-scene focus, conventional paragraphing against the focus model's hard line breaks (0142, 0220, 0393), and earlier explicit causal framing (0392). These are real and repeatable, and they are also local: none of them reversed a single pair.

Qwen 3.8 Max is better at the load-bearing items — constraint metabolism [C001][C015][C020][C033], second-party modeling and negotiated knowledge [C002][C016][C034], adversarial information design [C022][C027], epistemic calibration [C035], ethical bounding [C029][C036], object re-keying [C037], and costed endings [C038].

## Findings beyond the existing judging

Recurring and corroborated across packets but absent from evaluator notes:

- **The non-interrogative world.** No quoted dialogue and no character question in Qwen 3.7 Max's story sets, reported independently by claude-opus-5-xhigh and kimi-k3; Qwen 3.8 Max's scenes hinge on a question from a secondary mind [C002][C016][C034]. This is countable and correlates with protagonists who are never corrected.
- **Requirement-collision seams.** Qwen 3.7 Max's asserted-versus-dramatized contradictions cluster precisely where two prompt requirements pull against each other, which reframes them as compliance artifacts rather than irony [C005].
- **Graded source reliability.** Given the same "discredited textbooks" element, Qwen 3.8 Max makes the sources wrong about one thing and right about another; Qwen 3.7 Max simply vindicates them [C035].
- **Disclosure ethics.** On the same premise of a secret-keeper publishing secrets, only Qwen 3.8 Max registers the consent problem; a rubric scoring lyricism or theme would not catch it [C036].
- **Survival versus possession of information** [C022][C027], and **tone as conduct versus tone as paint** [C021] — the latter partly corroborated at 0014, where the evaluator independently noted "incandescent restraint" becoming a vow rather than a descriptor.

New and lower-confidence: the **directionality of care** — care as invitation and protocol limiting the custodian versus care as projection from a certain individual [C030]; and **absence made causally load-bearing** rather than atmospheric [C028].

Quantitative findings not visible in per-story judging: the focus model wins while writing fewer words on average (688.4 vs 728.6), and larger margins co-occur with relatively shorter focus stories (r = -0.506) — so verbosity is not the mechanism. Mean evaluator disagreement (0.950) and AB/BA order sensitivity (0.652) are non-trivial but small against a mean margin of +3.393.

## Disagreements and limitations

- **Intra-panel disagreement on the signature device.** read_01 and read_02 treat antithetical redefinition as Qwen 3.8 Max's insight-engine; kimi-k3 reports that Qwen 3.7 Max uses the same "not X but Y" construction just as often, so aphorism cannot differentiate them [C007][C032]. Preserve both: the difference is placement and consequence, not the construction.
- **Real reversals.** 0125 gives Qwen 3.7 Max a comparably intelligent third position while Qwen 3.8 Max weakens its own dilemma by having song persuade near-omnipotent beings [C008]; 0393 has Qwen 3.7 Max honoring a constraint Qwen 3.8 Max cancels [C019]; 0229 favors Qwen 3.7 Max on embodiment and suspense [C031][C023, counterexample]; 0220 briefly makes Qwen 3.7 Max the more withholding writer [C006].
- **Surface-cue sensitivity.** Qwen 3.8 Max's one-sentence-per-line layout enforces short sentences, guarantees rhythm and can disguise event-poverty; evaluators repeatedly listed conventional paragraphing as a comparison advantage. Any claim resting on apparent weightedness of lines should be discounted accordingly [C007].
- **Register defense (minority reading, held by three analysts).** Qwen 3.7 Max's explicitness, verbatim repetition and total closure may be a deliberate fable, parable or lullaby mode rather than lesser perception; the 0264 refrain functions as genuine litany [C015][C032]. The partial rebuttal is that its summary mode also removes causal friction, not only dialogue [C034].
- **Taste bias.** "Bittersweet equals deep" is itself a rubric preference; some readers will find Qwen 3.7 Max's complete resolutions more satisfying, and Qwen 3.8 Max ends nearly as totally in at least one story [C038][C025, counterexample].
- **Qwen 3.8 Max's own conveniences.** Its antagonists concede about as conveniently as Qwen 3.7 Max's threats evaporate [C004][C009, counterexample]; its ideological repertoire — consent, shared ownership, naming feelings — supplies ready-made resolutions (read_01, minority caution).
- **Scope.** Twenty short lyric-fabulist pairs; five-story windows per packet, so "all five / never" statements are packet-scoped. The material offers little basis for comparison in humor, realism, dialogue across social registers, or sustained causal plotting without magic (read_05). Story-level CI is ±0.365, so individual margins should not be over-read even though the aggregate direction is unambiguous.

## Representative case studies

**0230 — glass eye, discredited textbooks (+3.617).** The cleanest single illustration. Qwen 3.7 Max attaches the required tone phrase to snapping branches, where it cannot be evaluated; Qwen 3.8 Max makes it an observable property of crossed-out doses with prayers written in [C001]. Qwen 3.7 Max's relic flares with internal luminescence exactly when needed; Qwen 3.8 Max's occludes a lamp's glare and stays a lens thereafter [C003]. Qwen 3.7 Max isolates its truthful protagonist so truthfulness costs nothing; Qwen 3.8 Max makes it the limiting condition of a bargain with an armed courier [C033]. A child's question — will he decide for her — exposes the paternalism in the plan and redirects the climax [C002], the textbooks end up wrong about obedience and right about one fragile fact [C035], and the closing gain is measured against what was not fixed [C006][C038]. The evaluator independently described the divergence as psychological safety-as-elimination versus safety-as-relational-consent.

**0123 — quarantine over weather engineering (+4.100).** Premise parity is explicit: both stories hide weather manipulation behind a cordon [C039]. The divergence is handling. Qwen 3.7 Max seals a single ledger under a loose cobblestone in a courtyard its own watcher frequents and treats this as an unassailable testament, and the surveillance plot closes because rain makes the watcher uncomfortable [C022][C023]. Qwen 3.8 Max reasons that a lone accusation can be erased while shared weather cannot, sends the record to recording houses rather than police, and gives the wardens a stated countermeasure so publishing has a price [C022][C023]. Qwen 3.7 Max nonetheless builds the packet's better three-step inference here — no medical-waste signature, birds avoiding the sector, isobars — which is why the correct charge against it is untested causality, not absent causality [C022, counterexample].

**0125 — rope, grotto, energy beings (+2.917).** The strongest pro-comparison case. Qwen 3.7 Max's rope becomes a coherent model of temporal and historical experience [C011], and its protagonist rejects the eternity/oblivion binary through the story's own tactile concept of friction — a genuinely intelligent third position [C008]. Qwen 3.8 Max's reframing (letting moments remain movable) is more thematically integrated but weakens its impossible choice by having song persuade near-omnipotent beings to change the rules [C008, limitation]. The margin remains positive, but this pair is the best evidence that the gap is a tendency, not a gulf.

**0229 — lighthouse, scent, heat wave (+1.150).** The narrowest pair, and the clearest view of Qwen 3.8 Max's floor. Qwen 3.7 Max holds uncertainty in the body as the schooner approaches [C031], supplies precise apparatus and process [C024], and receives evaluator credit for scene construction and syntactic range; Qwen 3.8 Max over-glosses its tone phrase in successive definitions [C032], though it grounds the magic in an earlier rain-watered garden, refuses the promotion its plot has earned [C025], and frames the intention as invitation rather than command [C030]. Both leave the ship turning by fiat [C026].

**0148 — lighthouse prison, inherited lie (+4.167).** Qwen 3.7 Max repeats two required phrases nearly unchanged and resolves the inherited wolf paradox with literal wolves, producing clarity at the cost of the premise's competing versions of truth; Qwen 3.8 Max makes the assigned verb "hover" the prison's metaphysics and makes the prisoners' absence the actual mechanism of the rescue [C015][C028]. Its ending leaves a hush sustaining impossibilities until someone listens; Qwen 3.7 Max's certifies serenity in the face of an inevitable fate [C018]. The honest counter, from gpt-5.6-high, is that "no bodies" may evade the requested premise rather than fulfil it [C028, limitation]; and the second-person experiment here is Qwen 3.7 Max's one formal risk, judged by the evaluator as flattening rather than immersive.

## Cited claim ledger

- **C001 — Required elements as objects of interpretation versus items to be placed:** Both writers must insert the same abstract tokens. Qwen 3.7 Max inserts them as labels or decorative similes, often in semantically empty positions. Qwen 3.8 Max re-reads the token so that its second appearance means something different from its first, converting a checklist item into a discovery about the world or a character.
  - Story 0230, `qwen3.7-max`:
    > A sharp, crystalline pain lanced through his skull, echoing the fractured grace of the snapping apple branches high above him.
    The required tone-phrase is attached to snapping branches, which are not graceful in any determinable sense; the words are placed, not used.
  - Story 0230, `qwen3.8-max`:
    > Lior saw their fractured grace in the margins, where doses were crossed out and prayers inserted.
    The same tone-phrase becomes an observable property of a physical artifact and a judgment about the people who wrote it — crossed-out doses replaced by prayers is grace and fracture at once.
  - Story 0230, `qwen3.8-max`:
    > The rumored cures in discredited textbooks were not only instructions, but confessions of failed doctors.
    The required method phrase is re-classified mid-story; the plot device is reinterpreted as characterization of absent people.
- **C002 — Absence of second minds in Qwen 3.7 Max; interrogation as a structural engine in Qwen 3.8 Max:** Qwen 3.7 Max's five stories contain no quoted dialogue and, as far as I can find, no question asked by any character. The protagonist's understanding at the end is the one he began with, amplified. Qwen 3.8 Max stages at least one question per story from a secondary character, and the question changes what the protagonist does next — a social-cognitive move rather than a stylistic one.
  - Story 0230, `qwen3.8-max`:
    > She asked if he would decide for her, and the question cut clean.
    A child's question exposes the paternalism inside Lior's protective plan and redirects the entire climax; the relic ends in her pocket, by her choice.
  - Story 0142, `qwen3.8-max`:
    > One investor asked why the bridge in the painting had no gates at either end.
    The adversary reads the protagonist's art correctly and the negotiation turns on his reading, so the opposition possesses interpretive intelligence.
  - Story 0119, `qwen3.7-max`:
    > He was the silent guardian of their fates.
    The villagers exist only as recipients; nobody speaks, asks, or resists, and the story's evaluation of Elias is delivered by a narrator who shares his self-estimate.
- **C003 — New capability granted at need versus solution inside existing constraints:** At the crisis point Qwen 3.7 Max typically introduces a power the story has not established — the object simply works, or the threat is retired offstage. Qwen 3.8 Max's crises are resolved by reusing something already shown, often demoting a supposedly magical object to a mundane instrument, which keeps the causal ledger balanced.
  - Story 0230, `qwen3.7-max`:
    > Then, the antique glass eye flared with a dull, internal luminescence, and the loud psychic noise abruptly ceased.
    The relic's efficacy is asserted at the moment of need; nothing prior constrains or predicts it, and the discredited textbooks are retroactively declared correct.
  - Story 0230, `qwen3.8-max`:
    > He lifted the glass eye and let it occlude the lamp's harsh white glare.
    The same required action is performed with ordinary optics; the calming effect follows from softened light and slowed breathing, and the object stays a lens for the rest of the story.
  - Story 0142, `qwen3.7-max`:
    > The corporate auditors arrived with their clipboards, finding everything perfectly up to code.
    The announced threat is dispatched in one clause without an encounter, confirming that Qwen 3.7 Max's conflicts are declared rather than transacted.
- **C004 — Communities with internal divergence versus a uniform grateful mass:** Given nearly identical premises about coded communication under surveillance, Qwen 3.7 Max's lexicon encodes only external threat and communal obedience, while Qwen 3.8 Max's encodes commerce, betrayal, and unequal need inside the group. This is a difference of social modeling, not of prose quality.
  - Story 0142, `qwen3.8-max`:
    > When a golden fish appeared beside a door, the owner was ready to sell.
    The code includes a sign for defection, so the community is a population with divergent interests, and Lira's later insistence on written terms follows from that fact.
  - Story 0142, `qwen3.7-max`:
    > They worked in perfect silence, guided by the glowing orange roots of the mural.
    The populace is an instrument of the protagonist's signal; no one hesitates, bargains, or profits, so the "dual allegiance" element remains an internal mood rather than a social condition.
- **C005 — Asserted interior states that contradict the staged action:** Qwen 3.7 Max states psychological and cognitive facts in narration and then dramatizes behavior incompatible with them. The contradictions cluster exactly where two prompt requirements pull in different directions, indicating requirement-satisfaction rather than design.
  - Story 0119, `qwen3.7-max`:
    > This made his writings accidentally prophetic, a trait he barely understood himself.
    Two paragraphs earlier the same man deliberately orchestrates destinies and is currently engineering the mayor's route to smuggler's gold; deliberate engineering cannot be accidental, and the story never treats the clash as irony.
  - Story 0220, `qwen3.7-max`:
    > Through the glass, the hidden symbols formed an intuitively descriptive map of shapes that the hound instantly understood.
    The preceding sentence establishes that "Barnaby could not read human script"; the limitation is announced and then waived so that the required decoding can occur.
  - Story 0119, `qwen3.8-max`:
    > Her fortunes were accidentally prophetic, not from magic but from noticing which wounds repeated.
    Facing the same contradictory pair (deliberate orchestration plus accidental prophecy), Qwen 3.8 Max resolves it by giving the accuracy a psychological source, which the plot then confirms when the narrator's own hesitation has been "written into useful shape."
- **C006 — Closure as discharge versus closure as conditional continuation — with one clean reversal:** Qwen 3.7 Max ends by cancelling the story's tension entirely, usually with sleep, home, or a totalizing summary. Qwen 3.8 Max ends with an explicitly diminished, conditional gain that names what has not been solved. The difference is one of calibration; but story 0220 reverses it, which is the packet's most useful counterexample.
  - Story 0289, `qwen3.7-max`:
    > He was finally home.
    A decade of isolation and an unsent letter are resolved by a stranger taking his hand "without hesitation"; the ending asserts a completed transformation no scene has cost him anything to earn.
  - Story 0230, `qwen3.8-max`:
    > It did not cure grief, but it gave grief a smaller room.
    The gain is measured against what remains unfixed, which is consistent with the story's earlier redefinition of safety as consent within continuing danger.
  - Story 0220, `qwen3.8-max`:
    > It said, If you hear me, make the settlement a lamp, and I will walk toward it.
    Here Qwen 3.8 Max delivers the wish outright — the missing father speaks — while Qwen 3.7 Max's version of the same prompt leaves the lockbox unopened and Silas absent, so on this pair Qwen 3.7 Max is the more withholding writer.
- **C007 — Both writers run a visible insight-machine; only the machines differ:** Neither writer trusts the reader to extract meaning. Qwen 3.7 Max's engine is affirmational summary — a closing sentence that restates the theme in benevolent abstractions. Qwen 3.8 Max's engine is antithetical redefinition — a chiasmic reversal that reframes the theme. Qwen 3.8 Max's produces more content per instance, but both are automatic, and Qwen 3.8 Max's frequency makes its arrival predictable.
  - Story 0119, `qwen3.7-max`:
    > His open secrets would guide them all to a better tomorrow.
    The theme is restated as a benediction with no new information; several Qwen 3.7 Max paragraphs terminate in this move.
  - Story 0289, `qwen3.8-max`:
    > She understood then that the thread that connects all things is not a line but a willingness to return.
    The story's meaning is delivered by narrator-thesis in the same breath as the required motivation phrase; Qwen 3.8 Max's version is more thoughtful but equally explicit.
  - Story 0119, `qwen3.8-max`:
    > She was not escaping the island but tuning it.
    The identical syntactic template appears across stories ("not the absence of danger but consent within danger"; "not only instructions, but confessions"), showing a repeatable device rather than a fresh perception each time.
- **C008 — Binary pressure becomes a third option:** Qwen 3.8 Max repeatedly treats the supplied dilemma as something whose framing can itself be examined. The protagonist does not merely choose between rebellion and surrender, preservation and loss, or grief and change; the terms are reorganized. This produces conceptual intelligence because the story asks who designed the choice and what value the binary omits.
  - Story 0027, `qwen3.8-max`:
    > They could reignite the war, or they could reignite the promise that began it, she said.
    The repeated verb separates violent means from the rebellion’s original protective purpose. The required action becomes an ethical distinction rather than a simple plot command.
  - Story 0125, `qwen3.8-max`:
    > Instead of preserving a moment, he asked them to let moments remain movable.
    Miro questions the beings’ premise rather than accepting their allocation of mercy. The solution connects the story’s ideas of rope, pattern, and temporal texture.
  - Story 0125, `qwen3.7-max`:
    > Why choose between eternity and oblivion, he mused, when the present moment offered such exquisite, agonizing friction?
    Qwen 3.7 Max also rejects a false binary here, and does so through the story’s tactile concept of friction. This is the strongest reversal to Qwen 3.8 Max’s advantage.
- **C009 — Consequences have a social address:** Qwen 3.8 Max more often asks who beyond the protagonist is served, excluded, sacrificed, or given access. Beauty becomes care for people awake outside ordinary social hours; infrastructure decisions become political arithmetic. Qwen 3.7 Max’s horizons are more commonly dyadic or self-actualizing, even when the language invokes a whole cosmos.
  - Story 0209, `qwen3.8-max`:
    > Her grandmother had planted night blooms so the sick, the sleepless, and the lonely could meet beauty when day turned away.
    The answer to the botanical mystery is social rather than merely aesthetic. Three distinct groups explain both the flowers’ timing and the grandmother’s hidden labor.
  - Story 0392, `qwen3.8-max`:
    > They had been arithmetic, each body weighed against water futures, each silence purchased with promotion.
    The deaths are connected to resource allocation, urban development, career incentives, and record suppression. The antagonist is therefore a system of decisions, not just a malicious individual.
  - Story 0027, `qwen3.7-max`:
    > It was a beacon, broadcasting a frequency of defiance and hope across the entire star system.
    Qwen 3.7 Max can widen the scale, but this collective consequence remains generalized. The story does not show differentiated people, needs, or conflicts receiving the broadcast.
- **C010 — Feeling becomes an epistemic instrument:** Qwen 3.8 Max more often dramatizes emotional control as an active conversion rather than naming a stable virtue. Fear, grief, and inherited memory are neither unquestioned truth nor noise to suppress; they become usable only after attention and testing. That calibration creates psychological and investigative intelligence.
  - Story 0392, `qwen3.8-max`:
    > Mara felt another person's terror slide beneath her ribs, and she breathed until it settled into evidence.
    The sentence makes regulation observable and links vulnerability to professional judgment. Mara neither drowns in the memory nor dismisses it; she changes its status through disciplined attention.
  - Story 0392, `qwen3.7-max`:
    > Yet, his fortified vulnerability allows him to endure the psychological assault without losing his grip on reality.
    Qwen 3.7 Max identifies the correct psychological capacity, but the narrator supplies the interpretation directly. The behavior is subsequently demonstrated through forensics, though the phrase itself does much of the evaluative work.
- **C011 — Relics become operators:** In Qwen 3.8 Max, symbolic objects frequently acquire practical agency and pass beyond private ownership. The opera glasses distribute a question, the lantern verifies memory and opens concealed records, the rope becomes a route for strangers, and the postcards become a public memorial. Qwen 3.7 Max also uses sustained object symbolism, but the object more often confirms an already chosen personal meaning.
  - Story 0027, `qwen3.8-max`:
    > Mara pointed to the star through the opera glasses, letting each person look in turn.
    The inherited relic stops being a private token and becomes a shared interpretive instrument. Leadership is represented as circulating perception rather than issuing an order.
  - Story 0392, `qwen3.8-max`:
    > The memory did not arrive as feeling alone, because the lantern's brass held a notch matching a maintenance key.
    The lantern simultaneously carries historical meaning, tests a psychic memory, and mechanically unlocks evidence. Its symbolism is supported by plot function.
  - Story 0125, `qwen3.7-max`:
    > He was not merely unspooling a rope; he was excavating the dense, stratified history of human endurance.
    Qwen 3.7 Max’s rope is a strong counterexample: its material layers become a coherent model of temporal and historical experience, though the narrator explicitly announces that meaning.
- **C012 — Competence as choreography:** Qwen 3.7 Max has a recurring strength in staging method as a visible sequence of bodily actions. Ingredients are prepared in order, rope fibers are peeled and rewoven, and forensic observations accumulate item by item. This creates procedural legibility and a controlled forward rhythm even when the final inference is overstated.
  - Story 0392, `qwen3.7-max`:
    > The boots of the victim have left deep and frantic gouges in the grime, pointing away from the natural flow of the water.  Furthermore, a distinct smear of synthetic grease mars the rusted iron of a nearby support beam.
    The story presents directionality and chemical trace as separate observable facts. Elias’s competence is embodied in a sequence rather than merely asserted by his job title.
  - Story 0089, `qwen3.7-max`:
    > First, she carefully crushed dried star anise and celestial cardamom between her trembling palms.  Then, she sprinkled the powdered ghost pepper and silver saffron over the dark earth.
    Explicit temporal markers make the conjuring method tactile and reproducible within the fairy-tale logic. The physical sequence anchors an otherwise abstract metamorphosis.
  - Story 0392, `qwen3.8-max`:
    > She counted boot prints in the silt, measured mineral streaks on concrete, and noted where rust had been wiped from a valve wheel.
    Qwen 3.8 Max can be equally procedural, especially in this investigation. Qwen 3.7 Max’s advantage is a broader recurring preference for making the method the scene’s organizing spine.
- **C013 — Different levels of interpretive pressure:** Qwen 3.7 Max more often closes interpretive space by announcing a universal lesson immediately after the image or procedure. Qwen 3.8 Max usually supplies a more particular chain of discoveries before stating its conclusion, allowing provenance, place, and human need to narrow the meaning. The distinction is relative: Qwen 3.8 Max also writes explicit maxims.
  - Story 0209, `qwen3.7-max`:
    > He knew now that the flowers bloomed in the dark to remind us that beauty does not require an audience.
    The narrator converts the flowers into a universal moral. It is lucid, but it bypasses biological causality and reduces the grandmother, postcards, glass, and seasonal labor to one familiar proposition.
  - Story 0209, `qwen3.8-max`:
    > On the final cold night before spring, she traced the last etched stem and found her grandmother's initials.
    The realization is attached to a specific discoverable mark. The initials connect the glass, garden, postcards, and family silence before the narrator explains why the flowers matter.
  - Story 0089, `qwen3.8-max`:
    > The beast whisperer understands then that grief was never a wall, but a door waiting for a kinder key.
    This is a direct counterexample within Qwen 3.8 Max: a familiar metaphor tells the reader exactly how to interpret the metamorphosis and grief.
- **C014 — Disclosure: Qwen 3.8 Max withholds, Qwen 3.7 Max announces:** Across the pairs, Qwen 3.7 Max's narrator states the story's meaning after the decisive image has already done the work, converting discovery into lecture. Qwen 3.8 Max arranges objects, gestures, and exits so the reader must assemble the meaning from residue. The behavioral signature is where interpretive labor sits: inside Qwen 3.7 Max's prose as conclusion, inside Qwen 3.8 Max's structure as arrangement.
  - Story 0393, `qwen3.7-max`:
    > This was the hidden truth of genuine rehabilitation.
    The brace image had already dramatized the thesis (flaw carried, not erased); this sentence pre-empts the reader's inference. On the same prompt, Qwen 3.8 Max ends before the hearing, leaving the thesis audible in the repaired song rather than stated.
- **C015 — Required phrases: Qwen 3.7 Max recites, Qwen 3.8 Max re-functions:** Qwen 3.7 Max reproduces prompt tokens verbatim and repeatedly; in 148 both "sustains impossibilities" and "lighthouse prison off a jagged reef" appear twice nearly unchanged, reading as checklist compliance. Qwen 3.8 Max typically spends each token once, altered in grammar or function, so the constraint becomes load-bearing machinery rather than decoration.
  - Story 0148, `qwen3.8-max`:
    > Ewan needed the map because the tower had begun to hover between what happened and what was said.
    The assigned action "hover" becomes the story's metaphysics, the prison suspended between event and account. Qwen 3.7 Max spends the same word on dust motes and a pausing hand, both literal and decorative.
- **C016 — Populated scenes versus solitary meditation:** Qwen 3.8 Max dramatizes insight through other people, using dialogue, interviews, guardians, and repairers, so moral positions must be argued against resistance. Across all five stories Qwen 3.7 Max uses no direct dialogue at all; even crucial turns arrive as reported speech filtered through one narrating consciousness.
  - Story 0298, `qwen3.8-max`:
    > "A trammel needs anchor and consent," she said.
    > "You have neither."
    The story's central ethical problem, consent in sacrificial barter, is voiced by an opposing witness, forcing Mara to defend her position. The equivalent beat in Qwen 3.7 Max's 298 is narrated conclusion with no opposing voice.
- **C018 — Endings: Qwen 3.7 Max resolves the feeling, Qwen 3.8 Max leaves the meter running:** All five of Qwen 3.7 Max's endings certify a closed inner state, while Qwen 3.8 Max's endings displace resolution onto the world, leaving cost, obligation, or listening unfinished. The difference is whether the story stops when the character feels better or when the situation stops moving.
  - Story 0148, `qwen3.7-max`:
    > You breathe in the salty air, entirely at peace with your inevitable fate.
    The story certifies the narrator's serenity as its final fact. Qwen 3.8 Max's 148 ends with the hush "sustaining impossibilities until someone listened," and Qwen 3.8 Max's 298 binds Mara into ongoing servitude: "the promise kept her, fiercely gentle among the bones."
- **C019 — Counterweight: Qwen 3.7 Max's causal mechanics can be tighter:** When the prompt supplies a technical method, Qwen 3.7 Max sometimes makes it do literal causal work where Qwen 3.8 Max uses it atmospherically. In 264 Qwen 3.7 Max operationalizes wave functions as outcome-selection that causes the bloom; in 393 Qwen 3.7 Max respects its own constraint (the mainspring cannot be replaced, so the maker braced it), while Qwen 3.8 Max's repairer simply installs a new spring, quietly canceling her thesis that the break must be carried rather than swapped out.
  - Story 0264, `qwen3.7-max`:
    > He collapses the unlikely outcomes, forcing the seed to choose life.
    The assigned method becomes a mechanism with a consequence. Compare Qwen 3.8 Max's 264: "She let the spark answer itself through a wave function of green memory," where the phrase decorates an event that would occur anyway.
- **C020 — Constraint metabolized versus constraint inserted:** Given the same awkward prompt phrases, Qwen 3.8 Max reshapes the sentence or the whole story's tense so the phrase reads as native narration; Qwen 3.7 Max drops the phrase in verbatim and leaves a visible grammatical seam. This is a small mechanical signal of a large difference: whether the writer has absorbed the assignment or is checking it off.
  - Story 0014, `qwen3.7-max`:
    > He preferred to work in this high isolation, especially after the town goes silent in the valley below.
    Past-tense narration collides with the imported present-tense prompt phrase. The seam shows the element was pasted rather than rewritten.
  - Story 0224, `qwen3.7-max`:
    > Elara possessed a strange affliction, for she substitutes reality nightly, weaving new illusions over the physical world when the sun sets.
    Same collision in a second story, confirming a habit rather than a slip.
  - Story 0014, `qwen3.8-max`:
    > After the town goes silent, the gilded-leaf stationer climbs the stairway to the blooming labyrinth of bonsai forests on a mountaintop.
    Qwen 3.8 Max shifts the entire story into present tense so the awkward timeframe phrase becomes grammatically native; the same solution is used in 0224.
- **C021 — Tone as behavior versus tone as adjective:** Qwen 3.7 Max converts the required tone word into a descriptor attached to an object and then certifies the fit; Qwen 3.8 Max converts it into something a character does or refuses to do. The result is that Qwen 3.7 Max's tone is announced while Qwen 3.8 Max's is performed by the plot's omissions.
  - Story 0014, `qwen3.7-max`:
    > The metal caught the rising sun, glowing with a warm, incandescent restraint that perfectly matched his quiet demeanor.
    Restraint is treated as a visual property of gold leaf, and the narrator then grades its own work ("perfectly matched"). Nothing in the story is restrained; the ending grants total consolation.
  - Story 0014, `qwen3.8-max`:
    > For himself he keeps the last page blank, because the texture of what comes next must be earned, not invented.
    The tone is enacted as a withholding, and it costs the protagonist the one thing he most wants. The word is dramatized rather than applied.
- **C022 — Modeling how information survives other people:** Qwen 3.8 Max repeatedly thinks about adversarial transmission: redundancy, compartmentalization, plausible deniability, the difference between one witness and many. Qwen 3.7 Max's protagonists preserve truth by hiding it, which is presented as heroic but is operationally inert. This is social and institutional reasoning, not lyric skill.
  - Story 0066, `qwen3.8-max`:
    > Each person received only one line, so no single listener could betray the whole.
    A concrete tradecraft solution derived from the fact that other people can be broken. The method follows from a model of risk.
  - Story 0123, `qwen3.8-max`:
    > She knew a lone accusation could be erased, while shared weather could not.
    The dissemination choice (every recording house, not the police) is reasoned from how suppression actually works.
  - Story 0123, `qwen3.7-max`:
    > He sealed the thick ledger in a waterproof canvas casing and placed it beneath the loose cobblestone near the trickling fountain.
    The evidence is hidden in a single copy, in a courtyard the surveilling watcher already knows, and the story treats this as an unassailable testament. No adversary model is present.
- **C023 — Danger reported as already neutralized:** Qwen 3.7 Max introduces threats in the same clause that dissolves them, so the reader is never asked to hold uncertainty; the antagonists never act. Qwen 3.8 Max gives the antagonist a stated intention and lets the protagonist name her fear without resolving it.
  - Story 0066, `qwen3.7-max`:
    > The censors would only hear a melancholic tune, entirely missing the vital data hidden in the harmonics.
    The single obstacle is defeated by narratorial assurance rather than by event, and the censors never appear again.
  - Story 0123, `qwen3.7-max`:
    > He knew the watcher would eventually leave when the downpour became too uncomfortable granting Elias the long night to continue his vital observations.
    The surveillance plot is closed by weather and by the protagonist's confidence; nothing is risked.
  - Story 0123, `qwen3.8-max`:
    > He said the wardens planned to flood the courtyard if the record surfaced.
    A specific, proportionate countermeasure exists, which makes the subsequent decision to publish a real choice with a price.
- **C024 — Token-level cultural detail versus category-level costume — with a real reversal:** When inventing a lost culture, Qwen 3.8 Max supplies particulars that imply an unwritten social world; Qwen 3.7 Max supplies the generic furniture of "the past." The reversal is that Qwen 3.7 Max outperforms Qwen 3.8 Max on physical apparatus and process, where Qwen 3.7 Max's details are specific and correctly sequenced.
  - Story 0014, `qwen3.8-max`:
    > There are doorways painted blue for courage, kettles singing in rows, and women braiding ribbons into the manes of paper horses.
    Each item implies a custom, a belief, and a domestic economy the story does not have to explain.
  - Story 0014, `qwen3.7-max`:
    > He described their heavy woolen cloaks and the rhythmic clacking of their wooden looms in the winter cold.
    Default weaver iconography; nothing here could only belong to this valley. Compare Qwen 3.7 Max's 0066 "tales of fallen heroes and lost lovers," the same category-level fill.
  - Story 0229, `qwen3.7-max`:
    > He poured the dark liquid onto the heated brass plates of the lamp array, watching it hiss and vaporize.
    The reversal: Qwen 3.7 Max's material imagination is precise and causal at the level of objects and procedures, which Qwen 3.8 Max often skips.
- **C025 — Renunciation endings versus apotheosis endings:** Qwen 3.7 Max's protagonists finish larger than they began and are told so by the narrator; they do not change, they are confirmed. Qwen 3.8 Max's protagonists more often end by declining an elevation or admitting a limit, which reads as maturity because the story gives up something it could have kept.
  - Story 0224, `qwen3.7-max`:
    > She was no longer just a refugee hiding from her own mind, but a master of her own reality.
    Transformation is asserted in summary rather than shown in a changed behavior, and the reward is total.
  - Story 0066, `qwen3.7-max`:
    > He slept peacefully, dreaming of a world where the music never had to hide.
    A consolatory coda after a story in which nothing was risked; the closure exceeds the earned stakes.
  - Story 0229, `qwen3.8-max`:
    > Mara stayed assistant, not because she lacked authority, but because she had become the kind of strength that could wait.
    The story refuses the promotion its plot has earned, and Qwen 3.8 Max pairs this with an admitted fear in 0123 ("Mara opened her coat to the first drops and answered that she did").
- **C026 — Shared reliance on fiat magic — difference absent:** Both writers resolve their central impossibility by declaring that it works. Qwen 3.8 Max's version is embedded in imagery and Qwen 3.7 Max's in pseudo-technical exposition, but neither earns the mechanism, and the packet does not support a claim that one writer's speculative logic is tighter than the other's.
  - Story 0224, `qwen3.8-max`:
    > Seed what you fear, it reads, and the mountain will open.
    The instruction and its result arrive by decree; the stone simply obeys, exactly as Qwen 3.7 Max's obsidian relic does after its feather ritual.
  - Story 0014, `qwen3.7-max`:
    > By translating that pitch into numerical sequences, he could weave the present atmosphere directly into his fictional timelines.
    A causal link stated in the vocabulary of method but with no operative content; equivalent in kind to Qwen 3.8 Max's decreed transformations.
- **C027 — Constraint becomes protocol:** Qwen 3.8 Max more consistently converts strange prompt elements into procedures with social and causal consequences. In 0066, elusive lyrics do not merely conceal information; they create a secret-sharing system that determines how the community can act. Qwen 3.7 Max identifies an encrypted payload but largely announces its function instead of dramatizing its organization.
  - Story 0066, `qwen3.8-max`:
    > Each person received only one line, so no single listener could betray the whole.
    The sentence links lyric form, surveillance risk, collective participation, and plot logistics. The constraint generates an actual information architecture.
  - Story 0066, `qwen3.7-max`:
    > The words he whispered into the dark were not mere poetry, but encrypted coordinates and historical truths.
    Qwen 3.7 Max clearly states what the lyrics contain, but the encryption remains a label; the story supplies fewer consequences for how the information is divided, verified, or socially held.
- **C028 — Absence bears structural weight:** Qwen 3.8 Max can let an absence remain ontologically unresolved while still making it causally active. In 0148, missing prisoners, empty coats, and a story-generated prison all participate in the escape mechanism. Qwen 3.7 Max chooses a cleaner revelation—real wolves committed a massacre—which supplies direct stakes but collapses the premise's competing versions of truth.
  - Story 0148, `qwen3.8-max`:
    > The impossible thing was simple: the prisoners had vanished into the story told about them.
    > To free them, he had to enter the telling and leave a door open.
    The uncertainty is not atmospheric ornament. Ewan must act inside the uncertain relation between event and account, making absence load-bearing.
  - Story 0148, `qwen3.7-max`:
    > The wardens lie dead in the upper tiers, slain by the very beasts your father once lied about.
    The declarative explanation resolves the inherited wolf paradox immediately. It produces causal clarity but leaves less pressure on the distinction between truth, warning, and narrative.
- **C029 — Mercy without epistemic overreach:** In 0393, Qwen 3.8 Max makes a mature distinction between evidence that someone has changed and evidence that someone is innocent or safe. Qwen 3.7 Max reaches a more categorical parole judgment from the clockwork metaphor. Qwen 3.8 Max therefore seems more ethically and causally disciplined: the artifact can make repentance audible without becoming a complete risk assessment.
  - Story 0393, `qwen3.8-max`:
    > He would carry the music to the hearing, not as proof of innocence, but as proof that change could be made audible.
    The parallel clauses sharply limit what the music box can establish. Mercy becomes an action and a form of testimony, not an acquittal.
  - Story 0393, `qwen3.7-max`:
    > And because of that profound awareness, Marcus was finally safe to release.
    The conclusion equates self-awareness, represented by a mechanical brace, with future safety. That is a psychologically and institutionally larger claim than the evidence supports.
- **C030 — Directionality of care:** Both writers imagine tenderness as a force capable of guiding others, but Qwen 3.7 Max's care often operates as heroic projection from a certain individual. Qwen 3.8 Max more often describes care as invitation, current, or shared orientation. This creates a subtle difference in agency: Qwen 3.8 Max's protagonist guides without claiming total command over the recipient.
  - Story 0229, `qwen3.8-max`:
    > Then she let her intention go, not a demand for safety but an invitation for the ship to find its way.
    The contrast between demand and invitation makes noncoercion part of the magical mechanism rather than merely part of Mara's temperament.
  - Story 0229, `qwen3.7-max`:
    > He projected every ounce of his protective fury into the drifting mist, pushing the fragrance outward with his mind.
    The verbs “projected” and “pushing” make Elias the commanding source of salvation even though the story verbally opposes aggression.
- **C031 — Crisis enters the body:** Qwen 3.7 Max is more effective when suspense needs bodily pressure. In 0229, the ship's approach is observed through strained posture, duration, fog, and dangerous geography. Qwen 3.8 Max's corresponding turn is elegant but rapid. Qwen 3.7 Max's physical insistence gives the rescue a felt cost that its explicit moral language sometimes lacks.
  - Story 0229, `qwen3.7-max`:
    > Elias held his breath, his knuckles turning white as he gripped the iron railing.
    The body registers uncertainty before the rescue succeeds, briefly preventing the scene from functioning as a foregone symbolic demonstration.
  - Story 0229, `qwen3.8-max`:
    > The ship's bell answered once, faint and amazed, and the bow turned toward the safe channel.
    Qwen 3.8 Max's image is graceful, but the danger resolves within the same sentence and offers less bodily or navigational resistance.
- **C032 — Interpretive overcare:** Both writers frequently explain an image's moral meaning immediately after presenting it. Their preferred construction replaces one definition with another—“not merely this, but that”—which can sound incisive while reducing the reader's interpretive work. No consistent difference is strong enough here to favor either writer.
  - Story 0066, `qwen3.7-max`:
    > The broadcast was not just a transmission of data, but a lifeline to their shared humanity.
    The sentence converts an already legible action into an explicit universal moral, narrowing the image rather than adding a new consequence.
  - Story 0229, `qwen3.8-max`:
    > The hush was not silence; it was screaming tenderness, a scream softened into mercy, a scream that loved the world enough to be gentle.
    Qwen 3.8 Max's paradox has rhythmic force, but the successive glosses prescribe how the tonal phrase should be understood instead of allowing the scene to carry it.
- **C033 — Attributes as engines, not labels:** Qwen 3.8 Max converts required attributes into decision-forcing constraints: involuntary truthfulness means Lior cannot lie to an armed courier, so the climax must be built entirely from truthful moves; in 0089 the reluctance gets a specific reason (change might erase the shape Lira knew). Qwen 3.7 Max announces attributes and then routes around them — Elias's truthfulness costs nothing because he is alone, and the watcher in 0123 never acts on anything.
  - Story 0230, `qwen3.8-max`:
    > He could also lie, but his mouth had forgotten how to bend.
    The required attribute becomes the plot's limiting condition: the entire bargain scene exists because deception is impossible, so the element generates the drama instead of decorating it. Qwen 3.7 Max's 0230 neutralizes the same attribute by isolating the character.
- **C034 — Other wills in the room:** Qwen 3.8 Max's stories contain counterforces that act and secondary characters who decide: patrol boats search, a courier bargains, a follower testifies, Sora chooses, a woman returns a letter. Speech occurs and changes outcomes. Across all five Qwen 3.7 Max stories no character speaks at all, opposition is passive or absent, and resolution requires no negotiation with any resistant will.
  - Story 0089, `qwen3.7-max`:
    > No words were needed between them, as their hearts beat in a unified and rhythmic cadence.
    The reunion explicitly bypasses verbal negotiation; read beside Qwen 3.7 Max's four other dialogue-free, antagonist-free stories, it reveals worlds without responsive others, where closure can be declared rather than engineered.
- **C035 — Sources partly right: epistemic calibration:** Given the identical required element (rumored cures in discredited textbooks), Qwen 3.8 Max builds a world of partial reliability — the texts are wrong about obedience, right about one fragile fact — while Qwen 3.7 Max's textbooks are simply vindicated and the relic works exactly as advertised. Qwen 3.8 Max's protagonists verify through accumulated small matches ("many quiet entries aligning"); Qwen 3.7 Max's deduce entire conspiracies in single expository leaps.
  - Story 0230, `qwen3.8-max`:
    > The discredited textbooks stayed wrong about obedience, yet right about one fragile fact.
    Graded reliability forces the protagonist to judge which claim to trust — a marker of epistemic maturity that Qwen 3.7 Max's flat verdict ("The discredited textbooks had been right") forecloses in the same story slot.
- **C036 — Noticing what secret-keeping costs:** Both 0289 stories give a keeper of secrets the same move — making hoarded confessions public — but only Qwen 3.8 Max registers the ethical problem of who may disclose what, with whose permission. Qwen 3.7 Max's Elias exhibits a thousand strangers' secrets and the narration calls it sanctuary; consent is never sought or thematized. Qwen 3.8 Max's ghostwriter distinguishes secrets that "need air" from those needing names withheld, and 0230 makes consent the hinge of its climax.
  - Story 0289, `qwen3.7-max`:
    > He decided to weave these hidden confessions into a physical tapestry, revealing the invisible bonds of the city.
    The keeper unilaterally exposes what was entrusted to him, and the text treats exposure as pure gift — a moral blind spot that rubrics scoring lyricism or theme would not catch.
- **C037 — Objects that return changed:** Qwen 3.8 Max plants phrases and objects that recur with altered function: "Begin where you are" appears as fortune, then as map-marginalia, then as the literal phrase that opens a door; the 0089 fortune ends blank because the future "has begun writing itself in light." Qwen 3.7 Max plants objects too (specs, Clara's letter) but payoffs arrive within the same movement and do not re-key the story's meaning.
  - Story 0119, `qwen3.8-max`:
    > When my own knock came at dawn, I used the phrase "Begin where you are."
    The fortune becomes a usable password: theme converted into plot instrument. The callback closes a causal loop rather than merely echoing, which is structural intelligence rather than ornament.
- **C038 — Closure that keeps the bill:** Qwen 3.8 Max's endings preserve cost: grief gets a smaller room rather than a cure; safety lasts only as long as choice is protected; rain is "no longer an ending," implying it once was. Qwen 3.7 Max's endings declare totality — the entire infinite cosmos gained, "perfectly content," "finally home," "perfect harmony of untamed and eternal love." The recurring pattern reads as maturity in Qwen 3.8 Max (resolution as rebalancing) versus wish-completion in Qwen 3.7 Max.
  - Story 0230, `qwen3.8-max`:
    > It did not cure grief, but it gave grief a smaller room.
    The sentence measures what was not fixed, which is what makes the fix believable; Qwen 3.7 Max's closing superlatives answer every debt the story raised, leaving nothing for the reader to weigh.
- **C039 — Same invention, different engineering:** Premise originality is roughly equal: both 0123 stories independently make the quarantine a cover for weather manipulation, and both 0289s build a public installation from hoarded letters. The writers diverge in what the premise is made to do, not in the premise itself — so creativity rubrics scoring conceptual novelty would likely tie them, and any smartness verdict must rest on execution.
  - Story 0123, `qwen3.7-max`:
    > The military was not containing a microscopic disease because they were desperately concealing a failed experimental weather weapon that had created a perpetual localized supercell.
    Nearly the same concealed-weather conceit as Qwen 3.8 Max's storm gate and lightning diverted into canals; the match shows the gap is in how discovery is dramatized and used, not in inventiveness of premise.

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0014 | +3.967 | 604 | 714 | 3 | 0.600 |
| 0027 | +2.550 | 723 | 671 | 3 | 0.233 |
| 0066 | +3.450 | 625 | 745 | 3 | 1.233 |
| 0089 | +3.550 | 715 | 695 | 3 | 0.900 |
| 0119 | +4.867 | 694 | 768 | 3 | 0.600 |
| 0123 | +4.100 | 660 | 689 | 3 | 0.667 |
| 0125 | +2.917 | 667 | 709 | 3 | 0.500 |
| 0142 | +2.583 | 660 | 699 | 3 | 0.833 |
| 0148 | +4.167 | 664 | 773 | 3 | 0.333 |
| 0209 | +4.283 | 679 | 786 | 3 | 0.900 |
| 0220 | +3.733 | 739 | 693 | 3 | 0.200 |
| 0224 | +3.433 | 660 | 714 | 3 | 0.000 |
| 0229 | +1.150 | 757 | 689 | 3 | 1.767 |
| 0230 | +3.617 | 792 | 761 | 3 | 0.433 |
| 0231 | +3.200 | 707 | 780 | 3 | 0.400 |
| 0264 | +2.317 | 713 | 766 | 3 | 0.633 |
| 0289 | +2.817 | 706 | 745 | 3 | 0.967 |
| 0298 | +3.917 | 669 | 725 | 3 | 0.833 |
| 0392 | +3.750 | 694 | 726 | 3 | 0.500 |
| 0393 | +3.483 | 640 | 724 | 3 | 0.500 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-xhigh`, `gpt-5.6-high`, `kimi-k3`.
Synthesis editor: `claude-opus-5-xhigh`. Verified subjective claims: 39.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
