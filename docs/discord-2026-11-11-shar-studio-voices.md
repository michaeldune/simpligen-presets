Hey Shar, three related Video Studio asks around character voices.

1. A default voice on the character. The Studio already sends a cast member's `voice.path` to H3 as "Voice for <name>" (and puts voiced characters first), but nothing in 1.81.2 ever sets it: Character Studio has no voice field and the characters table has no column for it. None of the 95 cast entries in my films has one, so that path never fires. A "Voice sample" slot on the character screen, carried into every clip it's cast in, would switch it on.

2. The same over MCP. create_character has no voice argument and there's no tool to set one, so an agent can only lay a voice down as a timeline track with add_track. A voice argument on create_character (or a set_character_voice tool), plus the DELIVERY choice on shots in update_clip / apply_film_plan, would cover it.

3. A TTS step. Our IndexTTS 2.5 lip-sync cards can't join the Studio as packs: they read the line from quotes in the prompt and use audio_file as the voice to clone, while the Studio fills audio_file with the soundtrack. But the Studio already holds everything TTS needs per beat: the line, the speaker, their voice (once 1 exists) and DELIVERY (Calm, Cheerful, Whisper... maps neatly onto IndexTTS emotion text). Generating that line with the speaker's voice and laying it on the timeline as the clip's speak-mode audio would give real cloned dialogue that H3 lip-syncs to, and the audio stays editable on the timeline.

1 and 2 are small; 3 is the bigger one. Happy to test any of it.
