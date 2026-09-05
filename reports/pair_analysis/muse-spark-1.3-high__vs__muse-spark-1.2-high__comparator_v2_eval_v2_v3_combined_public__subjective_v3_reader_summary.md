# Muse Spark 1.3 (high) vs. Muse Spark 1.2 (high): comparative writing analysis

Focus model: `muse-spark-1.3-high`. Comparison model: `muse-spark-1.2-high`. Direct-comparison scope: `comparator_v2_eval_v2_v3_combined_public`.

## In one paragraph

Give both models the same short-fiction prompt and the required ingredients arrive differently. Muse Spark 1.3 turns a required trait into working machinery: a man involuntarily truthful because a childhood fever burned the filter from his speech becomes a toll keeper who charges travelers a true account of their day, a fee the story later collects [C030]. Muse Spark 1.2 more often names the same trait, hands it to a helpful side character, and lets the sentence stand as atmosphere. Conflict follows suit. In 1.2, opposition dissolves at the moment of recognition, and soldiers lower their hammers because a name found this way could not be ordered, only recognized [C035]; in 1.3, mercy takes the form of a lie to the council that carries a punishment somebody must risk [C035]. Endings differ accordingly: 1.3 leaves costs and unfinished business on the page, while 1.2 closes by stating what its heroine has learned. Across twenty shared prompts the ordering clearly reverses only once, on a piece about silence, where 1.2 hears a house through the kettle never whistling and a mother humming with her mouth closed [C031]. That gift for the exact small observation, like the neighbor's sugar bowl refilled only before the knock, is 1.2's best claim on a reader [C018].

## Quantitative context

Across 20 matched prompts, the focus model recorded 14 wins, 5 ties, and 1 loss at the ±0.5 tie threshold. Its mean signed margin was +0.980 ± 0.405 (95% normal half-width).

Mean lengths were 687.3 and 691.5 words; the correlation between length difference and margin was +0.349.

## Comparative portrait

The two writers share a register — lyric fable, one-sentence paragraphs, prompt tokens visible on the surface, a sensitive protagonist and an inherited object — so the load-bearing difference is not style but what each treats a required element as being.

Muse Spark 1.3 converts a supplied phrase into machinery that the plot must obey. An abstract music term becomes a survival rule ("If he finishes the song cleanly, the echo will finish it louder and Hush will hear his own name in it and wake"), and the rule dictates the tactic and the discovery [C014]. An attribute gets an etiology and then an institution: involuntary truthfulness produces a toll paid in "a true account of their day," which the story later charges and settles [C030]. Prompt wording is re-grammaticalized into the story's own facts — "arms of steel" become issued prosthetics whose confiscation is a statutory threat [C034], and second-person prompt timeframes are converted into first person rather than quoted [C008].

Muse Spark 1.2 more often installs the same phrase as mood, doctrine, or refrain: an interrupted cadence is a mentor's definition and a city-wide feeling that nothing in the plot can violate [C014]. Required strings recur verbatim, sometimes colliding with themselves in one sentence [C034], and the required attribute frequently migrates from the protagonist to a companion — the supervisor is "powerfully gentle," the pilgrim "perpetually surprised" [C009].

The consequences propagate. In 1.2, secondary figures largely confirm the protagonist ("You made them listen to each other again") and the physical world ratifies her intuition [C027][C028]; opposition dissolves at the moment of recognition, "because a name found this way could not be ordered, only recognized" [C035]. In 1.3, a council likes anything "that keeps feet moving and hearts calm," a prisoner mocks the heroine's ribbons, and mercy is a lie carrying the penalty of "the stripping of her arms" [C027][C035]. Endings follow: 1.2 consolidates privately and names the lesson [C016][C011]; 1.3 leaves social residue, explicit shortfall ("She had not saved anyone... but she had kept a light on"), and objects that carry the meaning unglossed [C028][C016].

1.2's countervailing strengths are real and specific: recursive emblem logic that makes a mechanism and a psychology share one structure [C004]; artifacts converted into working instruments, as when a thorn-needle fits the etched line and turns a lockless key into a pen [C021]; exact two-person etiquette (the sugar bowl "refilled only before Mara knocked") [C018]; portable aphorism ("Loneliness is not cured, it is witnessed") and a wordless bread-sharing beat [C039]; correct long-exposure astronomy underwriting a miracle [C013]; and silence rendered as positive sensory content [C031].

## Does either model seem smarter?

"Seems smarter" here means a reader impression produced by visible choices, not a claim about general capability.

Five of the six blinded readings register that impression for Muse Spark 1.3, and all five ground it in non-lexical behavior: rules stated then obeyed [C014]; planted questions paid off, so a riddle decodes into "check the tower keeper logs" and the protagonist acts on it [C015][C029]; incentives attached to falsehoods ("These fictions keep rents stable and grief quiet") [C017]; invented detail given downstream consequence [C019]; narrative form fitted to the concept, including a communal "we" for a story about curing loneliness and a dead narrator for chronological confusion [C036]; care modeled as dosage rather than disclosure — a bell at dawn, silence until noon, one story at dusk; a window left cracked and a blanket on the landing [C001]; institutions that classify and appropriate memory [C002]; and cost paid on stage [C012][C035].

Crucially, the impression does not track the usual proxies. Mean lengths are effectively identical (687.3 vs 691.5 words, −4.2), and several critics judge 1.2 the smoother, better-subordinated sentence-maker, treating its polish as a reason to discount, not credit, the ranking [C018][C031][C034].

The dissenting reading must be preserved. One packet (gpt-5.6-high, read_04) declines a global ranking and splits the credit: 1.2 shows the stronger selective and structural intelligence in assigning artifacts causal functions [C021], while 1.3 shows the stronger social, psychological, and epistemic intelligence [C022][C023][C024][C025]. Notably the same critic model, on a different packet, did rank 1.3 first — so this is prompt-dependent variation, not a stable critic bias.

Two further checks constrain the verdict. The ledger contains a genuine reversal: 1.3's appetite for machinery produces more findable contradictions, including two incompatible authors for the same clue and a telegraphed climax [C020]. And one reading finds no supportable difference at all in thematic self-explanation — both writers halt to announce meaning in nearly identical syntax [C033] — which limits any claim that 1.3 trusts the reader more.

## Narrative reasoning and aesthetic judgment

*Causal and structural foresight (recurring, panel-supported).* 1.3's plots move by derivation from stated constraints; 1.2's by accumulation and epiphany [C014]. Obligations are tracked to payoff in 1.3 [C015], while 1.2 in the same prompt poses a test and silently drops it [C029]. 1.2's own version of foresight is emblematic rather than sequential: several supplied elements converge on a single instrument that then enables the covert action [C021].

