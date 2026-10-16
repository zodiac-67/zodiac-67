import re, sys

OUT = "/home/user/zodiac-67/prompts/nepal-1800s-survive/phase-b-prompts.md"

FARMER = ("One young adult male minimalist 2D cartoon hill farmer with a white filled circular head, two small dark oval eyes, simple eyebrow strokes and a short curved mouth, wearing a small plain dark-brown cloth cap. He wears a simple off-white cotton tunic that crosses over the chest, is tied at the side and falls to mid-thigh, with short elbow-length sleeves, over loose off-white trousers that narrow at the ankles, and a plain rust-red cloth sash tied around the waist. His forearms, hands and lower legs are dark single-line strokes of constant medium weight; hands are small dark rounded shapes and he is barefoot with short dark rounded feet. Keep the same head-to-body proportions, cap, tunic, sash, white fill and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks, never the head shape or character design.")

HEALER = ("One older male minimalist 2D cartoon village healer, slightly shorter and slightly stooped compared with the young farmer, with a white filled circular head, two small dark oval eyes, thick white eyebrow strokes, a short rounded white beard shape below a calm short curved mouth. He wears a tall crown of upright peacock feathers on a plain cloth headband, a long plain white robe reaching his shins with a deep red cloth sash at the waist, and a long necklace of large dark-brown beads across the chest. His forearms, hands and lower legs are dark single-line strokes of constant medium weight; hands are small dark rounded shapes and he is barefoot with short dark rounded feet. Keep the same proportions, feather crown, robe, sash, beads, fill and outline weight in every shot. Exactly two arms and two legs exist; a moving limb replaces its previous pose rather than leaving another limb behind. Expressions change only the simple facial marks.")

OXEN = ("Two identical simple 2D cartoon oxen with warm brown flat-color bodies, short curved light horns, small dark dot eyes and dark stick-like legs, yoked together by one plain wooden beam.")

VOICE = ("One off-screen elderly male narrator throughout, around seventy years old, speaking clear English with a light, gentle Nepali accent. Warm, deep, slightly weathered low voice, low pitch, rich chest resonance, a soft touch of gravel and no breathiness. Slow, unhurried fireside-storytelling delivery with gentle pauses and restrained pitch variation, steady speaking pace, and close, dry studio sound. Keep the same vocal timbre, register, accent, pace, and recording quality throughout. Emotional progression belongs to the visuals and music; do not change the narrator's voice or switch to character dialogue.")

OUTPUT = "Generate one approximately 10-second video clip: 16:9 landscape, 720p target, 24 FPS, with synchronized audio."

STYLE = ("Style 4 Cozy Storytelling: full-color 2D cartoon animation with clear clean contours, soft natural light, gentle atmospheric depth and cinematic framing, set in a hill village of Nepal in the early nineteenth century. Use rapid scene changes, kinetic motion-graphic transformations, and frequent visual events, while preserving an identical stick-figure design, constant line weight, and strict temporal consistency. Vary wide, close and moving shots. Not a hand-drawn sketchbook look, no paper texture, not photorealistic, not 3D.")

PALETTE_BASE = "Colors are named in plain words only. The farmer's rust-red sash is his signature color in every shot."

COMP = ("Composition (16:9): stage action across left, center and right thirds with lateral camera movement and deliberate negative space; the overall journey direction moves left to right.")

BGM_1 = ("Audio: Voiceover clearly audible over a gentle Nepali folk theme played on sarangi bowed fiddle with soft bansuri flute and a light madal hand-drum pulse, slow warm tempo, establishing the musical theme for the whole video.")
BGM_N = ("Audio: Voiceover seamlessly continues the identical gentle Nepali folk theme from clip 1, sarangi bowed fiddle with soft bansuri flute and a light madal hand-drum pulse, maintaining identical tempo, key, and instrumentation. Synchronized SFX on physical actions.")
MIX = "Voice-first mix: the narration always sits clearly on top; music and sound effects stay underneath it. Environmental echo belongs to the sound effects only; the narration stays close and dry."

DIALOGUE_RULE = ("Audio voiceover only, strictly no speech bubbles, no dialogue boxes. The narrator speaks exactly the words below once, in this order, timed to the beats, without adding, omitting, paraphrasing, repeating or reordering any word, and without captions, subtitles or any visual transcription:")

NEG = ("Negative constraints: no photorealism, no 3D humanoid CGI, no realistic eyes, pupils or lips, no hair beyond the approved designs, no extra limbs, no duplicated or leftover limb poses, no malformed anatomy, no changing proportions or line weight, no extra people, villagers, crowds, soldiers or background figures, no visible words, letters, numbers, captions, subtitles, signs, labels, logos or watermarks, no speech bubbles, no dialogue boxes, no lip-synced character speech, no abstract liquid or shape morphing, no sketchbook borders or paper texture, no modern objects except the approved icon-only symbols.")

CAST_TEXT = {
    "F": "Cast in this clip: exactly one person, the farmer. No other people.",
    "FO": "Cast in this clip: exactly one person, the farmer, plus exactly two oxen. No other people.",
    "FH": "Cast in this clip: exactly two people, the farmer and the healer. No other people.",
}

C = []
def clip(**k): C.append(k)

clip(n=1, stage="Golden Hook", cast="F",
 setting="Interior of a small two-story stone-and-mud hill farmhouse before dawn: low dark wooden ceiling beams, packed-earth floor, an earthen hearth with faintly glowing orange embers at left-center, a woven straw sleeping mat on the floor beside it, a tiny square wooden window in the back wall showing stars above dark mountain silhouettes, and a plain wooden door on the right wall.",
 palette="Cool dawn blue-gray darkness, warming to firelight amber on the farmer's face as the flame rises; cool blue light at the door.",
 comp="Hearth and mat at left-center, window at center background, door at right; keep the right third open for the door light.",
 props="A plain brown blanket covering the farmer at the start, left on the mat when he rises. No other movable props in this clip.",
 first="The farmer lies on the straw mat beside the hearth under the brown blanket, eyes closed; the embers glow faintly; the wooden door is closed.",
 b=["Extreme close-up of the glowing embers; the camera tilts up as the farmer sits up on the mat and opens his eyes, the blanket sliding into his lap.",
    "He reaches his right hand toward the bare wall as if for a light switch; a simple glowing icon-only lightbulb outline flickers beside his hand and fades away. He kneels at the hearth and blows on the embers; a small flame rises and lights his face warm amber.",
    "Slow push-in past his shoulder to the tiny window and the starry peaks; he stands, walks right and pulls the wooden door open; cool blue dawn light floods in from the right."],
 vo=["You wake before dawn. No light switch.", "No clock. No doctor. Eighteen-fourteen, the hills of Nepal.", "Would you last a week?"],
 music="The theme begins very softly.",
 sfx="ember crackle, a soft breath on the coals, a distant rooster, the wooden door creaking open.",
 final="The farmer stands in the open doorway at right, silhouetted against blue dawn light, stepping outward to the right; the blanket lies on the mat; a small flame burns in the hearth.",
 neg="No electric light and no clock anywhere; the lightbulb exists only as a fading icon.")

