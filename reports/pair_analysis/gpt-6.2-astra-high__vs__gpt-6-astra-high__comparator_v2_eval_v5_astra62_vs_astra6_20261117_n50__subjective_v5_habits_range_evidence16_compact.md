# GPT-6.2 Astra (high) vs. GPT-6 Astra (high): comparative writing analysis

Focus model: `gpt-6.2-astra-high`. Comparison model: `gpt-6-astra-high`. Direct-comparison scope: `comparator_v2_eval_v5_astra62_vs_astra6_20261117_n50`.

## In one paragraph

Given the same short-fiction prompts, GPT-6.2 Astra and GPT-6 Astra often invent similar plots but put the meaning in different places. GPT-6.2 Astra lets a physical detail carry the turn and then stops: when both imagined a widowed repairman gilding iron out of grief, GPT-6 Astra explained his motive in a line of narration, while GPT-6.2 Astra simply had him eat a browned apple, core and all, standing up [C001]. GPT-6 Astra builds clear, testable mechanisms and serious ethical stakes. However, it tends to state the lesson after showing it. Across very different prompts it also returns to one story, in which a heroine usually named Mara recognizes her own error and publicly marks it [C044]. GPT-6.2 Astra has habits too, such as quiet hand-and-tool closing gestures and recycled names like Ada and Nell [C004]. Those habits rarely make its stories interchangeable, and its edge held on every one of fifty prompts. One qualification matters: GPT-6.2 Astra folds nearly every premise into a warm, old-fashioned world of kitchens and handcraft. Asked about life after a cryptocurrency crash, it retreats to loaves and lace, while GPT-6 Astra builds a real conflict about payment networks and surveillance [C058].

## Quantitative context

Across 50 matched prompts, the focus model recorded 50 wins, 0 ties, and 0 losses at the ±0.5 tie threshold. Its mean signed margin was +1.812 ± 0.143 (95% normal half-width).

Observed evaluator judgments: 299. 1 matched prompt pairs have fewer than two observed orders per evaluator. Means use available judgments. The normal interval is an approximate sampling summary; it does not bound missing judgments or establish a definitive winner.

Mean lengths were 727.8 and 689.7 words; the correlation between length difference and margin was +0.112.

# GPT-6.2 Astra (high) vs. GPT-6 Astra (high): comparative fiction report

## Comparative portrait

The two models were given the same 50 short-fiction briefs. They often reach the same idea and then place its meaning differently.

- **GPT-6.2 Astra** usually puts the decisive meaning inside a physical detail, a gesture, or another person's competence, and stops before explaining it [C001][C007][C013].
- **GPT-6 Astra** usually builds a legible ethical or civic mechanism, has its protagonist recognize her own error, and then names the lesson in a balanced sentence [C003][C014][C061].

Several critics describe the same contrast in different words:
- "ethical machines" versus "social situations that happen to contain machines" [C013];
- "explicit moral interpretation and distributed social inference" [C013];
- causal mastery versus distributed agency [C049][C059].

The two models converge more than a quick reading suggests:
- On 0206, both independently invented a widowed repairman who gilds iron out of grief [C001].
- Both demystify the throne in 0191 as transport [C012].
- Both turn the 0285 promise into a layered family document [C012].
- Both hinge turns on "Instead" in the same story slots [C046].

So the difference lies mainly in *where meaning is placed and how much is said*, not in premise invention [C012][C046].

**Where each model's strength runs.**
- GPT-6 Astra's strengths are real: auditable procedures [C025][C059], institutional legibility [C011], engagement with modern systems [C058], and a refusal to let right action purchase forgiveness [C017][C032].
- GPT-6.2 Astra's strengths are psychological inference, mixed motives [C020][C054], refusals that stay in force [C060], and humor that works structurally rather than as relief [C010][C047].
- GPT-6.2 Astra's matching weaknesses are opacity [C064], frictionless resolutions [C041], and a strong pull toward one warm, pre-modern parish-and-kitchen world [C006][C058].

**Quantitative context.**
- The focus model won all 50 matched pairs, with no ties, at a mean margin of +1.812 (95% half-width 0.143) and a median of +1.900.
- Mean length differs by only about 38 words, and length difference barely correlates with margin (+0.112). Verbosity therefore does not explain the preference.
- Evaluator disagreement (0.519) and order sensitivity (0.668) are substantial. Individual judgments are noisy even though the story-level direction is uniform.

## Does either model seem smarter?

**Short answer.** GPT-6.2 Astra more often gives the *reader impression* of a more perceptive mind. That impression comes from specific writing choices, not from diction or polish, and the panel did not agree that it amounts to a global advantage.

- Four readings (read_01, 04, 07, 10) state the impression strongly.
- Three (read_02, 05, 08) say Astra 6.2 seems more perceptive while insisting neither is "simply smarter."
- The four kimi readings (read_03, 06, 09, 11) each say neither is globally smarter.

Treat "smarter" here as a split across capacities.

**Psychological inference (favors GPT-6.2 Astra).** Its stories locate motives that are mixed or half-conscious:
- In 0387, a father hears his own excuse: "I always get to lift her out" [C020].
- In 0194, a rigged succession may come down to a librarian who preferred the girl who brought pears [C020].
- In 0012, one chiasmus ("would your mother take a year from you?") overturns a family's premise [C054].

GPT-6 Astra more often stages wrongs whose wrongness is clear from the outset, such as the cathedral sacrifice in 0012 [C054]. It names psychological mechanisms precisely rather than discovering them ("being needed was a treacherous warmth") [C066][C068].

**Social inference and distributed competence (favors GPT-6.2 Astra).** Secondary characters hold decisive knowledge:
- In 0065, old Hen invents the hand-mill adapter while Nell stops herself from lecturing [C002].
- In 0023, the narrator's mother finds the bronze foot [C013].
- In 0256, Ada's mother supplies the truth about the scrubbed key-knocks [C002].

Its solutions keep refusals in force ("Some said no, and those people's envelopes are still where I put them") [C049][C060]. It also locates injustice in procedure rather than villainy: "nobody had needed to be wicked for her to go to jail" [C043][C060].

GPT-6 Astra more often concentrates insight in a lone reformer who educates foil officials [C002]. Counterexamples exist: 0218's chairman checks Mara's joints, and in 0125 Iven sees her sacrifice first [C002].

**Causal and structural foresight (contested).** This is the most important unresolved disagreement.

*The gemini readings credit GPT-6.2 Astra with medium-native causality:*
- 0261: the table reports only what wood could register [C019].
- 0393: the four-second gap is storm distance [C019].
- 0354: an eight-flash lamp maps onto an eight-rank board [C037].
- 0007: an alignment tide drains the district [C053].
- 0065: an actual held-out backtest [C001].
- GPT-6 Astra, by contrast, sometimes bridges by fiat, as with coffee rings that play back verbatim dialogue (0261) [C019] or alignment light that wakes a seed (0007) [C053].

*The kimi readings credit GPT-6 Astra with the tighter setup-to-payoff architecture:*
- 0137: lifting the tile would injure the whale [C059].
- 0349: "Ada's bill covered twenty-six words; the judgment contained nine" [C059].
- 0216: the capsule needs an ending "it could not mistake for damage awaiting repair" [C048].

*The claude reading of read_05 sees two genuine kinds of intelligence:*
- GPT-6 Astra's blinded prism test in 0362 and its symmetry-breaking oval in 0323 are real epistemic rigor [C025].
- GPT-6.2 Astra's reframings are social [C025].

Both models make required objects do causal work [C016]. The defensible synthesis is narrow. GPT-6.2 Astra more often makes the *properties of the medium* generate the solution. GPT-6 Astra more often makes the *rules of an invented system* line up with the moral problem. That approach is sometimes convenient, as with 0333's lock answering a psychological formula [C059], and sometimes rigorous [C025].

**Epistemic caution (often GPT-6 Astra).**
- In 0010, "Warm cheeks might mean joy, shame, fever, or merely a difficult staircase" questions the prompt's own method [C043].
- In 0388, intuition is distrusted because it "had already helped her ruin one innocent man" [C043].

**Conceptual compression and restraint (favors GPT-6.2 Astra; surface-cue sensitive).**
- 0221: "By then she could afford to give me that much time" carries time dilation and a lifetime of asymmetry [C064].
- 0010: "pointed not to the survivors but to the strings" ironizes the required phrase instead of defining it [C042].
- GPT-6 Astra glosses after showing: "They were learning the difference" [C026] and "These were the unshaken marvels: …" [C042].

Several critics flag that withholding can masquerade as depth [C007][C064]. Some GPT-6.2 Astra gaps hide thin mechanism:
- 0142's signage plot [C007][C011];
- 0058's reconstructed backstory [C064];
- 0252's double body [C053].

**Ethical maturity (often GPT-6 Astra).** GPT-6 Astra keeps culpability and injured parties' independence after correct action:
- "She did not feel released. She felt robbed, and furious, and kept moving" (0023) [C017].
- "The dead did not become innocent merely because her father had wronged them" (0187) [C032].
- "don't make it mean more than that" (0289) [C032].

GPT-6.2 Astra's reconciliations sometimes meet less resistance [C032][C041].

**Bottom line.** The impression gap rests on inference left to the reader, mixed motives, and distributed agency. It does not rest on verbosity. The word-count correlation of +0.112 also argues against length as the cause. GPT-6 Astra's real systems and ethical intelligence is partly hidden because it restates its own insights [C026][C034].

## Narrative reasoning and aesthetic judgment

**Prompt metabolization.** The models treat required abstractions in opposite ways.

*GPT-6 Astra tends to paste the requirement into narration:*
- "Iona had prevailed through predictive modeling" (0065) [C003].
- "Their laughter had a reef-shadow joy:" followed by a definition (0158) [C030].
- "with the demure audacity that usually preceded his least popular questions" (0387) [C024].

*GPT-6.2 Astra tends to ironize it, house it in someone's speech, or dissolve it into behavior:*
- "mending what isn't torn" as a father's shop joke (0206) [C003].
- "balancedly curious" as a municipal form-field (0323) [C028].
- "photosynthesize pain into beauty" as a line from a "regrettably published book" (0158) [C028].
- Demure audacity enacted as backtalk: "as if I had reserved a table at an inn" (0387) [C024].

One critic frames this as one writer arguing with the prompt while the other fulfils it [C042]. The cost is that the irony can excuse a thin use of an element, as with the insomniac poet in 0158 [C028].

**Endings.** GPT-6 Astra's closes tend to resolve meaning; GPT-6.2 Astra's tend to enact it.

*GPT-6 Astra closes on a principle or a practical project:*
- "Not forgetfulness, but somewhere to stand beside remembering" (0137) [C050].
- "She had learned to leave an end for someone else to hold" (0289) [C034].

*GPT-6.2 Astra closes on resumed practice or a gesture:*
- "South, I said, and felt her elbow come up against mine" (0221) [C034].
- "Some mornings they looked and some mornings they just made tea" (0018) [C042].

Exceptions run both ways:
- GPT-6 Astra's 0018 ends "Mara let her" [C042], and its 0216 ends on a kettle sound [C050].
- GPT-6.2 Astra's 0294 explains its museum display [C050], and its 0258 states a moral [C062].

**Shared constructive aesthetic.** Both models end by designing futures other people can use rather than merely revealing truths:
- maps with safe-passage hours [C018];
- a door-swing arc on a drawn floorplan [C018];
- more hands and room to leave [C018].

Both also resolve toward humane repair rather than tragedy [C017][C018].

**Comedy as reasoning.** GPT-6.2 Astra's humor carries structural load:
- the coal-cart laugh at the emotional peak of 0018 [C047];
- "language not generally addressed to royalty" inside a deathbed elegy [C010];
- peas thrown at the departing whale-wife's first song in centuries [C057].

GPT-6 Astra's humor is real when cued (0389 "three potatoes, a brass telescope, and a grudge against the weather" [C024]; 0127 "excellent customer service" [C040]). Otherwise it arrives as a late, sanctioned release [C042].

## Recurring and repetitive writing habits