*Psychological inference (mixed).* 1.3 converts feeling into working behavior — grief into restlessness into precision [C024] — and uses jokes as characterization rather than decoration, staging Posy's cathedral-and-cider question instead of reporting that a child is jocular [C038][C006]. 1.2's inference is finer at two-person scale and less propagating: the mutual pretense of the sugar bowl is exact, but never returns or shapes the plot [C018].

*Conceptual compression.* This is 1.2's clearest advantage: "nested patterns" becomes recursively nested identities [C004], and a valve "implied the whole trumpet, the whole ceremony, the whole harbor listening" [C004]. 1.3 competes by extension rather than compression, pushing "deciduous vows" onto institutional betrayal and grief for the dead [C037].

*Relevant-detail selection.* 1.3's inventories are functional — brittle twine, green copper nails, chewed bread paste that actually seals cuts [C003] — and its procedures brace fantasy against bodies and payment [C022]. The risk that this becomes garnish is acknowledged in the same claims [C022][C003].

*Restraint and reader trust.* Genuinely contested. 1.3 more often ends on an unglossed object or an unfinished feather [C016]; 1.2 more often ends on a thesis sentence [C016]. But both preserve gaps deliberately when the material demands it — a pale circle marking failed memory, a wax seal displayed "not as closure but as evidence of interruption" — and that behavior supports no ranking [C026]; and the parity finding on self-explanation stands against the degree-claims [C033].

## Range, recurring habits, and floor versus ceiling

The most conspicuous habit is 1.2's default protagonist: Mara in all five stories of two separate packets, in the same close third person, with the same lone-sensitive-expert role-shape and vindicating outcome [C010][C032]. 1.3 varies name, person, gender, age, social station, and even aliveness, and the variation is functional rather than cosmetic — the person chosen enacts the premise [C010][C036]. Tone range differs likewise: 1.2's register barely varies across mandated tones, while 1.3 performs them, so the label words become nearly unnecessary [C038].

Floor versus ceiling is the honest framing. 1.2's peaks are real and occasionally unmatched — the astronomy [C013], the aphorism and the silent bread [C039], the nested lullaby [C004], the withheld-sound quiet [C031]. But those peaks are intermittent, and the same explicitness that yields them yields the closing lectures [C039]. Quantitatively the direction is consistent rather than occasional: 14 focus wins, 5 ties, 1 comparison win across 20 pairs, mean margin +0.980 with a story-level 95% half-width of 0.405 and a median of +1.183.

## What each model still does better

**Muse Spark 1.2, on present evidence:** rendering absence as positive perception, which is a harder and more literal solution than 1.3's simile for the same task [C031]; single-sentence psychological compression and portable maxims [C018][C039]; recursive emblem architecture [C004]; artifact-to-instrument engineering [C021]; occasional verifiable technical mechanism [C013]; and, by making fewer checkable propositions, fewer catchable continuity breaks [C020]. One critic also judged 1.2's refusal of a memory-for-peace bargain the most adult decision in its packet, against 1.3's more obliging cosmos in the same prompt [C028].

**Muse Spark 1.3:** constraint synthesis, from prompt string to story fact to punishable stake [C034][C030]; promise accounting and decoding chains [C015][C029]; incentive-bearing institutions [C017][C002]; secondary wills that can veto the protagonist's best-sounding formulation ("No, she said, this is only work done cleanly after work done badly") [C023][C027]; cost placement [C012][C035]; calibrated care [C001]; form-concept fit [C036]; and humor that does structural work [C038][C006].

Note the asymmetry honestly: 1.2's advantages are largely local and non-propagating — the insight is stated and abandoned [C018] — while 1.3's are architectural and recur across prompts. No compensating ceiling should be manufactured for 1.2 beyond what the ledger supports.

## Findings beyond the existing judging

1. **Where the margin closes, a documented 1.2 strength is present (new, corroborated).** Every near-tie and the single loss coincides with a ledger-recorded 1.2 capability: 0109 (−0.550) is where 1.2 renders silence as withheld sound [C031]; 0382 (−0.417) holds the sugar-bowl observation [C018]; 0298 (−0.250) is where 1.2 refuses the cure and 1.3's costs are questioned as compressed [C012]; 0346 (+0.150) is the nested-lullaby story [C004]; 0244 (+0.250) holds 1.2's best aphorism and its wordless bread beat [C039]; 0028 (+0.083) is where 1.2's fable recognition is coherent on its own terms [C005]. The blinded portraits therefore predict where scoring converges.

2. **The yellow-star natural experiment survived unblinded scoring (corroborated).** Both writers independently invented a chalk yellow star; 1.3 made it the causal pivot that changes the protagonist's decision, 1.2 made it decorative texture [C019]. That story carries the second-largest focus margin in the set (+2.167), and the story-level notes independently credit the chalk archive and the pseudonym discovery.

3. **Prompt metabolism is visible to conventional judging too (corroborated).** Story-level failure-mode notes flag near-verbatim required-phrase repetition and "checklist rhythm" in 0078 and 0320 — supporting [C034] and [C008] while also confirming their counterexamples that 1.3 is not immune [C030].

4. **Enactment beats naming, measurably (corroborated).** On 0135 (+1.250) the notes single out staggered intervals operating structurally versus merely being named — precisely [C001]. On 0180 (+2.617) they credit child dialogue delivering wisdom rather than narrator-stated wisdom [C038] and a death giving "deciduous vows" mortal weight [C037].

5. **A packet-level reversal that did not survive (new).** read_04 treated 1.2's 0184 as its substantial counterweight, and the ledger credits its institutional analysis of struck-out names [C025]; yet 0184 drew one of the largest focus margins (+2.133), with the notes preferring 1.3's conceptual engine of absent things exerting gravity [C021].

6. **Opposite error signatures (portrait-level only).** The ledger documents 1.2's structural duplications [C034]; the complementary observation that 1.3's errors are local typos appears in a portrait but has no ledger entry, so it is flagged as uncorroborated.

## Disagreements and limitations

- **Minority reading, preserved:** one packet finds no globally smarter writer, assigning structural-causal credit to 1.2 [C021] and social-psychological-epistemic credit to 1.3 [C022][C023][C024][C025]. Two ledger entries find outright parity [C026][C033].
- **Intra-panel conflict on the same story:** 1.2's 0298 refusal is read as the packet's most adult decision by one critic and as an instantly rewarded choice by another [C012].
- **Surface-cue sensitivity:** the Mara repetition is itself a surface tell and carries only because role-shape repeats with it [C032]; aphorism is a quotability proxy [C039]; wit [C038] and formal novelty [C036] are easily over-rewarded; conspiracy-shaped plots may manufacture occasions for naming institutions [C017].
- **Length:** means are near-identical, but within-pair word-count difference correlates +0.349 with margin, so length is not wholly inert even though it does not favor 1.3 on average (−4.2 words).
- **Measurement noise:** mean evaluator disagreement 0.599 and mean AB/BA order sensitivity 2.073 exceed several individual story margins; single-story results such as 0109 should be read as suggestive, with the aggregate direction carried by 14/5/1 and the interval around +0.980.
- **Prompt narrowness:** the packets sample lyric-uplift, absence-and-preservation prompts that may reward 1.3's mixed-register concreteness; a different prompt set could compress the gap [C005][C036].
- **1.3's own liabilities:** sentimental climaxes, rapid conversions, and over-plotting contradictions are documented, not incidental [C019][C020][C012].

