**New pack: Ming Image Design**
inclusionAI's Ming-Image 0.1 Design, a 6B model made for design work: app screens, web pages, posters, menus, infographics and ads, with the headlines, buttons and labels you ask for spelled right. Three cards, one 19 GB download, about 20-35 seconds a picture on a 12 GB card.

**Ming Image Design** - text to image at about 1 megapixel, about 20 seconds.
**Ming Image Design 4MP** - the same model at its native 2048 size, about 35 seconds. Icons, fine lines and small lettering come out cleaner.
**Ming Image Masked Edit** - change one part of an existing design and keep everything else exactly as it was. Picture 1 is the design, picture 2 is a mask: the same picture, black everywhere, painted white over the area to change (a white rectangle is enough). Then say what to change: Change the greeting to "Good evening, Sam".

Tips from testing:
- Brief it like a designer: the kind of page, the sections from top to bottom, the colours, and every piece of text in quotes (a button labelled "Pay Bills"). Quoted headlines, buttons and navigation came out right in every test.
- Long lists of short items (a menu, a price list) and small text the model adds on its own can slip a word or garble. Quote everything that matters, check the lettering, and re-roll the seed if a word slipped.
- Why the edit card needs a mask: Ming redraws the whole picture when it edits, and on its own it changed prices and small text nobody asked for on every seed we tried. The card pastes the edit back only inside the white area, so the rest stays pixel for pixel. Keep the white area tight: on a flat colour it can show as a faint box.
- It is not a photo model: people and photos come out flat.
- Pictures save as PNG with transparency.

Needs SimpliGen engine 0.38.0 or newer. MIT licence.
