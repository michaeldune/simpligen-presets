Shar, I think a Studio clip isn't sending the look's picture. Found it while filming a tutorial on 1.84.0.

What I did: made a look for Lori from a Wardrobe outfit (Mini Dress), filled all three views ("Ready for the studio"), cast Lori and the Mailbox street location in a new film, and rendered one clip locally on the official H3 Reference to Video card. In the clip editor, "Look in this clip: Mini Dress" was set, and both "Send the look picture too (+1 picture)" and "Send the look's words" were ticked.

What went out (generations row c091aa3a-e8bb-4b48-a3de-18d06b308b6a):
- referenceImages has two entries: "Lori" is her base portrait (896x1152, sweater and jeans) and "Mailbox street" is the location picture. None of the three look views is there.
- The prompt has the look's words: "<Subject 1> is Lori, the person in <Picture 1>, a woman, wearing This blue mini dress has a delicate white..."

So the dress reached H3 as words only, while Picture 1 shows her in a different outfit. The clip still looked close because the outfit description is detailed, but a plainer description would probably lose the dress to the sweater in the picture.

Expected: with the look picture ticked, I'd expect the look's front view (or portrait) to go in as Lori's picture, or as a third reference.

Small one in the same line: "wearing This blue mini dress has..." reads oddly because the outfit description starts with a full sentence. Something like "wearing an outfit described as: ..." would read better.

Happy to rerun anything if it helps.