## Representative case studies

**0151 — load-bearing versus decorative invention (+2.167).** Identical invented image, opposite office: 1.3's star bears a pseudonym the protagonist invented and changes what she signs; 1.2's is "a careless yellow star" improving camouflage and touching nothing downstream [C019]. 1.3 buys the payoff with a sentimental beat 1.2 avoids [C019].

**0070 — the strength and its shadow in one story (+1.167).** 1.3 decodes the riddle into an action and settles the toll it named [C029][C030]; 1.2 poses a test and abandons it [C015][C029] and misuses the shared attribute, treating compulsive sincerity as accuracy [C030]. In the same 1.3 story, the clue has two incompatible authors [C020].

**0180 — dialogue as reasoning (+2.617).** Practical inventory does the work [C003]; a child's joke reassigns interpretive authority [C006][C038]; the required metaphor is extended to institutional betrayal and unkeepable promises of the dead [C037]. 1.2's counter-strength here is genuine — mismatched perception bridging generations [C003] and a half-mended window that refuses completion [C007].

**0109 — the one reversal (−0.550).** 1.2 converts "summarizing silence" into withheld sounds and a mother "humming with her mouth closed" [C031]; both writers reach for the same insect-in-amber figure [C031], and both announce the theme in matching syntax [C033]. 1.3's compensation is epistemic: a first-person supplicant who must draw the failed map himself [C032][C028].

**0028 — cost versus recognition, scored a wash (+0.083).** 1.3 gives mercy a statutory penalty and a conflicted witness [C035][C002]; 1.2 dissolves armed opposition through recognition [C005]. 1.3 then converts its witness almost as quickly [C035] — which, with the fable defense of 1.2's mode [C005], explains the parity.

## Cited claim ledger

- **C014 — Rules versus atmospheres:** Given an abstract required concept, Muse Spark 1.3 (high) converts it into a physical constraint that generates the plot's decisions; Muse Spark 1.2 (high) converts it into a named mood or doctrine that characters discuss. This is the single most consistent difference and it drives most others: Muse Spark 1.3 (high)'s scenes have stakes because a stated law can be violated, while Muse Spark 1.2 (high)'s scenes proceed because the narrator says the next thing happens.
  - Story 0013, `muse-spark-1.3-high`:
    > If he finishes the song cleanly, the echo will finish it louder and Hush will hear his own name in it and wake.
    The music-theory term is restated as a survival rule with a consequence, which then dictates the tactic (sing the phrase wrong) and the discovery that follows from it.
  - Story 0013, `muse-spark-1.2-high`:
    > He called it the interrupted cadence, the moment a hymn almost resolves but turns aside, leaving expectation hanging in empty air.
    The same element appears as a mentor's definition and a city-wide feeling; nothing in the plot can fail or succeed because of it.
- **C030 — Prompt attributes as premises versus prompt attributes as adjectives:** Both writers reinstall required phrases verbatim, so the tic is shared. The difference is what happens next: Muse Spark 1.3 (high) derives consequences from an attribute (a cause, a social consequence, an economy), while Muse Spark 1.2 (high) sometimes duplicates the attribute onto extra characters to buy a plot beat and mis-reasons from it.
  - Story 0070, `muse-spark-1.3-high`:
    > He was involuntarily truthful since childhood fever had burned the filter from his speech.  Travelers paid him no coin after the grid failed, only a true account of their day.
    The attribute gets an etiology and then generates an institution, which the plot later charges and settles ("he wanted her honest evening").
  - Story 0070, `muse-spark-1.2-high`:
    > She was also involuntarily truthful, so when she said I think it is a bee, Jonah knew she was not guessing but remembering something true.
    The attribute is copied onto a second and third character and then misused: compulsive sincerity guarantees honesty about belief, not accuracy of a guess. The logic is doing decorative rather than load-bearing work.
- **C034 — Prompt text metabolized versus recited:** Muse Spark 1.2 (high) embeds required phrases verbatim and repeatedly, producing visible seams where the prompt text collides with itself. Muse Spark 1.3 (high) rewrites each element into the story's facts, so the phrase disappears into consequence. The difference is integration, not obedience: both writers hit every element, but Muse Spark 1.2 (high)'s prose keeps pointing at the checklist while Muse Spark 1.3 (high)'s hides it inside stakes.
  - Story 0382, `muse-spark-1.2-high`:
    > That night a flyer appeared under every door announcing a meteor shower viewing in the rooftop garden during a meteor shower, hosted by management with cheap cider.
    The setting and timeframe phrases are pasted twice inside a single sentence, an unambiguous seam. The same pattern recurs across Muse Spark 1.2 (high): "retrocognitively trapped" three times in 0028, the stepping-stone method phrase twice verbatim, "warm coldness" three times.
  - Story 0028, `muse-spark-1.3-high`:
    > Her arms were steel, forged by the relief corps to lift beams and carry the injured, and she had vowed to cradle empathy in arms of steel.
    Muse Spark 1.3 (high) literalizes "arms of steel" as issued prosthetics, which lets the later threat of "the stripping of her arms" convert a prompt phrase into a punishable stake; the required wording survives only inside the story's logic.
- **C008 — Required phrases re-grammaticalized vs pasted in raw:** Both writers must absorb awkward required strings, including second-person timeframes and method phrases. Muse Spark 1.3 (high) rewrites them into the story's own grammar and person; Muse Spark 1.2 (high) sometimes inserts them as inert tokens, leaving visible seams — a pronoun that belongs to the prompt rather than to the narrator.
  - Story 0235, `muse-spark-1.2-high`:
    > Everything changed after seeing your own grave, which she did on a Tuesday when the thaw exposed a small weathered headstone behind the cabin bearing her name and tomorrow's date.
    The second-person "your" survives inside third-person narration; the required timeframe is quoted rather than assimilated. Muse Spark 1.3 (high)'s version of the same element converts person cleanly: "I found the cabin the morning after I found my grave" (0235, Muse Spark 1.3 (high)). The pattern recurs in 0084, where Muse Spark 1.2 (high) writes "after the pilgrim arrives became a true timestamp" while Muse Spark 1.3 (high) writes "After the pilgrim arrives, the keeper lights no lamps."
