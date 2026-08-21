# Qwen 3.8 Max vs. Qwen 3.7 Max: comparative writing analysis

Focus model: `qwen3.8-max`. Comparison model: `qwen3.7-max`. Direct-comparison scope: `comparator_v2_eval_v2_v3_predecessor_depth_n50`.

## In one paragraph

Handed the same short-fiction prompt, Qwen 3.7 Max introduces each required element and then explains it — the assigned mood pinned to an object as an adjective, the narrator certifying that it fits [C021]. Qwen 3.8 Max puts the same elements to work, and its stories contain someone who can refuse. The difference is easiest to see in a single choice: asked to move truth past a censor, Qwen 3.7 Max's hero seals a ledger in canvas and hides it under a cobblestone, while Qwen 3.8 Max's gives each listener one line of the song, so no single person can betray the whole [C022]. Conflict follows from that. One writer's obstacles are retired by narration; the other's outcome waits on another character's decision, and the protagonist deliberately declines to press [C062]. The endings differ accordingly: peace, mastery and a certificate of completion on one side; on the other, a cost left unpaid and the knowledge handed to someone else [C089]. Qwen 3.8 Max is also the plainer and slightly shorter writer — worth knowing, because it came out ahead on all fifty shared prompts, and never for writing more.

## Quantitative context

Across 50 matched prompts, the focus model recorded 50 wins, 0 ties, and 0 losses at the ±0.5 tie threshold. Its mean signed margin was +3.220 ± 0.209 (95% normal half-width).

Mean lengths were 683.3 and 725.9 words; the correlation between length difference and margin was -0.355.

## Comparative portrait

The two writers are close in polish and far apart in posture. Qwen 3.7 Max (comparison) treats a prompt as a list to be honored visibly: the required phrase is inserted, often verbatim and sometimes twice, then glossed so the reader cannot miss it [C015][C055][C073]. Qwen 3.8 Max (focus) treats the same list as pressure to metabolize: the phrase is re-read so its second appearance means something the first did not, or is rewritten until it reads as native narration [C001][C020][C085]. Three consequences recur across every packet and all three critic models.

- **Population.** The comparison model's worlds contain one mind. In one packet none of its five stories contains quoted dialogue or a single question asked by any character [C002]; a second packet independently reports the same speechlessness across a different five [C034]. The focus model stages at least one question or negotiation per story, and the answer changes what the protagonist does [C002][C016].
- **Opposition.** Comparison threats are frequently retired in the clause that introduces them — censors who "would only hear a melancholic tune," a watcher who "would eventually leave" [C023]. Focus antagonists have stated countermeasures and independent volition [C023][C062][C088].
- **Closure.** Comparison endings certify a finished inner state or a completed mission; focus endings keep a cost visible and hand a practice to someone else [C018][C038][C063][C089].

**Replication.** This portrait replicates in the extension. The focus model wins 20/20 in the original cohort and 30/30 in the extension, mean margins +3.393 and +3.105 with overlapping intervals; the pooled record is 50 wins, 0 ties, 0 losses at ±0.5. The only material changes are a slight narrowing of the mean margin, a drop in evaluator disagreement (0.950 → 0.732) and a small rise in order sensitivity (0.652 → 0.717). No claim class in the ledger is reversed by the extension statistics.

## Does either model seem smarter?

Yes, and lopsidedly — as a reader impression produced by identifiable writing choices, not as a statement about either system's general capability. All twelve packets that render a verdict give the impression to the focus model; the two most balanced readings still concede it on maturity and consequence-modeling while contesting its scope [C087][C091].

The impression is **not** built from the usual proxies, and the record actively excludes them. Multiple analysts note the comparison model owns the more elevated diction — "isobars," "mirror neurons," "ocular prosthesis," "extrajudicial" — while the focus model writes plainer [C035][C039][C065]. Quantitatively the focus model is the shorter writer (683.3 vs 725.9 words; −42.6 mean), and the word-count difference correlates *negatively* with margin (−0.355): the focus model wins by more when it is relatively shorter. Verbosity and lexical show are ruled out by both the panel and the numbers, in both cohorts (−40.2 original, −44.2 extension).

Separated into components, the recurring, panel-supported behaviors are:

- **Constraint synthesis** — the abstract token becomes an operational rule the plot obeys, e.g. "psychological safety... not the absence of danger but consent within danger," immediately enacted [C001][C046][C060].
- **Causal/structural foresight** — planted phrases return with changed function; a fortune becomes a password that opens a door [C037][C070].
- **Psychological inference** — mixed motive and self-implication; a novelist who "had long confused control for care," a survivor whose kept-versus-given names "difference is not zero" [C054][C010].
- **Relevant-detail selection** — crowds itemized so one item collides with the setting; attributes instantiated as practice rather than adjective [C049].
- **Restraint** — a last page kept blank, a promotion declined, a remedy that "did not restore every lost thing" [C021][C025][C047].
- **Reader trust** — interpretive labor placed in arrangement rather than in a summarizing sentence [C014][C075].

Against this, the panel names one reusable machine that manufactures the *look* of judgment: the negate-then-substitute frame, at least fifteen times across five stories in one packet, roughly half of it load-bearing and half pure cadence — "The water did not splash, it rang" [C052][C064]. Both writers run automatisms; they fake different virtues, the comparison model's motivation-label faking clarity and the focus model's antithesis faking discrimination [C007][C090]. Fiat magic is shared and no analyst can rank the two on speculative rigor [C026]. **Replication:** the extension does not soften this. Disagreement fell while the sweep held, which is consistent with the impression being carried by structural behaviors rather than by contested surface taste.

## Narrative reasoning and aesthetic judgment

The focus model's reasoning advantage is clearest where information must survive other people. Given a censorship premise, the comparison model hides one copy of a ledger under a cobblestone the surveilling watcher already knows [C022]; the focus model splits a song so "each person received only one line, so no single listener could betray the whole" [C022][C027]. The same habit produces second-order thinking: after the debunking succeeds, the risk identified is the community's own reverence — "guard the stillpoint without turning it into a shrine" [C050]. It also produces epistemic calibration: discredited sources are "wrong about obedience, yet right about one fragile fact" [C035], and a music box is carried to a hearing "not as proof of innocence, but as proof that change could be made audible" [C029][C043].

The comparison model's reasoning is real, narrower, and located in physical procedure: eliminative arguments before a mechanism is asserted, correctly sequenced apparatus, and consequence landed in the body [C012][C024][C044][C065][C069][C083]. At its peak it produces a genuine category shift — "The pattern language was not merely descriptive. It was operational" — and plants anomalies long before explaining them [C087].

Aesthetically, the divide is a closure budget. The comparison model spends several consecutive sentences re-confirming survival, farewell, renewal and peace [C045]; it converts the assigned tone into a symptom and then cures it, ending in "absolute certainty" where "luminous doubt" was the brief [C047]. The focus model more often leaves the tone operative past the resolution [C047][C071]. Both, however, over-explain their images; no analyst grants either writer genuine ambiguity [C032][C013].

**Replication:** both halves of this section recur across original and extension evidence; the extension adds no prompt class in which the comparison model's procedural strength converts into a win.

## Range, recurring habits, and floor versus ceiling

Shared habits are extensive and should not be mistaken for differences: both recycle protagonist names (Elias/Elara against Mara), both lean on maxims, both cover every element, both explain their symbols, and premise originality is roughly equal — both independently make a quarantine a cover for weather engineering [C026][C032][C039][C064][C072][C084][C090].