clip(n=2, stage="Disrupting Assumptions", cast="F",
 setting="A stone village spring on a misty hillside at dawn: a moss-edged carved stone spout pouring a steady stream into a small stone basin, a steep stone footpath climbing to the upper right, a pine tree at the left edge of the frame, and soft white mist filling the valley below under a cool blue-gray sky.",
 palette="Cool dawn blue-gray and soft white mist, with the first pale gold of sunrise on the distant peaks at the end.",
 comp="The farmer enters at left, the spout at center, the steep path rising toward the upper right.",
 props="One round metal water pot with a wide belly and a narrow neck, warm brass in color. It starts empty, held under the farmer's left arm; after filling it is full and carried on his right shoulder.",
 first="Inherited from the previous clip: the farmer walks into frame from the left in cool blue dawn light, moving right, holding the empty water pot under his left arm.",
 b=["Wide establishing shot: the farmer walks right along the path to the spring; mist drifts across the valley and two small birds cross the sky.",
    "Medium shot: he holds the pot under the spout and water splashes and sparkles; gentle glowing icon-only sun and leaf symbols float softly above the spring like a peaceful daydream.",
    "He heaves the full pot onto his right shoulder with a visible strain, knees bending, and starts climbing the steep stone path to the upper right; the gentle icons dissolve; the first rays of sun touch the distant peaks."],
 vo=["We like to picture old village life", "as simple and peaceful. Fresh spring water, clean mountain air,", "no stress at all."],
 music="Calm and gentle.",
 sfx="trickling and splashing water, birdsong, footsteps on stone.",
 final="The farmer climbs the steep path toward the upper right with the full pot on his right shoulder; sunrise light breaks over the peaks ahead of him.",
 neg="")

clip(n=3, stage="Disrupting Assumptions", cast="FO",
 setting="The upper terraced fields of the hill village at sunrise: narrow stepped earthen terraces curving along a steep slope, low dry-stone retaining walls, freshly turned brown soil with green edges, and huge snow-capped Himalayan peaks glowing pink and gold in the background.",
 palette="Fresh terrace green, rich brown soil and warm sunrise gold against snow-white peaks.",
 comp="Water pot set down at left; the oxen and plow travel from center toward the right along the terrace edge; peaks fill the background.",
 props="The full brass-colored water pot arrives on the farmer's right shoulder and is set down on the low terrace wall at the left, where it stays. One simple wooden plow with a single curved handle, tied by a rope to the oxen's wooden yoke beam.",
 first="The farmer arrives from the left with the full water pot on his right shoulder; the two yoked oxen stand waiting on the terrace with the plow behind them.",
 b=["A sun flare rises over the ridge; wide shot: the farmer sets the water pot down on the low terrace wall at left and grips the plow handle with both hands behind the oxen.",
    "Lateral tracking shot from left to right: the oxen pull, the plow curls a ribbon of brown soil, and the farmer leans hard into the handle along the narrow terrace edge; small birds flutter up from the furrow.",
    "He pauses and wipes his brow with his forearm; one ox walks forward past the camera lens, its warm brown body filling the frame as a wipe."],
 vo=["But simple never meant easy.", "Before the sun clears the peaks, you are already behind the plow,", "and every furrow is yours."],
 music="The madal hand-drum pulse becomes slightly more present.",
 sfx="an ox bell, the plow scraping soil, fluttering wings, effortful breathing with no words.",
 final="The warm brown flank of an ox passing close to the lens fills the frame, moving right.",
 neg="Exactly two oxen; no other animals except small birds.")

clip(n=4, stage="Disrupting Assumptions", cast="F",
 setting="The packed-earth front courtyard of a two-story stone-and-mud farmhouse with a thick golden thatched roof, small dark wooden window frames and a low stone step at the door, in soft morning light, with green terraced slopes behind.",
 palette="Warm morning light, earthy browns and golden thatch, pale flour white.",
 comp="The mill at center-left with the farmer kneeling behind it; the house fills the right and background.",
 props="One round two-piece stone hand-mill on the ground: a flat lower stone and an upper stone with a center hole and an upright wooden handle near its edge. One small woven tray of grain, held by the farmer at the start and then set down. One wide clay bowl beside the mill that receives the flour.",
 first="Revealed as the passing brown wipe clears: the farmer already kneels at the stone hand-mill in the courtyard, holding the tray of grain.",
 b=["As the wipe clears, the farmer pours a stream of grain from the tray into the center hole of the mill and sets the tray down.",
    "Close-up insert: his right hand turns the wooden handle in steady circles; pale flour spills from the rim of the stones; a simple icon-only shop and sack symbol appears beside the mill and is crossed out with a single stroke.",
    "Pull back to a medium shot: a small pile of flour lies in the clay bowl as he keeps turning; the camera rises upward, following the circular motion, above the roof toward the treetops."],
 vo=["There is no shop, no sack of flour.", "Every meal begins with your own two hands,", "stone grinding on stone."],
 music="Steady and gentle.",
 sfx="the low rumbling grind of stone on stone, grain pouring, a chicken clucking softly.",
 final="The camera has risen above the thatched roof, framing a swaying green tree canopy, continuing the circular motion.",
 neg="The water pot and the oxen do not appear in this clip.")