- **C009 — The prompt's required attribute migrates to side characters:** Muse Spark 1.2 (high) repeatedly assigns the required character attribute to a companion or mentor rather than the protagonist; Muse Spark 1.3 (high) embodies it in the lead. Muse Spark 1.2 (high)'s protagonists become neutral observers surrounded by colorful carriers of the required trait, while Muse Spark 1.3 (high)'s protagonists are themselves marked by it, raising the emotional stakes and making the trait testable in action.
  - Story 0256, `muse-spark-1.2-high`:
    > Her supervisor, an old acoustician named Ellis, was powerfully gentle, moving through the aisles as if afraid to bruise the air.
    The attribute "powerfully gentle" belongs to the bell ringer, yet Muse Spark 1.2 (high) gives it to the supervisor; Muse Spark 1.3 (high) gives it to the ringer himself: "He is a large man with burned hands, powerfully gentle in the way he lifts glass and children and failing equipment" (0256, Muse Spark 1.3 (high)). The same migration occurs in 0084 (Jonah is "perpetually surprised"), 0244 (Tomas is "desperately jocular"), and 0298 (the keeper is "fiercely gentle"), while Muse Spark 1.3 (high) assigns each trait to June, Mara, and Ilsa.
- **C027 — Other people as obstacles versus other people as mirrors:** Muse Spark 1.3 (high) routinely gives secondary characters interests that conflict with the protagonist's, including ridicule of the protagonist's project; Muse Spark 1.2 (high)'s secondary characters are almost always facilitators whose main function is to confirm the protagonist's insight. This produces a difference in perceived social intelligence that has nothing to do with prose quality.
  - Story 0256, `muse-spark-1.3-high`:
    > Ansel frowns at the cost and the strangeness, but the city council likes anything that keeps feet moving and hearts calm.
    Two distinct institutional motives, neither aligned with the hero's, and the council's support is cynical rather than admiring — an accurate model of how odd projects actually get funded.
  - Story 0298, `muse-spark-1.3-high`:
    > On the second night he noticed the ribbons and mocked her for decorating death with nursery tales.
    Muse Spark 1.3 (high) plants the reader's most likely objection to the story's own conceit inside a character, forcing the narrative to earn its symbolism rather than assert it.
  - Story 0256, `muse-spark-1.2-high`:
    > You made them listen to each other again, he said, his voice powerfully gentle even over the ringing.
    The supervisor exists to validate; the council's earlier objection ("a straight line from station to station") is dissolved by results rather than negotiated with.
- **C028 — Indifferent cosmos versus confirming cosmos:** In Muse Spark 1.2 (high), the physical world reliably ratifies the protagonist's intuition with an event; in Muse Spark 1.3 (high), the world stays neutral and what the protagonist supplies is effort, testimony, or partial repair. Muse Spark 1.3 (high) also states the shortfall explicitly, which reads as authorial control over sentiment rather than absence of feeling.
  - Story 0287, `muse-spark-1.3-high`:
    > She had not saved anyone, she knew, being too wistfully pragmatic for such stories, but she had kept a light on.
    The story names and refuses the rescue fantasy its own materials invite; the achieved outcome earlier is modest and negotiated ("supper twice a week").
  - Story 0256, `muse-spark-1.2-high`:
    > She had been right, the path did not drain energy, it gathered it.
    The protagonist's aesthetic preference is confirmed by physics, and by a free-energy claim at that; the objection was raised only to be overturned.
  - Story 0109, `muse-spark-1.2-high`:
    > Where his palm had pressed, a faint line now glimmered across the blank page, a river of pale gold.
    The map is delivered by miracle. In Muse Spark 1.3 (high)'s version of the same prompt the narrator draws it himself, badly, by hand.
- **C035 — Opposition with a price versus opposition that yields on recognition:** Muse Spark 1.2 (high)'s conflicts resolve when everyone simultaneously recognizes the right thing; nobody loses anything. Muse Spark 1.3 (high)'s protagonists commit acts that carry penalties and force witnesses to choose between duty and loyalty, so the resolution costs a character something.
  - Story 0028, `muse-spark-1.2-high`:
    > The soldiers lowered their hammers, because a name found this way could not be ordered, only recognized.
    Armed opposition capitulates after touching a stone; the state's coercion evaporates without consequence to anyone, including the elders who sent it.
  - Story 0028, `muse-spark-1.3-high`:
    > Joren stared at her, understanding the lie, and warned her that lies to the council meant the stripping of her arms.
    The merciful act is a lie with a statutory penalty, witnessed by a brother whose duty conflicts; the resolution requires him to change under cost rather than merely to recognize a truth.
- **C016 — Terminal thesis sentence:** Muse Spark 1.2 (high) habitually closes by stating what the protagonist has become or learned, often in a "no longer this, but that" construction; Muse Spark 1.3 (high) more often closes on an object or image that carries the meaning without glossing it. The Muse Spark 1.2 (high) tic implies a narrator who arrived knowing the moral, which reduces the sense that the story discovered anything.
  - Story 0070, `muse-spark-1.2-high`:
    > Mara, still candid, told him she had been afraid that her years of taking tolls had been pointless, but now she saw they had taught her patience.
    The final sentence explicitly names the character arc as a lesson, converting the story into its own summary.
  - Story 0013, `muse-spark-1.3-high`:
    > Instead she painted a natural history of a moment that never resolved, a bird in flight above still water between high towers, and left the final feather unfinished.
    The theme is delegated entirely to an artifact and an omission; no sentence tells the reader what it means.
- **C011 — Theme declared by the narrator vs performed by form:** Muse Spark 1.2 (high)'s climaxes arrive as narrator-stated insight in a repeated "understood then" cadence across 0084, 0235, and 0244; Muse Spark 1.3 (high) more often lets structure, objects, or dialogue carry the meaning — most extremely in 0244, where a communal we-narration performs the reciprocity the story is about.
  - Story 0084, `muse-spark-1.2-high`:
    > She understood then that the chip had not been missing, nor had she; they had both been waiting for the sky to move enough to complete the image.
    Muse Spark 1.2 (high) closes three of five stories with this explanatory gesture, telling the reader what events meant. Muse Spark 1.3 (high)'s 0244 ends with an object and an injunction — "chalk on the platform reading take care of each other on purpose" — after a story narrated by the community itself ("That was when the story changes for our town"), so the theme exists in the form even where never stated.