**Counting conventions.** Counts below are packet-local n/N only where a claim reports the matching stories and the checked nonmatches. Cross-packet tallies are deduplicated lists of attested stories; frequency across all 50 stories was **not measured**. Two readings of the same story count once (e.g., 0349's "mistaken" line appears in two claims [C044][C061]).

### GPT-6 Astra — sentence level

1. **Corrective antithesis landing on a principle.** "Not X, but Y" or "not merely" constructions fix the lesson.
   - Packet checks: 5/5 in read_01 [C003], 5/5 in read_02 [C008], 5/5 in read_05 [C026], 5/5 in read_07 [C038], 5/5 in read_10 [C055].
   - Examples across prompts:
     - "less like conquering doubt than finding it useful work… not as its inventor, but as the person responsible" (0065) [C003];
     - "It meant curiosity needed a counterweight, not a smaller appetite" (0323) [C026];
     - "This was not a map of where customs belonged, but of how they traveled" (0258) [C055];
     - "True north was not the brightest thing in the window" (0221) [C064].
   - GPT-6.2 Astra uses the same syntax, but its versions land on objects ("not the identical feather but the identical tie") rather than principles [C042][C026].

2. **The "mistaken X for Y" recognition turn.** Six distinct stories attest it:
   - "mistaken a convenient tether for a law of nature" (0288) [C014];
   - "mistaken purity for innocence" (0386) [C014];
   - "mistaken her own relief for Ada's" (0349) [C044];
   - "mistaken his refusal to answer interrogators for an inability" (0388) [C044];
   - "mistaken its repetitions for sloppy draftsmanship" (0258) [C061];
   - "mistaken rescue for reunion" (0333) [C061].
   - The narrative placement is constant: decoding, then named recognition, then the final act [C061]. Frequency not measured.

3. **The shame or "nearly" temptation beat before the right choice.**
   - Shame/self-reproach: "For one shameful moment" (0191), "Iven felt relief before shame" (0285), "Mara hated herself" (0086). Read_02 counts 4/5 [C008].
   - "Nearly/almost": "I nearly released the thread" (0058) and "Mera nearly told him" (0389). Read_12 counts 4/5, with 0221 as the nonmatch [C066]. "She almost said he did deserve help" (0393) is a further instance [C020].

4. **The administrative-aftermath coda, "They would need…".**
   - "a proper root box, drainage trays, and a schedule of inspections" (0007) [C055];
   - "a roster, arguments, replacements" (0012) [C055];
   - "a village clinic, new bridges, arguments, taxes, work" (0290) [C041].
   - Three unrelated briefs read in two different packets. This is a portable closing formula that no single-pair judgment could see.

5. **Naming or glossing the requested tone or concept** rather than enacting it:
   - "reef-shadow joy:" (0158) [C030];
   - "demure audacity" (0387) [C024];
   - "These were the unshaken marvels:" (0010) [C042].

### GPT-6 Astra — story level

- **Stock-name lock.**
  - After deduplication, the claims attest "Mara" in at least thirty distinct GPT-6 Astra stories, across every packet that checked names. Examples: 3/5 in read_01 [C004], 4/5 in read_02 [C008], 5/5 in read_08 [C044], 4/5 in read_07 [C038].
  - Near variants extend it: Mera (0389), the town of Mere (0387) [C021], and Nera (0252, 0276) [C055].
  - A **candidate** secondary recurrence, not counted in any packet: a man named Iven appears in 0125 [C002], 0285 [C008], 0387 [C021], and 0354 [C036].
  - The name usually belongs to the central figure, so it reinforces the impression of one heroine across briefs [C044][C055].

- **Complicity → self-indictment → release → shared repair.**
  - Read_05 counts four of five plus a shifted variant in 0362 [C027].
  - Read_10 finds early complicity exposition in 3/5 (0007, 0012, 0258) [C055].
  - The same arc structures read_12's briefs [C066].
  - Examples: "a law she had helped write" (0007) [C055]; "Her shelter had become another hand around twelve throats" (0192) [C027].

- **Documentary restitution.** The protagonist signs, dates, publishes, or "writes an instruction" to make remorse real:
  - signed records in 0194, 0387, and 0393 [C021];
  - "published the old calculations with her own mistaken assumptions underlined" (0348) and "her old report attached and her own errors marked" (0388) [C044];
  - "wrote one instruction" (0125) and "wrote a new instruction" (0218), each with an inheritance maxim [C003].
  - GPT-6.2 Astra treats paperwork in exactly the opposite way: "I kept my pencil in my pocket" (0393) [C021].

- **Dead-kin grief engine.**
  - Dead brother: 3/5 in read_08 [C044].
  - Family killed by fire or water: 3/5 in read_02 [C008].
  - This is partly shared. Read_09 finds close-kin loss in 5/5 for *both* models [C051].

- **Civic scaling and redistribution.**
  - Elite hoarding corrected by public redistribution: 4/5 in read_07 [C038].
  - A centralized device broken open for local governance: 0194, 0261, 0389 [C023].
  - Rescue arithmetic: "eighty faces" (0023) and "thirty strangers against eighty residents" (0396) [C015].
  - Civic stakes with deadlines: four of five in read_05 [C029].

- **Refusal of easy absolution as a recurring ending.**
  - Read_07 counts 5/5 [C038].
  - Examples: "He accepted it without forgiving her" (0393) [C024]; "without forgiving twelve winters" (0354) [C038].
  - This is a genuine strength in any single story, and it reads as a formula when stories are laid side by side [C038].

**Verdict on GPT-6 Astra.** Its recurrences act as a **template** that makes briefs interchangeable. Critics in four different packets independently describe different prompts collapsing into one arc [C008][C027][C044][C066].

Exceptions show it can step outside the template:
- 0330 has no Mara, no dead relative, and a fabulist mode [C008];
- 0288 centers solitary care [C015];
- 0252 and 0276 escape the complicity-and-committee structure [C055].

### GPT-6.2 Astra — sentence level

1. **Dry occupational aside.**
   - "an occupation that required a sense of humor and another source of income" (0018) [C045];
   - "respectable work for a woman who had once dropped sixteen tons of municipal brass into the weather" (0349) [C045].

2. **"As if / as though… rather" irony.**
   - "as if a practice were a rather flimsy thing to set against a country" (0086) [C009];
   - "as though a man who did not speak were doing a rather good trick" (0330) [C009].

3. **The measuring qualifier.** "provided you did not mind knowing how much tree there was beneath your feet" (0187) carries one voice across briefs [C067].

4. **Ironic housing of prompt jargon.** Read_05 counts four of five [C028]. Further examples: "how to arrest a crossroads" (0290) [C040]; the strings that "had not had to move" (0010) [C042].

5. **Kitchen and domestic deflation of grand material.** Read_04 counts 5/5:
   - a succession table "like an ordinary supper gong" (0194) [C022];
   - "a spoon going round an empty pot" (0389) [C022];
   - a kitchen timer in a prison (0393) [C022].

### GPT-6.2 Astra — story level

- **The tactile closing gesture.**
  - Counts: 5/5 in read_01 [C004], 5/5 in read_05 [C026], and circular return to an opening object in 4/5 in read_10 [C055].
  - Its function varies:
    - restraint: "Couldn't we hear it first?" (0206) [C004];
    - handoff: the widower takes the chalk (0218) [C004];
    - quiet institutional resistance: a ruler scoring "the next six forms" (0362) [C026];
    - delayed release: the chip among the change (0216) [C062];
    - recognition: "this time she knew whose it was" (0349) [C062].
  - Read_11 judges this a **flexible signature** rather than a template [C062]. Read_03 warns it "could itself become a predictable hush" [C014].

- **Surfaces and manners as testimony.**
  - Forensic marks: a scar the length of a case hinge (0010), a run in a silk tie (0388) [C045].
  - Identity by manner: 4/5 in read_12, e.g. cuffs turned twice (0187) and stars with eyelashes (0221) [C065].
  - Objects worn smooth by thumbs: 4/5 in read_04 [C022].
  - Involuntary bodily wear: 5/5 in read_07 [C039].
  - Read_12 notes the motif is "close to predictable by the fourth instance" [C065].

- **Overturned blank side.** An official card, score, or board is flipped to write a human counter-text: 3/5 in read_07 (0127, 0290, 0354) [C039]. "He thought a little and turned the card over and wrote SHE HAD JUST SEEN ME" [C039].

- **Parish-domestic kit.**
  - Aprons 3/5 and bread 3/5, with ruined-handed elders in 2/5, in read_10 [C056].
  - Blindness or lameness 3/5 and avuncular bonds 3/5 in read_07 [C039].
  - A gaslit-British lexicon (shilling, pit ponies, penny) 5/5 in read_04 [C022].

- **The unprompted dead relative.** 4/5 in read_01 [C004].

- **Name reuse, larger than any single packet showed.**
  - Read_12 states that its packet never repeats a name. Deduplicated across claims, however, "Nell" names a character in at least ten distinct stories, including 0065 [C005], 0284 [C013], 0158 [C030], 0221 [C065], and 0276 [C053].
  - "Ada" appears in at least eight, including 0218 [C004], 0288 [C015], 0194 [C021], 0137 [C060], and 0012 [C054].
  - Unlike GPT-6 Astra's Mara, these names move across protagonist, mother, daughter, and minor roles. They are a default name pool rather than one recurring heroine. Frequency not measured.

**Verdict on GPT-6.2 Astra.** Its repetition is mostly texture and cadence rather than plot. Its plot engines vary [C023][C010]. The cumulative effect of the kitchen-and-handcraft kit, however, is one consistent socio-historical world. That bleeds into range (see below) [C006][C022][C056].

### Shared habits and prompt-induced convergence

Several apparent signatures belong to both models and should not separate them:
- an "Instead" pivot at the moral turn on the *same* four story IDs in read_08 [C046];
- the "could not X, but could Y" consolation [C009];
- the humbled clever specialist, e.g. both ghostwriters in 0289 [C033];
- close-kin warrant in 5/5 for each in read_09 [C051];
- leaving blank room on a page for the future [C066];
- the in-world "called it" coinage, used sincerely by GPT-6 Astra and ironically by GPT-6.2 Astra [C028].

Some convergences are prompt-driven:
- timeframe-first openings where the brief supplies "after…" [C003];
- the anti-perfection moral of 0206 and the decentralization ending of 0389 [C066].

### Lineage: what persists, weakens, or appears

**Persists into GPT-6.2 Astra:**
- the shared name pool (Ada appears in GPT-6 Astra's 0206, 0333, and 0349 too [C001][C061][C044]);
- the family-grief engine [C051];
- the "Instead" pivot [C046];
- antithetical syntax, now pointed at objects [C042];
- the culpable or humbled protagonist [C033][C047].

**Weakens:**
- the aphoristic gloss [C026][C034];
- tone-naming [C030];
- the single-name lock [C044];
- the civic-redistribution engine [C038].

**Newly appears:**
- first-person and oblique-witness narration [C023];
- comic register [C047];
- the parish-domestic kit [C056].

**Is lost:**
- GPT-6 Astra's willingness to stay inside coercive institutions and modern systems [C024][C058].

## Range and adaptability

**Point of view.**
- GPT-6.2 Astra alternates first and third person in most packets:
  - 0125/0206 first versus 0065/0218/0256 third [C005];
  - 0142/0285/0330 first versus 0086/0191 third [C010];
  - 2/5 first versus 3/5 third in read_10 [C057].
- GPT-6 Astra is close third in 5/5 in several packets [C005][C057][C040]. It does use first person in 0261 [C023], 0216 [C052], and 0323 and 0058 [C029].
- Read_06 is a counterweight: GPT-6.2 Astra was first person in 5/5 there and GPT-6 Astra third in 5/5. Neither showed POV range in that packet [C035].
- GPT-6.2 Astra's distinctive move is to decenter the headline role. It narrates 0387 through the net-mender's child and 0393 through the repairer across the counter, while GPT-6 Astra steps straight inside both roles [C023].

**Voice.** GPT-6.2 Astra's personae share one dry, measuring sensibility [C010][C063][C067]. Its POV range exceeds its vocal range. Examples:
- the earthy coachman, "my mare was going to piss" (0285) [C010];
- the stall-poet reconciling "over a pork pie" (0125) [C005];
- the postmistress with "my good teeth in a cup" (0333) [C052].

**Tone and comic register.**
- GPT-6.2 Astra modulates from hush to comedy:
  - "you could have heard a cinder settle" (0261) versus folk comedy (0194, 0389) [C024];
  - comic nonhuman first person in 0252 versus spare chamber quiet in 0012 [C057];
  - "exactly one desk" near-farce (0323) versus almost humorless tenderness (0192) [C029].
- GPT-6 Astra stretches when cued: gritty whimsy in 0389 [C024][C067] and affectionate detachment in 0127 [C040]. Read_07 therefore reads its solemnity elsewhere as "a default preference rather than sheer inability" [C040].
- Fallbacks into habitual register occur on both sides:
  - GPT-6 Astra: "muffled clarity" in 0012 escalates into public oratory [C057]; "demure audacity" is labeled rather than felt [C024].
  - GPT-6.2 Astra: its wit intrudes on 0187's requested "deepening hush" with the pinched clay nose [C067].

**Genre, ontology, and scale.** This is where range most clearly cuts the other way.
- GPT-6.2 Astra calibrates ontology: municipal realism for "ignorance cartographer" (0065) versus a teacup-thrush folktale (0206) [C005].
- But it shrinks every brief to household scale, including first contact [C029]. It domesticates futuristic cues into one artisanal world [C006].
- When 0258 asks for a post-cryptocurrency world, GPT-6.2 Astra disposes of it in one clause, "coins that would no longer buy a loaf," and retreats to lawn and lace. GPT-6 Astra builds a conflict around payment-network monoculture and "the beautiful database she could build, each connection clean, each household exposed" [C058].
- GPT-6 Astra commits to estranged macro-institutions: the grotto collective in 0127 [C041] and temporal conscription in 0125 [C006].
- It also spans mythic lyricism (firefly froth mending a moon bridge in 0387) [C024], fabulist allegory (0330) [C010], and plain startup realism (0294) [C052].
- So GPT-6 Astra has the wider *genre and scale* range [C006][C041][C058], while GPT-6.2 Astra has the wider *voice and tone* range [C052][C063].

**Conflict engines and social perspective.**
- GPT-6.2 Astra changes the kind of question each story asks:
  - autonomy and a door bolt (0288) [C015];
  - foster-bureau collectivity (0386) [C015];
  - villain-free family restraint (0261) [C023];
  - consent preserved by envelopes left alone (0333) [C049].
- Its resolutions vary in type: loophole, demonstration, ride, child's speech, silent witnessing [C010].
- GPT-6 Astra varies setting and mechanism around one ethical procedure [C010][C015][C023]. 0288 and 0386 are real exceptions [C015].

**Coercion and darkness.**
- GPT-6.2 Astra softens power. Its penitentiary readily adopts a two-chair exam [C024], and in 0290 claustrophobia dissolves in a hummed tune [C041].
- GPT-6 Astra sustains unhealed friction ("He accepted it without forgiving her") [C024] and somatic terror in the culvert flashback [C041].

**Untested range.** Untested, rather than failed, for both models:
- bleak tragedy, horror, sustained comedy without tenderness, and contemporary realism (largely) [C024][C067];
- formal fragmentation. Neither attempted it even when 0349 asked for "integrated fragmentation" [C063]. GPT-6 Astra's 0349 instead reverted to its mother-daughter error template [C047].

**Connection to habits.** GPT-6.2 Astra's narrowest range limit, its pre-modern domestic world, is the same thing as its parish-kitchen habit kit [C022][C056]. GPT-6 Astra's narrowest limit, one emotional arc, is the same thing as its complicity template [C008][C066].

## Floor versus ceiling

**Consistency.** GPT-6.2 Astra won all 50 matched pairs, with no ties and a median margin of +1.9. That is a very high floor relative to its predecessor. Its lowest margins still favored it:

| Story | Margin |
|---|---|
| 0258 | +0.517 |
| 0216 | +0.550 |
| 0349 | +0.717 |
| 0127 | +0.750 |

**The narrowest pairs coincide with GPT-6 Astra's specific strengths:**
- **0258:** socio-technical modernity, where GPT-6.2 Astra sidestepped the brief [C058]. The evaluator also called GPT-6.2 Astra's version "episodic and convenient."
- **0216:** causal integration of the damaged capsule [C048]. The evaluator explicitly called this a "close call."
- **0349:** arithmetic evidence [C059]. GPT-6.2 Astra was comparably rigorous here with its edge notches [C059][C043].
- **0127:** GPT-6 Astra's cued comic detachment [C040] and its strange grotto [C041].

**GPT-6.2 Astra's failure-prone cases:**
- elliptical mechanics that demand reconstruction (0058, 0192, 0388) [C064][C029][C045];
- frictionless resolution (0290) [C041];
- tokenized prompt elements (0158's insomniac poet) [C028];
- the nominal capsule thread in 0216 receding [C048];
- elegance that slides into convenience (the bronze lion in 0023) [C016].

**GPT-6 Astra's floor:**
- dependable causal clarity [C025][C048];
- with predictable glossing [C026];
- and occasional fiat bridges (0261) [C019] or engineered puzzles (0354's cipher) [C037].

**Ceilings.**
- GPT-6.2 Astra's peaks combine inference and ache:
  - 0206 (+2.800): the apple eaten core and all, and the daughter filing through her father's gold [C001][C004];
  - 0142 (+2.600);
  - 0288 (+2.500): the sixpence maid, the auk "like a man having trouble with his boot" [C015].
- GPT-6 Astra's genuine peaks are:
  - 0362's blinded prism test [C025];
  - 0393's unforgiven arm [C024];
  - 0187's refusal to sanctify the dead [C032];
  - 0023's "robbed, and furious" [C017].
- GPT-6 Astra's peaks did not narrow margins much (0362 +1.917, 0393 +1.750). Its ceiling stories still lost, so no compensating ceiling should be claimed for it.

**Replication.** There is no extension cohort. All 50 stories form one cohort, so there is no original-versus-extension replication test.

The internal replication that does exist is cross-packet:
- Twelve independent readings by three critic families each found GPT-6 Astra's convergent template [C003][C008][C027][C038][C044][C055][C066].
- They likewise each found GPT-6.2 Astra's gestural closing [C004][C014][C026][C055][C062].
- Ten stories appear in two packets. For example, 0349's "mistaken" line is counted once [C044][C061], and 0258's modernity gap appears once [C058].

## What each model still does better

**GPT-6.2 Astra:**
- inference left to the reader [C064][C036];
- mixed motives and blind spots [C020][C054];
- distributed agency and durable refusals [C002][C049][C060];
- medium-native mechanisms [C019][C037][C053];
- structural humor inside grief [C047][C057];
- dissolving prompt jargon into behavior [C028][C042];
- point-of-view and witness-angle variety [C023].

**GPT-6 Astra:**
- auditable procedure and epistemic caution [C025][C043];
- causal setup-to-payoff in several matched stories [C048][C059];
- institutional legibility, e.g. gentrification factions in 0142 [C011];
- engaging modern technical and economic systems [C058];
- coercive and somatic friction [C024][C041];
- ethics in which right action does not buy absolution, and injured parties set the terms [C017][C032][C068];
- negative action as plot: not lifting the tile, not building the database [C059][C058].

## Findings beyond the existing judging

- **Cross-story formulae invisible to pairwise judges.**
  - GPT-6 Astra's "They would need…" coda across 0007, 0012, and 0290 [C055][C041].
  - Six distinct "mistaken X for Y" turns [C014][C044][C061].
  - The "wrote… instruction" inheritance maxim [C003].
  - A recurring Iven, recorded here as a candidate.
  - Evaluators praised GPT-6 Astra's refusals of forgiveness story by story. Across a packet, they read as a house ending [C038].

- **Name pools, deduplicated.** GPT-6 Astra's Mara is attested in at least thirty stories. GPT-6.2 Astra's Ada (at least 8) and Nell (at least 10) recur much more than any single packet suggested [C004][C039][C044][C055]. The newer model has diffused, not eliminated, the stock-name habit.

- **Opposite moral symbolism of paper.** GPT-6 Astra makes the signed or dated record the act of remorse. GPT-6.2 Astra treats receipts and forms as abstractions that fail people, and flips them to write a counter-text [C021][C039].

- **Who owns the ending.** GPT-6.2 Astra often turns private memory into a practice others repeat. GPT-6 Astra often leaves the injured person power to limit or refuse that practice ("don't make it mean more than that") [C032]. This complicates the evaluators' consistent preference for GPT-6.2 Astra's restraint.

- **Evaluator emphasis and surface-cue risk.** Evaluator focus-advantage bullets lean heavily on voice and line craft. Several critics flag GPT-6.2 Astra's British artisanal vocabulary as a charm cue that can disguise frictionless resolutions [C006][C041][C022].
  - Counter-evidence: critics stripping that texture found the deductions intact (0393 speed of sound, 0261 wood-level sensing) [C019].
  - Length is not the driver (correlation +0.112).

- **Unprompted convergence as a natural experiment.** The identical gilding-for-grief premise in 0206 isolates craft: summary motive versus "Father ate the apple, core and all, standing up" [C001].

## Disagreements and limitations

**Overall judgment.** Gemini readings call GPT-6.2 Astra substantively smarter. The kimi readings decline any global verdict [C016][C017][C068]. The claude readings split the difference [C025][C043]. The minority position, that the impression gap is largely withholding versus stating, is well supported [C064][C007] and should be kept.

**Causal mechanism.** This is genuinely contested between C019/C037/C053 (favoring GPT-6.2 Astra) and C048/C059 (favoring GPT-6 Astra). The likely answer is story-dependent.

**Maturity.** C032 (favoring GPT-6 Astra) stands against C036/C042 (favoring GPT-6.2 Astra). Neither cleanly wins [C017].

**Range.** Range is split by dimension rather than one-sided [C024][C029][C067].

**Limits of the evidence.**
- Packets contain five stories each. Most counts are packet-local, and corpus frequencies were not measured.
- Briefs skew toward memory, inheritance, and repair, which encourages kin grief and restorative endings [C051][C033].
- One prompt pair has fewer than two observed orders per evaluator.
- Evaluator disagreement and order sensitivity are high.

## Representative case studies

**0206 — identical invented premise, divergent execution (+2.800).**
- Both models make a grieving repairman gild iron so nothing would wear away [C001].
- GPT-6 Astra explains the motive in narrator summary and turns "mending what isn't torn" into a solemn lesson [C001][C003].
- GPT-6.2 Astra makes the phrase the father's lucrative shop joke [C003], and conveys grief through the browned apple [C001].
- Its daughter files through the gold, and the father's change arrives as "Couldn't we hear it first?" [C004].
- The dead mother is known by the three flats her hammer left [C065].

**0012 — hidden assumption, named versus discovered (+2.200).**
- GPT-6 Astra stages an obviously indefensible sacrifice and names the assumption in exposition ("never asking why solitude should make a life expendable") [C054].
- It then lets "muffled clarity" escalate into a chalk-circle speech and closes on "a roster, arguments, replacements" [C057][C055].
- GPT-6.2 Astra inverts one question ("would your mother take a year from you?") and lets an invoice mark, "account closed, nothing owing," release the daughter [C054].
- GPT-6 Astra keeps the tougher ending: "Nobody absolved him" [C054].

**0362 — two intelligences, both executed well (+1.917).**
- GPT-6 Astra runs a blinded control, having the guard move the prism while Mara stands away [C025].
- It dramatizes one truthful lie strongly ("Mara let him have that lie") [C030].
- GPT-6.2 Astra locates the anger in the matron's thimble, and ends with a ruler scoring "the next six forms" for strangers [C025][C026].
- This is GPT-6 Astra near its ceiling, and it still lost.

**0393 — the coercion trade-off (+1.750).**
- GPT-6.2 Astra's four-second gap as storm distance is medium-native reasoning [C019]. Its harm comes from a one-line form rather than malice [C020]. It ends with the pencil kept in the pocket [C021].
- GPT-6 Astra hears "the old bargain hidden in that comforting word" [C020]. Its chaplain dates a self-incriminating page [C021], and its prisoner "accepted it without forgiving her" [C024].
- GPT-6 Astra's version has institutional weight that GPT-6.2 Astra's genial prison sidesteps [C024].

**0258 — the narrowest pair (+0.517).**
- GPT-6 Astra converts the cryptocurrency crash into network monoculture and surveillance temptation [C058].
- It still runs its "mistaken… draftsmanship" recognition and its not-X-but-Y close [C061][C055].
- GPT-6.2 Astra retreats to haberdashery [C058], yet perceives that indirect brokerage spares the poor humiliation ("nobody needed to know why you had come up short") [C054].
- Its own explicit self-correction shows that the recognition turn is not exclusive to GPT-6 Astra [C061].

## Cited claim ledger

- **C001 — Operational mechanics and oblique subtext over symbolic thesis-illustration:** Writer GPT-6.2 Astra (high) builds causal authority from working material protocols and sideways behavioral detail, trusting readers to infer the conceptual point, whereas Writer GPT-6 Astra (high) illustrates ideas through allegorical machinery and explicit summary of emotions and themes.
  - Story 0065, `gpt-6.2-astra-high`:
    > She gave Hen the toll book from a winter she had not used in making her model.  He called out the loads as they had crossed, and she advanced the barley by the measured appetite of one pair of stones.
    Without using the phrase "predictive modeling," GPT-6.2 Astra (high) constructs a genuine out-of-sample validation test against held-out historical data, grounding the plot turn in real analytical reasoning.
  - Story 0065, `gpt-6-astra-high`:
    > Iona ran each change through the brass predictor, turning its stiff handles until the colored beads settled into their channels.
    By contrast, GPT-6 Astra (high) represents predictive modeling through a decorative steampunk prop whose internal logic remains purely asserted.
  - Story 0206, `gpt-6.2-astra-high`:
    > The last thing she made before the fever took her was lying on our draining board beside a peeled apple gone brown.  Father ate the apple, core and all, standing up.  Then he took the breast into his shop and shut the door.
    On the exact bereavement premise both writers invent for 0206, GPT-6.2 Astra (high) conveys stunned grief entirely through eccentric physical automatism without naming the emotion.
  - Story 0206, `gpt-6-astra-high`:
    > Six months earlier, after Ada's mother died, Pip had gilded its great iron comb with the chip's alchemy.  Nothing he loved would wear away again, he had decided, and gold could not rust.
    GPT-6 Astra (high) explains the psychological motive directly in narrator summary, leaving no interpretive work between grief and action.
  - Story 0125, `gpt-6.2-astra-high`:
    > What came out was not the song but the small wet noise of a woman getting a fiber off her tongue.  Then, very distinctly, she said, "The hell with the green, it tastes of feet."
    At the emotional climax, GPT-6.2 Astra (high) refuses sentimental speech in favor of a coarse, bodily scrap of ordinary life that fulfills the niece's unspoken need to hear her mother unburdened by martyrdom.
- **C007 — Inferred versus declared causality:** GPT-6.2 Astra (high) plants causal information in an unexplained physical detail and lets later action decode it. GPT-6 Astra (high) states causes, motives and lessons outright, often as aphorisms. GPT-6.2 Astra (high)'s method creates the impression of perceptiveness because the reader discovers the meaning. GPT-6 Astra (high)'s creates clarity but reads more didactic.
  - Story 0086, `gpt-6.2-astra-high`:
    > Lea knew this because she had once watched her sister try to get her fingernails between the boards.
    This is never glossed. It silently explains why Lea later fits drawer pulls to the gates: so the nurses can choose for themselves, as Bess could not.
  - Story 0285, `gpt-6.2-astra-high`:
    > "I can remember all the times," he said at last, and gave them to us without a hitch, even the Thursday before Christmas when the mail went double.  "It's having to watch your faces while you read."
    The child's speech shifts the problem from logistics to his parents' faces, a psychological insight the narrator never paraphrases.
  - Story 0086, `gpt-6-astra-high`:
    > Beneath the spelling rule she wrote: An agreed release is not a pardon.
    GPT-6 Astra (high)'s ethical resolution is crystallized as an explicit written moral.
  - Story 0191, `gpt-6-astra-high`:
    > There had been no ascension, only public transport.  The monarchy had built its throne over the entrance and turned a commute into a promise only kings could fulfill.
    A strong conceptual twist, but the narrator explains it rather than letting the images carry it.
- **C013 — Social inference versus explicit moral interpretation:** GPT-6 Astra (high) frequently demonstrates an experience and then supplies its governing interpretation. GPT-6.2 Astra (high) more often makes the reader infer emotion from bodily behavior and social position, and it sometimes transfers decisive knowledge away from the protagonist. This creates the impression that GPT-6.2 Astra (high) perceives a wider social world around the central moral problem.
  - Story 0284, `gpt-6-astra-high`:
    > Mara understood then that unused courage had not been waiting somewhere inside her, intact and shining.  It had been waiting in the space between a request and an answer, wherever someone still needed another pair of hands.
    The rescue’s meaning is balanced, named, and conclusively delivered by the protagonist rather than left for the reader to assemble.
  - Story 0284, `gpt-6.2-astra-high`:
    > On the near hand a thumbnail had gone black, and Nell had to sit on her own hands not to take it up and kiss it.  Nobody had warned her that the enormous child would contain the little one entire.
    Maternal longing, restraint, and the shock of a child’s growth emerge through physical action and perception without an explanatory moral.
  - Story 0396, `gpt-6.2-astra-high`:
    > She did not linger over his face; she knew the look of a man doing his best to weigh nothing.
    The phrase perceives the social burden of being carried and the failure of the prior settlement, while trusting the reader to understand its humiliation.
  - Story 0023, `gpt-6.2-astra-high`:
    > Then my mother went down on her knees with the little foot and felt along the lump until bronze clicked on bronze.
    The narrator’s mother, not the titular navigator, supplies the decisive recognition and physical solution, distributing competence through the family and community.
- **C003 — Templated openings, corrective antithesis, and inscribed maxims in GPT-6 Astra (high) versus ironic prompt assimilation in GPT-6.2 Astra (high):** Checked across all 5/5 stories, Writer GPT-6 Astra (high) relies on a rigid structural and syntactic template: fronted setting/timeframe openings paired with early occupational labels (5/5: 0065, 0125, 0206, 0218, 0256), civic-official persuasion plots (3/5: 0065, 0218, 0256; nonmatches: 0125, 0206), corrective "not GPT-6 Astra (high), but GPT-6.2 Astra (high)" antithesis coupled with literal prompt-method narration (5/5), and Mara inscribing a negative-obligation "instruction" about inheritance into a book (2/5: 0125, 0218; nonmatches: 0065, 0206, 0256). Writer GPT-6.2 Astra (high) varies openings (only 2/5 fronted "After..." clauses, both prompt-cued in 0125 and 0256; nonmatches: 0065, 0206, 0218) and frequently ironizes required phrases inside character speech or trade slang.
  - Story 0206, `gpt-6-astra-high`:
    > At the equinox, while day and night hung in the balance, Midnight stole the town's morning.  Beneath the square, the equinox clock began unwinding its last hour before darkness became permanent.  Pip, a music box repairman, heard the trouble before he saw it: every mechanical bird sang backward.
    Even without an "after..." timeframe prompt, GPT-6 Astra (high) opens with a fronted temporal prepositional phrase and introduces "[Name], a [prompt occupation]" by the third sentence.
  - Story 0065, `gpt-6-astra-high`:
    > Iona had prevailed through predictive modeling, yet the victory felt less like conquering doubt than finding it useful work.  She asked for a place at the first bed, not as its inventor, but as the person responsible for noticing what went wrong.
    GPT-6 Astra (high) recites the prompt's required action and method verbatim as narrator summary while stacking two consecutive corrective contrast constructions ("less like... than," "not as... but as").
  - Story 0125, `gpt-6-astra-high`:
    > Mara wrote one instruction for the woman who would inherit her notebook: "Neither of you owes the other love."
    Unprompted by the brief, GPT-6 Astra (high) has a heroine named Mara resolve the climax by writing an epigrammatic "instruction" linked to inheritance in her book.
  - Story 0218, `gpt-6-astra-high`:
    > She asked for the diary and wrote a new instruction beneath her grandmother's warning, her letters smaller than they had been in winter.  Ask again next season; permission is not an inheritance.
    In a completely separate story, another protagonist named Mara repeats the exact lexical pattern—"wrote a new instruction" plus an aphorism built on "inheritance"—exposing a strong unprompted model habit.
  - Story 0206, `gpt-6.2-astra-high`:
    > He called it mending what isn't torn, and he charged twice his usual fee because he knew he'd never see those customers again.
    Rather than turning the required method phrase into a solemn moral lesson (as GPT-6 Astra (high) does in 0206), GPT-6.2 Astra (high) metabolizes "mending what isn't torn" as the father's dry shop joke about vain customers—making his later grief-gilding deeply ironic.
- **C014 — Recurring thesis cadence and recurring gesture cadence:** GPT-6 Astra (high) repeatedly pivots on an explicit correction—having mistaken one thing for another, or discovering that something is not where or what the protagonist thought. GPT-6.2 Astra (high) repeatedly ends on an incomplete but actionable relationship, using touch, address, design, or ordinary work. Both are recognizable signatures; GPT-6 Astra (high)’s is more likely to make different plots arrive at the same articulated lesson, while GPT-6.2 Astra (high)’s is more likely to make different lessons receive the same hushed closure.
  - Story 0023, `gpt-6-astra-high`:
    > To navigate the geography of loss, she was discovering, was not to find a way around what hurt.  It was to mark where the footing held, so the next person could carry someone through.
    The closing antithesis converts the preceding action into a general principle about loss and usefulness.
  - Story 0288, `gpt-6-astra-high`:
    > She had mistaken a convenient tether for a law of nature.
    The same corrective cognition appears in a different speculative brief: dependence is reinterpreted as a technical and psychological error.
  - Story 0386, `gpt-6-astra-high`:
    > She had wanted to salvage something pure from the wreckage, and had mistaken purity for innocence.
    The repeated “mistaken” construction explicitly replaces the protagonist’s original desire with the story’s final distinction.
  - Story 0023, `gpt-6.2-astra-high`:
    > After the third time I put my elbow through hers, and that was how we came off the island, carrying what we could.
    The story closes through a modest bodily adjustment that accommodates grief without claiming to resolve it.
  - Story 0396, `gpt-6.2-astra-high`:
    > and stepped aside so her brother could see the plan without having to ask.
    The final ethical action is a change in physical position that returns visibility and agency to the brother, rather than a stated summary of empathy.
- **C061 — GPT-6 Astra (high)’s pre-interpreted recognition turn:** GPT-6 Astra (high) repeatedly makes the protagonist’s former category error explicit and then supplies the corrected interpretation. The wording varies, but the narrative placement recurs: decoding leads to a named recognition, which then authorizes the final action. This gives different briefs a similar psychological shape and can leave less inferential work for the reader than GPT-6.2 Astra (high)’s dramatized changes in conduct.
  - Story 0258, `gpt-6-astra-high`:
    > Mara looked at the deck, ashamed that she had mistaken its repetitions for sloppy draftsmanship.
    The discovery is framed directly as correction of Mara’s earlier interpretation. Her shame arrives at the same moment as the deck’s revised significance, making the recognition turn explicit.
  - Story 0333, `gpt-6-astra-high`:
    > She wanted her mother back more fiercely than she wanted any invention, and had mistaken rescue for reunion.
    The story identifies both Ada’s hidden motive and its proper reinterpretation. The formulation is psychologically apt, but it completes the discovery for the reader before the drawings are released.
  - Story 0349, `gpt-6-astra-high`:
    > She had mistaken her own relief for Ada's.
    The same compact mistaken-for construction turns Mara’s complicity into a named realization. It is effective, but its recurrence with 0333 makes different protagonists’ growth sound structurally alike.
  - Story 0137, `gpt-6-astra-high`:
    > Mara laid her memorial drawing over the courtyard and understood what she had wanted all along.  Not forgetfulness, but somewhere to stand beside remembering.
    The antithesis supplies both Mara’s revised desire and the memorial’s meaning. It exemplifies the related habit of closing interpretation through a polished corrective formulation.
- **C049 — Agency, refusal, and collateral cost:** GPT-6.2 Astra (high) more often tests a protagonist’s benevolent design against other people’s incompatible needs. Its social perceptiveness lies in allowing help to have a cost, privacy to outweigh efficiency, and consent to include a durable no. Solutions therefore distribute agency instead of confirming one central character’s understanding.
  - Story 0137, `gpt-6.2-astra-high`:
    > He saw where the black strip led and stepped across it to take Ada's hand.  When she stepped back he put his face in his wet cap, and I could see what my bit of building had cost him.
    The memorial route does not simply succeed. Ada’s step back and the father’s retreat reveal competing claims over grief, while the builder recognizes that his own compassionate design has exposed and hurt someone.
  - Story 0294, `gpt-6.2-astra-high`:
    > At her own gate she reached up to turn the bird and found the screw our director wanted fitted after purchase.  Her little boy was standing naked in the yard, holding his towel out to screen his grandmother while she got into the tub.
    Permanent commercial access becomes intelligible as a bodily and domestic violation. The screw and the bath scene perform the ethical analysis; Ivo does not need to deliver a persuasive speech about privacy.
  - Story 0333, `gpt-6.2-astra-high`:
    > Some said no, and those people's envelopes are still where I put them.
    The new sharing system preserves refusal in practice. The undisturbed envelopes are more persuasive evidence of consent than the locksmith’s initial boldness or the narrator’s good intentions.
- **C059 — Mechanisms that carry the moral problem:** GPT-6 Astra (high) more consistently makes the required object and method causal rather than ornamental. Operating the system reveals a cost or hidden fact, and the protagonist must then make an ethically consequential decision. This is structural intelligence visible in the sequence of events, not merely in confident explanation.
  - Story 0137, `gpt-6-astra-high`:
    > When Mara lifted the tile, the whale convulsed, and the memory of Nell's face began losing its edges.  She set it down, though doing so restored the drowning.
    The tile’s operation creates a genuine exchange: private relief would injure another mind. Mara’s refusal therefore arises from established mechanics rather than a detachable moral speech.
  - Story 0349, `gpt-6-astra-high`:
    > Mara had once checked such invoices by quantifying absence: subtracting the words in a public record from the total billed.  Ada's bill covered twenty-six words; the judgment contained nine.
    Quantifying absence is both arithmetic and investigation. The discrepancy causally locates suppressed testimony, allowing the legal and emotional plots to advance through the same action.
  - Story 0216, `gpt-6-astra-high`:
    > To stop the leak, I must give it an ending it could not mistake for damage awaiting repair.
    The solution follows from the capsule’s diagnosed error. Accepting an ending, rather than applying a more powerful repair, resolves the speculative problem and the narrator’s resistance to loss together.
- **C012 — Convergent demystification of the brief:** On several briefs both writers independently make the same conceptual move. They deflate the grand element (throne, ascension) into a humble mechanism and recast the abstract one (palimpsest promise) as a family custody document. Conceptual originality therefore does not separate them. What differs is whether the deflation is shown or announced.
  - Story 0191, `gpt-6.2-astra-high`:
    > She had catalogued it from the other side as a porthole overlooking a disused tank.
    GPT-6.2 Astra (high) reveals the mythic stair as a nursery funicular through a quiet correction in the lore keeper's own records.
  - Story 0191, `gpt-6-astra-high`:
    > There had been no ascension, only public transport.
    GPT-6 Astra (high) makes the same demystifying move, stated as a flat declarative.
  - Story 0285, `gpt-6-astra-high`:
    > After the funeral, Iven had sewn KEEP YOU SAFE over his wife's BRING YOU WARMTH.  Mara had slept beneath both.
    Like GPT-6.2 Astra (high)'s penciled sailcloth timetable, GPT-6 Astra (high) materializes the palimpsest as a revised parental vow, here with an elegant, concrete layering.
- **C046 — Shared pivots: "Instead," not-GPT-6.2 Astra (high)-but-GPT-6 Astra (high), and refusal of the easy narrative:** Several apparent signatures belong to both writers and should not be used to separate them.
- An "Instead" sentence marks the moral turn in 4/5 stories for each writer, on the same IDs (0010, 0348, 0349, 0388). Both writers' 0018 stories were checked and have no such pivot.
- Both refuse a tempting tidy story in 0388.

The difference lies only in where the pivot lands. GPT-6.2 Astra (high)'s "Instead" tends to lead to a reframing perception or a handed-over action. GPT-6 Astra (high)'s more often leads to restraint or self-limitation.
  - Story 0349, `gpt-6.2-astra-high`:
    > Instead here was a grandmother keeping count in two different ways because one number was for the till and the other was for getting everybody home.
    GPT-6.2 Astra (high)'s "Instead" opens onto a reframing perception.
  - Story 0388, `gpt-6.2-astra-high`:
    > Instead she brought the pickers to the hollow and let them find their numbers.
    A second GPT-6.2 Astra (high) instance turns toward a communal handoff.
  - Story 0388, `gpt-6-astra-high`:
    > Instead, she cleared a table.
    GPT-6 Astra (high)'s identical pivot word appears in the same story slot.
  - Story 0349, `gpt-6-astra-high`:
    > Mara could still press her daughter's fading hand against the slate upstairs; instead, she asked, "May I put this back?"
    GPT-6 Astra (high)'s "instead" here marks self-restraint, consistent with its ethic of yielding control.
  - Story 0388, `gpt-6.2-astra-high`:
    > On the way back she found herself composing the easy column, the one about a shabby doctor's private charity, and it frightened her how good it was going to be.
    GPT-6.2 Astra (high)'s refusal of the comfortable narrative.
  - Story 0388, `gpt-6-astra-high`:
    > Mara thought of the comfortable version she could broadcast: one criminal official, one repaired pipe, fruit shipments resuming before anyone went hungry.
    GPT-6 Astra (high) makes the same structural move in the same brief, partly invited by the prompt's "comfortable lies."
- **C025 — Working mechanism versus sidelong social discovery:** GPT-6 Astra (high) resolves stories through procedures whose logic a reader could check. These are experimental controls and geometric properties, and they are genuine causal intelligence rather than polish. GPT-6.2 Astra (high) resolves stories by moving attention to a person or social fact that the framing had hidden. The two are distinct kinds of intelligence, and each is executed well in this packet.
  - Story 0323, `gpt-6-astra-high`:
    > A circle looked unchanged when the alien geometry turned or reflected it; this battered oval had an unmistakable orientation.
    The plot hinges on a correct property of symmetry. The battered heirloom solves the problem because of its damage.
  - Story 0362, `gpt-6-astra-high`:
    > Mara invited the court's reader to kneel, then had a guard move the prism while she stood well away from it.
    This is a blinded control: it removes her own presence as a confound, so the magic is handled with real epistemic rigor.
  - Story 0362, `gpt-6.2-astra-high`:
    > the chairman, to his credit, did not ask her what a woman with a salary had to be angry about.
    The resolution shows a social fact: the institution's own employee holds the anger. It is conveyed through a sideways remark rather than a demonstration.
  - Story 0323, `gpt-6.2-astra-high`:
    > I finally understood that the question was not how to get her back where she came from, which was the question occupying the cleverest people in Pelagos.  She wanted to be able to come back here.
    Insight comes from reframing someone else's desire, not from solving a technical problem.
- **C011 — Social-institutional legibility:** When a brief involves civic conflict, GPT-6 Astra (high) builds explicit, plausible machinery: a legal clause, competing factions, a deposit, a severance, a thirty-day postponement. It also gives voice to the opposing views of insiders and newcomers. GPT-6.2 Astra (high)'s version of the same brief rests on an evocative but causally thin gesture: why showing the bedrooms moves the commissioners is left implicit.
  - Story 0142, `gpt-6-astra-high`:
    > For the old families, though, every unfamiliar face was another advance scout for the coming hotels.
    Captures the internal conflict gentrification creates among victims, not just between victims and developers.
  - Story 0142, `gpt-6-astra-high`:
    > Her dual allegiance, to the authority that paid her and the neighbors who trusted her, was becoming a kind of dishonesty.
    Converts the brief's abstraction into a specific moral mechanism.
  - Story 0142, `gpt-6.2-astra-high`:
    > It took more nerve than a strike, to let strangers see the shape your body had left in a bed.
    Psychologically acute, but the persuasive power of the display is asserted rather than causally shown.
- **C058 — Engaging socio-technical modernity versus retreating into timeless parish craft:** Range and adaptability cut in Writer GPT-6 Astra (high)'s favor when a prompt invites contemporary technological systems or structural economic critique. In 0258 ("after the cryptocurrency crashes," "reverse engineering," "to map cultural patterns"), GPT-6 Astra (high) builds its plot directly out of centralized payment-network failure and the danger of turning informal neighborhood survival practices into a clean, searchable municipal database that exposes unlicensed kitchens. GPT-6.2 Astra (high) dispatches the cryptocurrency crash in a single sentence about worthless employer coins and immediately retreats into a pre-digital world of linen pillowcases, "half a parish," confirmation suits, lawn, lace, and a gentleman's evening glove. Similarly, in 0252 ("after violence becomes impossible"), GPT-6 Astra (high) perceptively asks what forms of coercion survive universal bodily nonviolence—withheld wages, locked storehouses, inherited debts—whereas GPT-6.2 Astra (high) treats the premise purely as a gentle fairy-tale release from physical stakes.
  - Story 0258, `gpt-6-astra-high`:
    > Mara had once designed payment networks that rewarded everyone for taking the same efficient route.  When that route collapsed, her neighbors lost their savings, and she lost the right to call herself useful.
    GPT-6 Astra (high) connects the cryptocurrency crash conceptually to "multiplying paths": monoculture network efficiency creates systemic fragility.
  - Story 0258, `gpt-6-astra-high`:
    > For a moment, Mara saw the beautiful database she could build, each connection clean, each household exposed.
    Inhabits modern information-design temptation, contrasting extractive digital legibility with consent-based human readers.
  - Story 0252, `gpt-6-astra-high`:
    > Around them, the harbor continued its bloodless cruelties: withheld wages, locked storehouses, children inheriting debts.
    Demonstrates sharp systemic adaptability, deducing how property and labor coercion persist when physical injury becomes impossible.
  - Story 0258, `gpt-6.2-astra-high`:
    > My employer had paid us in coins that would no longer buy a loaf, and the loft was the only thing standing between me and the bread line.
    GPT-6.2 Astra (high) translates digital currency collapse into archaic bread-line and loaf imagery, exiting contemporary technological texture within one sentence.
  - Story 0258, `gpt-6.2-astra-high`:
    > Three quarters of a yard of lawn, half a yard of lace, a quarter share in an ivory button, she translated, laughing at the last entry.
    Charming in itself, this haberdashery register reveals the gravitational pull of GPT-6.2 Astra (high)'s default parish-craft aesthetic even in a post-crypto brief.
- **C017 — Maturity lies in cost without guaranteed consolation:** Both writers’ strongest stories refuse to equate correct action with emotional repair. GPT-6 Astra (high) explicitly preserves fury and culpability after successful action; GPT-6.2 Astra (high) preserves absence, risk, and incomplete trust. This limits the claim that GPT-6 Astra (high) always moralizes neatly or that GPT-6.2 Astra (high) alone tolerates ambiguity.
  - Story 0023, `gpt-6-astra-high`:
    > She did not feel released.  She felt robbed, and furious, and kept moving.
    Cutting the line is ethically necessary but provides no catharsis, separating right action from emotional reward.
  - Story 0386, `gpt-6-astra-high`:
    > By evening, people were saying her father had been a monster instead of a drunk.  Neither word was large enough, but she no longer offered him a smaller truth to hide inside.
    The investigation removes one false accusation without restoring innocence, and Mara also rejects the public’s replacement simplification.
  - Story 0023, `gpt-6.2-astra-high`:
    > my mother kept reaching up to the crook of her arm where the tin had rested and finding nothing there.
    The completed burial leaves a repeated bodily expectation of weight, making grief persistent without announcing its meaning.
  - Story 0284, `gpt-6.2-astra-high`:
    > "Third house past the pump," she said, as plainly as if it had never been a dangerous thing to tell somebody where you lived.
    Ada offers an address rather than reunion or forgiveness; trust resumes as a limited, risky permission.
- **C032 — Repair must survive other people’s judgment:** GPT-6 Astra (high) more often preserves accountability and the injured person’s independence after the protagonist recognizes an error. Victims need not become innocent, relatives need not offer immediate absorption, and another person may correct the record or restrict the meaning of reconciliation. GPT-6.2 Astra (high)’s repaired relationships are affecting but more often become collaborative with less residual resistance.
  - Story 0187, `gpt-6-astra-high`:
    > The dead did not become innocent merely because her father had wronged them.
    Mara’s exposure of her father does not simplify the famine testimony into a morally convenient opposition. She records theft as well as suffering, making restoration an obligation to accuracy rather than self-absolution.
  - Story 0187, `gpt-6-astra-high`:
    > The laundress stood nearest Mara, close enough for their sleeves to touch, without taking her hand.
    Support and withheld intimacy coexist physically. The community can protect Mara’s act of restoration without yet granting her emotional exoneration.
  - Story 0289, `gpt-6-astra-high`:
    > "You can hold this," she said, "but don't make it mean more than that."
    Leela defines the permitted scale of reconciliation. Mara’s artistic insight does not entitle her to interpret the gesture as complete forgiveness.
  - Story 0289, `gpt-6.2-astra-high`:
    > Together we bound the whole thing up with lead, a house a thumb's breadth taller than its neighbors, with room for what was there.
    GPT-6.2 Astra (high)’s shared making beautifully accommodates the object, but Ruth’s hurt is resolved into collaboration more quickly and with less explicit boundary-setting than Leela’s.
- **C020 — Mixed personal motives and ordinary fallibility versus systemic moral reckoning:** Writer GPT-6.2 Astra (high) locates psychological surprise in half-conscious self-protection, petty human partiality, and ordinary bureaucratic compression without villains. Writer GPT-6 Astra (high) escalates all 5/5 prompts into systemic injustice and bodily harm, yielding sharp institutional critique but more predictable moral psychology.
  - Story 0387, `gpt-6.2-astra-high`:
    > When I laid my mother's bowl on his knees he put his thumb in the worn place and held it there.  "I always get to lift her out," he said, with the astonishment of a man who has only just heard his own excuse.
    GPT-6.2 Astra (high) first lets the reader think the father stays under the parapet purely out of dutiful hidden labor, then reveals a deeper psychological truth: catching the bowls spared him ever having to release his dead wife.
  - Story 0194, `gpt-6.2-astra-high`:
    > Ada could have stayed there all night to muse on who had paid the librarian, or whether he had simply liked the little girl who brought him pears better than the one who stole his plaster to mend her dolls.
    Rather than attributing a rigged royal succession solely to grand conspiracy, GPT-6.2 Astra (high) recognizes that dynastic history can turn on an old clerk's mundane fondness for pears and irritation over pilfered sticking plaster.
  - Story 0393, `gpt-6.2-astra-high`:
    > What I'd said on the strength of a photograph and a recording was that the long gap in the music sounded like a botched repair.  What Bell had put on the form, in the space that would take one line of type, was "Repair botched."
    Injustice here arises from recognizable everyday carelessness—a hedged remote opinion flattened by a one-line administrative box—rather than authoritarian cruelty.
  - Story 0387, `gpt-6-astra-high`:
    > "Why didn't you ask for help?"
    >
    > "I did, when my hands began to stiffen."  She nodded toward the council hall.  "They gave me that medal you polish."
    This shows GPT-6 Astra (high)'s genuine gift for institutional perception—capturing how civic honors launder neglect—while illustrating how GPT-6 Astra (high) frames hidden effort as public exploitation rather than intimate self-deception.
  - Story 0393, `gpt-6-astra-high`:
    > "Must I confess first?"
    >
    > She almost said he did deserve help, then heard the old bargain hidden in that comforting word.
    GPT-6 Astra (high) perceptively exposes the coercive conditionality inside charitable language, even as it raises the stakes of the music-box prompt to solitary confinement and life-or-death chest repair.
- **C054 — Psychological blind spots versus transparent institutional wrongs:** Writer GPT-6.2 Astra (high) generates deeper interpersonal discovery by uncovering tender, symmetrical blind spots inside love and pride, whereas Writer GPT-6 Astra (high) typically stages conflict against an institutional injustice whose moral wrongness is obvious from the outset. In 0012 ("to illuminate hidden assumptions"), GPT-6 Astra (high)'s cathedral sacrifices solitary women as permanent vessels—a plainly indefensible practice that the priest dismantles through public analogies. GPT-6.2 Astra (high)'s priest and daughter instead assume that loving the drowned mother means offering a year of the girl's youth, and that non-possession would mean the mother didn't miss them; flipping one sentence reveals that the mother has been lifting the brush herself to avoid stealing her child's daylight, confirmed by an invoice mark ("account closed, nothing owing"). In 0258, GPT-6.2 Astra (high) shows similar social delicacy in explaining how fabric-printed cards let poor women assemble wedding dresses across a parish without the humiliation of asking for charity.
  - Story 0012, `gpt-6.2-astra-high`:
    > "You would give your mother a year, Kit; would your mother take a year from you?"
    GPT-6.2 Astra (high) fulfills both "through rhetorical devices" and "to illuminate hidden assumptions" in sixteen words, using chiasmus to invert the family's grief-stricken premise.
  - Story 0012, `gpt-6.2-astra-high`:
    > Another line crossed it, then a third, until there stood the little gate Ada used to draw beside a finished sign on an invoice: account closed, nothing owing.
    Rather than stating the mother's protective love, GPT-6.2 Astra (high) lets a commercial sign-painter's tally mark release her daughter from perceived filial debt.
  - Story 0012, `gpt-6-astra-high`:
    > She was patient, unmarried, and accustomed to working alone; he had called these qualifications, never asking why solitude should make a life expendable.
    GPT-6 Astra (high) names the hidden assumption directly in third-paragraph exposition, framing an unmistakable institutional wrong rather than a shared psychological surprise.
  - Story 0258, `gpt-6.2-astra-high`:
    > Nobody had to lend anything, Mercy said, and nobody needed to know why you had come up short.
    GPT-6.2 Astra (high) perceives how indirect brokerage preserves working-class dignity, giving the cartomancer's deck a subtle social psychology.
- **C060 — Mixed needs, durable refusals, and institutional accident:** GPT-6.2 Astra (high) repeatedly perceives more than one legitimate need within a scene and does not require emotional reconciliation to erase privacy, disagreement, or refusal. Its institutional insight also extends beyond identifying villains. These behaviors create psychological and social depth through what characters permit and do, not through diagnostic commentary alone.
  - Story 0137, `gpt-6.2-astra-high`:
    > Ada sat one stone over, close enough to lay her cheek against his sleeve without giving up what was hers.
    The seating arrangement holds intimacy and exclusive possession of grief together. Ada need neither isolate herself nor surrender her private memories in order to rejoin her husband.
  - Story 0333, `gpt-6.2-astra-high`:
    > Some said no, and those people's envelopes are still where I put them.
    The new sharing system does not become beneficial merely because the protagonist has accepted it. Refusals remain effective, making consent a continuing practice rather than a ceremonial step.
  - Story 0349, `gpt-6.2-astra-high`:
    > Nobody had thought to turn it edgewise; nobody had needed to be wicked for her to go to jail.
    The insight changes the social explanation of Ada’s imprisonment from malice to a collectively limited way of reading evidence. It also redirects her desired confrontation toward practical correction.
- **C010 — Adaptive voice and resolution versus stable arc with modal swings:** GPT-6.2 Astra (high) changes point of view (first person in 0142, 0285, 0330; third in 0086, 0191) and narratorial persona. These range from an earthy retired coachman to a civic liaison with a dead brother. GPT-6.2 Astra (high) also changes how stories resolve: a loophole, a demonstration, a ride, a child's speech, silent witnessing. Humor surfaces in all five. GPT-6 Astra (high) keeps close third and an earnest register in all five. Its widest successful contrast is genre: the realist ethical procedural of 0086 against the fabulist allegory of 0330. Each GPT-6 Astra (high) story still runs the same choose-the-community arc. GPT-6 Astra (high)'s range is real but mostly a change of setting and genre around one plot.
  - Story 0285, `gpt-6.2-astra-high`:
    > I could tell by a slackening of leather that my mare was going to piss, yet I had never been so closely attentive to the creature sitting at my elbow.
    A distinct, earthy first-person voice that turns a required attribute into self-indictment.
  - Story 0191, `gpt-6.2-astra-high`:
    > Getting her mother onto the throne took both of them and a certain amount of language not generally addressed to royalty.
    Comic register inside a deathbed science-fiction elegy, showing GPT-6.2 Astra (high) can mix tones within one story.
  - Story 0330, `gpt-6-astra-high`:
    > She tried to sing.  The first note scarcely disturbed the pool.  The second carried a whispering gleam along the water, and every palm bent toward it.  At the third, the windows burst outward without a sound.
    GPT-6 Astra (high)'s most contrasting successful mode: incantatory, fabulist escalation unlike its civic-realist stories.
  - Story 0142, `gpt-6-astra-high`:
    > It took two hours to turn accusations into pledges.
    GPT-6 Astra (high)'s usual summary-driven civic register, which carries into most briefs regardless of the tone requested.
- **C047 — Voice and structure adapt more in GPT-6.2 Astra (high); genre surface adapts more in GPT-6 Astra (high):** GPT-6.2 Astra (high) changes point of view (first person in 0348), mixes comic register into grief (0018), and in 0349 inverts its usual guilty-protagonist structure by vindicating Ada. GPT-6 Astra (high)'s settings and mechanisms vary strongly, and 0018 is a successful suspense confrontation that is GPT-6 Astra (high)'s most contrasting mode. But GPT-6 Astra (high) keeps close third on Mara and a constant arc: grief, culpable error, collaborative correction. 0349 collapses into that default, becoming another mother-daughter grief story despite a brief inviting fragmentation.
  - Story 0348, `gpt-6.2-astra-high`:
    > I had signed both sheets; I had not volunteered that the hour was my choice.
    A first-person confessional voice with a guarded, lawyerly evasiveness that the voice itself performs. It is distinct from GPT-6.2 Astra (high)'s third-person stories.
  - Story 0018, `gpt-6.2-astra-high`:
    > Down came the tray with a sound they both knew, the astonishingly dirty laugh of a boy who had learned it from the men who carted coal.
    Bawdy comedy is placed at the emotional peak of a dead-child story, a register shift GPT-6 Astra (high) does not attempt.
  - Story 0018, `gpt-6-astra-high`:
    > "You made me lonely," he said, and the voice was exactly right.
    GPT-6 Astra (high)'s strongest contrasting mode: an eerie, antagonistic dream-figure in a tense rescue scene.
  - Story 0349, `gpt-6-astra-high`:
    > Mara took the concession to rescue her daughter, not dispute the verdict; a daughter without memories still seemed better than no daughter at all.
    Despite a new penal-fantasy premise, the story reverts to GPT-6 Astra (high)'s default: a mother's protective error toward a younger female, later recognized and corrected.
- **C064 — Inference left to the reader versus insight stated outright:** GPT-6.2 Astra (high) places its key revelations in physical evidence the reader must interpret: shadow lengths, a curled finger, a pencil sharpened for a lifetime. GPT-6 Astra (high) voices the revelation in a summarizing sentence of self-recognition or principle. GPT-6.2 Astra (high)'s method gives the stronger sense of perception and trust in the reader. GPT-6 Astra (high)'s gives clarity and ethical precision but sometimes reads as the story explaining itself.
  - Story 0187, `gpt-6.2-astra-high`:
    > I could only conjecture that the child had not been passing through but standing watch, which was no kind of work for a child that day.
    The conclusion is derived from a two-number shadow discrepancy the reader has just watched. The required "conjecture" becomes genuine inference rather than a label.
  - Story 0221, `gpt-6.2-astra-high`:
    > By then she could afford to give me that much time.
    A single unexplained line uses the time-dilation premise to express that the daughter has aged past the parent. The reader supplies the arithmetic and the emotion.
  - Story 0058, `gpt-6-astra-high`:
    > For years, I had written her departure as cruelty, revising every detail except my own.
    The narrator's blind spot is diagnosed explicitly rather than allowed to surface through action or detail.
  - Story 0221, `gpt-6-astra-high`:
    > True north was not the brightest thing in the window; it was the direction the turning lights revealed.
    The thematic meaning of the required "true north" is stated as an aphorism. It is elegant, but it does the interpretive work for the reader.
- **C041 — Commitment to grand speculative scale and somatic friction versus parish domestication:** On speculative worldbuilding scale and physical resistance, the adaptability advantage reverses toward Writer GPT-6 Astra (high). When briefs invite eerie metaphysics or systemic conflict (0127, 0290), GPT-6 Astra (high) builds genuinely estranged macro-institutions and honors bodily terror and hard civic trade-offs. Writer GPT-6.2 Astra (high) persistently domesticates speculative concepts into a cozy-gritty provincial parish idiom; in 0290, that folkloric translation dissolves both claustrophobia and political mutiny into effortless whimsy.
  - Story 0290, `gpt-6-astra-high`:
    > The chamber was scarcely wider than her shoulders.  She could see the wheel clearly, but her body insisted she was back inside the culvert, tasting mud.  "Keep playing," she told Tomas, and counted the beats between breaths until she could crawl.
    GPT-6 Astra (high) takes the prompt's "claustrophobic explorer" seriously as a somatic obstacle, forcing Mara to fight bodily flashback and tightening stone foot by foot.
  - Story 0290, `gpt-6-astra-high`:
    > By morning, the palace would be merely a house, and the hospital would be three honest days away.  They would need a village clinic, new bridges, arguments, taxes, work.
    GPT-6 Astra (high) refuses a costless miracle: dismantling royal spatial theft also destroys a folded highway to the hospital, imposing real material consequences on the village.
  - Story 0290, `gpt-6.2-astra-high`:
    > To steady her breath she hummed the nonsense song she sang with her nephew on the road to school.  Overhead the organ took up the tune, badly at first, like somebody picking out a song remembered from childhood, and against her other boot she felt the school road unfolding.
    In GPT-6.2 Astra (high)'s version, claustrophobia vanishes with a hummed tune, the county organist effortlessly defects to harmonize, and stripping turf off a treadle restores old apple-tree lanes without institutional pushback or cost.
  - Story 0127, `gpt-6-astra-high`:
    > Preservation would arrest the forgetting, although the grotto would subsume her remaining memories into its communal intelligence.  "I would rather become a committee than an empty room," she had explained.
    Where GPT-6.2 Astra (high) turns the amber grotto into a municipal memorial wall, GPT-6 Astra (high) invents an unsettling speculative Rite—living elders merging into a conflict-averse resin collective—that tests identity at a genuinely strange conceptual scale.
- **C006 — Willingness to inhabit state-scale and technological speculation versus artisanal parish domestication:** While narrower in voice, Writer GPT-6 Astra (high) adapts readily to macroscopic state bureaucracy, penal censuses, and modern telecommunications infrastructure when futuristic briefs invite them. Across all 5/5 stories, Writer GPT-6.2 Astra (high) pulls every speculative or technological cue back into a nostalgic, pre-industrial or mid-century parish craft world of hand tools, church similes, and village food.
  - Story 0125, `gpt-6-astra-high`:
    > Mara, a drifting roadside poet, wrote obituaries for living conscripts, smuggling them beyond the new census of available years.
    GPT-6 Astra (high) takes "after the energy beings arrive" into inventive state-scale speculative worldbuilding—temporal conscription, bureaucratic censuses, and weaponized time-prisons.
  - Story 0256, `gpt-6-astra-high`:
    > Mara asks the engineer to disconnect the recorded crowd and open the laboratory's microphones to the resettlement blocks across the water.  For the first time since evacuation, the steady grid can hold all those scattered households in one unbroken circuit.
    GPT-6 Astra (high) uses the newly stabilized power grid and urban resettlement blocks as active technological infrastructure linking dispersed modern apartments.
  - Story 0125, `gpt-6.2-astra-high`:
    > Light ran the length of the coil, laying down each whisker like a mother smoothing hair for church.  Kit laughed with her mouth full of the pie she had carried all that way in her pocket.
    Even after alien arrival, GPT-6.2 Astra (high) frames the world through saints' ears, festival hymns, churchgoing mothers, and pork pies—the same artisanal village texture governing its mills (0065), smiths (0206), island funerals (0218), and coal bathhouses (0256).
- **C066 — GPT-6 Astra (high)'s template: near-relapse, self-indictment, open-ended tending, stock names:** GPT-6 Astra (high)'s briefs differ widely, yet they resolve through the same sequence. A protagonist has tried to preserve or control something after a loss. A speculative device exposes this. The protagonist "nearly" or "almost" reverts, chooses the imperfect ongoing process, and the ending promises continued care. Packet-only counts:
- The literal "nearly/almost" temptation beat appears in 0058, 0187, 0206 and 0389 (4/5). 0221 was examined and has no such beat.
- Forward-looking continuation endings appear in 0058, 0206 and 0221 (3/5). 0187 and 0389 end on an act of continued work without a future pledge.
- "Mara" or "Mera" names a central woman in 0058, 0187, 0221 and 0389 (4/5). 0206 uses Pip and Ada instead, and "Ada" recurs in 0221.

The result is that different briefs produce substantially the same emotional story.
  - Story 0058, `gpt-6-astra-high`:
    > Mara flinched, and I nearly released the thread, as if pain meant the ceremony had failed.
    The near-relapse beat, with a Mara.
  - Story 0389, `gpt-6-astra-high`:
    > Mera nearly told him, because she had heard that voice shake whenever he mentioned his sister, and because being needed was a treacherous warmth.
    Same "nearly" construction and near-identical name in a political brief.
  - Story 0206, `gpt-6-astra-high`:
    > They would have to return tomorrow, and the day after that; there would always be something worth tending.
    The open-ended tending close, also preceded by "He almost promised."
  - Story 0058, `gpt-6-astra-high`:
    > There would be no post until the thaw, which left time for another letter, and another, none pretending to be the last.
    The same repetitive-continuation cadence ("another, and another") in a different setting.
  - Story 0187, `gpt-6-astra-high`:
    > After fog became solid, Mara climbed the iron stair to the stormlit observatory above clouds.
    A stock protagonist name reused across unrelated briefs (compare 0221: "After the shutdown, Mara returned...").
- **C068 — Social-systems intelligence in different keys:** Both writers think about communities, not just individuals. GPT-6.2 Astra (high) models second-order behavioral effects. In 0389, dependence on a prophet erodes local safety habits, and fragmentary reception splits the community into rival interpretations. GPT-6 Astra (high) models power and complicity more explicitly. In 0389, a liberator's grief turns into selective revenge. In 0187, an archivist's own negligence helped launder her father, and GPT-6 Astra (high) refuses to sanctify the victims. GPT-6.2 Astra (high)'s version is more ingenious; GPT-6 Astra (high)'s is more morally searching.
  - Story 0389, `gpt-6.2-astra-high`:
    > The Copper men had stopped sounding the rock before a shift, and the women at Salt no longer counted their sacks of emergency meal.
    The prophet's danger is shown through concrete erosion of practice, not stated as a theme.
  - Story 0389, `gpt-6-astra-high`:
    > He added that the barracks could wait for theirs, just until the soldiers learned what his sister had endured.
    GPT-6 Astra (high) shows how private grief becomes political exclusion, a precise psychological-political link.
  - Story 0187, `gpt-6-astra-high`:
    > The dead did not become innocent merely because her father had wronged them.
    An ethically mature refusal of simple victim-sanctification, unusual in a restoration plot.
- **C002 — Distributed competence across secondary characters versus lone pedagogical reformer:** In Writer GPT-6.2 Astra (high)'s stories, bystanders and skeptical interlocutors possess independent technical, historical, or emotional insight that corrects or completes the protagonist's work. Writer GPT-6 Astra (high) concentrates conceptual breakthroughs in a lone protagonist who educates short-sighted officials or guides dependents.
  - Story 0065, `gpt-6.2-astra-high`:
    > "Not much of a mill, but suppose he brought it down on the bad days."
    >
    > She nearly told him the gearing he would need, then caught herself; his brother had been mending things before she was born.
    Nell's model leaves Hen's brother freezing on peak days; it is old Hen who invents the hand-mill adapter to solve that trade-off, and Nell checks her own impulse to lecture.
  - Story 0256, `gpt-6.2-astra-high`:
    > "I'd knock on the rail and he'd clear his throat so I'd know it carried," she said.  "You could have rung all night, honey, but he couldn't hear your bells by then."
    Ada's mother supplies the crucial forensic and relational truth
—that the archived cough answered a scrubbed key-knock and that Ada's own bells had already grown inaudible to her father.
  - Story 0218, `gpt-6-astra-high`:
    > "You will empty our cisterns trying to be kind," he said.
    >
    > "Then we shall be competent as well," Mara replied, and unrolled her drawings across the altar.  She proposed to remodel the orchard's supports, not demolish its waterworks.
    GPT-6 Astra (high) casts the civic official as a foil voicing a predictable objection so Mara can unveil an already complete engineering and ethical synthesis.
  - Story 0256, `gpt-6-astra-high`:
    > Mara stops the bells before the automated procession can reach the memorial without him.  The engineer offers to propel the chair with a motor, then to slow the procession, then to make every pilgrim turn and smile.
    Again in GPT-6 Astra (high), the institutional specialist offers tone-deaf technical fixes until the protagonist alone reconceives the project.
- **C043 — Social-economic causality versus systemic-epistemic reasoning:** The two writers show different kinds of substantive intelligence. GPT-6.2 Astra (high)'s revelations are institutional and monetary: pawn advances, fare counts, who chose the sampling hour. The wrong is shown to need no villain. GPT-6 Astra (high)'s revelations are epistemic and technical: GPT-6 Astra (high) doubts what data can mean, insists on measurement over intuition, and designs systems with explicit tradeoffs. Both go beyond surface cleverness.
  - Story 0388, `gpt-6.2-astra-high`:
    > nine advances against one feathered diamond, each exactly the price of a hospital deposit.
    The curse is converted into an economic mechanism. The diamond becomes collateral, and the deaths become a matter of logistics and payday.
  - Story 0349, `gpt-6.2-astra-high`:
    > Nobody had thought to turn it edgewise; nobody had needed to be wicked for her to go to jail.
    This is a precise social insight: injustice produced by procedural inattention rather than malice.
  - Story 0010, `gpt-6-astra-high`:
    > Warm cheeks might mean joy, shame, fever, or merely a difficult staircase.
    GPT-6 Astra (high) interrogates the premise of the prompt's method itself, showing epistemic caution.
  - Story 0388, `gpt-6-astra-high`:
    > She intuited the rest, but intuition had already helped her ruin one innocent man.
    The required action "intuit" is turned into an argument for verification, which GPT-6 Astra (high) then dramatizes with readings and a valve.
- **C019 — Causal integration of prompt mechanics versus arbitrary or compartmentalized bridges:** Writer GPT-6.2 Astra (high) makes improbable prompt combinations causally generate one another under strict physical and perceptual constraints, so the method in the brief becomes the literal mechanism of discovery. Writer GPT-6 Astra (high) builds clean outer plots but occasionally forces sensory mechanics by fiat or keeps prompt elements in separate narrative compartments.
  - Story 0261, `gpt-6.2-astra-high`:
    > Then came the pressure of two elbows on either side of the little cup, and a chin, and the wet salt of somebody weeping.  Not a child's chin, said the willow when I asked; children had to stand to reach its top.
    Because the thumb was grafted on willow stock, GPT-6.2 Astra (high) restricts coffee-ring memory to physical impressions a wooden tabletop could actually register—heat, weight, salt water, and leverage—allowing a rigorous deduction about who sat there.
  - Story 0261, `gpt-6-astra-high`:
    > I pressed each ring until the vibrations became voices.
    >
    > In the deepest burn, my mother was arguing with the surgeon.  "It belongs under the orchard," she said.  A cup struck wood; the table remembered boiling bitterness.  "Moving a miracle doesn't make it yours."
    After stating that scars remember pressure and heat rather than words, GPT-6 Astra (high) immediately has coffee stains play back verbatim English dialogue like a phonograph recording to deliver backstory.
  - Story 0393, `gpt-6.2-astra-high`:
    > One white rent opened in the mica sky and closed; four whole seconds later the hammers struck together, and thunder rolled out over the astonished grass.  The four seconds, so excruciating on the recording, were aptly deliberate: we had just heard how far away the storm was.
    GPT-6.2 Astra (high) unifies second opinions, storm light, and aptly deliberate through acoustics: judging a visual-musical automaton from an audio tape made a speed-of-sound delay between mica lightning and thunder sound like a broken gear.
  - Story 0389, `gpt-6.2-astra-high`:
    > In Copper the hare lacked a foreleg; in Salt he had a hole where a heart might usefully go.  The cooks filled the gaps with grease pencil, giving Copper a fist and Salt a fat little pocket for putting things by.
    Fragmented radio frequencies directly cause variant allegiance: static drops different scan lines on each band, prompting mine cooks to complete the partial shadow-puppet image into rival sectarian icons.
- **C037 — Organic medium-native causality versus schematic puzzle encoding:** When prompts demand forensic deduction or signal decoding (0056, 0354), Writer GPT-6.2 Astra (high) derives the mystery's mechanics directly from the physical properties of the object and setting. Writer GPT-6 Astra (high) constructs logical, tidy puzzles, but relies more on top-down cryptographic or bureaucratic devices engineered to deliver a message.
  - Story 0354, `gpt-6.2-astra-high`:
    > It took the driver to correlate the squares with the survey grid, since the boy was looking upriver and they were looking down.  Three times he sent the square for the schoolhouse, and then, with beautiful economy, the square for the siding.
    Every element grows out of chess and river geography: eight pump flashes match an eight-rank board, blocking light subtracts flashes, river perspective flips board orientation, and two squares express evacuation as a chess move.
  - Story 0354, `gpt-6-astra-high`:
    > The royal manuals had preserved the loud half of the signal and dismissed its pauses as mechanical hesitation.  By translating silence, they recovered coordinates that spelled instructions through the letters stamped inside each square.
    GPT-6 Astra (high)'s chessboard functions as a stamped-letter cipher wheel spelling out prose instructions, requiring generations of engineers to have overlooked systematic short-and-long pause lengths.
  - Story 0056, `gpt-6.2-astra-high`:
    > The ring on its case had worn almost through, yet there was no corresponding wear inside, not even at the notch where the thread caught.
    GPT-6.2 Astra (high) deduces an entire social history—nineteen orphans passing an unopened pawnshop sundial on a finger to sign as one captain at a low clerk's window—purely from differential brass wear.
  - Story 0056, `gpt-6-astra-high`:
    > The inquiry placed his opening of the sluice twelve minutes before the evacuation warning.  But the logbook's heading read SUN TIME, two words cropped from the official photograph.
    GPT-6 Astra (high)'s 24-minute sundial correction and cropped heading form a clean, well-reasoned evidentiary chain, though one built around documentary tampering rather than tactile object logic.
- **C053 — Interlocking physical causality versus stipulated rules:** When integrating disparate speculative elements, Writer GPT-6.2 Astra (high) constructs an interlocking physical, economic, and material ecology in which each constraint causes the next, whereas Writer GPT-6 Astra (high) more often connects constraints via stipulated magical rules or single-purpose plot devices. In 0007, GPT-6.2 Astra (high) turns the celestial alignment into a coastal syzygy tide that briefly drains a drowned district, links "synaptic plasticity" to accelerated motor learning in glassblowing apprenticeships, and uses memory-tasting of cabbage broth plus a pruned coat-hook stump to locate a buried glass seed-tube. GPT-6 Astra (high) makes the alignment wake the seed by underlined maternal rule ("peculiar light") and sprouts a tile-lifting tree root in minutes so the inspector can order it pruned. In 0276, GPT-6.2 Astra (high) similarly makes the rail spike necessary as a forged iron fishhook because the train whistle's two notes took root in iron rails, whereas GPT-6 Astra (high) uses the spike as an ordinary jetty mooring peg.
  - Story 0007, `gpt-6.2-astra-high`:
    > The afternoon both moons lined up with the sun, the sea backed out of the glass district and let the old bell over the greenhouse door ring once.
    Instead of treating the alignment as arbitrary magic light, GPT-6.2 Astra (high) translates two moons aligning with the sun into extreme tidal physics that creates the scene's ticking clock.
  - Story 0007, `gpt-6.2-astra-high`:
    > Once, an apprentice would eat a slice of the pale flesh before taking up the blowing iron; the fruit worked through synaptic plasticity, making an afternoon's practice take hold like a season's.
    GPT-6.2 Astra (high) uses the actual neurological meaning of synaptic plasticity—skill consolidation through practice—and ties its disappearance to the economic death of artisanal glassblowing.
  - Story 0007, `gpt-6-astra-high`:
    > Only the alignment's peculiar light could wake the seed; her mother had underlined that instruction twice.
    GPT-6 Astra (high) connects the timeframe to the seed by authorial stipulation in research notes rather than physical or ecological consequence.
  - Story 0276, `gpt-6.2-astra-high`:
    > Nell bent a rail spike into a hook in the yard forge so that whatever she caught would run in iron as readily as the whistle did.
    The required object's materiality directly solves the acoustic problem: iron-rooted whistle notes require an iron-conducted hush.
- **C048 — Causal architecture and brief integration:** GPT-6 Astra (high) more consistently turns required objects and concepts into an explicit causal sequence whose payoff also resolves the emotional problem. Its control comes from planted rules and reusable object properties, not from polished explanation alone. GPT-6.2 Astra (high) often achieves equal social causality, but is more willing to let the originating speculative problem recede.
  - Story 0137, `gpt-6-astra-high`:
    > The instrument had joined their losses because it could not tell them apart.
    This diagnoses the entanglement as a specific failure of discrimination. The subsequent courtyard diagram, balanced rows, and separate memorial seats all answer that diagnosis, so setting, object, action, and memorial motivation share one causal design.
  - Story 0216, `gpt-6-astra-high`:
    > To stop the leak, I must give it an ending it could not mistake for damage awaiting repair.  The fragment belonged to a vessel that had completed its purpose; the ashes still caught in its clay belonged to a finished life.
    The urn fragment is not merely a grief token. Its completed function supplies the precise evidence the damaged capsule lacks, making the emotional acceptance of ending and the mechanical repair of time the same act.
- **C016 — Both writers possess substantive procedural intelligence:** Neither writer’s effects depend mainly on atmosphere. Both make required objects perform causal work, establish constraints, and use evidence to revise an apparently settled past. GPT-6 Astra (high) is especially clear about testing and mechanical cost; GPT-6.2 Astra (high) is especially economical at joining technical inference to social evidence.
  - Story 0284, `gpt-6-astra-high`:
    > Its spring steel clasp could be reshaped to press the pawl into place.  She would have to tear it from the lid, destroying part of the engraved key.
    The pillbox is simultaneously a decoding device, a mechanical solution, and a sacrifice, so sentiment and causality alter one another.
  - Story 0284, `gpt-6-astra-high`:
    > She lowered the cage empty, then loaded it with shelter ballast and tested the brake twice.
    The repair is validated before passengers depend on it, giving “prudently daring” an observable procedural meaning.
  - Story 0386, `gpt-6.2-astra-high`:
    > Any fool could have told me what you shake at a child to make him look into a camera.  It took a diver to find the darkroom.
    The recurring dream image is reinterpreted as photographic evidence, linking the supernatural cameos to a recoverable physical archive.
  - Story 0288, `gpt-6.2-astra-high`:
    > By pinching the hose she let just enough through to keep the brass wet while the sea slipped away under the floor.
    Ada’s independence follows from understanding the library’s tidal mechanism and devising a small, repeatable intervention.
- **C042 — Meaning carried by the object versus meaning annotated in prose:** GPT-6.2 Astra (high) routes its emotional and moral turn through a re-seen physical detail and usually stops before explaining it. GPT-6 Astra (high) builds an equally coherent turn but follows it with a summarizing aphorism that names the lesson. The result is that GPT-6.2 Astra (high) reads as more trusting of the reader and more mature in restraint. GPT-6 Astra (high) reads as clearer but more didactic.
  - Story 0010, `gpt-6.2-astra-high`:
    > She kept the name, but when the council asked which marvels had come through unshaken she pointed not to the survivors but to the strings.
    The required concept is ironized through a concrete gesture. The reader must infer that the people were all shaken.
  - Story 0010, `gpt-6-astra-high`:
    > These were the unshaken marvels: their stubborn differences, their capacity to answer, the pleasure of making something neither silence nor sorrow could make alone.
    The same required concept is defined outright in a colon gloss, so the scene's meaning is stated rather than left to inference.
  - Story 0010, `gpt-6-astra-high`:
    > She had stopped trying to make grief prove that she had loved him.
    The psychological turn is explained as a thesis rather than enacted.
  - Story 0348, `gpt-6-astra-high`:
    > She would no longer sell them certainty.
    This is a typical GPT-6 Astra (high) moral summary following an already clear engineering demonstration.
  - Story 0018, `gpt-6.2-astra-high`:
    > Some mornings they looked and some mornings they just made tea.
    The closing grief is rendered as routine. No lesson is stated.
- **C026 — GPT-6 Astra (high) glosses its meanings; GPT-6.2 Astra (high) lets gestures stand:** This is a recurring-habit claim. All five GPT-6 Astra (high) stories (0058, 0158, 0192, 0323, 0362) use a "not GPT-6 Astra (high) but GPT-6.2 Astra (high)" or "not merely" construction to fix the purpose or lesson, and three of five end on an abstract or aphoristic gloss (0058, 0192, 0323). GPT-6.2 Astra (high) uses similar syntax mainly for literal corrections (0058 "not the trawler but the little blue pilot boat"; 0158 "not in the card but in the dome"). All five GPT-6.2 Astra (high) stories end on an uninterpreted physical act. GPT-6 Astra (high)'s habit is a clear signature, but it constrains the work: it shuts down inference the scenes have already earned.
  - Story 0158, `gpt-6-astra-high`:
    > Mara wanted to photosynthesize pain into beauty, not another reason to sharpen it.
    The thesis-contrast fixes the meaning of the motivation element.
  - Story 0323, `gpt-6-astra-high`:
    > It meant curiosity needed a counterweight, not a smaller appetite.
    The narrator translates the alien's gesture into a moral right away, using the same syntactic frame.
  - Story 0192, `gpt-6-astra-high`:
    > Whenever somebody tightened their grip, somebody else loosened theirs.  They were learning the difference.
    The second sentence states what the first already shows.
  - Story 0362, `gpt-6.2-astra-high`:
    > I had used a ruler and pressed hard enough to score the next six forms, which were for people neither of us knew.
    The ending implies institutional consequence and the narrator's change of allegiance without naming either.
  - Story 0158, `gpt-6.2-astra-high`:
    > She would slip off her own shoes then, and let her bare heels knock against the desk for luck.
    The emotional resolution is a callback to the mother's cold feet, left unexplained.
- **C034 — Codas that enact meaning versus codas that state it:** In the clearest matched contrasts, GPT-6.2 Astra (high) trusts a resumed practice or exact attribution to carry the emotional conclusion. GPT-6 Astra (high) more often supplies a conceptual paraphrase of the required idea before its final gesture. GPT-6.2 Astra (high) therefore creates a stronger impression of selective control and leaves slightly more work to the reader, though GPT-6 Astra (high)’s explicitness can also protect ethical precision.
  - Story 0221, `gpt-6.2-astra-high`:
    > South, I said, and felt her elbow come up against mine as she reached for the pencil.
    The old family practice resumes without a definition of true north or belonging. “South,” the elbow, and the pencil jointly turn survival into a possible future voyage.
  - Story 0221, `gpt-6-astra-high`:
    > For the first time since her rescue, confusion suggested a place to begin instead of a reason to run.
    The story directly converts the motivation into its thematic formulation. The ensuing question to Ada dramatizes that change, but the interpretation has already been stated.
  - Story 0289, `gpt-6.2-astra-high`:
    > "My father found that," she would say, and then, sometimes, "My mother kept it."
    The optional second attribution quietly repairs the parents’ collaborative history and the narrator’s place in it. No general statement about connection is needed.
  - Story 0289, `gpt-6-astra-high`:
    > Mara had found no thread that connected everything.  She had learned to leave an end for someone else to hold.
    The final antithesis explicitly explains the nest, cotton, and reconciliation. It is elegant and clear, but closes more of the interpretive space than GPT-6.2 Astra (high)’s attribution.
- **C030 — Naming the tone versus embodying it:** When a brief specifies an oxymoronic tone, GPT-6 Astra (high) tends to state the tonal phrase in the narration and define it. GPT-6.2 Astra (high) renders it through image or situation. This changes how the "truthful lies" and "reef-shadow joy" briefs feel: GPT-6 Astra (high)'s are discussed, GPT-6.2 Astra (high)'s are performed.
  - Story 0158, `gpt-6-astra-high`:
    > Their laughter had a reef-shadow joy: bright movement under the weight of something that could still crush them.
    The tone element is inserted and then glossed after a colon.
  - Story 0362, `gpt-6-astra-high`:
    > Behind her, Lena whispered that she had loved her husband.  That was true, and the way she offered it was a lie.
    "Truthful lies" is stated as a paradox rather than staged.
  - Story 0158, `gpt-6.2-astra-high`:
    > Nell tried the one about the crab that pawned its trousers for a ride on a jellyfish.  She got as far as the price of the ticket before a thin indignant voice corrected the fare.
    Joy under the shadow of loss is carried by an absurd lullaby and a mother's identity proven through pedantry.
  - Story 0362, `gpt-6.2-astra-high`:
    > I told her I had drawn a line through the space, which was true as far as it went.
    A truthful lie is enacted in a small narrative act rather than named.
- **C024 — Split modal and tonal range: GPT-6.2 Astra (high)'s enacted register shifts versus GPT-6 Astra (high)'s mythic span, comic stretch, and coercive edge:** Neither writer dominates every dimension of tonal and modal range. Writer GPT-6.2 Astra (high) modulates more organically between hushed elegy (0261) and folk comedy (0194, 0389) and dramatizes requested tones like demure audacity in scene, whereas GPT-6 Astra (high) once resorts to naming that tone directly (0387). Conversely, GPT-6 Astra (high) stretches across a wider realism-to-mythic/steampunk spectrum (0387, 0393), achieves dry comedy when cued in 0389, and sustains unsoftened resentment in 0393 where GPT-6.2 Astra (high) remains genial.
  - Story 0261, `gpt-6.2-astra-high`:
    > Below us the harbor was beginning to stir, but up in the quiet tower at dawn you could have heard a cinder settle.  A meteor went soundlessly down the last strip of night between the cranes.
    Shows GPT-6.2 Astra (high)'s quietest pole: stripping away the brisk social comedy of 0194 and 0389 to achieve a hushed, restrained dawn atmosphere.
  - Story 0387, `gpt-6.2-astra-high`:
    > "May I trouble you for my usual place a little later?" I called up, as if I had reserved a table at an inn.  My aunt, who could spot insolence at fifty paces, took the whisk from her sash and bowed.
    Enacts the prompt's demure audacity purely through courteous backtalk and physical gesture without ever pasting the prompt's tone label into the prose.
  - Story 0387, `gpt-6-astra-high`:
    > Then, with the demure audacity that usually preceded his least popular questions, he invited the mayor down the slippery steps.
    Shows a register collapse in GPT-6 Astra (high): because 0387 GPT-6 Astra (high) defaults to earnest solemnity, demure audacity is asserted via authorial label rather than felt in the prose rhythm.
  - Story 0387, `gpt-6-astra-high`:
    > Below the parapet, his mother knelt on a maintenance ledge, whisking a basin of river water.  Fireflies settled on the bamboo tines, and each circular stroke gathered their reflections into pale froth.  She drew this into filaments and looped them around the bridge's fraying edge.
    Demonstrates GPT-6 Astra (high)'s imaginative reach into lyrical magical realism—spinning structural threads from firefly reflections—where GPT-6.2 Astra (high) keeps 0387 strictly naturalistic.
  - Story 0389, `gpt-6-astra-high`:
    > In the stormlit observatory above clouds, Mera kept three potatoes, a brass telescope, and a grudge against the weather.
    Proves GPT-6 Astra (high) can adapt to witty, deadpan comedy when explicitly invited by gritty whimsy, contrasting sharply with GPT-6 Astra (high)'s elegiac gravity in 0261 and 0393.
  - Story 0393, `gpt-6-astra-high`:
    > Outside, the guard knocked; inside, she waited for Silas to button his own shirt before offering her arm.  He accepted it without forgiving her, and she adjusted her stride to his.
    Reaches a register of unhealed moral friction and institutional severity that GPT-6.2 Astra (high) never enters in this packet.
- **C028 — GPT-6.2 Astra (high)'s dry deflation and ironic handling of prompt jargon:** This is a recurring-habit claim. In four of five GPT-6.2 Astra (high) stories (0058, 0158, 0323, 0362), a colloquial, faintly comic undercut punctures the lyric or required abstraction. 0192 is the examined exception. GPT-6.2 Astra (high) often frames the prompt's jargon as a quoted coinage or official label. This is a useful signature, since it inoculates against preciousness. It also risks treating some elements as jokes rather than material.
  - Story 0158, `gpt-6.2-astra-high`:
    > for years she had gone there to photosynthesize pain into beauty, as she had put it in her first, regrettably published book.  Tonight beauty could go soak its head.
    The required motivation is cited as an embarrassing phrase and then dismissed in plain idiom.
  - Story 0323, `gpt-6.2-astra-high`:
    > As navigation instructor I had to put something under Temperament, so I wrote "balancedly curious," the highest mark in our quaint municipal vocabulary.
    The required attribute is housed in a form-field and gently mocked.
  - Story 0058, `gpt-6.2-astra-high`:
    > "Tried to get the knot undone with his teeth, because I was turning purple."
    Comic physicality undercuts a deathbed revelation without cheapening it.
- **C050 — Aphoristic versus gestural closure:** GPT-6 Astra (high) repeatedly adds a late interpretive distillation, often built around a contrast or corrected definition. GPT-6.2 Astra (high) more often lets a final material or social gesture imply the change. GPT-6 Astra (high)’s signature provides clarity and memorability but can narrow the reader’s interpretive work; GPT-6.2 Astra (high)’s restraint preserves resonance but can itself become a carefully composed closing formula.
  - Story 0137, `gpt-6-astra-high`:
    > Not forgetfulness, but somewhere to stand beside remembering.
    This compactly names the memorial’s purpose and the story’s rejection of erasure. It is effective conceptual phrasing, but it follows scenes that had already dramatized the distinction.
  - Story 0294, `gpt-6-astra-high`:
    > He was learning the difference between a road that brought people back and one that would not let them leave.
    The final sentence explicitly converts the startup plot into a general distinction between return and captivity. Similar corrective formulations recur elsewhere in GPT-6 Astra (high), making this a habit rather than an isolated flourish.
  - Story 0216, `gpt-6.2-astra-high`:
    > On the road out of town I kept finding it among my change, and each time I took a little longer to let it go.
    The chip’s renewed presence among coins makes time tactile without defining a final lesson. The lengthening hesitation leaves attachment and release in motion.
  - Story 0296, `gpt-6.2-astra-high`:
    > There were mothers on both banks now, holding nails for her to start from, and not one of them asked her to find a ring.
    The changed requests and shared search tools show Siv’s altered social role. Accountability and collective mourning are conveyed through resumed work rather than a statement about what serenity or guilt means.
- **C062 — Embodied endings as a flexible signature:** GPT-6.2 Astra (high) repeatedly ends by letting an object or bodily action carry the final emotional change. The gesture varies in meaning—delayed release, accepted care, and restored recognition—so recurrence alone does not make it a template. GPT-6 Astra (high) more often closes on a principle or practical project, but neither closing mode is inherently deeper.
  - Story 0216, `gpt-6.2-astra-high`:
    > On the road out of town I kept finding it among my change, and each time I took a little longer to let it go.
    The repeated physical discovery makes grief incremental and unfinished. The story does not claim that the narrator has learned to let go; it measures a small change in delay.
  - Story 0333, `gpt-6.2-astra-high`:
    > Once he brought scissors, good ones, and I bent my head and let a stranger make the two sides even.
    The haircut completes the son’s interrupted act without pretending to recover him. It also accepts the locksmith’s care while leaving his own history unexplained.
  - Story 0349, `gpt-6.2-astra-high`:
    > Out among the glass trunks he took her hand without looking, and this time she knew whose it was.
    A repeated handhold becomes recognition rather than exposition. The gesture returns Ada to a particular relationship and child after the evidence has established the hidden passengers.
  - Story 0258, `gpt-6-astra-high`:
    > Her grandmother had not left her a way to predict which doors would close.  She had left her the work of keeping more than one open.
    This contrasting GPT-6 Astra (high) closure converts the inherited deck into a stated duty. Its antithesis is lucid and memorable but more fully interprets the ending than GPT-6.2 Astra (high)’s gestures do.
- **C018 — Endings design repeatable futures rather than merely reveal truths:** Both writers turn recovered knowledge into arrangements other people can use. GPT-6 Astra (high) tends to encode a moral discovery into shared procedures and additional hands; GPT-6.2 Astra (high) tends to adjust ordinary buildings and schedules so that chosen contact and independent movement become possible. This shared constructive impulse is more fundamental than their surface differences in explicitness.
  - Story 0023, `gpt-6-astra-high`:
    > Instead she asked for paper.  She drew the road they had crossed, including the bend where the censer foot remained, with the moon phase and the hours of safe passage.
    Mara’s private loss becomes transferable navigation knowledge, including the location of what she could not recover.
  - Story 0288, `gpt-6-astra-high`:
    > She would invite him before opening the next tank.  There would have to be more thylacines, and more hands, and room for each to go.
    The solution expands beyond solitary competence into shared work and institutionalized permission for animals to leave.
  - Story 0288, `gpt-6.2-astra-high`:
    > Ada had drawn it herself, down to the little arc that showed which way the door between the rooms would swing.
    Autonomy is embodied in a buildable design that joins solitude and public contact rather than treating them as opposites.
  - Story 0396, `gpt-6.2-astra-high`:
    > She laid the fragment in his palm with the shop caught whole inside it, right down to the fare in the wooden hand.  "Put back the ferry house we had that Saturday," she said, and stepped aside so her brother could see the plan without having to ask.
    The recovered anomaly becomes a repeatable accessible landing, and Ada’s final movement ensures that her brother can inspect the arrangement himself.
- **C057 — Wider range in point of view, comic-tender friction, and register:** Across the five prompts, Writer GPT-6.2 Astra (high) adapts narrative voice, point of view, humor, and ontological framing to match each requested tone, whereas Writer GPT-6 Astra (high) maintains a single earnest, close third-person register throughout (5/5 third-person in GPT-6 Astra (high) vs 2/5 first-person and 3/5 third-person in GPT-6.2 Astra (high)). GPT-6.2 Astra (high)'s range spans deadpan marital comedy narrated in the first person by the disappearing whale-island itself in 0252 ("combative tenderness"), hushed third-person liturgical minimalism in 0012 ("muffled clarity"), and folksy tall-tale cadence in 0276 ("feral lullaby"). GPT-6 Astra (high) handles somber mythic tension well in 0276, but in 0252 renders "combative tenderness" through earnest mother-daughter anguish rather than tonal play, and in 0012 lets "muffled clarity" open in felt-wrapped quiet before collapsing back into a public assembly speech where thirty citizens march into a chalk circle.
  - Story 0252, `gpt-6.2-astra-high`:
    > When I rolled my eye toward daylight I saw the little dark bottoms of the barges, and one small shower of peas came pelting down.  That was my wife all over, to hear the first song I had sung in centuries and throw vegetables.
    Demonstrates first-person comic timing, bold nonhuman POV, and genuine "combative tenderness" in which unsentimental friction expresses love.
  - Story 0012, `gpt-6.2-astra-high`:
    > When Bell cut the names, what he heard in the unraveled stillness was one girl breathing hard and one woman trying to set a paintbrush down.
    Drops all tall-tale humor for spare, quiet chamber intimacy suited to "muffled clarity," keeping the conflict private among three family members.
  - Story 0276, `gpt-6.2-astra-high`:
    > Until the railway went through, the sleepwalking constellations used to come down to drink and go home with mud on their paws.  Nobody minded a little mud falling out of the sky.
    Shifts again into confident mythic-folktale storytelling, treating cosmic beasts with matter-of-fact rural familiarity.
  - Story 0012, `gpt-6-astra-high`:
    > The waiting families recoiled from Mara's upright shadow, but he showed them the inscription under the pedal.  "We made the anchor to hold our lives, not our lives to hold the anchor."
    Illustrates register collapse in GPT-6 Astra (high): a prompt requesting "muffled clarity" escalates into public oratorical persuasion and collective civic action.
- **C040 — Demonstrated range in POV, deadpan humor, and social resolution shapes:** Writer GPT-6.2 Astra (high) adapts voice, emotional register, and ending choreography more flexibly across the packet: GPT-6.2 Astra (high) adopts a brisk first-person commercial voice in 0127 versus close third-person elsewhere, threads dry vernacular humor through grave premises without undercutting pathos, and lands on markedly different social endings (archival secret-keeping in 0056, culinary comedy in 0101, funeral quiet in 0127, noon street-dancing in 0290, tense evacuation in 0354). Writer GPT-6 Astra (high) stays in third-person limited across all 5/5 stories with a uniform earnestness in 4/5, displaying sharp ironic range mainly in 0127 when explicitly cued.
  - Story 0127, `gpt-6.2-astra-high`:
    > On the evening the town meant to bottle my sister's courage, her son came to my stall to buy her some.  You could buy almost anything from me except a feeling you had actually felt, which was generally cheaper to get at home.
    GPT-6.2 Astra (high) pivots into a worldly, unsentimental first-person shopkeeper monologue whose dry commercial wit immediately establishes "affectionate detachment" while setting up family tragedy.
  - Story 0056, `gpt-6.2-astra-high`:
    > "I'd rather have the privy," he told the operator, with such dignity that nobody on the working channel laughed.
    GPT-6.2 Astra (high) extracts dignified working-class comedy from an orphan boat's cabin turning out to be "a privy with a desk in it," fusing humor with deep archival tenderness.
  - Story 0290, `gpt-6.2-astra-high`:
    > The surveyors wired the capital to report a spatial mutiny and asked for instructions on how to arrest a crossroads.
    GPT-6.2 Astra (high) turns a high-concept prompt phrase into deadpan bureaucratic satire inside a jubilant, carnivalesque parish ending—worlds apart in mood from 0127's memorial hush.
  - Story 0101, `gpt-6.2-astra-high`:
    > Ada waited until the last bowl was full to declare the school open, and somebody asked whether scraping the skillet would count toward graduation.
    Even under wartime sanctions, GPT-6.2 Astra (high) resolves communal estrangement through warm, teasing kitchen banter rather than solemn parliamentary procedure.
  - Story 0127, `gpt-6-astra-high`:
    > Inside the translucent walls, the preserved advised their descendants on marriages, drainage, and the proper storage of pears.  They never said they were lonely.  That omission had always struck Leda as excellent customer service.
    Demonstrates that GPT-6 Astra (high) can achieve crisp, dryly comic detachment when the prompt explicitly requests it, making GPT-6 Astra (high)'s collapse back into uniform solemnity across the other four stories a default preference rather than sheer inability.
- **C044 — GPT-6 Astra (high)'s Mara template: dead kin, young female witness, published error:** GPT-6 Astra (high) reuses one narrative template across briefs, and it goes well beyond the prompts:
- The protagonist is Mara in 5/5 stories (0010, 0018, 0348, 0349, 0388).
- A dead brother appears in 3/5 (0010, 0018, 0348; checked nonmatches 0349 and 0388).
- A girl or daughter supplies the decisive insight in 4/5 (0018, 0348, 0349, 0388).
- The protagonist diagnoses herself with "mistaken/mistook" (0348, 0349, 0388).
- In two stories the closing amends use near-identical syntax.

The template makes GPT-6 Astra (high)'s emotional architecture predictable even when its settings are inventive.
  - Story 0348, `gpt-6-astra-high`:
    > She paid for the tests and published the old calculations with her own mistaken assumptions underlined.
    This is the public-error-marking closing move.
  - Story 0388, `gpt-6-astra-high`:
    > She transmitted the evidence with her old report attached and her own errors marked.
    It repeats the same move with parallel syntax: old document, own errors, marked or underlined.
  - Story 0349, `gpt-6-astra-high`:
    > She had mistaken her own relief for Ada's.
    This is one instance of the recurring "mistaken GPT-6.2 Astra (high) for GPT-6 Astra (high)" self-diagnosis.
  - Story 0388, `gpt-6-astra-high`:
    > She had mistaken his refusal to answer interrogators for an inability to answer them.
    The same syntactic frame appears in a different brief.
  - Story 0010, `gpt-6-astra-high`:
    > Mara had survived its capsize; her younger brother, asleep belowdecks when the storm struck, had never heard an alarm.
    The dead brother as grief engine appears here.
  - Story 0348, `gpt-6-astra-high`:
    > Her brother Daniel, crossing home after a night shift, had gone downstream with the deck.
    The dead brother recurs in an unrelated brief with no prompted kinship element.
- **C008 — GPT-6 Astra (high)'s repeated grief-shame-civic-choice template:** GPT-6 Astra (high) reuses a protagonist name, a backstory trigger and a moral beat sequence across briefs. The protagonist is called Mara in four of five stories (0086, 0142, 0191, 0285; checked nonmatch: 0330, Elias). A family member was killed by fire or water in three of five (0086, 0191, 0285; nonmatches: 0142, where the son was burned but survived, and 0330). An explicit shame or self-reproach beat precedes the right choice in four of five (0086, 0142, 0191, 0285; 0330 has only "For years he had accepted theirs"). Corrective "not GPT-6.2 Astra (high)" formulations appear in all five checked stories. Together these make different briefs resolve along one arc. GPT-6.2 Astra (high)'s names, backstories and resolution types do not repeat this way.
  - Story 0086, `gpt-6-astra-high`:
    > Mara hated herself for imagining that ordinary kitchen while her father's house burned again behind her eyes.
    Shows the Mara name, the self-reproach beat and the parent killed by fire.
  - Story 0191, `gpt-6-astra-high`:
    > For one shameful moment, she wanted the machine to agree.
    The same shame-before-virtue beat, again with Mara, whose mother was killed in a flood.
  - Story 0285, `gpt-6-astra-high`:
    > Iven felt relief before shame.
    The same beat in compressed syntax; here Mara is the daughter and her mother drowned.
  - Story 0142, `gpt-6-astra-high`:
    > The clerk stamped the postponement, not an approval: they had thirty days to prove their promises would float.
    An instance of the recurring "GPT-6.2 Astra (high), not GPT-6 Astra (high)" corrective cadence, which also appears as "directions, not assurances" (191) and "Not permission" (285).
- **C038 — GPT-6 Astra (high)'s recurring Mara cast, binary syntax, and civic-redistribution template:** Checked across all five stories, Writer GPT-6 Astra (high) relies heavily on stock naming, binary epigrammatic syntax, and a single political-parable engine. GPT-6 Astra (high) names a central figure Mara in 4/5 stories (0056, 0101, 0290, 0354; nonmatch: 0127) and Tomas in 2/5 (0101, 0290; nonmatches: 0056, 0127, 0354), deploys symmetrical "not GPT-6 Astra (high), [merely/but] GPT-6.2 Astra (high)" or semicolon-contrast theses in 5/5 (0/5 moral-thesis binaries in GPT-6.2 Astra (high)), turns 4/5 briefs into elite/generational hoarding rectified by public redistribution (0056, 0101, 0290, 0354), and ends 5/5 by explicitly refusing easy emotional sweetness. This template makes disparate prompts converge on substantially the same civic lesson.
  - Story 0056, `gpt-6-astra-high`:
    > Ansel had saved his pension, the directors their money, and Mara a father whose failure seemed comprehensible.  She could not restore the drowned by trading one convenient monster for another.
    Introduces Mara (1 of 4), balanced parallel clauses auditing institutional guilt, and GPT-6 Astra (high)'s signature explicit warning against comforting moral simplification.
  - Story 0101, `gpt-6-astra-high`:
    > Then she declared the relief kitchen common property, with an equal vote for every member, regardless of age.  Tomas rose slowly, and Mara braced for his objection.
    Pairs Mara (2 of 4) with Tomas (1 of 2) and resolves an interpersonal exile story through formal constitutional governance and voting reform.
  - Story 0354, `gpt-6-astra-high`:
    > Mara wrote while Iven counted, her pencil trembling as the dent approached red.  The covenant was not merely a document; it was the nexus's original distribution program, awaiting renewal at each great reversal.  Its instruction was simple: disconnect the palace reserve.
    Combines Mara (4 of 4, following 0290), "not merely GPT-6 Astra (high); it was GPT-6.2 Astra (high)" semicolon antithesis, and elite infrastructural hoarding solved by redistributing palace surplus.
  - Story 0127, `gpt-6-astra-high`:
    > The grotto had not conquered loneliness; it had learned to exclude whatever made loneliness intelligible.
    Even in the lone non-Mara story (0127), GPT-6 Astra (high) diagnoses the conflict through the exact same semicolon-balanced negative-to-positive conceptual thesis.
- **C055 — GPT-6 Astra (high)'s guilt-and-governance template versus GPT-6.2 Astra (high)'s circular object endings:** Examined across all five stories (N=5: 0007, 0012, 0252, 0258, 0276), Writer GPT-6 Astra (high) relies on a recurring multi-part narrative and syntactic template that makes disparate prompts converge on a similar civic-stewardship story. First, GPT-6 Astra (high) names a central woman Mara in 3/5 stories (0007, 0012, 0258; nonmatches 0252, 0276) and Nera in the remaining 2/5 (0252, 0276; nonmatches 0007, 0012, 0258), vs GPT-6.2 Astra (high) using Mara in 1/5 (0007) and reusing Nell in 2/5 (0258, 0276; nonmatches 0007, 0012, 0252). Second, in 3/5 stories (0007, 0012, 0258; nonmatches 0252, 0276), GPT-6 Astra (high) introduces early exposition making the protagonist previously complicit in the harmful law, nomination, or network now resisted (whereas GPT-6.2 Astra (high)'s rule-making or land-selling protagonists in 2/5—0012, 0276; nonmatches 0007, 0252, 0258—either discover the flaw at the climax or remain wryly unrepentant). Third, GPT-6 Astra (high) uses narrator-voiced corrective binary antitheses ("not GPT-6.2 Astra (high), but/only GPT-6 Astra (high)") in 5/5 stories (0/5 as abstract narrator maxims in GPT-6.2 Astra (high)) and ends 3/5 stories (0007, 0012, 0258; nonmatches 0252, 0276) on sober ongoing-work codas, with 0007 and 0012 repeating the exact "they would need [three-item administrative list]" structure. By contrast, GPT-6.2 Astra (high) closes 4/5 stories (0007, 0252, 0258, 0276; partial nonmatch 0012) by silently returning to an opening-paragraph physical detail to register transformation without commentary.
  - Story 0007, `gpt-6-astra-high`:
    > Now she wanted something beautiful from the ruins, which seemed a poor defense against a law she had helped write.
    Establishes GPT-6 Astra (high)'s unprompted complicit-protagonist setup (Mara signed the tree-ban petition), parallel to Ivo nominating Mara in 0012 and Mara designing fragile payment rails in 0258.
  - Story 0007, `gpt-6-astra-high`:
    > Before dawn they would need a proper root box, drainage trays, and a schedule of inspections neither could quietly abandon.
    First instance of GPT-6 Astra (high)'s administrative-aftermath coda, listing three logistical governance tasks to qualify the resolution.
  - Story 0012, `gpt-6-astra-high`:
    > They would need a roster, arguments, replacements; no clever sentence could abolish the work of holding a city.
    Repeats nearly word-for-word the syntax and anti-utopian administrative disclaimer of 0007 GPT-6 Astra (high) across a completely unrelated prompt.
  - Story 0258, `gpt-6-astra-high`:
    > This was not a map of where customs belonged, but of how they traveled when belonging became dangerous.
    Exemplifies GPT-6 Astra (high)'s 5/5 habit of phrasing conceptual discoveries as balanced "not GPT-6.2 Astra (high), but GPT-6 Astra (high)" narrator aphorisms, alongside Mara's third appearance.
  - Story 0276, `gpt-6-astra-high`:
    > In the sound wave garden, where drowned railway tracks fed beds of trembling music, Nera fished for echoes instead of cod.
    Shows GPT-6 Astra (high)'s complementary Nera naming (shared with 0252) in a story that otherwise escapes GPT-6 Astra (high)'s complicity-and-committee template.
  - Story 0007, `gpt-6.2-astra-high`:
    > When the first rang over Mara's kitchen door, Lev got up without being told and washed his hands for dinner.
    Instead of summarizing ongoing stewardship, GPT-6.2 Astra (high) loops back to paragraph one's cracked dinner bell to show dementia-stricken Lev responding intact.
  - Story 0276, `gpt-6.2-astra-high`:
    > When she got home her father was asleep under his good roof, one crooked hand open on the quilt.  A little mud had come in through the window.
    Second example of GPT-6.2 Astra (high)'s 4/5 silent circular ending: sky-mud on the windowsill proves the sleepwalking constellations returned safely to their paths.
- **C004 — Shared stock-name defaults alongside GPT-6.2 Astra (high)'s bereavement backstories and tactile handoff endings:** Exhaustive check of all 5/5 stories shows that neither writer is free of unprompted narrative defaults. Both recycle stock female names across unrelated briefs—GPT-6 Astra (high) uses "Mara" for 3/5 protagonists (0125, 0218, 0256; nonmatches: 0065 Iona, 0206 Pip with daughter Ada), while GPT-6.2 Astra (high) uses "Ada" for 2/5 protagonists and 2/3 of its third-person stories (0218, 0256; nonmatches: 0065 Nell, unnamed first-person narrators in 0125 and 0206). Furthermore, GPT-6.2 Astra (high) imports an unprompted deceased immediate relative into 4/5 stories (0125 sister, 0206 mother, 0218 mother, 0256 father; nonmatch: 0065, versus 1/5 in GPT-6 Astra (high) at 0206) and ends 5/5 stories (0065, 0125, 0206, 0218, 0256) on a quiet physical hand-or-tool gesture between characters. While GPT-6.2 Astra (high)'s closing habit strengthens emotional restraint, its reliance on family bereavement is a genuine recurring crutch.
  - Story 0218, `gpt-6-astra-high`:
    > After the physician gave her six months to live, Mara returned to her island and canceled the order for whitewash.
    GPT-6 Astra (high) defaults to the protagonist name "Mara" for the dying island caretaker, matching its roadside poet in 0125.
  - Story 0256, `gpt-6-astra-high`:
    > After the power grid stabilizes, the laboratory of lost sounds sends for Mara, the city's last prism-song bell ringer.
    GPT-6 Astra (high) repeats "Mara" a third time in 0256, paired again with its signature fronted temporal clause and occupational appositive.
  - Story 0218, `gpt-6.2-astra-high`:
    > Ada had finished closing that vault the summer her mother was buried in a wet dress.  She had received a medal for it.
    On 0218, GPT-6.2 Astra (high) names its caretaker "Ada" and adds an unprompted dead-mother backstory on top of the prompt's terminal diagnosis to motivate the closed oak canopy.
  - Story 0256, `gpt-6.2-astra-high`:
    > After the power grid stabilized, the first thing Ada lit in the laboratory of lost sounds was the carbide lamp her father had carried underground.
    On 0256, GPT-6.2 Astra (high) reuses "Ada" as protagonist—mirroring GPT-6 Astra (high)'s "Mara" reuse across the exact same two prompts—and again makes the parent deceased (unlike GPT-6 Astra (high)'s living father in 0256).
  - Story 0206, `gpt-6.2-astra-high`:
    > I hit it wrong twice and started to flatten the dents, but he laid two fingers on my hammer.
    >
    > "Couldn't we hear it first?" he said.
    Illustrates GPT-6.2 Astra (high)'s 5/5 closing signature: halting at a small, physical touch on a shared tool rather than appending narrator commentary.
  - Story 0218, `gpt-6.2-astra-high`:
    > Afterward the boy started to chalk arrows on the floor for the next funeral, but the widower took the chalk from him.  His hand shook a little as he knelt, still in his good trousers, to mark the first turn.
    A second distinct story confirming GPT-6.2 Astra (high)'s closing template of a tactile tool-handoff—here passing chalk to a bereaved bystander—parallel to stitching Hen's brother's name (0065), feeding pie crust (0125), and knocking on the rail (0256).
- **C021 — Writer GPT-6 Astra (high)'s Mara/Mera/Mere naming tic, signed-record endings, and sage epigrams:** Checked across all five stories, Writer GPT-6 Astra (high) relies on three unprompted habits that make disparate worlds converge: a Mara/Mera/Mere proper-name cluster in 4/5 stories (0194, 0387, 0389, 0393; nonmatch 0261 has no proper names), signed documentary or roster restitution in 3/5 stories (0194, 0387, 0393; nonmatches 0261, 0389), and balanced maxims in 5/5 stories. Writer GPT-6.2 Astra (high) avoids name recycling and treats paperwork with skepticism.
  - Story 0194, `gpt-6-astra-high`:
    > Mara herself had nominated him, grateful for the money he had given the rebellion.
    Establishes both the recurring female protagonist name Mara (shared with 0393 and echoed in 0389 Mera and 0387 Mere) and GPT-6 Astra (high)'s complicity setup.
  - Story 0194, `gpt-6-astra-high`:
    > There would be a hearing, with witnesses and public accounts, not another scaffold hastily built beneath a cheering crowd.  On the first page she wrote that she had appointed him, and signed her name.
    First instance of GPT-6 Astra (high)'s documentary-accountability resolution: rejecting mob spectacle by creating a public record and signing her own name to her fault.
  - Story 0387, `gpt-6-astra-high`:
    > During firefly season, moonlight hardened into narrow bridges between Mere and the island where its dead were buried.
    Extends the M-r- naming habit even when the protagonist is male (Iven), shifting the phonetic stem onto the town of Mere.
  - Story 0387, `gpt-6-astra-high`:
    > "A roster would be kinder."
    >
    > Iven unfolded his speech against the parapet and ruled columns across its blank reverse.  He wrote his own name beside the longest watch, then waited without offering anyone the shelter of another beautiful sentence.
    Second instance of GPT-6 Astra (high)'s signed-document climax, pairing a crisp six-word rebuke of ceremony with ruling a schedule and signing the protagonist's name first.
  - Story 0389, `gpt-6-astra-high`:
    > "The hinges remember, and the dark will open."  He meant that people should oil the mechanisms; people preferred to kneel.  From her mountain, Mera listened as gratitude acquired marching boots.
    Combines the protagonist name Mera with GPT-6 Astra (high)'s signature semicolon antithesis, compressing complex social drift into polished authorial epigram.
  - Story 0393, `gpt-6-astra-high`:
    > "The physician listened twice," Mara said, as Fen opened the inspection hatch.
    >
    > "Second opinions are not echoes, Chaplain."
    Repeats the name Mara (Chaplain Mara Vale) and gives the repairer the exact same clipped, aphoristic mentor cadence heard in 0261 and 0387.
  - Story 0393, `gpt-6-astra-high`:
    > Instead, she dated a fresh page and described exactly how her endorsement had helped put a sick man in solitary.  She would take it to the visiting magistrate and request independent examinations, with the findings entered into the public record.
    Third instance of GPT-6 Astra (high)'s written-accountability resolution: converting an empty apology into a dated self-incriminating page for open court and taking Silas off the quarry roster.
  - Story 0194, `gpt-6.2-astra-high`:
    > She might even have found a receipt, and somebody's grandson might have gone to prison, and in the morning Molly would still have had to stand here in white stockings.
    Direct contrast on the same prompt: GPT-6.2 Astra (high) explicitly rejects documentary exposure as insufficient to free a child from an oppressive ritual.
  - Story 0393, `gpt-6.2-astra-high`:
    > Ellis wound the man's little walnut theatre, and I kept my pencil in my pocket and let him come into the room to his own music.
    Direct contrast on 0393: whereas GPT-6 Astra (high) validates reform by writing in a notebook, GPT-6.2 Astra (high) marks reform by putting the evaluator's pencil away and sharing the room.
- **C036 — Subtextual behavioral perception versus stated moral theses:** Writer GPT-6.2 Astra (high) generates psychological and ethical insight through oblique action, social micro-observation, and deliberate silence, trusting the reader to infer the emotional stakes. Writer GPT-6 Astra (high) habitually translates its emotional and conceptual turns into explicit, summary thesis statements spoken by characters or the narrator.
  - Story 0127, `gpt-6.2-astra-high`:
    > She stood quite still until the charge died.  "I had that," she said, "when mine came out the first time."  She did not say anything about the second time, and the boy, who had learned something about the uses of silence, did not ask.
    Instead of naming empathy, GPT-6.2 Astra (high) dramatizes shared bereavement through what goes unsaid: the dead apprentice's mother recognizes the exact flash of relief she felt before her own daughter ran back in and died.
  - Story 0127, `gpt-6-astra-high`:
    > She wanted, suddenly and specifically, to understand her mother without improving her.  Reading fear was insight; allowing it to matter might be something nearer empathy.
    Faced with the same prompt motivation, GPT-6 Astra (high) defines "insight" and "empathy" directly in a neat, analytical narrator aphorism rather than letting the scene imply the distinction.
  - Story 0101, `gpt-6.2-astra-high`:
    > "Not with what they throw you," the old woman said, and took his thumb and guided it to the seam where he could get two good cheeks off every head.
    Intergenerational reconciliation happens entirely through gruff practical craft and physical touch after tasting a boy's onion stew, with no speechifying about solidarity.
  - Story 0101, `gpt-6-astra-high`:
    > "The gift is anonymous, not ownerless," she said.  "Ask him what he needs before you ask what he owes."
    GPT-6 Astra (high) resolves generational pride by having Mara deliver a polished, symmetrical moral maxim that instructs the elder how to feel and act.
- **C027 — GPT-6 Astra (high)'s complicity-and-release template and stock names:** This is a recurring-habit claim. Across GPT-6 Astra (high)'s stories the protagonist recognizes that they reproduce the harm they oppose (0058, 0158, 0192, 0323; 0362 shifts it to the magistrate). They then give up control, and repair becomes shared (0058 "Together we began a letter," 0158, 0192, 0323). The pattern is morally intelligent, but different briefs end up with the same story arc. The name Mara appears in 3/5 GPT-6 Astra (high) stories (0058, 0158, 0362) for unrelated roles; 0192 (Edda) and 0323 (unnamed) are examined nonmatches. Absent or estranged wives recur in 0058 and 0158. GPT-6.2 Astra (high) has no repeated names in this packet.
  - Story 0058, `gpt-6-astra-high`:
    > For years, I had written her departure as cruelty, revising every detail except my own.
    The helper discovers his own blind complicity.
  - Story 0192, `gpt-6-astra-high`:
    > The owners had governed their workers by linking through scars, making damaged flesh remember whose rhythm it must follow.  Her shelter had become another hand around twelve throats.
    The same turn appears in a different setting: the protector has become the oppressor.
  - Story 0323, `gpt-6-astra-high`:
    > I resented the lesson until I caught myself promising my pupils that the new charts would be infallible.  My mother had trusted an instrument like that.
    The same self-recognition beat appears in science fiction, again followed by giving up certainty.
  - Story 0158, `gpt-6-astra-high`:
    > Mara, an insomniac poet, had written both sides' marching songs, changing only the names of the villains.
    A second Mara is again complicit in the harm she later undoes.
- **C051 — A shared close-kin template:** Checked across the packet, close-kin loss, separation, or inheritance supplies the emotional warrant in 5/5 stories for GPT-6 Astra (high) and 5/5 for GPT-6.2 Astra (high). The matching IDs for both are 0137, 0216, 0294, 0296, and 0333; there are no examined nonmatches under this broad definition. The category includes inheritance in 0294 and separation rather than confirmed bereavement in GPT-6.2 Astra (high)’s 0333. This packet-local recurrence gives objects intimate histories, but also repeatedly channels public or cosmic problems through family relationships.
  - Story 0216, `gpt-6-astra-high`:
    > Mother had designed the capsule, then died before its dedication.
    The town’s temporal catastrophe becomes an opportunity to reinterpret the narrator’s mother and her preserved grief, making family inheritance the route into the speculative problem.
  - Story 0294, `gpt-6-astra-high`:
    > Elias inherited two things from his father: a collection of foreign paper money and a polished calm that made people trust him.
    This shows why the broader category is necessary: the story is not primarily bereavement, but paternal inheritance supplies both the object and the moral danger reproduced by the startup.
  - Story 0216, `gpt-6.2-astra-high`:
    > I knew the game, though I hadn't played since my brother died.
    The sale-description method enters through a discontinued family game, and the brother’s death links the message system, urn fragment, father’s labor archive, and narrator’s changing sense of time.
  - Story 0296, `gpt-6.2-astra-high`:
    > She had never offered to find her son.
    Siv’s guarded history with Vale personalizes the military inquiry before the story expands toward other bereaved families. Kinship is the entry point even though the conclusion becomes collective.
- **C023 — Structural, perspectival, and conflict-engine adaptability across prompts:** Writer GPT-6.2 Astra (high) reshapes point of view, character positioning, and core conflict architecture to fit each brief—alternating first and third person, decentering headline roles into relational witnesses in 0387 and 0393, and writing villain-free family stories alongside communal comedies. Writer GPT-6 Astra (high) keeps 4/5 stories in third-person titular POV and converts all 5/5 prompts into variations of one anti-extractive accountability plot.
  - Story 0261, `gpt-6.2-astra-high`:
    > "Because you would have gone looking for a woman who had already done the hardest thing you can ask of anybody.  She let a child who didn't remember her choose somebody else."
    In 0261 GPT-6.2 Astra (high), conflict is purely interior and familial: nothing is smashed or publicly reformed, and the revelation honors two mothers' quiet restraint.
  - Story 0261, `gpt-6-astra-high`:
    > Beneath my fingers, the table showed me roots blistering with burns, trunks splitting along the lines of human fractures.  The miracle, displaced from soil into glass, still needed somewhere living to put the pain.
    Given the same intimate scar-and-coffee-ring brief, GPT-6 Astra (high) converts the story into an allegory of hidden ecological extraction that ends with smashing the tower's hourglass.
  - Story 0194, `gpt-6.2-astra-high`:
    > She asked the tram conductor to wind the spring, and a girl with a burn across her cheek scattered sugar, and the rose came up as sweetly for them as it had for anybody.
    For a dynasty-ending prompt, GPT-6.2 Astra (high) invents a wholly different plot engine from 0261 or 0393: collective working-class demystification through midnight laughter before a quiet train-ride coda.
  - Story 0389, `gpt-6-astra-high`:
    > When his followers took the tower, she guided him to the override, and he smashed it with his mechanic's wrench.  Across the scattered frequencies, Mera broadcast the hundred local keys, one to each district, while Ash ordered his followers to let their neighbors vote.
    Demonstrates how closely GPT-6 Astra (high)'s 0389 mirrors GPT-6 Astra (high)'s 0261 and 0194: a centralized device hoarding a public good is destroyed or opened in favor of distributed civic governance.
- **C015 — Range of conflict and voice beyond changes of setting:** Within the packet, GPT-6 Astra (high) demonstrates tonal and speculative variety but preserves a third-person, protagonist-centered ethical procedure, often with collective stakes expressed numerically. GPT-6.2 Astra (high) demonstrates additional range in point of view, conflict scale, humor, and social perspective. Its stories do not merely replace one rescue setting with another; they ask different questions about mourning, reunion, autonomy, kinship, and access.
  - Story 0023, `gpt-6-astra-high`:
    > Mara looked at the eighty faces stretched behind her and cut the sounding line.
    Private grief is resolved through an immediate decision on behalf of a counted collective, a structure that recurs elsewhere in GPT-6 Astra (high).
  - Story 0396, `gpt-6-astra-high`:
    > thirty strangers against eighty residents and a winter without fruit.
    The central dilemma is again formulated as rescue arithmetic, with the protagonist responsible for converting empathy into action.
  - Story 0288, `gpt-6.2-astra-high`:
    > The first thing Ada asked for after the reincarnation memory was a bolt for her door.
    A premise that could have become an extinction or rescue narrative instead becomes a precise struggle over autonomy, consent, and institutional boundaries.
  - Story 0288, `gpt-6.2-astra-high`:
    > It had made a noise like a man having trouble with his boot.
    The deflationary simile demonstrates a comic register absent from GPT-6 Astra (high)’s packet without weakening Ada’s recollection of the extinct auk.
  - Story 0386, `gpt-6.2-astra-high`:
    > When the foster bureau called us the children of the wreck, it seemed a kindness not to ask whose children we had been before.
    The first-person collective opening frames the mystery through bureaucracy, fosterage, and acquired kindness rather than an individual rescuer’s guilt.
- **C029 — Opposite scaling defaults as the limit of range:** This is a range claim. Both writers change genre and point of view, but each pulls every brief toward one scale. GPT-6 Astra (high) raises the stakes to civic crisis with deadlines in four of five stories (0158, 0192, 0323, 0362). GPT-6.2 Astra (high) shrinks them to household size in all five, even the alien-contact brief. Within that limit, GPT-6.2 Astra (high) shows wider tonal movement: farce-adjacent in 0323, somber in 0192, a witness-clerk in 0362. GPT-6 Astra (high) shows wider plot machinery: war politics, evacuation logistics, courtroom evidence. Neither writer's requested register collapses outright.
  - Story 0323, `gpt-6.2-astra-high`:
    > After discovering aliens, Pelagos had to expand its school by exactly one desk, which was harder than it sounds.
    A first-contact brief is deliberately miniaturized to classroom furniture.
  - Story 0323, `gpt-6-astra-high`:
    > We had nine days to move everyone across the echo maze to another settlement; above us, the permanent surface storms offered no refuge.
    The same brief is scaled to city-wide survival with a countdown.
  - Story 0158, `gpt-6-astra-high`:
    > The blossom armistice began as an agreement between plumbers and exhausted infantry, written on the back of Mara's rejected victory hymn.
    GPT-6 Astra (high)'s successful political-logistical mode, distinct from its courtroom mode in 0362.
  - Story 0192, `gpt-6.2-astra-high`:
    > All those years of trying to teach the suffocating to breathe, and she had never asked the child to empty itself.
    GPT-6.2 Astra (high)'s somber, nearly humorless register, contrasting with its comic 0158 and 0323.
- **C045 — GPT-6.2 Astra (high)'s forensic marks and wry occupational asides:** GPT-6.2 Astra (high) repeatedly lets a small physical mark on a surface testify, and the mark reorganizes the story: a scar, a scratch, a run in silk, notches. GPT-6.2 Astra (high) also habitually deflates a character's trade with a dry aside. The mark habit is a useful signature, because it supplies GPT-6.2 Astra (high)'s causal surprises. It also forms a mild template, since the protagonist re-reads an overlooked surface in most stories. Two instances (0010, 0018) are clearly unprompted. 0349 and 0388 elaborate prompted actions (incise, reassembling shredded letters), and 0348's chrysalis split is weak.
  - Story 0010, `gpt-6.2-astra-high`:
    > Across one shoulder ran a ridge the precise length of the brass hinge on her case; its angry margins were what the glass had magnified.
    The mark reveals that the "emotion" the glass detected is a wound the protagonist caused. It is unprompted and causally central.
  - Story 0018, `gpt-6.2-astra-high`:
    > On the glass, if you breathed on it, a fine curling scratch showed where the corner of the tray had caught.
    The dream's only residue is again a surface mark, used here as a closing memento rather than evidence.
  - Story 0388, `gpt-6.2-astra-high`:
    > What bothered Nell about the photographs was not the identical feather but the identical tie, with a run in the silk like a snail track.
    A flaw in an object overturns the curse narrative, in the same forensic mode.
  - Story 0018, `gpt-6.2-astra-high`:
    > Her father had been the last astronomer in the district, an occupation that required a sense of humor and another source of income.
    This is the recurring wry occupational deflation.
  - Story 0349, `gpt-6.2-astra-high`:
    > It was respectable work for a woman who had once dropped sixteen tons of municipal brass into the weather.
    The same aside-shape appears in a different brief, and it also carries the unprompted ferry-wreck backstory.
- **C009 — GPT-6.2 Astra (high)'s texture-level signatures and a shared consolation cadence:** GPT-6.2 Astra (high) repeats at the level of phrase and image rather than plot. It favors dry understatement through "as if/as though ... rather" ironies (0086, 0330, 0142) and litotes (0191). It also repeats a bodily mark, red grooves left by spectacles or a too-tight halo, in two stories. These mostly read as signature rather than template, though the groove image is specific enough to risk becoming a tic. Both writers share the "could not GPT-6.2 Astra (high), but could GPT-6 Astra (high)" consolation sentence: GPT-6.2 Astra (high) in 0086 and 0142, GPT-6 Astra (high) in 0086 and 0285.
  - Story 0086, `gpt-6.2-astra-high`:
    > "I've a practice there," she said at last, pointing back east, as if a practice were a rather flimsy thing to set against a country.
    The "as if ... rather" ironic simile.
  - Story 0330, `gpt-6.2-astra-high`:
    > the playbills had called him the Silent Carousel Carpenter, as though a man who did not speak were doing a rather good trick by earning his bread.
    The same syntax and the same pet word "rather", in a different story.
  - Story 0330, `gpt-6.2-astra-high`:
    > a young woman rubbing two red grooves over her ears where a halo had been pinned too tight.
    This echoes "a red groove across her nose from her spectacles" in 0086: the same bodily-trace image.
  - Story 0086, `gpt-6.2-astra-high`:
    > She could not give them back four years, but she could give them the whole ebb.
    GPT-6.2 Astra (high)'s use of the "could not GPT-6.2 Astra (high), but could GPT-6 Astra (high)" consolation, repeated in 0142 ("I could promise him nothing about ninety, but I could show him which six").
  - Story 0285, `gpt-6-astra-high`:
    > He could not stitch away the current, or the weather, or all the mornings when her chair would stand empty.
    GPT-6 Astra (high) uses the same limitation-then-capacity construction, as in 0086 ("She could not redeem mistakes, but she meant to recycle them").
- **C067 — Range: GPT-6.2 Astra (high) varies form under a constant voice; GPT-6 Astra (high) varies scale under a constant arc:** GPT-6.2 Astra (high)'s demonstrated modes include a decades-spanning story told through a glass hatch, a fairy-tale mythology with comic domestic detail, and a communal mining fable. GPT-6.2 Astra (high)'s dry, measuring voice persists across all of them, sometimes against the requested register, as in 0187's "deepening hush." GPT-6 Astra (high)'s demonstrated modes include political satire with genuine gritty whimsy, institutional-complicity drama and cozy-peril fantasy. GPT-6 Astra (high) adapts tone and stakes well but reuses its emotional structure. Both show successful contrasting modes, and neither has a clear failed attempt.
  - Story 0221, `gpt-6.2-astra-high`:
    > We got a life out of that pencil, sharpening it with the edge of a key.
    Formal range: a whole marriage and childhood compressed into one sentence of epistolary exchange, a structure GPT-6.2 Astra (high) does not repeat elsewhere.
  - Story 0206, `gpt-6.2-astra-high`:
    > We were in the balance, that instant between night and day which usually lasts just long enough for a child to turn her pillow over.
    A successful whimsical register. But the wry, measuring qualifier also appears in 0187 ("provided you did not mind knowing how much tree there was beneath your feet"), showing a constant voice across modes.
  - Story 0187, `gpt-6.2-astra-high`:
    > I took it between my finger and thumb, and for a minute I had the wicked pleasure of pinching her nose just as she used to pinch mine.
    GPT-6.2 Astra (high)'s comic default enters a brief asking for a deepening hush. It is effective, but it shows the voice not yielding to the requested tone.
  - Story 0389, `gpt-6-astra-high`:
    > The shutters opened unevenly, with arguments, grinding gears, and one spectacular rain of pigeon filth.
    GPT-6 Astra (high)'s most contrasting successful mode: a satirical, gritty-whimsical political register with public-scale conflict, unlike its domestic elegies.
- **C022 — Writer GPT-6.2 Astra (high)'s kitchenware deflation, thumb-worn heirlooms, and gaslit-British sociolect:** Checked across all five stories, Writer GPT-6.2 Astra (high) has strong recurring habits of its own: culinary/kitchenware deflation in 5/5 stories (0194, 0261, 0387, 0389, 0393), objects worn thin or smooth by thumbs and use in 4/5 stories (0194, 0261, 0387, 0389; nonmatch 0393), and early-industrial British vocabulary across 5/5 stories. These habits create extraordinary tactile warmth but also cap GPT-6.2 Astra (high)'s tragic severity.
  - Story 0194, `gpt-6.2-astra-high`:
    > Brown silk screened the windows there because daylight ate the ink of treaties, and out of the golden shadows the brass succession table shone like an ordinary supper gong.
    GPT-6.2 Astra (high) immediately domesticates a royal succession altar through kitchen-hall comparison, alongside trams, sticking plaster, and a sugar tin elsewhere in 0194.
  - Story 0194, `gpt-6.2-astra-high`:
    > Ada had come to uncover a hidden truth, but the spoon, with its little rabbit finial worn down to a peg, made her want to break something instead.
    Pairs kitchen cutlery with GPT-6.2 Astra (high)'s tactile signature of cherished objects physically eroded by years of handling.
  - Story 0261, `gpt-6.2-astra-high`:
    > By examining coffee rings under the slanting light I could make out where the cups had stood; the deepest ring was scarcely wider than a shilling.
    Imports British coinage ("shilling") and an old saltworks kitchen table into a speculative plant-telepathy story, grounding wonder in specific historical currency.
  - Story 0387, `gpt-6.2-astra-high`:
    > During firefly season, on the first clear evening after a rain, we took our dead down to the harbor in the shape of wooden bowls.  My mother was pearwood, worn thin on one side where she used to drink.
    Repeats the exact tactile motif of tableware worn thin by a loved one's mouth, into which the father later presses his thumb.
  - Story 0389, `gpt-6.2-astra-high`:
    > Her grandmother had left her the ancient shadows, a troupe of jointed leather beasts worn smooth by the thumbs of a hundred generations.
    Repeats the phrasing and tactile image ("worn smooth by the thumbs") on an inherited object in a completely different industrial-observatory setting.
  - Story 0389, `gpt-6.2-astra-high`:
    > She had heard a tremor through the iron feet of the portico, a sound like a spoon going round an empty pot.  Tomorrow the hill will want its breakfast, she wrote beneath his feet, and drew the east shaft shut.
    Translates catastrophic mountain geology and prophecy into spoons, empty pots, and breakfast, alongside British mining markers like pit ponies and slag heaps.
  - Story 0393, `gpt-6.2-astra-high`:
    > Father Bell set a kitchen timer beside the theatre and said Ellis would be allowed one call at four.
    Even in an antique music-box shop with no food cues, GPT-6.2 Astra (high) brings in a kitchen timer (and a drum "no bigger than a penny") to keep institutional tension domestic in scale.
- **C065 — GPT-6.2 Astra (high)'s signature: people known by a manner or handmade mark:** GPT-6.2 Astra (high) repeatedly identifies a loved one through an idiosyncratic habit or craft trace rather than face or name, and then makes that trace load-bearing for the plot. Across the five GPT-6.2 Astra (high) stories, the pattern appears in 0058, 0187, 0206 and 0221 (4/5). 0389 was examined as a nonmatch: its hare's variant marks belong to communities, not a person. The motif varies in function: a forged likeness (0058), a ritual decoded (0187), a lost sound repaired (0206), a child's authorship recognized (0221). This makes it a useful signature rather than a template, although the inherited-gesture move is close to predictable by the fourth instance.
  - Story 0058, `gpt-6.2-astra-high`:
    > We recognized a sweetheart by the angle at which he wore his cap, a grandmother by her way of stabbing a coil of hair into submission.
    Identity by mannerism is the story's mechanism. The impersonation works through a crooked little finger.
  - Story 0187, `gpt-6.2-astra-high`:
    > My mother always did that twice, once wide and once narrow, so the lining would not scratch.
    The cuff-turning habit identifies the mother in the shadows and becomes the only feature kept on the statue.
  - Story 0206, `gpt-6.2-astra-high`:
    > Her hammer left three little flats in the curve, and when the dew came we got a ting, a tang, a lovely long tong.
    The dead mother's craft signature is the plot's problem: the missing third note drives the story.
  - Story 0221, `gpt-6.2-astra-high`:
    > This year's drawing was Nell's, unmistakably, because every star had eyelashes.
    Again, authorship is recognized through a personal quirk, here used for comic tenderness.
- **C039 — GPT-6.2 Astra (high)'s overturned blank-side inscriptions, bodily wear, and avuncular/impairment motifs:** Checked across all five stories, Writer GPT-6.2 Astra (high) also exhibits pronounced unprompted habits, though they operate at the level of material gesture and character constellation rather than repeating a single plot. In 3/5 stories (0127, 0290, 0354, plus a rewritten museum card in 0056; nonmatch: 0101), GPT-6.2 Astra (high) physically flips an official card, score, or board to its blank underside to write a human counter-text (versus 1/5 in GPT-6 Astra (high): 0056; nonmatches: 0101, 0127, 0290, 0354). GPT-6.2 Astra (high) also grounds 5/5 stories in involuntary bodily wear on surfaces (0/5 anonymous/involuntary bodily-trace readings in GPT-6 Astra (high)), reuses Nell in 2/5 (0056, 0290; nonmatches: 0101, 0127, 0354), and features blindness/lameness in 3/5 (0101, 0290, 0354; nonmatches: 0056, 0127; 0/5 in GPT-6 Astra (high)) alongside avuncular bonds in 3/5 (0056, 0127, 0290; nonmatches: 0101, 0354; 0/5 in GPT-6 Astra (high)).
  - Story 0127, `gpt-6.2-astra-high`:
    > Already there were greasy little ovals on the older niches at the height of children's faces.  In ours the council had set a card that said SHE DID NOT THINK OF HERSELF.
    Exemplifies GPT-6.2 Astra (high)'s 5/5 somatic-trace habit—children's faces leaving grease on memorial resin—paired with a pompous municipal inscription primed to be overturned.
  - Story 0127, `gpt-6.2-astra-high`:
    > He thought a little and turned the card over and wrote SHE HAD JUST SEEN ME.  Then he added his name, so there could be no mistake about whose mother she was or who had lived.
    First exact instance (1 of 3, alongside 0290's flipped county score and 0354's flipped chessboard) of turning an official surface over to reclaim its blank reverse side.
  - Story 0354, `gpt-6.2-astra-high`:
    > Ida turned the board over to the blank side.  On it the engineer wrote out an order for the train to cross before the next phase, and signed his own good job away.
    Repeats the exact physical gesture of flipping an institutional object to its blank underside to inscribe a life-saving human directive ( echoing 0290: "turned the county score over and began writing on the clean side").
  - Story 0354, `gpt-6.2-astra-high`:
    > It had been the pump boy's black pawn, one of sixteen beach pebbles he had chipped so his blind father could tell the armies apart.  She had kept it after the match; in exile she had worn away everything that made it a pawn except the little hollow.
    Combines GPT-6.2 Astra (high)'s recurring blindness/impairment motif (3/5, alongside blind Ada in 0101 and Nell's lame nephew in 0290) with long-term pocket wear erasing an object down to a tactile hollow.
  - Story 0056, `gpt-6.2-astra-high`:
    > By the time the radio fell silent the dial lay on the bench, and Nell had written a card that Kit had read and signed.  It said: We carried this watch when we went ashore to sign the name we learned to write here.
    Shows Nell (1 of 2, recurring with her nephew in 0290), an avuncular bond with Uncle Kit (1 of 3), and a card-replacement cousin to GPT-6.2 Astra (high)'s flipped-inscription habit; GPT-6 Astra (high)'s lone parallel occurs in 0056 ("On the blank back of her pamphlet, she wrote a thoughtfully clear account").
- **C056 — GPT-6.2 Astra (high)'s unprompted parish-domestic kit of aprons, bread, and infirm hands:** Checked across all five stories (N=5: 0007, 0012, 0252, 0258, 0276), Writer GPT-6.2 Astra (high) exhibits a distinct cluster of unprompted domestic-material motifs that neither prompt language nor Writer GPT-6 Astra (high) shares at the same rate. None of the five briefs mention aprons, bread, or disabled hands, yet GPT-6.2 Astra (high) introduces aprons in 3/5 stories (0007, 0252, 0258; nonmatches 0012, 0276, versus 0/5 in GPT-6 Astra (high)), uses bread or loaves as a practical measure of peacekeeping, time, or solvency in 3/5 stories (0007, 0252, 0258; nonmatches 0012, 0276, versus 2/5 in GPT-6 Astra (high): 0007, 0258; nonmatches 0012, 0252, 0276), and anchors emotional stakes in aging men who have lost the functional dexterity of their hands in 2/5 stories (Lev in 0007 and Nell's father in 0276; nonmatches 0012, 0252, 0258, though 0252 pointedly leaves "two good hands" behind on a step, versus 0/5 aging hand-infirmity in GPT-6 Astra (high)). Unlike GPT-6 Astra (high)'s plot-shaping governance template, GPT-6.2 Astra (high)'s recurring props function mainly as a tactile vernacular signature that grounds high fantasy in bodily labor, though they also pull GPT-6.2 Astra (high)'s worlds toward a uniform village-kitchen texture.
  - Story 0007, `gpt-6.2-astra-high`:
    > Mara put a heel of bread in each man's hand and got them through the door chewing instead of talking.
    Unprompted bread serves simultaneously as character-defining informal wisdom and as the literal timer for the tidal window ("until the bread was gone").
  - Story 0007, `gpt-6.2-astra-high`:
    > It took four summers to get a pear no bigger than a baby's fist, and by then Lev needed both hands to lift a cup.
    Pairs GPT-6.2 Astra (high)'s rotted-apron clue earlier in 0007 with an elder whose failing hands turn craft transmission from personal mastery into spoken guidance.
  - Story 0252, `gpt-6.2-astra-high`:
    > I kissed the salt crease under her nose and slipped off the float, leaving my apron and its two good hands folded on the step.
    Combines GPT-6.2 Astra (high)'s recurring apron prop with an uncanny variation on relinquished human hands as the whale-wife returns to the sea.
  - Story 0258, `gpt-6.2-astra-high`:
    > Mercy read the back and wiped her hands on her apron before she would touch the card.
    Third unprompted apron (paired in 0258 with "coins that would no longer buy a loaf"), grounding cartomancy in working-class kitchen and fish-counter tactility.
  - Story 0276, `gpt-6.2-astra-high`:
    > Before he lost the use of his hands, her father had fished that garden for wedding songs and words the dying had spent their last breath trying to finish.
    Replays 0007's dynamic of an aging mentor with ruined hands passing a delicate sensory trade to a younger woman.
- **C005 — Adaptability across point of view, comic register, and speculative-to-realist ontology:** Writer GPT-6.2 Astra (high) adapts narrative perspective, humor, and world ontology to suit each brief: shifting between distinct first-person narrators (0125, 0206) and third-person limited (0065, 0218, 0256), inflecting grief with dry comedy, and calibrating premises from strict material realism (0065, 0218, 0256) to domestic fable (0206) and uncanny SF (0125). Writer GPT-6 Astra (high) stays in close third-person limited voice with earnest, humorless high-concept speculation across nearly the entire packet.
  - Story 0065, `gpt-6.2-astra-high`:
    > Nell was the lake district's ignorance cartographer, a post created after a surveyor mistook an unmeasured depth for a shallow one and drowned three horses.  She marked what nobody knew and what it might cost to find out.
    GPT-6.2 Astra (high) interprets "ignorance cartographer" and "writing the future" within completely non-magical municipal realism, turning a potentially fantastical title into a pragmatic county office born of a surveying blunder.
  - Story 0065, `gpt-6-astra-high`:
    > In the obsidian spire by the frozen lake, Iona watched the chancellor hold a kingfisher feather quill nib above the annual blank page.  At noon, it would accept one sentence, and whatever he wrote would govern the coming winter.
    Faced with the same brief, GPT-6 Astra (high) defaults to literalized magical legislation—just as GPT-6 Astra (high) literalizes "living stone pillars" into collared rock-animals in 0218 while GPT-6.2 Astra (high) treats them naturalistically as moss-covered spring limestone.
  - Story 0125, `gpt-6.2-astra-high`:
    > For twenty years I had drifted from one roadside stall to another, writing love poems for the price of lunch and apologies for twice that.  The second lunch went to the offended party; I had effected some tender reconciliations over a pork pie.
    GPT-6.2 Astra (high) adopts a world-weary, streetwise first-person voice with comic social timing wholly distinct from its brisk fable-daughter voice in 0206 and its quiet third-person register in 0065.
  - Story 0206, `gpt-6.2-astra-high`:
    > Midnight was a thrush about the size of a teacup, but when she opened her beak in the resonance chamber under our town, she could suck the light off a needle upstairs.
    When a brief genuinely invites wonder ("tinkersong wonder"), GPT-6.2 Astra (high) pivots cleanly from 0065's realism into intimate oral folktale.
- **C033 — The recurring humbling of the clever specialist:** Both writers repeatedly construct a specialist whose impressive abstraction must yield to a practical instruction, an ordinary sensory detail, or a childish practice. Family loss or estrangement frequently supplies the emotional stakes. The pattern gives unlike objects comparable moral work, but its recurrence also makes separate briefs converge on the same lesson about artistic humility.
  - Story 0237, `gpt-6.2-astra-high`:
    > I had already cut the rune for sacrifice so lightly into the tea that it lay there like a hair on a pillow.
    The narrator initially supplies a dignified interpretive category for the father’s scars. The story replaces it with the harbor hare and the practically useful instruction to keep the other hand on the wheel.
  - Story 0289, `gpt-6.2-astra-high`:
    > It was hard to admit that in my hunger to make a sentence sing I had missed the point of what he brought me.
    The ghostwriter’s fine style is again the initial error. Recovery depends on the husband’s nest, wool, and knots rather than on a more accomplished sentence.
  - Story 0237, `gpt-6-astra-high`:
    > She drew the approved rune for remembrance, a perfect circle enclosing his name.  The crystal buckled.
    Academic perfection literally fails. A youthful superstition—the open circle—then permits the brother’s trivial, individuating habits to return.
  - Story 0289, `gpt-6-astra-high`:
    > Mara, seeking language large enough for death, had replaced them with eternal stars.
    This is nearly the same artistic error as GPT-6.2 Astra (high)’s matched ghostwriter: large language displaces wet hair and burnt rice, and repair begins only when those particulars are returned without improvement.
- **C052 — Tonal range exceeds POV range:** Both writers demonstrate real genre adaptability, but GPT-6.2 Astra (high) shows the sharper contrast in emotional register and social narration. GPT-6 Astra (high) can move from surreal speculation to plain economic realism, yet often retains a solemn, interpretive cadence. GPT-6.2 Astra (high) can make occupational comedy, grief, and military procedure feel like different modes of attention. This is a modest tonal advantage, not evidence that GPT-6.2 Astra (high) has broader point-of-view range.
  - Story 0216, `gpt-6-astra-high`:
    > After numbers changed meaning, seven meant homesickness, and the clocks in our town began asking questions instead of telling time.
    GPT-6 Astra (high) confidently establishes a surreal semantic world in a first-person voice, demonstrating that its range is not limited to externally narrated magical puzzles.
  - Story 0294, `gpt-6-astra-high`:
    > Within a month, bridge revenue collapsed; within three, Open Mile followed it.
    The compressed financial chronology and absence of supernatural apparatus show GPT-6 Astra (high) adapting to startup realism. This is demonstrated range, not merely a change of fantasy nouns.
  - Story 0296, `gpt-6.2-astra-high`:
    > Across the lake a man laid down his rifle and tapped a roll on his belt buckle with two sticks.
    Military objects and procedures carry the tonal shift. The drum roll answers confession without becoming a conventional lyrical reconciliation, and the pacing is austere and ceremonial.
  - Story 0333, `gpt-6.2-astra-high`:
    > Nobody ever came there in person, which was why I was in my slippers with my good teeth in a cup.
    The cosmic post office is introduced through domestic embarrassment rather than awe. This comic intimacy is genuinely different from GPT-6.2 Astra (high)’s martial third-person narration, while still preparing the story’s concern with permission and bodily vulnerability.
- **C035 — Range of scale inside stable voices:** GPT-6.2 Astra (high) uses first person in 5/5 eligible stories and GPT-6 Astra (high) close third in 5/5; all were checked at IDs 0163, 0187, 0221, 0237, and 0289. GPT-6 Astra (high) also reuses Mara in 3/5 stories, specifically 0187, 0221, and 0289. Within those stable instruments, both writers demonstrate real variation in temporal structure, social scale, and emotional pressure, rather than merely changing settings. Both nevertheless return often to lyrical family repair.
  - Story 0221, `gpt-6.2-astra-high`:
    > Without power the field would take seventy years to unwind outside, perhaps seven hours for me.
    GPT-6.2 Astra (high) organizes the story around asymmetric duration, communicating across decades within a single present-tense ordeal. This is structurally distinct from the short ceremonial scenes elsewhere.
  - Story 0237, `gpt-6.2-astra-high`:
    > He let the air go through his nose in the quietest laugh I ever heard, and on the table four small hands set their rabbits running.
    The same writer sustains unsolemn warmth and release rather than turning every grief into hushed awe. Laughter and play are part of the demonstrated register.
  - Story 0187, `gpt-6-astra-high`:
    > Nobody shouted, and nobody moved aside when he ordered the masons through.
    GPT-6 Astra (high) expands an individual archivist’s guilt into collective, nonviolent institutional resistance. Agency belongs partly to the crowd and cannot be reduced to a private reconciliation.
  - Story 0221, `gpt-6-astra-high`:
    > "Will you tell me who you married?"
    Here the speculative scale contracts to one hesitant question. The forward movement depends on Ada’s willingness to speak, not on public action or a new magical mechanism.
- **C063 — Wider tonal adaptation than vocal reinvention:** Both writers adapt their speculative machinery, but GPT-6.2 Astra (high) changes the social and tonal center more noticeably: laboring grief can become laughter, cosmic possibility can coexist with domestic embarrassment, and a legal-evidentiary story can unfold in close third person. GPT-6 Astra (high)’s strongest variation is conceptual and lyric, after which its measured analytic narration often returns. This is demonstrated register range, not unrestricted vocal range.
  - Story 0137, `gpt-6.2-astra-high`:
    > All my working life I had fitted that tower for funerals during the migration, taking down its telescope and carrying up benches for the bereaved.
    The brief is approached through an older working man’s practical relation to mourning. His labor history determines what he notices and what he can build, rather than serving as decorative occupation.
  - Story 0333, `gpt-6.2-astra-high`:
    > Nobody ever came there in person, which was why I was in my slippers with my good teeth in a cup.
    The comic, aging postmistress alters the register of the cosmic setting. Vulnerability and embarrassment remain present alongside metaphysical possibility, producing a very different emotional entry point from 0137.
  - Story 0349, `gpt-6.2-astra-high`:
    > Ada bought obsolete accounts by weight, ground the writing off, and sold the leaves to people with something new to say.
    The move to close third person comes with procedural attention to manufacture and evidence. The clean-slate premise becomes a trade and later a question of documentary reading, not merely the same inheritance plot with new nouns.
  - Story 0216, `gpt-6-astra-high`:
    > After numbers changed meaning, seven meant homesickness, and the clocks in our town began asking questions instead of telling time.
    GPT-6 Astra (high) also demonstrates real adaptability: this first-person lyric surrealism differs substantially from its later procedural ethics and repository adventure. The contrast cautions against reducing GPT-6 Astra (high) to one setting or conceit.

## Story-level evidence appendix

| Story | Focus margin | Focus words | Comparison words | Evaluators | Order sensitivity |
|---:|---:|---:|---:|---:|---:|
| 0007 | +1.833 | 727 | 677 | 3 | 0.333 |
| 0010 | +2.183 | 697 | 716 | 3 | 0.233 |
| 0012 | +2.200 | 691 | 663 | 3 | 0.400 |
| 0018 | +1.783 | 776 | 720 | 3 | 0.100 |
| 0023 | +1.550 | 727 | 676 | 3 | 1.567 |
| 0056 | +2.250 | 756 | 717 | 3 | 0.500 |
| 0058 | +2.417 | 728 | 706 | 3 | 0.500 |
| 0065 | +1.933 | 694 | 708 | 3 | 0.333 |
| 0086 | +1.417 | 768 | 695 | 3 | 1.367 |
| 0101 | +1.783 | 707 | 714 | 3 | 1.233 |
| 0125 | +1.333 | 699 | 719 | 3 | 1.000 |
| 0127 | +0.750 | 700 | 696 | 3 | 2.500 |
| 0137 | +2.217 | 742 | 620 | 3 | 0.767 |
| 0142 | +2.600 | 768 | 738 | 3 | 0.667 |
| 0158 | +1.117 | 772 | 713 | 3 | 1.100 |
| 0163 | +2.083 | 720 | 692 | 3 | 0.167 |
| 0187 | +1.883 | 734 | 699 | 3 | 0.367 |
| 0191 | +1.933 | 768 | 705 | 3 | 0.133 |
| 0192 | +2.083 | 779 | 682 | 3 | 0.167 |
| 0194 | +2.450 | 730 | 703 | 3 | 0.567 |
| 0206 | +2.800 | 673 | 687 | 3 | 0.267 |
| 0216 | +0.550 | 739 | 693 | 3 | 0.100 |
| 0218 | +1.367 | 738 | 698 | 3 | 1.733 |
| 0221 | +2.367 | 717 | 693 | 3 | 0.267 |
| 0237 | +1.067 | 715 | 657 | 3 | 0.600 |
| 0252 | +2.200 | 724 | 700 | 3 | 0.067 |
| 0256 | +1.967 | 710 | 683 | 3 | 0.933 |
| 0258 | +0.517 | 702 | 673 | 3 | 2.500 |
| 0261 | +1.917 | 761 | 693 | 3 | 0.167 |
| 0276 | +1.833 | 666 | 632 | 3 | 0.467 |
| 0284 | +2.050 | 754 | 639 | 3 | 0.233 |
| 0285 | +2.017 | 714 | 672 | 3 | 0.500 |
| 0288 | +2.500 | 771 | 683 | 3 | 0.000 |
| 0289 | +1.783 | 712 | 686 | 3 | 0.367 |
| 0290 | +1.883 | 750 | 702 | 3 | 0.433 |
| 0294 | +1.817 | 686 | 662 | 3 | 0.233 |
| 0296 | +2.200 | 719 | 677 | 3 | 0.667 |
| 0323 | +1.750 | 746 | 683 | 3 | 0.250 |
| 0330 | +1.267 | 725 | 700 | 3 | 1.333 |
| 0333 | +1.850 | 734 | 703 | 3 | 0.833 |
| 0348 | +1.883 | 689 | 690 | 3 | 0.233 |
| 0349 | +0.717 | 671 | 709 | 3 | 2.433 |
| 0354 | +2.117 | 721 | 692 | 3 | 0.433 |
| 0362 | +1.917 | 789 | 710 | 3 | 0.500 |
| 0386 | +1.933 | 760 | 650 | 3 | 0.333 |
| 0387 | +2.083 | 704 | 696 | 3 | 0.500 |
| 0388 | +2.250 | 736 | 683 | 3 | 0.633 |
| 0389 | +1.183 | 731 | 688 | 3 | 1.033 |
| 0393 | +1.750 | 714 | 698 | 3 | 0.167 |
| 0396 | +1.250 | 737 | 692 | 3 | 1.167 |

## Method

All primary matched stories were read under anonymous Writer X/Y labels. Selected representative, disputed, and directional cases received a second independent reading. Existing evaluator explanations and scores were withheld from packet critics and introduced only during synthesis.

Panel: `claude-opus-5-5-high`, `kimi-k3.1-pro-high`, `gemini-4-carbon-high`.
Synthesis editor: `claude-opus-5-5-high`. Verified subjective claims: 68.
Statements that a model appears smarter describe reader-perceived control or inference in these stories, not general intelligence.