clip(n=5, stage="Unveiling Insider Secrets", cast="F",
 setting="A steep pine and rhododendron forest slope above the village: tall straight pines, rhododendron trees with bright red blossoms, dappled sunlight on a carpet of needles, and a narrow trail leading out to the right.",
 palette="Deep forest green, dappled gold light and bright red blossoms.",
 comp="Tree trunks frame the left and center; the trail exits on the right.",
 props="One curved khukuri knife with a dark wooden handle in a simple dark sheath tucked into the farmer's rust-red sash; drawn to cut, then sheathed again. One tall cone-shaped woven bamboo basket with a flat woven forehead strap; it starts empty on the ground and ends full of leafy fodder and dry sticks, carried on the farmer's back with the strap across his forehead.",
 first="A swaying green forest canopy fills the frame, continuing the circular camera motion from the previous shot; the empty basket stands on the ground below.",
 b=["The canopy sways; the camera tilts down the tree trunks to the farmer, who draws the khukuri from his sash and cuts a bundle of leafy fodder from a low branch.",
    "He stacks the fodder and dry sticks into the empty basket, slides the khukuri back into its sheath at his sash, places the forehead strap on his brow and lifts the loaded basket onto his back with a small stagger; red blossoms drift down.",
    "Simple glowing icon-only flame and animal-head symbols pulse beside the basket; he leans forward under the load and walks out of the forest to the right."],
 vo=["Here is what nobody tells you:", "much of your day just feeds the fire and the animals.", "Firewood, fodder, then the climb home."],
 music="Steady and gentle.",
 sfx="forest birds, a branch being cut, snapping twigs, the basket creaking.",
 final="The farmer exits frame right, bent under the full basket; the khukuri is sheathed at his sash.",
 neg="")

clip(n=6, stage="Unveiling Insider Secrets", cast="F",
 setting="The upper storeroom under the thatched roof of the farmhouse: a low slanted ceiling of bamboo and thatch, thin beams of light through small gaps, a notched log ladder rising through a square opening in the floor, and three woven grain baskets with lids standing in a row.",
 palette="Dim warm browns with slanted golden light beams and floating dust.",
 comp="The ladder opening at left; the three baskets in a row from center to right.",
 props="Three identical tall woven grain baskets with round woven lids; from left to right the first is full of golden grain, the second half full, the third almost empty. The khukuri stays sheathed at the farmer's sash. The forest load basket is not in this room.",
 first="The farmer's head and shoulders rise through the floor opening as he climbs the notched log ladder, empty-handed.",
 b=["Low angle: he climbs the last rungs into the storeroom; golden dust motes float in a slanted beam of light.",
    "He lifts the lid of each basket in turn from left to right, full, half, almost empty; he scoops one small handful from the last basket and studies it, eyebrows tilting into a worried expression.",
    "He lets the grain fall back; raindrops start tapping on the thatch above and a few drips sparkle through the light beam; he looks up."],
 vo=["Inside, you count the baskets of grain.", "The harvest is still months away,", "and every handful must last until then."],
 music="The music softens.",
 sfx="a creaking ladder, woven lids lifting, grain trickling, the first raindrops on thatch.",
 final="The farmer looks up toward the thatch as rain drips through the light beam; the lids are open.",
 neg="")

clip(n=7, stage="Unveiling Insider Secrets", cast="F",
 setting="The same terraced hillside fields seen earlier in the story, now in a heavy monsoon downpour: a dark slate-gray sky, sheets of slanting rain, swollen mud, water streaming over the terrace edges, and the peaks hidden in cloud.",
 palette="Heavy slate gray and rain-dark brown, with one white lightning flash at the end.",
 comp="The farmer runs from left to center; the collapsing wall section is at center-right.",
 props="One woven bamboo rain cover shaped like a curved shell, held over the farmer's head and back at first, then dropped on the terrace where it stays. Several rounded gray stones from the collapsed terrace wall, lifted back into the gap.",
 first="Continuing the rain that began in the previous clip: heavy rain sweeps across the terraces; the farmer runs in from the left holding the rain cover over his head and back.",
 b=["Wide shot: sheets of rain cross the slope as the farmer runs right along the terrace edge.",
    "A section of the low stone terrace wall slumps and slides in the mud; he drops the rain cover and hauls rounded stones back into the gap one after another, ankle-deep in mud, rain streaming off him.",
    "A rumble shakes the camera; a bright lightning flash fills the entire frame with white."],
 vo=["Then the monsoon arrives.", "The same rain that feeds your fields", "can wash them down the mountain in a single night."],
 music="The arrangement thins to a lone sarangi line over a faint pulse.",
 sfx="pounding rain, sliding mud, stones thudding, a thunder crack with the lightning.",
 final="A full-frame white lightning flash.",
 neg="No oxen and no water pot in this clip.")

clip(n=8, stage="Unveiling Insider Secrets", cast="F",
 setting="A narrow rain-soaked stone footpath climbing below the farmhouse at dusk turning to night: dark wet stone walls along the path, puddles reflecting faint light, softer falling rain, and the farmhouse above on the right with one small window glowing warm from a lamp inside.",
 palette="Deep blue dusk and rain-dark stone, with one warm amber window and doorway.",
 comp="The path climbs from lower left to the farmhouse door at upper right.",
 props="No carried props. The khukuri stays sheathed at the farmer's sash.",
 first="Emerging from the white flash: the farmer trudges up the path to the right, soaked, arms wrapped around himself.",
 b=["As the white fades to blue dusk, the farmer walks up the path to the right, shivering, arms hugging his chest.",
    "He stumbles and steadies himself with one hand against the stone wall; simple wavy icon-only fever lines rise from his head; far away, a small icon-only medical cross symbol appears on the dark horizon and fades out.",
    "He reaches the farmhouse door, which glows warm from inside; the camera pushes slowly toward the warm doorway light until it fills the frame."],
 vo=["And then, you fall sick. A fever burns through the night.", "No hospital. No pills.", "Nobody is coming from outside."],
 music="A sparse, lone sarangi line.",
 sfx="softer rain, a distant thunder rumble, unsteady footsteps, a wooden door latch.",
 final="Warm amber doorway light fills the frame.",
 neg="")