- **C004 — Recursive emblem logic:** Muse Spark 1.2 (high) is especially adept at conceptual compression. A single object can imply an absent institution, and a required formal idea can become a sequence of emotional viewpoints. This produces a lucid, almost liturgical compositional control.
  - Story 0346, `muse-spark-1.2-high`:
    > She tried again through nested patterns, humming the lullaby first as a mother, then as a daughter, then as the child she never stopped being.  Each layer nested inside the last, not louder but deeper, until the pane began to thin and tremble.
    “Nested patterns” is not left as visual ornament. Muse Spark 1.2 (high) translates it into recursively contained identities, allowing the mechanism and Mara's psychology to share one structure.
  - Story 0135, `muse-spark-1.2-high`:
    > The valve did not make music on its own, but it implied the whole trumpet, the whole ceremony, the whole harbor listening.
    The valve serves as disciplined metonymy: one fragment carries the missing instrument, political ritual, and listening community without requiring a longer historical scene.
- **C021 — Symbolic gear-train closure:** Muse Spark 1.2 (high) more consistently makes the assigned artifacts change what actions are possible. The stories operate as legible causal-emblem systems: an object is not only symbolic but converted into a tool that activates the required action. This is substantive structural selection rather than verbal sophistication, although it can make outcomes feel overdesigned.
  - Story 0384, `muse-spark-1.2-high`:
    > The needle fit perfectly into the etched line on the river stone, turning a key with no apparent lock into a pen.
    The apparently useless key, the heritage thorn, and the forger's craft converge into one instrument. That instrument then enables the covert unlinking, giving several prompt elements one causal hinge.
- **C018 — Muse Spark 1.2 (high)'s micro-etiquette and portable maxims:** At the two-person, sentence-level scale, Muse Spark 1.2 (high) is the more perceptive writer, noticing the choreography of mutual pretense and compressing interior states into memorable formulations. This is a real intelligence, distinct from polish, and it is Muse Spark 1.2 (high)'s best claim on the reader.
  - Story 0382, `muse-spark-1.2-high`:
    > In truth Mara's cupboard was full, and Elara's sugar bowl was almost always empty, refilled only before Mara knocked.
    The required phrase "agreed upon lies" is reinterpreted from conspiracy to tenderness, and the observation is exact: both parties maintain the fiction, and one of them prepares for it in advance.
  - Story 0233, `muse-spark-1.2-high`:
    > She went anyway, because faith had become too heavy to carry downhill.
    An abstract state (disenchantment) is compressed into a physical figure that also fits the climb she is undertaking, doing characterization and setting in one clause.
- **C039 — Aphoristic compression and quiet symbolic gesture:** Muse Spark 1.2 (high)'s distinctive gift is the compact maxim and the wordless relational beat, and at its best it rivals anything in Muse Spark 1.3 (high). The same explicitness, however, produces Muse Spark 1.2 (high)'s redundant thesis-endings, so the strength and the flaw are one habit.
  - Story 0244, `muse-spark-1.2-high`:
    > Loneliness is not cured, the woman said, it is witnessed.
    Ten words compress the story's entire argument; it is the packet's most quotable sentence and demonstrates real verbal intelligence.
  - Story 0244, `muse-spark-1.2-high`:
    > A third arrived at two, a deminer with a scar like a zipper, who simply sat beside Mara for an hour and shared his bread without speaking.
    A perfectly judged silent beat that enacts the maxim without commentary — proof Muse Spark 1.2 (high) can withhold when it chooses, which makes the over-explanation elsewhere a habit rather than a limitation of ability.
- **C013 — Muse Spark 1.2 (high)'s under-credited technical causality:** Muse Spark 1.2 (high)'s best moments contain real physical mechanism that Muse Spark 1.3 (high) rarely attempts; the 0084 climax runs on correct long-exposure astronomy, and the miracle is earned through instrumentation rather than incantation.
  - Story 0084, `muse-spark-1.2-high`:
    > The drone did not move, but the Earth did, and over ninety seconds the stars drew pale arcs across the sensor while the chip's glyphs pulsed in time.
    This is how star-trail photography actually works: fixed camera, Earth's rotation, timed exposure drawing arcs. Muse Spark 1.2 (high) builds the story's revelation on that real mechanism plus a plausible magnetometer sync, giving the fantasy an engineering spine. Muse Spark 1.3 (high)'s mechanisms are social and metaphoric — a chip as the "reed" of a stone instrument — elegant but unverifiable.
- **C031 — Silence rendered as negation — a specific Muse Spark 1.2 (high) strength:** Asked to dramatize "summarizing silence," Muse Spark 1.2 (high) finds sensory correlatives built out of withheld sounds, which is a harder and more literal solution than Muse Spark 1.3 (high)'s more abstract thickening of quiet. This is a genuine craft advantage for Muse Spark 1.2 (high) and the packet's best refutation of a blanket preference for Muse Spark 1.3 (high).
  - Story 0109, `muse-spark-1.2-high`:
    > In that quiet she heard the house again, the kettle never whistling, the pages turning without a hand.  She heard her mother humming with her mouth closed, saving the tune for later.
    Three sounds defined by what is missing, plus a psychologically exact image of thrift and deferral in a dying parent. The prompt's abstraction is converted into concrete perception.
  - Story 0109, `muse-spark-1.3-high`:
    > That was her gift, to let quiet thicken until meaning showed through it like insects in amber.
    Muse Spark 1.3 (high) explains the gift with a simile rather than staging it; the mechanism is asserted where Muse Spark 1.2 (high)'s is heard.
- **C015 — Promise accounting:** Muse Spark 1.3 (high) plants questions and pays them off with specific, checkable answers; Muse Spark 1.2 (high) sometimes plants a question and steps over it. This creates an impression of a narrator who is tracking obligations to the reader rather than improvising forward.
  - Story 0070, `muse-spark-1.3-high`:
    > If the hive forgets the flower, check the keeper, meant check the tower keeper logs.
    The riddle quoted earlier in the story is decoded into an instruction that the protagonist then physically follows up the tower to the chalk slate, closing the loop.
  - Story 0070, `muse-spark-1.2-high`:
    > To test her, Jonah asked her to reveal what the old keeper had told her years ago on the causeway, a story she had never shared.
    The story never supplies the withheld story; the next sentence has Mara open the matchbox instead, and the "test" is silently dropped.
- **C029 — Clues that decode versus clues that decorate:** Given the same "cryptic riddle" prompt, Muse Spark 1.3 (high) builds an inference chain in which the riddle maps onto a specific investigative action and the answer changes what a character does; Muse Spark 1.2 (high) supplies a stock riddle whose solution is functionally inert, and drops a test it has just set up. This is puzzle bookkeeping, not style.
  - Story 0070, `muse-spark-1.3-high`:
    > If the hive forgets the flower, check the keeper, meant check the tower keeper logs.
    An explicit decoding step: the figurative line resolves into a location, which resolves into evidence (the slate, the handwriting, the named order). The clue does work.
  - Story 0070, `muse-spark-1.2-high`:
    > To test her, Jonah asked her to reveal what the old keeper had told her years ago on the causeway, a story she had never shared.
    The test is posed and then abandoned — she opens the matchbox instead — and the riddle's answer ("bee") is never used to open, ignite, or determine anything; the resolution is an unrelated offering ritual.
