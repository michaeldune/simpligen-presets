Yes, and the reason nothing you add to the prompt works is that you are fighting it the wrong way round.

H3 generates audio for the **entire duration of the clip**, every time. It does not have the option of producing
nothing. So any stretch of time you have not given it something to put there, it fills, and what it reaches for is
speech. Telling it not to is a generator-directed instruction with no referent in the scene, which is why "no talking",
"do not speak", "silent" and negative prompts all slide straight off. The same way "keep it short" does nothing. You
cannot subtract the audio. You have to **claim the time with something else**.

Which clause you want depends on your case.

**Case 1: no dialogue at all, and they still mutter, sing or laugh.**

Ask for music, not silence and not ambience. Ambience alone was not enough in my tests, it reduced the voice but
gibberish words survived. Switching to an explicit instrumental track fixed it on 5 of 5 renders, including the two
seeds that had reliably sung before. Append this, adjusting only the genre:

```
The soundtrack is upbeat instrumental dance music with a strong steady drum beat, bass and brass, playing from
start to end; the dancing lands on the beat. The music has no vocals: no singing, no humming, no spoken words.
Every person's lips stay closed in a smile throughout.
```

Three parts doing three jobs: a positive description that occupies the whole duration, a no-vocals prohibition, and
a closed-lips end state so the mouth matches. Drop any one of them and it tends to come back.

**Case 2: you have a line, and it garbles or repeats after the line ends.**

Same cause. A single sentence is about six seconds of speech, so in a 13-second shot you have left roughly seven
seconds unclaimed, and it fills them by repeating and mangling your line. Three sentences fix it:

```
The instant that sentence ends, her lips close completely and all speaking motion stops. For the entire remainder
of the shot she stays silent with her lips closed and still, her hands resting on the desk. She speaks only once,
does not repeat any part of the line, and no further words or vocal sound occur.
```

That removed the invented words completely on a seed that had garbled twice before, leaving 6.4 seconds of held
silence.

Two things that look like they should work and do not, because they are the first things everyone tries:

- **Covering only the moment the line ends.** "When the dialogue ends she closes her mouth" does not remove the extra
  words, it **moves them later**, into the part of the clip you still have not claimed. You have to describe the
  leftover time, not just the hand-off into it.
- **Modal phrasing.** "She should close her mouth" is noticeably weaker than describing the closure as something that
  happens: "her lips close completely and all speaking motion stops".

The general rule, if you want one sentence to take away: **describe what the audio and the mouth are doing for every
second of the clip.** H3 only invents in the gaps you leave it.