clip(n=9, stage="Unveiling Insider Secrets", cast="FH",
 setting="The same farmhouse interior where the story began, now at night: low dark wooden beams, a steady fire in the earthen hearth at left-center throwing warm leaping shadows, the straw mat beside it, and the plain wooden door on the right wall.",
 palette="Warm firelight amber against deep night shadows.",
 comp="The farmer at left, the door and the healer's entrance at right.",
 props="One round flat two-sided hand drum with a curved wooden stick handle, carried by the healer. One small bundle of green herb leaves, carried by the healer and then laid beside the farmer, where it stays. A small handful of grain in the healer's palm, scattered into the fire.",
 first="Inherited warm light: the farmer lies under a plain brown blanket on the straw mat beside the hearth, eyes half closed; the door on the right is closed.",
 b=["The door opens on the right and the healer steps in from the rainy night with the drum and herb bundle; firelight catches his feather crown.",
    "He sits by the fire and beats the drum in a steady rhythm; he scatters a handful of grain into the flames and bright sparks spiral upward; he lays the herb bundle beside the farmer.",
    "He gently holds the farmer's wrist with one hand, the drum resting in his lap; the rising sparks dissolve into soft pale morning light."],
 vo=["But the village has its healer.", "With his drum, his prayers and his herbs,", "he is doctor, priest and comfort, all at once."],
 music="The theme returns warmly; the madal pulse aligns with the healer's drumbeat.",
 sfx="the door opening, rain outside, steady drumbeats, crackling fire, rising sparks.",
 final="Soft pale light fills the frame as the sparks dissolve.",
 neg="The healer does not speak, chant words or lip-sync.")

clip(n=10, stage="Unveiling Insider Secrets", cast="FH",
 setting="The healer's small stone hut with a low thatched roof on a quiet hillside at dawn, a small fenced herb patch of leafy green plants in front, morning mist drifting through, and a ridge path leading away to the right.",
 palette="Soft dawn light, fresh herb greens and drifting white mist.",
 comp="The hut at left, the herb patch at center, the ridge path exiting right.",
 props="One fresh green leaf picked by the healer and held up; one matching leaf picked by the farmer. The healer's drum hangs on a peg beside the hut door and is not carried.",
 first="Out of the pale light: the farmer, recovered but tired, walks slowly beside the healer along the herb patch, both moving right.",
 b=["Wide shot in drifting mist: the farmer and the healer walk slowly side by side to the herb patch.",
    "The healer picks a leaf and holds it up to the farmer; the farmer picks the same kind and nods; a simple icon-only book symbol appears and fades away, while a thin warm glowing line passes from the healer's head to the farmer's head.",
    "The farmer steps onto the ridge path to the right; the healer raises one hand in a wave and stays behind beside his hut."],
 vo=["You live. And you learn:", "knowledge here lives in people, not in books.", "Lose the old healer, and you lose it all."],
 music="Gentle and warm.",
 sfx="birdsong, wind in the grass, rustling leaves.",
 final="The farmer walks right onto the ridge path alone; the healer remains small beside the hut at left behind him.",
 neg="")

clip(n=11, stage="Unveiling Insider Secrets", cast="F",
 setting="A high, windy ridge trail above the clouds, overlooking folds of blue-green valleys and distant hills under a vast pale sky, with tall grass bending in the wind.",
 palette="Thin-air sky blue, snow-peak white and blue-green valleys.",
 comp="The ridge runs left to right across the lower third; the distant horizon sits at the right.",
 props="The khukuri in its sheath at the farmer's sash.",
 first="The farmer walks onto the ridge path from the left, alone, moving right.",
 b=["Wide shot: the farmer walks along the ridge, wind snapping at his rust-red sash; he stops abruptly.",
    "Close-up: his hand rests on the sheathed khukuri at his sash; on the distant horizon simple icon-only crossed-swords and war-drum symbols pulse faintly.",
    "He turns back toward home, to the left and down the path, and a gust carries a swirl of leaves across the camera lens, filling the frame."],
 vo=["Then word comes up the trail.", "The kingdom is at war on its far borders,", "and young men like you may be called."],
 music="A low, tense sarangi line.",
 sfx="strong wind, rustling grass.",
 final="A swirl of leaves fills the frame as a wipe.",
 neg="No soldiers, armies, battles or messengers; the war appears only as small distant icons.")

clip(n=12, stage="Ultimate Truth Revelation", cast="F",
 setting="Time jump, months later: the same terraced hillside fields seen earlier in the story, now at harvest in warm autumn sun, the terraces full of tall golden ripe rice rippling in the breeze, a clear blue sky and bright snow-capped peaks behind.",
 palette="Rich harvest gold and clear sky blue.",
 comp="The farmer enters at left; the basket stands at the terrace edge on the right.",
 props="One small curved iron sickle with a wooden handle in the farmer's right hand. Bundles of golden rice sheaves that he ties. The tall cone-shaped woven bamboo basket with its flat forehead strap stands empty at the terrace edge on the right, then fills with sheaves.",
 first="As the leaves clear: golden rice fills the terraces and the farmer wades in from the left holding the sickle.",
 b=["The leaf swirl clears to reveal rippling golden rice; the farmer wades into the field from the left.",
    "He cuts handfuls of stalks with the sickle and ties them into sheaves; golden chaff floats in the warm light.",
    "He lifts one sheaf high above his head and smiles widely, then lowers it into the basket at the right, which is now full to the brim."],
 vo=["Months later, the terraces turn gold.", "You cut the rice yourself.", "The reward is real, and you can hold it."],
 music="The theme swells warmly and fully.",
 sfx="rustling stalks, the sickle's swish, a warm breeze.",
 final="The farmer stands beside the full basket placing its forehead strap on his brow, ready to walk right.",
 neg="No other harvesters.")