- **C017 — Who profits from the story's lie:** When Muse Spark 1.3 (high) introduces a falsehood or institutional failure, it attaches beneficiaries, incentives and material consequences; Muse Spark 1.2 (high)'s institutions are set dressing that neither wants nor gains. This is the clearest case of substantive social intelligence rather than social vocabulary.
  - Story 0382, `muse-spark-1.3-high`:
    > These fictions keep rents stable and grief quiet, but they make the walls restless.
    The prompt phrase "agreed upon lies" is given an economic function and a class of beneficiaries; the ghost-story element is subordinated to a property-management motive, later named as protecting "the owner son."
  - Story 0233, `muse-spark-1.3-high`:
    > She abolished the seer tax, opened the granaries, and taught Tova to read maps by candlelight.
    The epiphany is cashed out in three concrete governmental acts, including a tax whose existence retroactively explains the court seer's earlier warnings.
- **C019 — Load-bearing versus decorative invention (the yellow star):** Both writers spontaneously invented the same image in 0151, which isolates the variable. Muse Spark 1.3 (high) assigns invented details structural work — they change what a character decides; Muse Spark 1.2 (high) assigns them texture and mild plausibility work. This is the difference between originality that pays and originality that merely occurs.
  - Story 0151, `muse-spark-1.3-high`:
    > Beside the star, in wobbly green letters, the children had added MAIL IT HOME.
    The star contains a pseudonym the protagonist herself invented; children she never met have archived a client's survival, which supplies the external argument that makes her sign her own letter with her real name.
  - Story 0151, `muse-spark-1.2-high`:
    > Mara smiled, pretending to be a stranger, and watched the girl add a careless yellow star to the code.  The addition was imperfect, but it made the cipher look even more innocent.
    The same image is a passing charm with a small tactical benefit; nothing downstream depends on it, and the protagonist's own dilemma remains untouched.
- **C036 — Narration that enacts the concept:** Muse Spark 1.3 (high) chooses narrative persons and frames that embody each prompt's core concept, so the form argues the theme. Muse Spark 1.2 (high) uses an identical third-person past for all five stories regardless of concept, a default rather than an instrument.
  - Story 0244, `muse-spark-1.3-high`:
    > That was when the story changes for our town, not with the water but with the quiet after, when the relief trucks could not get through and the radio kept promising help.
    A story about curing loneliness through mutual need is narrated in first person plural by the cured community; the "we" is the thesis made grammatical.
  - Story 0235, `muse-spark-1.3-high`:
    > The scroll claimed the cabin was a waystation between my death and my final dream, and that I had built it myself from remembered lumber.
    "After seeing your own grave" becomes literal death narrated by the dead man, so chronological confusion is experienced rather than described; Muse Spark 1.2 (high) renders the same element as a headstone that later "melted back into thaw," retracting its own premise.
- **C001 — The ethics of dosage:** Muse Spark 1.3 (high) repeatedly understands care as a problem of timing and permeability. Rather than maximizing emotional disclosure, Muse Spark 1.3 (high)'s protagonists ration experience and leave controlled openings through which vulnerable people can approach. This is a subtle form of psychological intelligence because it models support without possession.
  - Story 0135, `muse-spark-1.3-high`:
    > She rang the old signal bell for three minutes at dawn, then left silence until noon, then opened one story at dusk.  People could bear homecoming in small doses, she had learned, the way eyes adjust after darkness.
    The required “staggered intervals” become an actual trauma-informed practice. Silence is not decorative atmosphere but part of the intervention's causal design.
  - Story 0287, `muse-spark-1.3-high`:
    > She did not invite him inside at first, but left the kitchen window cracked and a blanket on the landing.
    The precise boundary matters: Mara offers warmth and access without forcing intimacy on Ellis or pretending that trust already exists.
- **C002 — Institutional peripheral vision:** Muse Spark 1.3 (high) more consistently sees that private mercy occurs inside systems that classify, punish, falsify, and extract information. Records are not neutral symbols; they are instruments contested by councils, witnesses, clerks, and families. That gives Muse Spark 1.3 (high) stronger social and causal intelligence.
  - Story 0028, `muse-spark-1.3-high`:
    > The council called her gift a sickness and ordered her to report only useful memories for trials and claims.
    The sentence identifies both stigmatization and bureaucratic appropriation: the council rejects Mara's experience while valuing whatever can serve prosecution or property claims.
  - Story 0135, `muse-spark-1.3-high`:
    > A widow corrected a death date, a daughter added a marriage in exile, a clerk admitted he had burned two ledgers.
    History emerges through unequal testimony, correction, and culpability. The clerk's admission prevents the archive from becoming a frictionless celebration of communal memory.
- **C012 — Prices paid on stage vs resolutions by recognition:** Muse Spark 1.3 (high)'s plots put cost in the present action — exile accepted, a sentence shouldered, a grid failure weathered mid-ceremony — while Muse Spark 1.2 (high)'s conflicts typically resolve through insight followed by immediate reward. Muse Spark 1.3 (high)'s causality is more expensive; Muse Spark 1.2 (high)'s is more epiphanic.
  - Story 0298, `muse-spark-1.3-high`:
    > At dawn the wardens returned, and Ilsa felt the iron of his sentence settle cold around her own ankles.
    The bartered-destiny premise becomes literal cost: Ilsa takes Tomas's punishment, loses her market standing, and the story continues past the bargain into consequences. Muse Spark 1.2 (high)'s 0298 climax is a refusal followed instantly by reward — blood "in that instant budded with white blossoms" — so the ethical choice is never tested against its price. The asymmetry repeats in 0256, where Muse Spark 1.3 (high) stages a grid failure during the pilgrimage and Muse Spark 1.2 (high)'s pilgrimage succeeds on first attempt.
- **C022 — Mundane ballast for miracles:** Muse Spark 1.3 (high) repeatedly braces fantasy with safety procedures, repair materials, food, payment, and bodily labor. These details supply humor and physical resistance without repudiating wonder. The result is a distinctive practical intelligence: characters test fate rather than merely comprehend it.
  - Story 0320, `muse-spark-1.3-high`:
    > Fantasy practicality was her creed, pack rope, mark bolts, test voltage before touching fate.
    The sentence makes the fantastic and the procedural simultaneous rather than oppositional. Its sequence also establishes a credible working hierarchy: secure the body and inspect the mechanism before interpreting the supernatural.
