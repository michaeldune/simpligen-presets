Shar, a question from the LoRA tutorial (app 1.84.0, engine v0.45.0): what is the "+ triggers: beadsart" line under an added LoRA meant to do? It reads as if the app adds the trigger word to the prompt for you, but in my test the LoRA did almost nothing until I typed the word in myself.

Setup: official Krea 2 Turbo card, 1024x1024, 8 steps, seed 424242, same prompt each time ("A red fox sitting in a snowy forest clearing at sunrise, soft golden light through the pine trees."). LoRA "KR2 - Plastic Beads Art" (base model krea2, trigger "beadsart").

1. No LoRA: a photo of a fox (cdada42b-bdfe-44b7-b62c-88f47a4780f6).
2. LoRA at 1, word not typed: still nearly the same photo (a2b7ab47-3343-4d70-b498-6f5401608429).
3. LoRA at 1, "beadsart, " typed at the start: a full bead-art fox (e7fdb54b-3c6d-4a38-b7d5-e4446be88149).
4. Word typed, LoRA removed: a normal fox photo (93fe70e5-d7cf-47bd-acbe-2ba7243494e1).

In run 2 the stored prompt_content has no "beadsart", while user_loras carries "trigger_words":"beadsart","strength":1. So the job does receive the trigger words. I can't tell from my side whether the engine adds them to the prompt and the LoRA is just weak without them, or doesn't add them at all.

If it's only meant as a reminder, a word like "Trigger word (type it in your prompt): beadsart" would stop people thinking it's automatic. If it's meant to add the word, run 2 suggests it isn't reaching the prompt. Either way, one seed only, so take it as a pointer rather than proof.