clip(n=13, stage="Ultimate Truth Revelation", cast="F",
 setting="A steep rocky mountain trail climbing toward a high snowy pass: enormous snow-capped peaks filling the background, thin clear air, a stone cairn strung with small plain colored prayer flags fluttering in the wind, and a rock overhang shelter near the top right.",
 palette="Snow-peak white and thin-air blue, turning deep orange at sunset; small bright prayer-flag colors.",
 comp="Very wide scale contrast: a tiny farmer on the switchback trail, giant peaks above; the rock shelter at upper right.",
 props="The tall cone-shaped woven bamboo basket, now full of grain, carried on the farmer's back with the flat forehead strap across his brow; set down at the rock shelter at the end.",
 first="The farmer climbs in from the left with the full basket on his back, the forehead strap across his brow.",
 b=["Very wide shot: the tiny farmer climbs the switchback trail beneath giant peaks; his breath makes small white clouds.",
    "Lateral tracking shot to the right: the peaks loom larger; he passes the cairn and its fluttering prayer flags; beside the path a simple glowing icon-only arrow shows a grain symbol turning into a salt-crystal symbol.",
    "The sun sets behind the pass, turning the snow deep orange; he reaches the rock overhang and sets the basket down."],
 vo=["Then you shoulder the extra grain", "and walk for days toward the high passes,", "to trade it for Tibetan salt."],
 music="Steady, with a sense of distance.",
 sfx="high wind, flags fluttering, crunching gravel, heavy breathing with no words.",
 final="The farmer kneels beside the basket under the rock overhang in deep orange sunset light.",
 neg="No other travelers, traders or pack animals; the prayer flags are plain colored cloth with no markings.")

clip(n=14, stage="Ultimate Truth Revelation", cast="F",
 setting="A small trail camp under a rock overhang high in the mountains at night: a small crackling fire, the full basket resting against the rock, and an enormous clear starry sky with the Milky Way above dark snowy peaks.",
 palette="Warm firelight amber against deep night blue and a silver starfield.",
 comp="The farmer and fire at left-center under the overhang; the open starry sky fills the right and top.",
 props="The full woven basket resting upright against the rock wall. A small fire of sticks. A small handful of grain roasting in the farmer's palm.",
 first="Night has fallen: the farmer sits by the small fire under the overhang, the basket against the rock behind him.",
 b=["Medium shot: the farmer roasts a little grain in his palm over the fire and eats it slowly.",
    "Slow orbiting camera around him; simple glowing icon-only symbols of a cooking pot, a salt crystal and an oil lamp rise from the basket one by one and settle in a line along the curve of his back.",
    "The symbols fade; he lies back and looks up; the Milky Way fills the frame and a single shooting star streaks across in a long arc."],
 vo=["And here is the hard truth:", "nothing was given to you. Every comfort, even salt,", "was carried on your own back."],
 music="Quiet and reflective.",
 sfx="fire crackle, faint wind, a soft whoosh for the shooting star.",
 final="A shooting star traces a long arc across the starry sky.",
 neg="")

clip(n=15, stage="Ultimate Truth Revelation", cast="F",
 setting="Time cut to the autumn festival season: a grassy hilltop at golden hour with a tall traditional swing made of four long bamboo poles tied together at the top, a rope seat hanging between them, and garlands of orange marigold flowers tied to the poles; the whole valley and terraces glow below.",
 palette="Golden-hour light, marigold orange and warm sky.",
 comp="The swing frame at center; its arc sweeps from left to right across the frame.",
 props="The bamboo swing with its rope seat, fixed in place. Marigold petals that scatter.",
 first="The swing's rope seat arcs into frame along the same curved path as the shooting star, with the farmer standing on the seat gripping both ropes.",
 b=["The swing sweeps into frame on a long arc matching the shooting star; the farmer stands on the seat, gripping both ropes.",
    "He pumps higher and higher, then stretches one arm out wide with a joyful open smile; marigold petals scatter; the camera rides the swing's arc.",
    "At the very top of the arc the frame fills with golden sky, and a single small warm lamp flame appears at the center and grows."],
 vo=["And yet, when the festivals came,", "people did not just rest. They flew.", "Joy was not a luxury. It was survival."],
 music="The theme at its fullest and brightest.",
 sfx="swing ropes creaking, rushing wind, scattering petals.",
 final="Golden sky fills the frame with a single small lamp flame glowing at the center.",
 neg="No other festival-goers and no crowds.")

clip(n=16, stage="Ultimate Truth Revelation", cast="FH",
 setting="The front stone steps of the two-story stone-and-mud farmhouse with its golden thatched roof at dusk during the lamp festival, under a deep blue evening sky, with rows of small clay oil lamps along the steps and the window ledge.",
 palette="Warm firelight amber flames against deep blue dusk.",
 comp="The steps run across the lower frame; the healer enters from the left.",
 props="Many small round clay oil lamps, mostly unlit at first, lit one by one by the farmer with a thin burning stick. One round clay bowl with a woven cover, brought by the healer and shared.",
 first="The lamp flame from the previous shot becomes one lit clay lamp on the steps; the farmer kneels beside it holding a thin burning stick.",
 b=["The farmer moves along the steps lighting lamp after lamp with the thin burning stick; a row of warm flames multiplies.",
    "The healer arrives from the left carrying the covered bowl and sets it on the step; the farmer stands and greets him with both palms pressed together, and the healer returns the gesture.",
    "They sit side by side on the steps; the healer lifts the woven cover and warm steam rises; they share the food and the farmer laughs; small icon-only hearts drift up between them and fade."],
 vo=["When you fell, the village caught you.", "The healer, your neighbors, the shared bowl of food.", "People were the safety net."],
 music="Warm and full.",
 sfx="small flames flickering, footsteps, the woven cover lifting, gentle laughter with no words.",
 final="The farmer stands up from the step and starts walking right toward the terrace edge; the healer stays seated with the bowl; the lamps keep burning.",
 neg="Neither character speaks or lip-syncs; no neighbors or other people are visible.")