- **C023 — Metaphors subject to appeal:** Muse Spark 1.3 (high) is more willing to let another person veto the protagonist's grand interpretation. This creates rhetorical self-auditing: the story can retain its symbolism while refusing to let the central consciousness monopolize its moral meaning.
  - Story 0384, `muse-spark-1.3-high`:
    > This is calibrated treason in reverse, I whispered, measuring loyalty instead of betrayal.  She touched the key with no apparent lock where it rested on the page.  No, she said, this is only work done cleanly after work done badly.
    The keeper replaces the narrator's flattering, symmetrical formulation with a plainer account of repair. Her correction demonstrates social and ethical control because the story knows its own best-sounding phrase may not be its truest one.
- **C024 — Emotion converted into procedure:** Muse Spark 1.3 (high) more often makes grief or guilt modify how a character works. Feeling becomes timing, precision, secrecy, or restraint rather than remaining a backstory token attached to an heirloom. This gives the occupations psychological causality.
  - Story 0078, `muse-spark-1.3-high`:
    > Grief made her restless, and restlessness made her precise, because stillness on open water meant being taken.
    The brother's death explains both the requested restless tone and the prophet's exact working style. The causal chain is somewhat explicit, but it connects psychology to survival behavior rather than merely soliciting sympathy.
- **C025 — Sideways institutional pressure:** Muse Spark 1.3 (high) more regularly inserts a compact social contradiction not required to solve the fantasy problem: workers are paid in odd commodities, religious forgery serves generals, and an oracle occupies an ambiguous legal status. Such details imply systems extending beyond the protagonist's thematic mission.
  - Story 0109, `muse-spark-1.3-high`:
    > They kept a pebble-shore oracle in the north tower, half prisoner and half guest.
    The unresolved status makes the fort morally legible in seven words: it needs the oracle, honors her, and controls her. The story does not stop to turn that contradiction into a subplot, which helps it feel socially observed rather than diagrammed.
- **C020 — Reversal: Muse Spark 1.3 (high)'s density buys contradictions and telegraphing:** The same appetite for machinery that makes Muse Spark 1.3 (high) look controlled also makes Muse Spark 1.3 (high) the writer more likely to break its own continuity, over-foreshadow, or assert a revelation the scene has not earned. Muse Spark 1.2 (high)'s thinner plots are correspondingly harder to catch out.
  - Story 0070, `muse-spark-1.3-high`:
    > A junior tech wrote the riddle to reveal the truth without signing her name.
    Four lines later the story concludes "Mara understood her brother had left the clue before security took him," leaving two incompatible authors for the same message with no reconciling sentence.
  - Story 0013, `muse-spark-1.3-high`:
    > Free it and we drown, Tin whispered, but Mara knew she would have to uncage the bird before the end.
    The narrator announces the climax in advance, converting a decision into a scheduled obligation and undercutting the later "she chose to uncage" moment.
- **C033 — No difference in thematic self-explanation:** A tempting claim — that one writer trusts the reader more — is not supported. Both writers halt the action to announce the meaning in nearly identical syntax, and both end on aphorism. Any ranking on "restraint" or "ambiguity" would be noise here.
  - Story 0109, `muse-spark-1.3-high`:
    > I understood then that to map endless night one must not chart stars but intervals between losses.
    The narrator states the story's governing idea outright rather than letting the pebbles and blank page carry it.
  - Story 0109, `muse-spark-1.2-high`:
    > Mara understood then that her mother had been mildly obsessed not with loss but with preservation, keeping the shape of light so it could be found again.
    Same move, same construction, same position in the arc; the packet gives no basis for calling either writer more elliptical.
- **C038 — Humor performed versus humor reported:** Muse Spark 1.3 (high)'s jokes are played on the page and carry exposition, characterization, and the mandated tones; Muse Spark 1.2 (high) asserts that characters are jocular while the register stays solemn, so required attributes like "desperately jocular" and "endearingly feisty" are labeled rather than demonstrated.
  - Story 0180, `muse-spark-1.3-high`:
    > You said cathedrals are for God, she said, kicking a fallen finial, so why does God need cider?  Fen laughed until his quartz eye fogged, and said God probably preferred pie.
    Posy's feistiness and Fen's tenderness are established through an actual exchanged joke; the humor also smuggles in the orchard's economics, doing double duty.
  - Story 0244, `muse-spark-1.2-high`:
    > Tomas was desperately jocular, the kind of child who made jokes when the lights went out, who offered to sell her invisible umbrellas during a storm.
    Muse Spark 1.2 (high) summarizes jocularity instead of staging it; the one concrete joke is reported at a distance, and the story's tone remains uniformly gentle-solemn despite the attribute.
- **C006 — Jokes that carry doctrine:** Muse Spark 1.3 (high) uses humor to test abstractions socially. Characters tease, misunderstand, and revise one another, so wisdom emerges through conversational resistance rather than arriving already solemn and certified. This tonal flexibility makes the intergenerational relationship feel reciprocal.
  - Story 0180, `muse-spark-1.3-high`:
    > You said cathedrals are for God, she said, kicking a fallen finial, so why does God need cider?  Fen laughed until his quartz eye fogged, and said God probably preferred pie.
    Posy's joke challenges inherited categories of sacred space, while Fen's answer accepts her terms rather than correcting her. Their theology is generated through play, which prepares the later “deciduous vows” lesson.
- **C037 — Theme extended by application versus theme announced at close:** Muse Spark 1.2 (high)'s endings restate the moral the scenes already carried, flattening inference into verdict. Muse Spark 1.3 (high) puts the required concept under new pressure — institutions, the dead, broken contracts — so the metaphor generates meaning the prompt did not supply.
  - Story 0028, `muse-spark-1.2-high`:
    > Warm coldness settled over the ancient plaza beneath a shattered sky, not as contradiction but as truth, that gentleness could be radical and endurance could be tender.
    The closing sentence explains the paradox the scenes already demonstrated; Muse Spark 1.2 (high)'s 0235 ends the same way, defining "jaded wonder" as "attention paid long enough to love what remains strange."
  - Story 0180, `muse-spark-1.3-high`:
    > The guild had promised to stay forever, which was an evergreen vow in a deciduous world, and so it snapped.  June had promised to return each harvest, and when fever stopped her, Fen had to let that leaf go or hate the tree.
    "Deciduous vows" is extended to institutional betrayal and to grief for the dead, whose promises cannot be kept and must be released; the concept works harder than the prompt required.
- **C003 — Matter as coauthor:** In Muse Spark 1.3 (high), physical materials redirect plans and generate thought. Tools are mismatched, exhausted, or repurposed, and solutions emerge from their actual affordances. Meaning therefore appears to be made through work rather than merely illustrated by props.
  - Story 0180, `muse-spark-1.3-high`:
    > Inside were brittle twine, copper nails gone green, a bent spoon, stale altar bread, and a pocket catechism swollen with rain.  Using forgotten bag contents, they propped limbs with broken pew slats, tied them with twine, and sealed cuts with chewed bread paste.
    The inventory is causally active. Age, brittleness, shape, and adhesiveness determine what Fen and Posy can do, while sacred debris becomes horticultural equipment without losing its comic associations.
