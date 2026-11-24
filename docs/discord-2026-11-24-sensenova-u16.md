**New pack: SenseNova U1.6**
SenseNova U1.6 is an 8B image model that reads and draws pictures in one network. It makes pictures of about 4 megapixels, it is very good at exact lettering, and it edits pictures from a sentence. Thanks to Russ44 for finding it.

**The three cards**
- **SenseNova U1.6**: text to image in 8 steps. Posters, signs, menus and infographics, as well as portraits and photo-style scenes.
- **SenseNova U1.6 Quality**: the same model at 50 steps, with more skin and fabric texture.
- **SenseNova U1.6 Edit**: give it a picture and say what to change. Add a second picture to borrow something from it, such as an outfit or a poster.

**What you need**
One 17.6 GB model file plus an 815 MB LoRA, downloaded from Hugging Face when you install the preset, so no Civitai key is needed. The text encoder is inside the model file. It runs on a 12 GB card and needs SimpliGen's engine at v0.46.0 or newer.

**How fast** (in the app, 12 GB RTX 4070 Ti, about 4 megapixels)
- Standard card: about 12 seconds.
- Quality card: about 80 seconds.
- Edit card: about 19 seconds, or 25 with two pictures.

**What we checked**
- Text in quotes came out letter for letter on 7 of 7 posters and infographics.
- Edits kept faces and untouched lettering in 10 of 10 tries, including a new headline on a poster and an outfit taken from a second picture.

**How to prompt it**
Write a full description in plain sentences: the kind of picture, the subject, the setting, the light and the layout. Put every word that should appear in the picture inside double quotes and say where it goes. A one-line prompt gives a plain result.

In the Preset Store after the next sync.