clip(n=17, stage="Ultimate Truth Revelation", cast="F",
 setting="A terrace-edge overlook just beyond the farmhouse at dusk deepening into night: the dark grassy hillside in the foreground, and below a wide dark valley dotted with tiny warm lamp lights from distant houses, under the first stars.",
 palette="Deep night blue with tiny warm valley lamps, and cool pale glowing icons that fade.",
 comp="Silhouette of the farmer at right-center; the valley spreads across the lower frame; the farmhouse window glows at left.",
 props="None carried.",
 first="The farmer walks in from the left and stops at the terrace edge, looking out over the valley.",
 b=["Silhouette composition: the farmer stands at the terrace edge at right-center as tiny valley lamps twinkle below.",
    "Cool glowing icon-only ghost symbols of a mobile phone, a clock and a medical cross float slowly up out of the valley, drift past him and away into the sky, fading.",
    "He turns back to the left toward the farmhouse; the last fading icon dissolves into the warm hearth glow from the farmhouse window."],
 vo=["They had almost nothing we have:", "no phone, no clock, no clinic.", "But they had something we keep losing."],
 music="The theme begins to soften.",
 sfx="night insects, a soft breeze.",
 final="The warm glow of the farmhouse window fills the center of the frame.",
 neg="The icons are plain silhouettes: the phone has a blank screen and the clock has no numbers.")

clip(n=18, stage="Elevation & Discussion", cast="F",
 setting="The same farmhouse interior where the story began, at night: low wooden beams, the earthen hearth at left-center with a calm steady fire, the woven straw mat, and the tiny square window in the back wall showing stars; as the camera pulls out, the thatched roof, the terraced hillside, the starlit valley and snow peaks under a clear night sky.",
 palette="Calm firelight amber inside, deep starry night blue and silver snow peaks outside.",
 comp="Mirror the opening: hearth at left-center, window at center; the final wide shot places the glowing window small at lower center under a wide sky.",
 props="A few dry sticks beside the hearth; the farmer feeds one into the fire.",
 first="Through the warm window glow: the farmer sits cross-legged by the calm hearth, relaxed, mirroring the very first scene.",
 b=["Medium shot mirroring the opening scene: the farmer, calm and content, feeds a dry stick into the hearth fire; the flames brighten gently.",
    "The camera pulls back slowly past him, through the tiny window and out over the thatched roof.",
    "Wide final shot of the starlit valley, the dark terraces and the glowing snow peaks, with the one small warm farmhouse window glowing; hold steadily on this final image."],
 vo=["No hospitals, but each other.", "We have hospitals, and scroll alone.", "So what did we lose, and what did we gain?"],
 music="The theme resolves on its final soft sarangi phrase.",
 sfx="gentle fire crackle fading, a night breeze.",
 final="A still wide shot of the starlit valley with one glowing farmhouse window, held steady for the end card.",
 neg="")

APPROVED = {
1:"You wake before dawn. No light switch. No clock. No doctor. Eighteen-fourteen, the hills of Nepal. Would you last a week?",
2:"We like to picture old village life as simple and peaceful. Fresh spring water, clean mountain air, no stress at all.",
3:"But simple never meant easy. Before the sun clears the peaks, you are already behind the plow, and every furrow is yours.",
4:"There is no shop, no sack of flour. Every meal begins with your own two hands, stone grinding on stone.",
5:"Here is what nobody tells you: much of your day just feeds the fire and the animals. Firewood, fodder, then the climb home.",
6:"Inside, you count the baskets of grain. The harvest is still months away, and every handful must last until then.",
7:"Then the monsoon arrives. The same rain that feeds your fields can wash them down the mountain in a single night.",
8:"And then, you fall sick. A fever burns through the night. No hospital. No pills. Nobody is coming from outside.",
9:"But the village has its healer. With his drum, his prayers and his herbs, he is doctor, priest and comfort, all at once.",
10:"You live. And you learn: knowledge here lives in people, not in books. Lose the old healer, and you lose it all.",
11:"Then word comes up the trail. The kingdom is at war on its far borders, and young men like you may be called.",
12:"Months later, the terraces turn gold. You cut the rice yourself. The reward is real, and you can hold it.",
13:"Then you shoulder the extra grain and walk for days toward the high passes, to trade it for Tibetan salt.",
14:"And here is the hard truth: nothing was given to you. Every comfort, even salt, was carried on your own back.",
15:"And yet, when the festivals came, people did not just rest. They flew. Joy was not a luxury. It was survival.",
16:"When you fell, the village caught you. The healer, your neighbors, the shared bowl of food. People were the safety net.",
17:"They had almost nothing we have: no phone, no clock, no clinic. But they had something we keep losing.",
18:"No hospitals, but each other. We have hospitals, and scroll alone. So what did we lose, and what did we gain?",
}

def build(c):
    p = []
    p.append(OUTPUT)
    p.append(STYLE + " Setting for this clip: " + c["setting"])
    chars = [CAST_TEXT[c["cast"]], "The farmer: " + FARMER]
    if "H" in c["cast"]: chars.append("The healer: " + HEALER)
    if "O" in c["cast"]: chars.append("The oxen: " + OXEN)
    p.append("\n\n".join(chars))
    p.append("Palette and mood: " + c["palette"] + " " + PALETTE_BASE)
    p.append(COMP + " " + c["comp"])
    p.append("Movable props: " + c["props"])
    p.append("First frame: " + c["first"])
    p.append("Timed visual beats:\n- [0–3s] (narration part 1): " + c["b"][0] +
             "\n- [3–7s] (narration part 2): " + c["b"][1] +
             "\n- [7–10s] (narration part 3): " + c["b"][2])
    p.append(DIALOGUE_RULE + "\nPart 1 [0–3s]: \"" + c["vo"][0] + "\"\nPart 2 [3–7s]: \"" + c["vo"][1] + "\"\nPart 3 [7–10s]: \"" + c["vo"][2] + "\"")
    p.append("Narrator voice: " + VOICE)
    bgm = BGM_1 if c["n"] == 1 else BGM_N
    p.append(bgm + " Arrangement in this clip: " + c["music"] + " Sound effects: " + c["sfx"] + " " + MIX)
    p.append("Final frame: " + c["final"])
    p.append(NEG + ((" " + c["neg"]) if c["neg"] else ""))
    return "\n\n".join(p)

# ---------- checks ----------
errs = []
assert len(C) == 18
for c in C:
    joined = " ".join(c["vo"])
    if joined != APPROVED[c["n"]]:
        errs.append(f"clip {c['n']} VO mismatch:\n  {joined}\n  {APPROVED[c['n']]}")