One analyst argues the comparison model is wide-band and the focus model narrow-band: two near-mechanical element-recitations and three genuinely inventive stories against a uniform register, sentence length and moral temperature [C091]. This is a **one-packet, medium-confidence** reading, and another packet contradicts it directly, finding the focus model shifting register by genre — parable-plain declaratives in one story, lyric in another — while the comparison model holds one expository voice across ghost story, science fiction and fable [C091 vs. read_12's register observation]. The quantitative record tests the floor/ceiling claim: the focus model's minimum margin across all 50 pairs is +0.850 and its maximum +4.867, so within this sample its floor sits above the comparison model's ceiling on every prompt, while the *variance* in margin is largely produced by comparison-model peaks. That is a corroborated refinement, not a refutation: the comparison model has a real ceiling; it never reached the focus model's floor in a sampled pair, in either cohort.

## What each model still does better

**Focus (Qwen 3.8 Max), recurring and corroborated:** constraint metabolism [C020][C085]; tone converted into conduct rather than adjective [C021][C049][C086]; second minds with volition and consent as the plot's hinge [C002][C034][C062]; adversarial and institutional modeling [C022][C088]; objects that acquire new causal grammar rather than confirming a personal meaning [C011][C037][C040][C070][C078][C081]; calibrated, transmitting endings [C063][C089]; complicit protagonists [C054]; graded reliability of sources [C035]; minted rather than borrowed aphorism, where the comparison model's climactic wisdom is a near-verbatim Leonard Cohen lyric presented as a character's discovery [C066].

**Comparison (Qwen 3.7 Max), genuine but narrower and never decisive here:** material mechanism, including a repair that uses the warping of the metal to lock the glass [C051]; the coin as a functioning grafting counterweight [C058]; bodily suspense in a rescue [C031]; a wave-function method that actually selects an outcome [C019]; explanatory reframing as a distinctive intelligence of its own — "panic was just a miscalculation of sensory input" — which generates plot rather than decorating it [C059]; planted-anomaly reveals [C087]; and legibility, which several analysts defend as deliberate fable clarity rather than deficiency [C013][C019][C056]. It also produced one packet's only formal point-of-view risk. None of these strengths produced a win at ±0.5 in either cohort.

## Findings beyond the existing judging

- **New, corroborated:** the blinded panel's reversal prompts are the same prompts where the margin is smallest. The narrowest results — +0.850, +1.150, +1.417, +2.317 — fall on exactly the stories where analysts credited the comparison model with testable protocol, single-scene suspense, cleaner causal progression, and operationalized method [C019][C031][C069][C083]. Conversely the widest margins (+4.867, +4.817, +4.283, +4.167, +4.100) fall where the panel located the sharpest structural gap: speechless worlds, an unused camera, an explained moral in place of a discovery [C002][C040][C081]. Two independent judging layers agree on where the gap is thin.
- **New, and it removes an explanation:** typographic lineation cannot be the mechanism. Evaluators explicitly flagged the focus model's hard line breaks as a defect on two prompts and it still won both by +2.583 and +3.733; and the packets disagree about which model even has the metronomic layout, one assigning one-sentence-per-line to the comparison model and two to the focus model. **Surface-cue-sensitive** claims resting on layout should be discounted accordingly [C007][C052].
- **New:** restraint alone is not what the scoring tracks. On the one prompt where the panel found a clean reversal — the comparison model withholding, the focus model granting an outright wish — the focus model still won by a large margin, on grounds of plausibility and object integration [C006].
- **Corroborated:** evaluator notes independently reproduce ledger claims they never saw, including the tone-cure defect [C047], the camera as active instrument [C040], the coin reframed to hold breath instead of value [C057] alongside the comparison model's mechanically superior counterweight [C058].
- **Caution, extension-specific:** order sensitivity rose to 0.717 in the extension while disagreement fell to 0.732. Per-story margins should therefore be read with more slack than the aggregate sweep, which is unaffected.

## Disagreements and limitations

Minority readings worth preserving: one analyst holds that there are two distinct intelligences here and neither is globally superior, crediting the comparison model with the higher peak of conceptual invention and the focus model with a narrower band [C087][C091]. A second finds a comparison-model story reaching a third position on an impossible choice as intelligently as the focus model, and calls its acceptance of mortality more restrained than the focus model's magical renegotiation [C008]. A third finds the comparison model stricter on local causal mechanics in two places, and notes the two converge on one prompt's thesis, making the gap "a tendency, not a gulf" [C019]. A fourth records the comparison model briefly the more sober writer at one climax. These are well supported and should not be flattened.

Limitations. Per-story cohort labels were not supplied to me, so stability is tested through the aggregate statistics and through the breadth of packet coverage — the panel and evaluator evidence together span all 50 pairs. Packets overlap, so several prompts are seen by more than one analyst; this strengthens corroboration but inflates apparent independence. Both writers occupy one register family: no humor, essentially no formal experiment, little dialogue across social registers, and every prompt hands both a competent expert who is never wrong, which caps any psychological-depth claim for either [C072]. The taste for implication over statement is itself a bias the analysts flag [C038][C056]. Finally, "seems smarter" here means an impression produced by writing choices; nothing in this evidence measures general intelligence.

## Representative case studies

**Glass eye / discredited textbooks.** Comparison: the relic "flared with a dull, internal luminescence" and the psychic noise stops, the textbooks retroactively vindicated [C003]. Focus: the same eye is used to occlude a lamp's glare, the textbooks stay "wrong about obedience, yet right about one fragile fact," and a child's question — "She asked if he would decide for her" — redirects the climax so the relic ends in her pocket by her choice [C002][C035]. Margin +3.617.

**Fair-trade ink.** Comparison resolves an interpersonal deadlock chemically, "melting her paranoid defenses," and calls the result perfectly balanced without registering that an honesty-driven protagonist has overridden a survivor's consent [C062]. Focus gives the officer physical evidence he perceives himself, then withholds pressure at the decisive instant. Margin +2.917 — a moderate result for a large conceptual gap, which is itself informative.

**Somatic markers (narrowest pair, +0.850).** The comparison model converts skepticism into a testable protocol with a thirty-minute exposure and an observable finger twitch, while the focus model lets lamps brighten without a switch [C083]. **Prompt-dependent:** where the brief rewards procedure, the gap nearly closes.

**Stillpoint.** The comparison model builds the strongest pure causal chain in its packet, glass panels "precisely angled to refract ambient radiation," and plants the unnatural stillness long before explaining it [C087]. The focus model wins anyway on aftermath: the flaw reinterpreted as "a record of pressure," and villagers taught to guard the site "without turning it into a shrine" [C050]. Margin +2.883 — the clearest illustration that the comparison model's ceiling is real.

**Fortune-cookie writer (widest pair, +4.867).** Comparison: a silent guardian whose villagers never speak, whose deliberate orchestration is simultaneously "accidentally prophetic," ending in sleep [C005]. Focus: a first-person narrator whose accuracy comes "not from magic but from noticing which wounds repeated," and whose planted phrase later works as a password [C005][C037].

## Cited claim ledger

- **C015 — Required phrases: Qwen 3.7 Max recites, Qwen 3.8 Max re-functions:** Qwen 3.7 Max reproduces prompt tokens verbatim and repeatedly; in 148 both "sustains impossibilities" and "lighthouse prison off a jagged reef" appear twice nearly unchanged, reading as checklist compliance. Qwen 3.8 Max typically spends each token once, altered in grammar or function, so the constraint becomes load-bearing machinery rather than decoration.
  - Story 0148, `qwen3.8-max`:
    > Ewan needed the map because the tower had begun to hover between what happened and what was said.
    The assigned action "hover" becomes the story's metaphysics, the prison suspended between event and account. Qwen 3.7 Max spends the same word on dust motes and a pausing hand, both literal and decorative.
- **C055 — Rubric visible as narration versus givens metabolized:** Qwen 3.7 Max narrates with the assignment's headings: "motivation" is labeled in four of five stories ("His driving motivation was to collect the shapes of different hopes" — Qwen 3.7 Max, 48; "Her motivation was deeply personal" — Qwen 3.7 Max, 6; "His motivation was not simply" — Qwen 3.7 Max, 190), and the timeframe is labeled as such twice ("This specific timeframe always marked the beginning of his true work" — Qwen 3.7 Max, 190; "the timeframe inside the whisper of closing pages" — Qwen 3.7 Max, 48). Qwen 3.8 Max uses the words "motivation" and "timeframe" zero times, converting the same elements into story facts: "She meant to construct bridges from silos, not merely store what the past had threshed" (Qwen 3.8 Max, 350). The labeled style reads as compliance being demonstrated; the metabolized style reads as a world being inhabited.
  - Story 0350, `qwen3.7-max`:
    > Her singular motivation was to construct bridges from silos, transforming their isolated echo chambers into a unified sanctuary.
    The sentence pauses the story to certify a required element and pre-summarize its outcome, where Qwen 3.8 Max's equivalent line states intention as desire inside the fiction and adds resistance ("not merely store") instead of a success forecast.
- **C073 — Checklist display vs. metabolized elements:** Both writers include every required element, but Qwen 3.7 Max allocates display-sentences whose sole job is to exhibit the phrase, parking traits on props, while Qwen 3.8 Max lets the same phrase migrate and do structural work late in the story. Element-coverage rubrics would score these identically and miss the difference entirely.
  - Story 0064, `qwen3.7-max`:
    > His workspace was tenderly organized with small glass jars and polished wooden spindles.
    The required attribute is attached to furniture in a sentence with no narrative consequence; the trait never touches Elias or the plot.
  - Story 0064, `qwen3.8-max`:
    > Lark carried the antique sovereign case back through the graves, no longer burdened, but tenderly organized by purpose.
    The same attribute resurfaces in the closing lines as a transformed state of the protagonist; the required element became load-bearing for the arc.
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
- **C085 — Constraint as label versus constraint as event:** Given identical element lists, Qwen 3.7 Max often states the element and then explains its significance in a following clause, so the narration doubles as a compliance report. Qwen 3.8 Max more often fuses two elements into a single action or relation, letting the constraint generate plot rather than annotation.
  - Story 0006, `qwen3.7-max`:
    > She was an arsonist's daughter firefighter, spending her days battling the blazes that consumed the dry brush.
    The required character phrase is inserted verbatim as a predicate nominative, then padded with a generic gloss; nothing dramatic follows from the collision of arsonist and firefighter.
  - Story 0006, `qwen3.8-max`:
    > She came as the arsonist's daughter and as the firefighter who had answered his fires.
    The same phrase becomes a causal fact — she has personally extinguished her father's arson — which then supports the town's suspicion, her guilt, and the graft's meaning.
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
- **C034 — Other wills in the room:** Qwen 3.8 Max's stories contain counterforces that act and secondary characters who decide: patrol boats search, a courier bargains, a follower testifies, Sora chooses, a woman returns a letter. Speech occurs and changes outcomes. Across all five Qwen 3.7 Max stories no character speaks at all, opposition is passive or absent, and resolution requires no negotiation with any resistant will.
  - Story 0089, `qwen3.7-max`:
    > No words were needed between them, as their hearts beat in a unified and rhythmic cadence.
    The reunion explicitly bypasses verbal negotiation; read beside Qwen 3.7 Max's four other dialogue-free, antagonist-free stories, it reveals worlds without responsive others, where closure can be declared rather than engineered.
- **C016 — Populated scenes versus solitary meditation:** Qwen 3.8 Max dramatizes insight through other people, using dialogue, interviews, guardians, and repairers, so moral positions must be argued against resistance. Across all five stories Qwen 3.7 Max uses no direct dialogue at all; even crucial turns arrive as reported speech filtered through one narrating consciousness.
  - Story 0298, `qwen3.8-max`:
    > "A trammel needs anchor and consent," she said.
    > "You have neither."
    The story's central ethical problem, consent in sacrificial barter, is voiced by an opposing witness, forcing Mara to defend her position. The equivalent beat in Qwen 3.7 Max's 298 is narrated conclusion with no opposing voice.
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
- **C062 — Whether the other person is allowed to choose:** Facing identical prompts requiring a negotiated outcome, Qwen 3.7 Max resolves interpersonal resistance by removing the other party's agency and treats this as ethically clean; Qwen 3.8 Max makes the other party's discretion the hinge, supplies a perceptual cause for their change, and dramatizes the protagonist withholding pressure. This is moral-psychological modelling, not tone.
  - Story 0139, `qwen3.7-max`:
    > As the trembling fingers of Kaelen grasped the pen, the aromatic vapors of the ink began to work, melting her paranoid defenses into a pliable and rational acceptance of the equitable trade.
    A protagonist defined by "an innate compulsion for absolute truth" drugs a torture survivor into signing, and the narration calls the result "perfectly balanced" — a contradiction the story never registers.
  - Story 0139, `qwen3.8-max`:
    > Voss lifted the sheet, saw the man's branded shoulder, and understood that paperwork could be a coffin.
    > He took the stamp from his coat, held it above the ink, and paused.
    The conversion has a specific physical cause the officer perceives himself, and the pause preserves his freedom to refuse; Mara then explicitly declines to press — "honesty is strongest when it lets the other hand choose."
- **C088 — Institutions, bystanders and euphemism as causal forces:** Qwen 3.8 Max consistently gives the surrounding society independent behavior that constrains the protagonist — neighbors who avoid her, officials who arrive with instruments, states that operate through language. Qwen 3.7 Max's societies are usually a crowd that switches from apathy to awakening, or are absent from the frame entirely.
  - Story 0197, `qwen3.8-max`:
    > The Ministry had spent the season publishing revised histories, turning drowned villages into empty fields and hungry children into weather.
    Shows the exact grammatical operation of the regime's lie — agents converted into landscape and climate — rather than asserting that archives were altered.
  - Story 0197, `qwen3.7-max`:
    > The citizens stopped in the streets, their apathy shattering as the coded freedom of the truth resonated in their minds.
    Mass psychology as an instantaneous switch triggered by information alone; the population has no prior interests, fears or divisions that the broadcast must overcome.
- **C018 — Endings: Qwen 3.7 Max resolves the feeling, Qwen 3.8 Max leaves the meter running:** All five of Qwen 3.7 Max's endings certify a closed inner state, while Qwen 3.8 Max's endings displace resolution onto the world, leaving cost, obligation, or listening unfinished. The difference is whether the story stops when the character feels better or when the situation stops moving.
  - Story 0148, `qwen3.7-max`:
    > You breathe in the salty air, entirely at peace with your inevitable fate.
    The story certifies the narrator's serenity as its final fact. Qwen 3.8 Max's 148 ends with the hush "sustaining impossibilities until someone listened," and Qwen 3.8 Max's 298 binds Mara into ongoing servitude: "the promise kept her, fiercely gentle among the bones."
- **C038 — Closure that keeps the bill:** Qwen 3.8 Max's endings preserve cost: grief gets a smaller room rather than a cure; safety lasts only as long as choice is protected; rain is "no longer an ending," implying it once was. Qwen 3.7 Max's endings declare totality — the entire infinite cosmos gained, "perfectly content," "finally home," "perfect harmony of untamed and eternal love." The recurring pattern reads as maturity in Qwen 3.8 Max (resolution as rebalancing) versus wish-completion in Qwen 3.7 Max.
  - Story 0230, `qwen3.8-max`:
    > It did not cure grief, but it gave grief a smaller room.
    The sentence measures what was not fixed, which is what makes the fix believable; Qwen 3.7 Max's closing superlatives answer every debt the story raised, leaving nothing for the reader to weigh.
- **C063 — Monument endings versus transmission endings:** Qwen 3.7 Max terminates consequence: the curse is fully broken, the promise fully kept, and twice the protagonist is dissolved or drowned after all stakes are already settled, so no aftermath is owed. Qwen 3.8 Max ends with residue and propagation — a partially paid debt, a practice passed to others, a stranger receiving the same call.
  - Story 0038, `qwen3.7-max`:
    > With her purpose fulfilled, she closed her eyes and let the ocean reclaim everything.
    The death follows the completed data transfer and costs the plot nothing; it functions as a full stop rather than a consequence.
  - Story 0177, `qwen3.8-max`:
    > Somewhere, another walker felt the path arrive and lifted a frightened face.
    The resolution is explicitly incomplete and reproducible; the story's premise is shown continuing to operate on someone outside the frame.
- **C089 — Sealed exit versus returned custody, and surviving cost:** Qwen 3.7 Max ends at the threshold of revelation with the protagonist removed from the world and the threat neutralized. Qwen 3.8 Max ends after revelation with the protagonist back among others, the knowledge handed off, and at least one cost still unpaid. This structural habit is the packet's most reliable per-writer signature.
  - Story 0079, `qwen3.7-max`:
    > She descended into the light, and above her the crack slowly sealed itself shut.
    The story stops precisely where consequences would begin; the city she has just steered toward the watchers is left offstage and unaddressed.
  - Story 0079, `qwen3.8-max`:
    > When the children asked what the song meant, Ilem gave each a reed whistle.
    > He told them to listen for the pattern languages beneath every bright and silent thing.
    Knowledge is transmitted rather than consumed; the closing image is a distributed capability, matching Qwen 3.8 Max's endings in 0006, 0197 and 0388.
  - Story 0077, `qwen3.8-max`:
    > She was still photographically cursed, but she no longer feared the picture that might wait behind her eyes.
    The premise's damage persists after victory; only the relation to it changes, which is a more discriminating resolution than removing the condition.
- **C087 — Mechanism with measurements and planted anomalies:** At its best Qwen 3.7 Max builds reveals out of physical systems whose components were specified earlier, and supports them with quantities and angles. This yields a distinctive pleasure — the sense that the world was engineered before it was described — that Qwen 3.8 Max's more analogical machinery does not reproduce.
  - Story 0079, `qwen3.7-max`:
    > The pattern language was not merely descriptive.  It was operational.  The old cartographers had not just mapped the turtle-cities.  They had communicated with them.
    A genuine conceptual inversion: notation reclassified as interface. It retroactively justifies the whistle's tuning from the conch's encoded frequencies and produces the measurable consequence of the city tilting.
  - Story 0388, `qwen3.7-max`:
    > Inside the shattered glass dome, the howling air was remarkably, almost unnaturally, still.
    Planted early and paid off much later by the refraction-and-filtration explanation; the anomaly is evidence, not atmosphere, which is exactly the epistemic behavior a debunker story needs.
- **C091 — Wide-band Qwen 3.7 Max, narrow-band Qwen 3.8 Max:** Qwen 3.7 Max's quality varies enormously by prompt: two stories are near-mechanical element-recitations, three contain genuine invention. Qwen 3.8 Max holds a nearly identical register, sentence length and moral temperature across all five, which yields reliability but also a lower ceiling — Qwen 3.8 Max never risks the tonal or conceptual swing that produces Qwen 3.7 Max's best moments.
  - Story 0006, `qwen3.7-max`:
    > Her motivation was deeply personal, driven by a quiet need to prove that scars can sing.
    Representative of Qwen 3.7 Max's floor: the sentence exists to discharge an element, and the whole story proceeds as captioned tableaux with commentary.
  - Story 0388, `qwen3.7-max`:
    > They were precisely angled to refract ambient radiation into a subterranean filtration grid.
    Representative of Qwen 3.7 Max's ceiling: an ordinary described object is retroactively revealed as purposeful engineering, the kind of turn absent from Qwen 3.7 Max 0006 and 0197.
  - Story 0388, `qwen3.8-max`:
    > The debunker did not celebrate, because truth was fragile and easily stolen again.
    Typical Qwen 3.8 Max cadence and stance; the identical measured, one-clause-per-line temperament appears in the arson story, the funhouse story and the dystopia, indicating a single default mode rather than prompt-specific adaptation.
- **C035 — Sources partly right: epistemic calibration:** Given the identical required element (rumored cures in discredited textbooks), Qwen 3.8 Max builds a world of partial reliability — the texts are wrong about obedience, right about one fragile fact — while Qwen 3.7 Max's textbooks are simply vindicated and the relic works exactly as advertised. Qwen 3.8 Max's protagonists verify through accumulated small matches ("many quiet entries aligning"); Qwen 3.7 Max's deduce entire conspiracies in single expository leaps.
  - Story 0230, `qwen3.8-max`:
    > The discredited textbooks stayed wrong about obedience, yet right about one fragile fact.
    Graded reliability forces the protagonist to judge which claim to trust — a marker of epistemic maturity that Qwen 3.7 Max's flat verdict ("The discredited textbooks had been right") forecloses in the same story slot.
- **C039 — Same invention, different engineering:** Premise originality is roughly equal: both 0123 stories independently make the quarantine a cover for weather manipulation, and both 0289s build a public installation from hoarded letters. The writers diverge in what the premise is made to do, not in the premise itself — so creativity rubrics scoring conceptual novelty would likely tie them, and any smartness verdict must rest on execution.
  - Story 0123, `qwen3.7-max`:
    > The military was not containing a microscopic disease because they were desperately concealing a failed experimental weather weapon that had created a perpetual localized supercell.
    Nearly the same concealed-weather conceit as Qwen 3.8 Max's storm gate and lightning diverted into canals; the match shows the gap is in how discovery is dramatized and used, not in inventiveness of premise.
- **C065 — Reversal: Qwen 3.7 Max establishes rules and lands consequence in the body:** On physical causality Qwen 3.7 Max is the stronger writer. He states the constraint that makes an odd prompt element necessary, then pays it off with a specific sensory event. Qwen 3.8 Max's equivalent moments are efficacious by fiat and abstract at the point of payoff, substituting a beautiful noun list for a felt result.
  - Story 0093, `qwen3.7-max`:
    > Silas felt the rough, sharp bite of the stone beneath his knees, a beautiful, painful sensation he had almost completely forgotten.
    The return of friction — the story's premise — is registered on a specific body part as a mixed sensation, closing a chain that began with the dust's "internal gravity." It is the packet's most concrete payoff.
  - Story 0093, `qwen3.8-max`:
    > It touched each eel, and each eel remembered pressure, hunger, direction, and the dignity of resistance.
    The matched climax resolves into an abstract quadruple, with "dignity of resistance" carrying rhetorical rather than physical weight; nothing is felt by anyone.
- **C046 — Building at the seam between required elements versus arranging them in a row:** Given the same element lists, Qwen 3.8 Max locates where two elements share a logic and grows the plot from that overlap, so the object's specific nature drives events. Qwen 3.7 Max supplies each element in turn, correctly but interchangeably, so objects often function generically (a key that is merely a key, a lens that is merely glass).
  - Story 0100, `qwen3.8-max`:
    > They were not haunting the library; they were waiting for someone to file them gently.
    Undertaker, library, and distress signals are fused into one idea: mourning as cataloguing. The rest of the story follows from it — restored cards, unopened letters, names filed for rest.
  - Story 0197, `qwen3.8-max`:
    > She opened the booth, found a brass crank, and turned it until the lagoon hummed with a low coded tone.
    The key is used as telephony, not as a lock; the defunct phone company, the coded-freedom tone, and the lagoon become one mechanism.
- **C060 — Labeling the abstraction versus arguing with it:** Given the same abstract prompt element, Qwen 3.7 Max attaches it to a noun and glosses it in expository apposition, leaving it inert; Qwen 3.8 Max converts it into a contested proposition that generates the story's conflict. The result is that Qwen 3.8 Max's required elements are load-bearing while Qwen 3.7 Max's are ornamental tags.
  - Story 0177, `qwen3.7-max`:
    > For a decade, he had obeyed a decaying directive, an old military order that lost more meaning with every passing season.
    The phrase is named, defined, and then does no further work; the plot proceeds by console, wafer seal, and dream-vision rather than by any pressure the directive exerts.
  - Story 0177, `qwen3.8-max`:
    > A voice from the walls said, "Shelter is obedience."
    > Mara answered, "Shelter is a question."
    Two consecutive lines turn the same required element into a live dispute over what a directive means; the rest of the story tracks the word's mutation, "letters crawling from PROTECT to KEEP to HUNT."
- **C037 — Objects that return changed:** Qwen 3.8 Max plants phrases and objects that recur with altered function: "Begin where you are" appears as fortune, then as map-marginalia, then as the literal phrase that opens a door; the 0089 fortune ends blank because the future "has begun writing itself in light." Qwen 3.7 Max plants objects too (specs, Clara's letter) but payoffs arrive within the same movement and do not re-key the story's meaning.
  - Story 0119, `qwen3.8-max`:
    > When my own knock came at dawn, I used the phrase "Begin where you are."
    The fortune becomes a usable password: theme converted into plot instrument. The callback closes a causal loop rather than merely echoing, which is structural intelligence rather than ornament.
- **C070 — Motifs that change jobs:** Qwen 3.8 Max more consistently reuses a required abstraction in several causal roles. In 0001, a pause is first a ledger gap and interrupted breath, then an interpretive method, then a public interruption that allows evidence to be seen. Qwen 3.7 Max tends to state the abstraction’s personal meaning once the mechanism has done its work. Qwen 3.8 Max’s advantage is selective intelligence: fewer conceptual elements do more jobs.
  - Story 0001, `qwen3.8-max`:
    > The lanterns paused.
    > In that pause, Mira lifted the scorched testament high enough for its hidden names to catch firelight.
    The thematic “pause” becomes an actual temporal opening in the confrontation. This converts an interpretive motif into strategy rather than leaving it as commentary.
  - Story 0001, `qwen3.7-max`:
    > She realized that the pauses in her life, the silent moments between the chaos, were where her true strength was forged.
    Qwen 3.7 Max clearly supplies the intended significance, but the pause remains primarily a summarized life lesson. It does not acquire as many distinct functions within the plot.
- **C054 — Protagonists who owe something:** Qwen 3.8 Max self-implicates its healers: the novelist "had long confused control for care" (Qwen 3.8 Max, 48) and cut her characters' hopes "to make her book more severe"; the survivor's mercy-mathematics matter because he is himself in the ledger. Qwen 3.7 Max's protagonists are pure victims or pure fixers whose insights land on others — the oppressor's fear, the guilds' division — while their own wounds sit safely in backstory.
  - Story 0201, `qwen3.8-max`:
    > He sees the number of names he gave, and he sees the number of names he kept.
    > The difference is not zero, and that truth hurts more than the clinic knives.
    The survivor is morally implicated in what he survived; the non-zero remainder gives the story's concept of mercy something real to measure, where Qwen 3.7 Max's matching story gives the protagonist clean hands and a solvable equation.
- **C010 — Feeling becomes an epistemic instrument:** Qwen 3.8 Max more often dramatizes emotional control as an active conversion rather than naming a stable virtue. Fear, grief, and inherited memory are neither unquestioned truth nor noise to suppress; they become usable only after attention and testing. That calibration creates psychological and investigative intelligence.
  - Story 0392, `qwen3.8-max`:
    > Mara felt another person's terror slide beneath her ribs, and she breathed until it settled into evidence.
    The sentence makes regulation observable and links vulnerability to professional judgment. Mara neither drowns in the memory nor dismisses it; she changes its status through disciplined attention.
  - Story 0392, `qwen3.7-max`:
    > Yet, his fortified vulnerability allows him to endure the psychological assault without losing his grip on reality.
    Qwen 3.7 Max identifies the correct psychological capacity, but the narrator supplies the interpretation directly. The behavior is subsequently demonstrated through forensics, though the phrase itself does much of the evaluative work.
- **C049 — Attributes instantiated as practice versus attributes asserted as adjective:** Given peculiar character attributes, Qwen 3.7 Max attaches the phrase to a noun and moves on, sometimes transferring it to scenery; Qwen 3.8 Max converts it into observable behavior, including a working method the character could actually be seen performing.
  - Story 0098, `qwen3.7-max`:
    > surrounded by luminescent orchids that pulsed with an empirically whimsical rhythm
    The character attribute is displaced onto flowers as decoration; nothing Silas does is whimsical or, strictly, empirical.
  - Story 0098, `qwen3.8-max`:
    > She counted rain omens, recorded jokes told by tide pools, and admitted she was afraid.
    Three concrete practices that are simultaneously whimsical and methodological, plus an epistemic virtue (declared uncertainty) that belongs to real inquiry.
- **C021 — Tone as behavior versus tone as adjective:** Qwen 3.7 Max converts the required tone word into a descriptor attached to an object and then certifies the fit; Qwen 3.8 Max converts it into something a character does or refuses to do. The result is that Qwen 3.7 Max's tone is announced while Qwen 3.8 Max's is performed by the plot's omissions.
  - Story 0014, `qwen3.7-max`:
    > The metal caught the rising sun, glowing with a warm, incandescent restraint that perfectly matched his quiet demeanor.
    Restraint is treated as a visual property of gold leaf, and the narrator then grades its own work ("perfectly matched"). Nothing in the story is restrained; the ending grants total consolation.
  - Story 0014, `qwen3.8-max`:
    > For himself he keeps the last page blank, because the texture of what comes next must be earned, not invented.
    The tone is enacted as a withholding, and it costs the protagonist the one thing he most wants. The word is dramatized rather than applied.
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
- **C047 — Prescribed tone treated as a condition to be abolished versus a condition to be inhabited:** Qwen 3.7 Max converts atmospheric requirements into solvable problems and announces their elimination in the closing movement, which retroactively drains the story of the quality it was built to produce. Qwen 3.8 Max keeps the tone operative past the resolution, letting success arrive contaminated.
  - Story 0098, `qwen3.7-max`:
    > The luminous doubt that had plagued his mind was finally replaced by absolute certainty.
    The required tone is named as a symptom and then cured, so the story's final register is the opposite of its brief.
  - Story 0098, `qwen3.8-max`:
    > It did not restore every lost thing, and that restraint made Mira doubt her own success.
    Doubt is produced by the resolution rather than dispelled by it, and the doubt is specific — about the adequacy of the remedy, not free-floating mood.
- **C014 — Disclosure: Qwen 3.8 Max withholds, Qwen 3.7 Max announces:** Across the pairs, Qwen 3.7 Max's narrator states the story's meaning after the decisive image has already done the work, converting discovery into lecture. Qwen 3.8 Max arranges objects, gestures, and exits so the reader must assemble the meaning from residue. The behavioral signature is where interpretive labor sits: inside Qwen 3.7 Max's prose as conclusion, inside Qwen 3.8 Max's structure as arrangement.
  - Story 0393, `qwen3.7-max`:
    > This was the hidden truth of genuine rehabilitation.
    The brace image had already dramatized the thesis (flaw carried, not erased); this sentence pre-empts the reader's inference. On the same prompt, Qwen 3.8 Max ends before the hearing, leaving the thesis audible in the repaired song rather than stated.
- **C075 — Glossing what the scene already showed:** Qwen 3.7 Max recurrently follows a dramatized beat with a sentence assigning its emotional meaning, releasing the same information twice and shrinking ambiguity. Qwen 3.8 Max more often lets the beat stand or converts it into a subsequent action, trusting the reader to arrive.
  - Story 0064, `qwen3.7-max`:
    > This revelation gave the gardener a profound sense of peace and purpose.
    The baker's hidden fortune was already dramatized; this sentence instructs the reader what to feel about it.
  - Story 0329, `qwen3.7-max`:
    > She had finally succeeded in breaking free from the subterranean despair of her youth.
    Announces success and retroactively supplies a motivation label after the escape scene has already played out.
- **C052 — The definitional reversal as engine and as tic:** Qwen 3.8 Max's most frequent rhetorical structure is negate-then-substitute. Because it has the grammatical shape of a correction, it reads as insight whether or not a correction has occurred. Roughly half its uses carry real conceptual revision; the rest replace one word with a prettier one. Naming it matters because it is the single largest contributor to Qwen 3.8 Max's impression of intelligence and is not itself intelligence.
  - Story 0249, `qwen3.8-max`:
    > The water did not splash, it rang.
    Pure substitution: no prior expectation is corrected and no fact about the world changes; the device supplies cadence rather than thought.
  - Story 0197, `qwen3.8-max`:
    > The signal carried coded freedom, not a battle cry, but a promise that no honest line would stay erased in that city.
    Here the same structure does argue something — that resistance is continuity of transmission rather than confrontation — but the reader must distinguish it from the empty instances by content, not by form.
- **C064 — A single reusable nuance-machine:** Much of Qwen 3.8 Max's apparent subtlety is produced by one syntactic template — negate the obvious reading, then substitute an elevated one — deployed at least fifteen times across five stories. It reliably yields the surface of discrimination, but its content is uneven, and some instances collapse under paraphrase. This tempers the intelligence gap without erasing it.
  - Story 0168, `qwen3.8-max`:
    > Mira wanted to enlighten the mountain, not with victory, but with witness.
    Representative instance; the same frame appears in 0038 ("not as weapons but as letters"), 0093 ("not a command but an invitation"), 0139 ("not as a plea, but as evidence"), 0177 ("not leading but inviting").
  - Story 0177, `qwen3.8-max`:
    > She said, "The path chooses because mercy needs feet."
    The packet's clearest case of euphony outrunning sense: the aphorism is climactic, quotable, and does not survive restatement in plain terms.
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
- **C090 — Rival automatisms: the motivation label and the antithesis reflex:** Each writer has a compulsive sentence-shape that simulates a mental act. Qwen 3.7 Max's announces purpose in the language of a form field; Qwen 3.8 Max's supplies a rejected alternative to every assertion, which mimics discrimination even where none has occurred. Neither is inherently worse; they fake different virtues.
  - Story 0197, `qwen3.7-max`:
    > His motivation was simple but profound, driven by a desperate need to hold the line against the tyranny of indifference that allowed the regime to erase millions without a single protest.
    The word "motivation" is imported from the brief; the sentence explains the character to the reader instead of letting behavior imply it. The same construction appears in 0006 and 0388.
  - Story 0006, `qwen3.8-max`:
    > It was not music, yet it was a beginning, and beginnings can be songs.
    The antithesis frame arrives with no new information; the negation and the aphorism cancel, leaving cadence. The same frame recurs in every Qwen 3.8 Max story, including sentences that do earn it.
- **C026 — Shared reliance on fiat magic — difference absent:** Both writers resolve their central impossibility by declaring that it works. Qwen 3.8 Max's version is embedded in imagery and Qwen 3.7 Max's in pseudo-technical exposition, but neither earns the mechanism, and the packet does not support a claim that one writer's speculative logic is tighter than the other's.
  - Story 0224, `qwen3.8-max`:
    > Seed what you fear, it reads, and the mountain will open.
    The instruction and its result arrive by decree; the stone simply obeys, exactly as Qwen 3.7 Max's obsidian relic does after its feather ritual.
  - Story 0014, `qwen3.7-max`:
    > By translating that pitch into numerical sequences, he could weave the present atmosphere directly into his fictional timelines.
    A causal link stated in the vocabulary of method but with no operative content; equivalent in kind to Qwen 3.8 Max's decreed transformations.
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
- **C027 — Constraint becomes protocol:** Qwen 3.8 Max more consistently converts strange prompt elements into procedures with social and causal consequences. In 0066, elusive lyrics do not merely conceal information; they create a secret-sharing system that determines how the community can act. Qwen 3.7 Max identifies an encrypted payload but largely announces its function instead of dramatizing its organization.
  - Story 0066, `qwen3.8-max`:
    > Each person received only one line, so no single listener could betray the whole.
    The sentence links lyric form, surveillance risk, collective participation, and plot logistics. The constraint generates an actual information architecture.
  - Story 0066, `qwen3.7-max`:
    > The words he whispered into the dark were not mere poetry, but encrypted coordinates and historical truths.
    Qwen 3.7 Max clearly states what the lyrics contain, but the encryption remains a label; the story supplies fewer consequences for how the information is divided, verified, or socially held.
- **C050 — Second-order social consequences and the maintenance ending:** Qwen 3.8 Max consistently thinks past the victory to the institution that must survive it, including the risks created by the victory itself. Qwen 3.7 Max ends at the moment of achievement and describes the community only as a future beneficiary the hero imagines, never as an actor.
  - Story 0388, `qwen3.8-max`:
    > She taught the villagers how to guard the stillpoint without turning it into a shrine.
    Anticipates the failure mode of debunking — that a demystified site becomes re-mystified — which is exactly the error the whole story diagnosed.
  - Story 0098, `qwen3.8-max`:
    > If it contradicted evidence, they would keep it as a story, because imagination also needed shelter.
    A designed procedure with an explicit branch for disconfirmed cases; the community, not the expert, executes it over three days.
- **C029 — Mercy without epistemic overreach:** In 0393, Qwen 3.8 Max makes a mature distinction between evidence that someone has changed and evidence that someone is innocent or safe. Qwen 3.7 Max reaches a more categorical parole judgment from the clockwork metaphor. Qwen 3.8 Max therefore seems more ethically and causally disciplined: the artifact can make repentance audible without becoming a complete risk assessment.
  - Story 0393, `qwen3.8-max`:
    > He would carry the music to the hearing, not as proof of innocence, but as proof that change could be made audible.
    The parallel clauses sharply limit what the music box can establish. Mercy becomes an action and a form of testimony, not an acquittal.
  - Story 0393, `qwen3.7-max`:
    > And because of that profound awareness, Marcus was finally safe to release.
    The conclusion equates self-awareness, represented by a mechanical brace, with future safety. That is a psychologically and institutionally larger claim than the evidence supports.
- **C043 — Question-preserving archaeology:** In the archaeological dispute, Qwen 3.8 Max understands evidence as something that complicates political claims; Qwen 3.7 Max treats spectacle as decisive proof of a glorious counter-history. Qwen 3.8 Max’s conceptual intelligence lies in resisting the easy inversion from degrading myth to flattering myth.
  - Story 0205, `qwen3.8-max`:
    > She told them they wanted a verdict, but the place offered only a question.
    The archive does not authorize either faction’s total story. Its value lies in redirecting judgment toward continuing obligations of care.
  - Story 0205, `qwen3.7-max`:
    > Armed with this luminous proof Kaelen knew he could finally dismantle their oppressive narrative.
    Qwen 3.7 Max makes the discovery politically legible, but a single projection is allowed to settle origin, intention, doctrine, and future leadership at once.
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
- **C044 — Diagrammatic competence:** Qwen 3.7 Max more consistently supplies explicit mechanical sequences: identify components, align or calibrate them, observe a threshold, and trigger an outcome. This creates a useful local impression of procedural intelligence and gives fantastic machinery readable handrails.
  - Story 0143, `qwen3.7-max`:
    > The acid was slowly eating through the final membrane, counting down the seconds until the shutter would open.
    The physical deterioration of a barrier provides a clear timer and directly causes the camera event.
  - Story 0270, `qwen3.7-max`:
    > She aligned her thumbs with the fractal nodes, pressing down in the exact sequence dictated by the tail of the kite.
    The decoding is translated into a visible manual procedure rather than remaining purely intuitive or symbolic.
  - Story 0143, `qwen3.8-max`:
    > Each plate was coated with salts that changed color after measured delays, turning exposure into a patient clock.
    Qwen 3.8 Max can provide comparably lucid mechanics, so Qwen 3.7 Max’s advantage is one of frequency and emphasis rather than exclusive ability.
- **C069 — Local procedural intelligence:** When Qwen 3.7 Max slows down enough to connect discovery, test, feedback, and consequence, the prose can display stronger local causal intelligence than Qwen 3.8 Max’s associative leaps. Story 0079 is the clearest case: an encoded frequency leads to a musical test, physical vibration, and the turtle-city’s change of course. Qwen 3.8 Max’s corresponding shell language is more evocative but less testable.
  - Story 0079, `qwen3.7-max`:
    > The pattern language was not merely descriptive.  It was operational.  The old cartographers had not just mapped the turtle-cities.  They had communicated with them.
    This realization follows an observable experiment with the whistle. It changes both the meaning of cartography and the city’s physical behavior, so the exposition is supported by action.
  - Story 0079, `qwen3.8-max`:
    > They spelled thirst, they spelled distance, they spelled a road folded beneath the heat.
    Qwen 3.8 Max produces a resonant semantic progression, but the clicks’ translation is asserted rather than demonstrated. The passage shows symbolic compression more than procedural causality.
- **C083 — Local rules as suspense machinery:** At its best, Qwen 3.7 Max devises explicit operational rules that immediately constrain behavior. Bodily states become inputs, artistic gestures become outputs, and danger follows from breaking the rule. This creates a strong impression of local causal intelligence even when the larger thematic arc is conventional.
  - Story 0329, `qwen3.7-max`:
    > The living statues were blind, tracking only the erratic frequencies of fear and rebellion.
    > By keeping her heartbeat slow and rhythmic, she masked her presence as mere ambient machinery.
    The surveillance rule simultaneously explains the statues, the heart-rhythm method, and why panic would be dangerous. It turns an abstract requirement into a usable suspense constraint.
  - Story 0281, `qwen3.7-max`:
    > When warmth bloomed in her left hand, she painted wide, sweeping curves.
    > When coolness threaded through her spine, she drew tight spirals.
    The somatic markers produce distinct, observable artistic decisions. The sequence makes an otherwise mystical experiment procedurally legible.
- **C045 — Closure budget:** Qwen 3.8 Max is generally more controlled about how much resolution an ending consumes. Its closing images preserve continuation or incompleteness, while Qwen 3.7 Max often adds several synonymous assurances that the art survived, the grief healed, and the protagonist found peace. Qwen 3.8 Max’s selectivity lets an image carry implications without repeatedly certifying them.
  - Story 0247, `qwen3.8-max`:
    > The harbor carried her sign forward, luminous and unfinished, like a song made of mercy.
    “Unfinished” keeps the communal practice alive beyond Mara without claiming perfect preservation or total healing.
  - Story 0247, `qwen3.7-max`:
    > She knew the melody would survive.  The ocean whispered its final goodbye.  Tomorrow would bring a new song.  Elara smiled at the thought.  Her heart was finally at peace.  The silver tide continued to roll.
    Several consecutive sentences independently confirm survival, farewell, renewal, happiness, peace, and continuity, diminishing the need for inference.
- **C071 — Partial recognition over declared completion:** Qwen 3.8 Max more often allows an ending to preserve damage, uncertainty, or another person’s autonomy. This produces an impression of psychological maturity and formal control: the story ends after a meaningful change but before total cure. Qwen 3.7 Max more often names the achieved meaning and declares the work complete, which provides clarity at the cost of interpretive afterlife.
  - Story 0322, `qwen3.8-max`:
    > Mara placed the thread in his hand and did not demand recognition.
    > He looked at the thread, then at her, and his eyes filled with slow alarm.
    > He remembered her voice before he remembered her name.
    Mara accepts an incomplete, unsettling return rather than forcing a sentimental restoration. The sequence gives connection a precise psychological texture: recognition can arrive in fragments and still matter.
  - Story 0322, `qwen3.7-max`:
    > He closed his eyes and listened to the silence, the unsettling calm of a gallery at rest, knowing his work was finally complete.
    The final clause closes both the project and its interpretation. It is controlled and legible, but it forecloses the instability implied by altered memories and an illusion gallery.
- **C032 — Interpretive overcare:** Both writers frequently explain an image's moral meaning immediately after presenting it. Their preferred construction replaces one definition with another—“not merely this, but that”—which can sound incisive while reducing the reader's interpretive work. No consistent difference is strong enough here to favor either writer.
  - Story 0066, `qwen3.7-max`:
    > The broadcast was not just a transmission of data, but a lifeline to their shared humanity.
    The sentence converts an already legible action into an explicit universal moral, narrowing the image rather than adding a new consequence.
  - Story 0229, `qwen3.8-max`:
    > The hush was not silence; it was screaming tenderness, a scream softened into mercy, a scream that loved the world enough to be gentle.
    Qwen 3.8 Max's paradox has rhythmic force, but the successive glosses prescribe how the tonal phrase should be understood instead of allowing the scene to carry it.
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
- **C072 — Assigned traits, provisional people:** Neither writer establishes a consistent advantage in deep characterization. Both frequently announce the required attribute and then organize the protagonist as an ideal reader-operator of the story’s conceptual system. The characters possess motives and selective memories, but secondary relationships seldom exert independent pressure for long. This limits claims that either writer is globally more psychologically intelligent.
  - Story 0001, `qwen3.8-max`:
    > Mira had been steadily adaptive since childhood, shaping molten glass while storms shifted the dunes around her village.
    The sentence efficiently connects attribute, craft, and background, but adaptability is supplied through summary rather than tested through a complicated interpersonal choice.
  - Story 0079, `qwen3.7-max`:
    > Elara was quietly driven, a woman who spoke little and worked through every burning noon while others sheltered beneath canvas awnings.
    Qwen 3.7 Max likewise states the attribute, though the contrast with sheltering residents adds behavioral support. Elara remains primarily the competent consciousness needed to decode the world.
- **C084 — The caregiver-rescue attractor:** Qwen 3.7 Max repeatedly remaps distinct prompts onto a similar emotional structure: Elara uses an artistic or quasi-scientific method to reach an inaccessible Julian. The recurrence produces fluency and emotional continuity, but it also makes the stories feel less selectively imagined. Qwen 3.8 Max uses a comparable coma-rescue plot once, yet ranges more often toward crowds, ecological archives, testimony, and collective refusal.
  - Story 0249, `qwen3.7-max`:
    > Her motivation was singular and desperate, seeking to breathe life into a shared dream she held with Julian, whose physical body lay comatose in the ward below.
    This establishes the recurring configuration directly: Elara's performance is organized around restoring an unreachable Julian.
  - Story 0281, `qwen3.7-max`:
    > She walked to where he sat in the corner armchair, his eyes open but fixed on some interior distance she could never reach.
    A different prompt again becomes a devoted Elara attempting to bridge Julian's inaccessible consciousness through art, bodily signals, and speculative science.
  - Story 0247, `qwen3.8-max`:
    > Mara did not ask them to remember her name.
    > She asked them to listen for the ones whose names had become water.
    Qwen 3.8 Max's forgotten artist redirects the emotional center away from recovering one intimate bond or her own legacy and toward a community's neglected dead.
- **C086 — Tone received as a noun versus tone dispersed into diction:** Qwen 3.7 Max frequently hands the assigned tone to the character as an abstract substance she feels, so the tone word floats free of the sentences around it. Qwen 3.8 Max distributes the tone into verbs, textures and smells, so the required mood is inferable before it is named.
  - Story 0006, `qwen3.7-max`:
    > The dark water mirrored the bruised sky, offering a profound kelp drift peace that always settled her restless mind.
    "Kelp drift peace" is delivered as a commodity the setting dispenses; the surrounding diction is neutral and would support any calm tone at all.
  - Story 0077, `qwen3.8-max`:
    > Mara understood the method, and she began to walk deeper into the funhouse corridor where the floorboards sweated perfume and brine.
    Repulsive allure is enacted at the level of the verb and the paired nouns — sweetness and secretion in one image — rather than asserted as a mood the character receives.
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
- **C040 — Constraint transmutation:** Qwen 3.8 Max more often makes several required elements causally transform one another. An empty camera, sign language, moonlight, mapped silence, and music become one operating system rather than separate prompt fulfillments. Qwen 3.7 Max usually introduces the same elements clearly but can abandon an object once its thematic function has been stated.
  - Story 0247, `qwen3.8-max`:
    > She had carved tiny signs into the pressure plate, a map only silence could read.
    > When the moon passed through the lens, the marks shone on the water as silver lines.
    The camera’s lack of film becomes functional: its physical interior carries signs, while its lens projects those signs onto water that then behaves like musical notation.
  - Story 0247, `qwen3.7-max`:
    > She did not need the empty device to capture this fleeting magic, for the memory was etched directly into her spirit.
    Qwen 3.7 Max explicitly removes the camera from the operative chain, reducing it to a preliminary emblem of unrecorded experience.
- **C078 — Objects retired vs. objects given afterlives:** When a required object finishes its function, Qwen 3.7 Max shelves it and declares it complete; Qwen 3.8 Max transforms it and lets it carry meaning into the ending. A small recurring difference that element-checklists cannot detect.
  - Story 0329, `qwen3.7-max`:
    > The locust shell lay quietly on the wooden planks, its purpose beautifully fulfilled.
    The narration pronounces the object done, closing by decree what the image could have kept alive.
  - Story 0329, `qwen3.8-max`:
    > In the orchard, the locust shell dissolved into a small gold leaf.
    > Mara tucked the leaf into her case and smiled through tears.
    The tool becomes a keepsake that travels forward with the character; meaning stays inside the story's world instead of being summarized by the narrator.
- **C081 — Prompt nouns get careers:** Qwen 3.8 Max more often makes an assigned object evolve from relic to instrument to meaning-bearing consequence. Qwen 3.7 Max commonly gives the object an immediate symbolic label and leaves it in that role. This is not simply better symbolism; it is a difference in whether a prompt element enters the story's causal grammar.
  - Story 0247, `qwen3.8-max`:
    > She had carved tiny signs into the pressure plate, a map only silence could read.
    The film-less camera's apparent deficiency becomes the mechanism by which sign language, moonlight, water, and music interact. Several constraints become mutually necessary.
  - Story 0247, `qwen3.7-max`:
    > She did not need the empty device to capture this fleeting magic, for the memory was etched directly into her spirit.
    Qwen 3.7 Max explicitly dismisses the camera from the operative solution. It remains a symbol of unrecorded experience rather than an active component of the performance.
- **C066 — Borrowed wisdom versus minted wisdom:** Both writers end on aphorism, but their provenance differs. Qwen 3.7 Max's climactic insights are recognizable circulating quotations delivered as the character's hard-won discovery; Qwen 3.8 Max's are constructed for the specific story and consistent with its events. This is a selective-intelligence difference: knowing that a familiar phrase cannot carry a scene's revelation.
  - Story 0168, `qwen3.7-max`:
    > "But the cracks are just the places where the light eventually gets in to wake the sleeping woods."
    A near-verbatim Leonard Cohen lyric, presented as the mentor's original wisdom; the same story's other keynote, "Your grief is just love with nowhere to go," is likewise a widely circulated formulation.
  - Story 0038, `qwen3.8-max`:
    > It said: strength is the place where fear learns to keep watch for others.
    Newly built, and it restates the prompt's "encrypt vulnerability as strength" in terms the story has actually earned through the coffins, the children, and the copied dance.
- **C051 — Reversal: Qwen 3.7 Max's material mechanism against Qwen 3.8 Max's figurative climax:** When a physical problem must be solved, Qwen 3.7 Max frequently invents a workable material solution, while Qwen 3.8 Max often escalates into metaphor at the decisive moment, letting an abstract noun perform the action. This is the clearest place where Qwen 3.8 Max's lyricism substitutes for causality.
  - Story 0100, `qwen3.7-max`:
    > He began to fit the pieces into the warped bronze, using the very distortion of the metal to lock the glass in place.
    The obstacle (a warped housing, a shattered lens) becomes the means of repair — a real solution derived from the specific damage described.
  - Story 0100, `qwen3.8-max`:
    > Elias occupied another impossible space, squeezing his grief into the crack between living and drowned.
    At the climax the required method is applied to an emotion rather than a body, and the resulting widening of the crack is asserted rather than caused.
- **C058 — Engineering ingenuity with arbitrary objects:** Qwen 3.7 Max consistently solves the prompt's arbitrary props as functioning mechanisms: the coin becomes a grafting counterweight, the storm glass runs on real camphor chemistry, and the cuckoo-clock weight anchors an acoustic baffle. Its methods cause their climaxes, as in story 190: "He turned a small dial on his control panel, widening the primary acoustic baffle" (Qwen 3.7 Max, 190). This is substantive causal cleverness, not vocabulary.
  - Story 0006, `qwen3.7-max`:
    > The heavy brass coin acted as a perfect counterweight, holding the red thread taut without crushing the tender bark.
    The required object performs mechanical work that the scene genuinely needs — tension without crushing — giving the ritual a plausible body where Qwen 3.8 Max's use of the same object is atmospheric.
- **C031 — Crisis enters the body:** Qwen 3.7 Max is more effective when suspense needs bodily pressure. In 0229, the ship's approach is observed through strained posture, duration, fog, and dangerous geography. Qwen 3.8 Max's corresponding turn is elegant but rapid. Qwen 3.7 Max's physical insistence gives the rescue a felt cost that its explicit moral language sometimes lacks.
  - Story 0229, `qwen3.7-max`:
    > Elias held his breath, his knuckles turning white as he gripped the iron railing.
    The body registers uncertainty before the rescue succeeds, briefly preventing the scene from functioning as a foregone symbolic demonstration.
  - Story 0229, `qwen3.8-max`:
    > The ship's bell answered once, faint and amazed, and the bow turned toward the safe channel.
    Qwen 3.8 Max's image is graceful, but the danger resolves within the same sentence and offers less bodily or navigational resistance.
- **C019 — Counterweight: Qwen 3.7 Max's causal mechanics can be tighter:** When the prompt supplies a technical method, Qwen 3.7 Max sometimes makes it do literal causal work where Qwen 3.8 Max uses it atmospherically. In 264 Qwen 3.7 Max operationalizes wave functions as outcome-selection that causes the bloom; in 393 Qwen 3.7 Max respects its own constraint (the mainspring cannot be replaced, so the maker braced it), while Qwen 3.8 Max's repairer simply installs a new spring, quietly canceling her thesis that the break must be carried rather than swapped out.
  - Story 0264, `qwen3.7-max`:
    > He collapses the unlikely outcomes, forcing the seed to choose life.
    The assigned method becomes a mechanism with a consequence. Compare Qwen 3.8 Max's 264: "She let the spark answer itself through a wave function of green memory," where the phrase decorates an event that would occur anyway.
- **C059 — Explanatory reframing as intellectual signature:** Qwen 3.7 Max reaches for conceptual redescription — emotion restated as mechanism or system — which is a real and distinctive kind of smartness: "Mercy was not the absence of retribution, but the conscious refusal to propagate the cycle of systemic violence" (Qwen 3.7 Max, 201). The cost is anesthetic: once panic is a miscalculation, the fix is calibration, and the story loses what cannot be calibrated. Qwen 3.8 Max's parallel wisdom carries more with less theory: "Silence can carry you," she said, "if you let it hold what is heavy" (Qwen 3.8 Max, 190).
  - Story 0190, `qwen3.7-max`:
    > He knew that panic was just a miscalculation of sensory input.
    A genuinely interesting clinical reframe that re-describes fear as information-processing and thereby motivates the story's acoustic-engineering solution — conceptual intelligence generating plot, not just decorating it.
- **C056 — Whether the universe endorses the moral:** In Qwen 3.7 Max, the setting converts when the insight lands: forests soften, batons power down, applause erupts "loud, messy, and deeply united" (Qwen 3.7 Max, 350). In Qwen 3.8 Max, the world stays noncommittal or returns only ambiguous signs — a crack that is "not music," warmth that is "perhaps his fever." This is the deepest maturity divide in the packet: whether reality is made to applaud the protagonist's growth.
  - Story 0201, `qwen3.7-max`:
    > The oppressive glow of the canopy seemed to soften, shifting from a punishing glare to a gentle twilight.
    The penal biome itself relents the moment forgiveness is whispered, ratifying the moral from outside. Qwen 3.8 Max's matching passage keeps the world neutral: "the forest keeps its purple silence, neither granting absolution nor demanding more blood" (Qwen 3.8 Max, 201), which forces the mercy to stand without cosmic sponsorship.
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
- **C057 — Motif economy versus decorative simile:** Qwen 3.8 Max metabolizes the required object into a governing image-system that pays off late: in story 6 the coin, the stump's "throat opening after long silence," and the final "thin green note" all trade in one breath-and-song economy. Qwen 3.7 Max's images are individually pleasant but reset per sentence — bruised sky, slow silent ships, warm protective blanket — decoration rather than structure.
  - Story 0006, `qwen3.8-max`:
    > The foreign coin warmed against her chest, drilled once so it could hold breath instead of value.
    The arbitrary prompt object is re-purposed — value converted to breath — which binds the coin into the story's song motif and sets up the ending's "proof" acoustically rather than by assertion.
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

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0001 | +3.633 | 664 | 726 | 3 | 0.733 |
| 0006 | +3.083 | 699 | 706 | 3 | 0.167 |
| 0014 | +3.967 | 604 | 714 | 3 | 0.600 |
| 0027 | +2.550 | 723 | 671 | 3 | 0.233 |
| 0038 | +3.750 | 668 | 644 | 3 | 1.167 |
| 0048 | +3.800 | 693 | 742 | 3 | 1.400 |
| 0064 | +3.417 | 651 | 693 | 3 | 0.833 |
| 0066 | +3.450 | 625 | 745 | 3 | 1.233 |
| 0077 | +3.050 | 746 | 723 | 3 | 0.900 |
| 0079 | +1.417 | 713 | 725 | 3 | 2.167 |
| 0089 | +3.550 | 715 | 695 | 3 | 0.900 |
| 0093 | +3.083 | 661 | 645 | 3 | 0.167 |
| 0098 | +3.867 | 608 | 707 | 3 | 0.733 |
| 0100 | +3.250 | 607 | 698 | 3 | 0.700 |
| 0119 | +4.867 | 694 | 768 | 3 | 0.600 |
| 0123 | +4.100 | 660 | 689 | 3 | 0.667 |
| 0125 | +2.917 | 667 | 709 | 3 | 0.500 |
| 0139 | +2.917 | 679 | 792 | 3 | 0.033 |
| 0142 | +2.583 | 660 | 699 | 3 | 0.833 |
| 0143 | +3.200 | 602 | 746 | 3 | 0.400 |
| 0148 | +4.167 | 664 | 773 | 3 | 0.333 |
| 0165 | +2.950 | 740 | 704 | 3 | 0.233 |
| 0168 | +2.800 | 711 | 718 | 3 | 1.067 |
| 0177 | +3.350 | 650 | 781 | 3 | 0.700 |
| 0190 | +2.917 | 634 | 765 | 3 | 0.833 |
| 0197 | +3.167 | 600 | 675 | 3 | 0.333 |
| 0201 | +3.350 | 639 | 781 | 3 | 0.700 |
| 0205 | +3.217 | 657 | 709 | 3 | 0.233 |
| 0209 | +4.283 | 679 | 786 | 3 | 0.900 |
| 0220 | +3.733 | 739 | 693 | 3 | 0.200 |
| 0224 | +3.433 | 660 | 714 | 3 | 0.000 |
| 0229 | +1.150 | 757 | 689 | 3 | 1.767 |
| 0230 | +3.617 | 792 | 761 | 3 | 0.433 |
| 0231 | +3.200 | 707 | 780 | 3 | 0.400 |
| 0247 | +4.817 | 639 | 755 | 3 | 1.633 |
| 0249 | +2.883 | 779 | 752 | 3 | 0.567 |
| 0264 | +2.317 | 713 | 766 | 3 | 0.633 |
| 0270 | +2.883 | 796 | 707 | 3 | 0.767 |
| 0281 | +0.850 | 707 | 723 | 3 | 2.700 |
| 0289 | +2.817 | 706 | 745 | 3 | 0.967 |
| 0298 | +3.917 | 669 | 725 | 3 | 0.833 |
| 0310 | +3.483 | 724 | 796 | 3 | 0.367 |
| 0322 | +3.417 | 797 | 743 | 3 | 0.500 |
| 0324 | +2.883 | 674 | 702 | 3 | 0.433 |
| 0329 | +3.033 | 702 | 738 | 3 | 0.067 |
| 0350 | +2.833 | 695 | 709 | 3 | 0.333 |
| 0388 | +2.883 | 663 | 702 | 3 | 0.233 |
| 0391 | +2.967 | 601 | 717 | 3 | 0.400 |
| 0392 | +3.750 | 694 | 726 | 3 | 0.500 |
| 0393 | +3.483 | 640 | 724 | 3 | 0.500 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-xhigh`, `gpt-5.6-high`, `kimi-k3`.
Synthesis editor: `claude-opus-5-xhigh`. Verified subjective claims: 91.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