- **C026 — Truth that preserves the gap:** Both writers can distinguish repair from fabricated completeness. Muse Spark 1.3 (high) literalizes this through blank spaces and relinquished authorship; Muse Spark 1.2 (high) preserves evidence of interruption while merging rival records. This shared behavior is a substantive sign of epistemic maturity, so it cannot support a stable comparative ranking.
  - Story 0384, `muse-spark-1.3-high`:
    > Where memory failed, I left space and marked the gap with a pale circle.
    The forger refuses to turn stylistic mastery into false historical certainty. Selective omission becomes more truthful than a seamless reconstruction.
- **C010 — One reusable heroine and one voice vs five fitted persons:** Muse Spark 1.2 (high) names the protagonist Mara in all five stories and keeps the same close-third explanatory apparatus; Muse Spark 1.3 (high) varies name, grammatical person, and narrative distance — June in third person, an unnamed dead first-person narrator, a Mara seen from a communal we, Jonah Mar, Ilsa. The range is not cosmetic: each Muse Spark 1.3 (high) telling is fitted to its premise, and the packet's boldest literalization comes from the writer willing to change person.
  - Story 0298, `muse-spark-1.2-high`:
    > Mara had always been a reckless idealist, the kind who believed you could trade grief for grace if you bargained hard enough.
    This is the fifth consecutive "Mara had/was" opening from Muse Spark 1.2 (high) (0084, 0235, 0244, 0256, 0298), each in the same narrative voice. Muse Spark 1.3 (high)'s matching story opens "Her name was Ilsa," and Muse Spark 1.3 (high)'s 0235 solves the premise by making the narrator actually dead: "I found the cabin the morning after I found my grave."
- **C032 — Default-protagonist inertia and its correlate in role-shape:** Muse Spark 1.2 (high) instantiates the same protagonist — named Mara, third-person, lone sensitive expert, vindicated by the ending — in all five prompts; Muse Spark 1.3 (high) varies name, gender, person, and social station, and correspondingly varies what a protagonist can be. The naming itself is trivial; the correlated sameness of function is not.
  - Story 0109, `muse-spark-1.3-high`:
    > I came to the storm-tossed ridge fort because the maps had stopped working.
    Muse Spark 1.3 (high) shifts to first person and to a professional supplicant with a practical commission, which changes the story's epistemics: the map must be made by the narrator's own unreliable hand.
  - Story 0109, `muse-spark-1.2-high`:
    > The wind had taken the roofs from the storm-tossed ridge fort long before Mara arrived.
    The same protagonist name and stance arrive on a fifth consecutive prompt; across the packet her situation is reliably "bereaved woman inherits object, is proven right by a mentor and by the world."
- **C005 — Recognition does too much work:** Muse Spark 1.2 (high) more often lets a discovered symbolic truth dissolve political opposition without enough intervening choice, self-interest, or negotiation. Muse Spark 1.3 (high) usually gives resistance a human agent and an explicit cost, even when Muse Spark 1.3 (high) also hastens the final conversion.
  - Story 0028, `muse-spark-1.2-high`:
    > One by one, scavengers, soldiers, and finally Joren pressed their hands to the stone, tracing absence until the pattern spelled an older name, Asha, meaning gathering.  The soldiers lowered their hammers, because a name found this way could not be ordered, only recognized.
    The scene's fable logic is coherent, but the word “because” conceals the causal gap. Recognition itself is treated as sufficient to override orders, hierarchy, and possible punishment.
  - Story 0028, `muse-spark-1.3-high`:
    > Joren stared at her, understanding the lie, and warned her that lies to the council meant the stripping of her arms.
    Muse Spark 1.3 (high) establishes that mercy requires a specific official to become complicit in a punishable lie. This preserves more agency and danger than anonymous collective recognition does.
- **C007 — Damage versus destiny:** Muse Spark 1.3 (high) more often treats imperfection as evidence that an object has passed through contested reality; Muse Spark 1.2 (high) more often lets an object reveal that it was destined to complete a design. The difference is not realism versus fantasy but whether symbolic closure leaves a remainder.
  - Story 0135, `muse-spark-1.3-high`:
    > Mara fitted her dented valve into the broken trumpet and blew a low, imperfect note that startled the gulls.  The crowd quieted because imperfection proved the instrument was real and not a council broadcast.
    The damaged sound does not restore an ideal ceremony. Its defect authenticates a provisional civic practice and distinguishes it from official propaganda.
  - Story 0028, `muse-spark-1.2-high`:
    > Mara placed her tessera back into the hollow of the stepping stone, where it fit perfectly, completing a corner of the lost design.
    The perfect fit confirms a preexisting symbolic order. It is satisfying and controlled, but it narrows contingency: the artifact's meaning has been waiting to be correctly recognized.

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0013 | +1.467 | 781 | 787 | 3 | 2.067 |
| 0028 | +0.083 | 787 | 672 | 3 | 3.167 |
| 0070 | +1.167 | 681 | 771 | 3 | 2.133 |
| 0078 | +1.500 | 627 | 670 | 3 | 2.000 |
| 0084 | +1.200 | 670 | 703 | 3 | 1.733 |
| 0109 | -0.550 | 664 | 715 | 3 | 2.433 |
| 0135 | +1.250 | 692 | 701 | 3 | 1.833 |
| 0151 | +2.167 | 667 | 625 | 3 | 0.667 |
| 0180 | +2.617 | 733 | 723 | 3 | 0.433 |
| 0184 | +2.133 | 714 | 613 | 3 | 0.733 |
| 0233 | +0.550 | 726 | 605 | 3 | 2.900 |
| 0235 | +1.383 | 629 | 708 | 3 | 1.567 |
| 0244 | +0.250 | 775 | 799 | 3 | 3.367 |
| 0256 | +2.233 | 734 | 654 | 3 | 0.400 |
| 0287 | +1.383 | 676 | 631 | 3 | 1.900 |
| 0298 | -0.250 | 680 | 680 | 3 | 1.833 |
| 0320 | +0.667 | 647 | 637 | 3 | 3.000 |
| 0346 | +0.150 | 614 | 745 | 3 | 3.167 |
| 0382 | -0.417 | 616 | 750 | 3 | 3.033 |
| 0384 | +0.617 | 633 | 640 | 3 | 3.100 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-xhigh`, `gpt-5.6-high`, `kimi-k3`.
Synthesis editor: `claude-opus-5-xhigh`. Verified subjective claims: 39.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