prompts = {c["n"]: build(c) for c in C}
for n, t in prompts.items():
    if t.count(VOICE) != 1: errs.append(f"clip {n} voice block count")
    if t.count(FARMER) != 1: errs.append(f"clip {n} farmer block")
    if re.search(r"#[0-9a-fA-F]{3,6}\b|\bRGB\b|\bHSL\b|Pantone", t): errs.append(f"clip {n} color notation")
    if re.search(r"same (character|narrator)", t, re.I): errs.append(f"clip {n} shortcut")
    if re.search(r"\d{4}", t.replace("720p","").replace("0–3s","").replace("3–7s","").replace("7–10s","")):
        errs.append(f"clip {n} contains a 4-digit number")
for n in (9, 10, 16):
    if HEALER not in prompts[n]: errs.append(f"clip {n} missing healer")
for n in set(prompts) - {9, 10, 16}:
    if HEALER in prompts[n]: errs.append(f"clip {n} has healer")
if errs:
    print("\n".join(errs)); sys.exit(1)

words = sum(len(APPROVED[n].split()) for n in APPROVED)
print("checks passed; VO words:", words, "; prompt lengths:", [len(prompts[n].split()) for n in sorted(prompts)])

# ---------- document ----------
STITCH = [
 (1,2,"The farmer steps out of the door moving right into blue dawn → he enters the spring scene from the left, moving right."),
 (2,3,"He climbs right with the full pot as the sun breaks → he arrives at the terraces with the pot and sets it down."),
 (3,4,"An ox wipes the frame brown → the wipe clears on the courtyard. Cut on the most fully brown frame."),
 (4,5,"The camera rises with the circular motion to a tree canopy → the forest canopy match-cut."),
 (5,6,"He exits right under the full basket → cut to the loft ladder (different room; the basket intentionally stays outside)."),
 (6,7,"Rain starts on the thatch and he looks up → the monsoon downpour on the terraces (approved return)."),
 (7,8,"White lightning flash → out of the white onto the dusk path. Cut both clips on their brightest white frame."),
 (8,9,"Push into the warm doorway light → the warm hearth interior (approved return)."),
 (9,10,"Sparks dissolve into pale light → pale dawn mist at the healer's hut."),
 (10,11,"He walks right onto the ridge path → he enters the ridge from the left."),
 (11,12,"Leaf swirl fills the lens → leaves clear on the golden harvest. Time jump: months later (approved return to the terraces)."),
 (12,13,"He puts on the full basket, ready to walk right → he climbs the mountain trail with the basket."),
 (13,14,"He sets the basket down at the overhang at sunset → night at the same overhang, by the fire."),
 (14,15,"Shooting-star arc → the swing arc. Time cut: festival season. Align the arcs."),
 (15,16,"Lamp flame at the center of the golden sky → the same flame becomes the first lamp on the steps."),
 (16,17,"He walks right toward the terrace edge → he arrives at the overlook from the left."),
 (17,18,"The last icon dissolves into the window glow → through the window glow into the hearth (callback to clip 1)."),
]

md = []
md.append("# Phase B: Omni Flash Prompt Package")
md.append("*Could You Survive 1814 Nepal?* · 16:9 · 3:00 · 18 clips · Style 4 Cozy Storytelling\n\nBuilt from the approved `phase-a.md`. Each prompt below is **self-contained**: copy one code block into Gemini Omni Flash per clip.")
md.append("## 1. Global continuity block (review summary)")
md.append(f"""- **Format:** 16:9, 720p target, 24 FPS, about 10 s per clip, 18 clips, synchronized audio.
- **Style:** Style 4 Cozy Storytelling, full-color 2D cartoon. Each segment gets a new setting. Approved returns: house interior (clips 1, 9, 18), terraces (clips 3, 7, 12), house exterior (clips 4, 16).
- **Cast:** the farmer in all clips; the healer in clips 9, 10 and 16; the oxen in clip 3. No other people. The full design blocks are repeated verbatim in every prompt where each character appears.
- **Palette:** plain color words only. Cool dawn blue-gray, terrace green and gold, monsoon slate gray, firelight amber, snow-white and sky blue. The rust-red sash is the farmer's signature color.
- **Narrator:** an elderly grandfather with a light Nepali accent. The full voice block is repeated verbatim in all 18 prompts.
- **Music:** one sarangi, bansuri and madal theme. Clip 1 establishes it, and clips 2–18 continue it at identical tempo, key and instrumentation, changing only the arrangement density.
- **Continuity:** left-to-right journey direction, props tracked with their owners, and named wipes and match cuts. Time jumps after clip 11 (months later) and before clip 15 (festival season).
- **Text:** none on screen. The overlays in §4 are added in post-production.""")
md.append("## 2. Prompts")
for c in C:
    md.append(f"### Clip {c['n']} · {(c['n']-1)*10//60}:{(c['n']-1)*10%60:02d}–{c['n']*10//60}:{c['n']*10%60:02d} · {c['stage']}")
    md.append("```text\n" + prompts[c["n"]] + "\n```")
md.append("## 3. Stitching guide")
md.append("| Cut | What carries across |\n|---|---|\n" + "\n".join(f"| {a} → {b} | {t} |" for a,b,t in STITCH))
md.append("""**Assembly notes**
- Inspect every join in the actual footage. A requested wipe or flash may not land on the last generated frame, so trim to the best usable frame instead of the final one.
- Use a short audio crossfade of about 4–6 frames on music at every cut. Never crossfade through the middle of a narrated word.
- If the music drifts between clips, the cleanest fix is one continuous background track laid under the whole edit, keeping each clip's narration and sound effects.
- Hold the last frame of clip 18 for 2–3 extra seconds for the end card.""")
md.append("## 4. Post-production overlays (not in prompts)")
md.append("| Clip | Overlay | Placement |\n|---|---|---|\n| 1 | NEPAL, 1814 | lower-left |\n| 11 | 1814: KINGDOM AT WAR | upper-right sky |\n| 12 | MONTHS LATER | upper-left |\n| 18 | WHAT DID WE LOSE? | center-lower |\n| 18 (end card) | TELL US BELOW | under the previous overlay |")
md.append("## 5. Voice and music continuity note")
md.append("""- All 18 prompts contain the identical full narrator block. There are no "same narrator" shortcuts, and no clip gives a conflicting voice direction.
- Prompt compliance is not the same as audio consistency. **Listen** to the generated clips side by side and compare identity, timbre, register, accent, pace, texture and recording sound.
- If one clip sounds like a different person, first check its prompt was pasted complete. Then regenerate only that clip, keeping everything else fixed.
- If voice matching across 18 independent generations still isn't good enough, the fallback is to record or generate **one continuous external voiceover** of the approved narration and lay it over the edit. The script is in `phase-a.md`.
- The elderly Nepali-accented profile hasn't been tested with the provider; only the skill's male baritone block has been confirmed by listening. Treat clips 1–3 as a test batch before generating the rest.""")
md.append("## Phase B checks")
md.append(f"✅ Phase A approved · ✅ exactly 18 standalone prompts · ✅ every prompt repeats ratio, style, character, palette, voice, audio, transition and negative locks · ✅ narration in each prompt exactly matches Phase A ({words} words; checked by script) · ✅ narration audio-only and never displayed · ✅ no technical color notation · ✅ identical voice block in all 18 prompts · ✅ healer only in clips 9, 10 and 16 · ✅ three timed beats with ≥4 devices per clip · ✅ every cut named in the stitching guide · ✅ overlays kept separate")
open(OUT, "w").write("\n\n".join(md) + "\n")
print("wrote", OUT)

