Hey Shar, a gap in the prompt-guide index that is hurting H3 users of the assistant. ein95charly in support says Astra/Opus prompts make H3 characters read the prompt aloud and talk in a jumble of languages.

The official H3 Turbo pack has no entry in https://www.simpligen.io/presets/prompt-guides/index.json and no promptFamily, so get_prompt_guide for minimax-h3-turbo-pack:minimax-h3-turbo-i2v returns family null, generic true. The generic guide tells the assistant to "put the spoken words in quotation marks", with nothing about <d>[Language] tags or the no-speech sentence. That is the recipe for both symptoms: quoted prose gets spoken, and unclaimed time gets filled with invented speech. minimax-h3-pack:minimax-h3-i2v gets the real minimax-h3-video guide, so it is only the mapping.

Missing from the index (official packs):
- minimax-h3-turbo-pack: t2v, i2v, r2v (checked in the app: generic)
- minimax-h3-two-stage-pack: t2v, i2v, r2v
- minimax-h3-tts-lipsync-pack: r2v
(The last two aren't installed here, so I could only see they're absent from the index, not test them.)

Mapping these to minimax-h3-video should fix it for everyone. A smaller tweak might also help: the generic guide's dialogue advice ("put the spoken words in quotation marks") is the opposite of what H3 wants, so any H3 card that falls through to generic gets steered wrong.