# ---------- compact prompts (<= 4000 chars, for API tools with a prompt limit) ----------
FARMER_C = ("The farmer: a young adult man drawn as a minimalist 2D cartoon: white filled circular head, two small dark oval eyes, simple eyebrow strokes, short curved mouth, small plain dark-brown cloth cap; off-white crossover cotton tunic to mid-thigh with elbow-length sleeves, loose off-white trousers narrowing at the ankles, plain rust-red waist sash; forearms, hands and lower legs are dark single-line strokes of constant medium weight, small dark rounded hands, barefoot. Same proportions, outfit and line weight in every shot; exactly two arms and two legs, and a moving limb replaces its previous pose.")
HEALER_C = 'The healer: an older man in the same drawing style, slightly shorter and stooped: white filled round head, small dark oval eyes, thick white eyebrows, short white beard, calm mouth; tall upright peacock-feather crown on a cloth headband, long plain white robe, deep red sash, long dark-brown bead necklace; dark single-line limbs, small rounded hands, barefoot. Exactly two arms and two legs.'
OXEN_C = "Two identical simple cartoon oxen: warm brown bodies, short curved light horns, dark dot eyes, stick-like legs, yoked by one wooden beam."
VOICE_C = ("Narrator: one off-screen elderly man of about seventy, clear English with a light, gentle Nepali accent; warm, deep, slightly weathered low voice with rich chest resonance and a soft touch of gravel, no breathiness; slow, unhurried fireside storytelling with gentle pauses and a steady pace; close, dry studio sound. Keep this exact voice throughout; no character dialogue.")
STYLE_C = '10-second 16:9 clip with synchronized audio. Cozy Storytelling style: full-color 2D cartoon, clean contours, soft natural light, cinematic framing; a Nepali hill village in the early nineteenth century. Identical character design and constant line weight. Not sketchbook, photoreal or 3D.'
MUSIC1_C = "Music: gentle Nepali folk theme on sarangi with soft bansuri flute and a light madal hand-drum pulse, slow warm tempo."
MUSICN_C = 'Music: continue the identical Nepali folk theme from clip 1 (sarangi, soft bansuri, light madal pulse), same tempo, key and instruments.'
DIAL_C = 'Audio-only voiceover (no speech bubbles, captions or subtitles): the narrator speaks exactly the quoted words once, in order.'
NEG_C = 'Avoid: photorealism, 3D CGI, realistic eyes or hair, extra or duplicated limbs, changing proportions or line weight, other people, any visible text, letters, numbers, logos, speech bubbles, lip-sync, liquid morphing, modern objects except icon-only symbols.'
CAST_C = {"F": "Only one person appears: the farmer.", "FO": "Only one person appears, the farmer, plus exactly two oxen.", "FH": "Exactly two people appear: the farmer and the healer."}

def build_c(c):
    p = [STYLE_C,
         "Setting: " + c["setting"] + " Mood: " + c["palette"] + " Layout: " + c["comp"],
         CAST_C[c["cast"]] + " " + FARMER_C + ((" " + HEALER_C) if "H" in c["cast"] else "") + ((" " + OXEN_C) if "O" in c["cast"] else ""),
         "Props: " + c["props"],
         "Start: " + c["first"],
         DIAL_C,
         "[0–3s] VO \"" + c["vo"][0] + "\" " + c["b"][0],
         "[3–7s] VO \"" + c["vo"][1] + "\" " + c["b"][1],
         "[7–10s] VO \"" + c["vo"][2] + "\" " + c["b"][2],
         "End: " + c["final"],
         VOICE_C,
         (MUSIC1_C if c["n"] == 1 else MUSICN_C) + " " + c["music"] + " SFX: " + c["sfx"] + " Voice-first mix.",
         NEG_C + ((" " + c["neg"]) if c["neg"] else "")]
    return "\n\n".join(p)

compact = {c["n"]: build_c(c) for c in C}
over = {n: len(t) for n, t in compact.items() if len(t) > 4000}
print("compact lengths:", [len(compact[n]) for n in sorted(compact)])
if over: print("OVER 4000:", over); sys.exit(2)
for n, t in compact.items():
    assert t.count(VOICE_C) == 1 and t.count(FARMER_C) == 1
    assert (HEALER_C in t) == (n in (9, 10, 16))
    assert " ".join(re.findall(r'VO "(.*?)"', t)) == APPROVED[n], n
    assert not re.search(r"\d{4}", t)
cm = ["# Compact prompts (≤ 4,000 characters)", "Same content as `phase-b-prompts.md`, condensed for tools with a 4,000-character prompt limit, such as the vidIQ Omni Flash tool. The character, voice and music blocks are identical across all 18 prompts."]
for c in C:
    cm.append(f"### Clip {c['n']} · {c['stage']} · {len(compact[c['n']])} chars")
    cm.append("```text\n" + compact[c["n"]] + "\n```")
open(OUT.replace("phase-b-prompts.md", "phase-b-compact.md"), "w").write("\n\n".join(cm) + "\n")
print("wrote compact")
