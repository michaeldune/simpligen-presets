Hi! Sorry it's been frustrating. This is fixable, and it comes from how the prompt is written, not from your install.

Two things cause it:

1. **H3 always makes a soundtrack.** If the prompt doesn't say exactly what is spoken and when, it fills the time with made-up speech, which comes out as nonsense or a mix of languages.
2. **H3 says quoted text out loud.** In a plain prose prompt, words in "quotes" (or text from the Dialogue box) get spoken, sometimes along with bits of the description.

H3 was trained on a structured format. Ask Astra or Opus to write the prompt like this:

```
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium shot of a woman in a grey coat by a rainy window. The camera pushes in with small amplitude at slow speed. The woman, with a calm low voice (S1), says: <d>[English] I'll be right back.</d> The instant the line ends her lips close, and she stays silent for the rest of the shot. Nobody else speaks or sings.

overall_soundscape: Rain on the glass, a clock ticking.

non_diegetic_music: N/A
```

The rules that fix your two problems:
- Spoken words go **only** inside `<d>[Language] ... </d>`, with a real language tag: [English], [French], [German], [Spanish] and so on.
- A shot where nobody talks ends with: *Nobody speaks or sings; every mouth stays closed.*
- Leave the Dialogue box empty when you use this format.
- No other quotation marks in the prompt.

Why the assistant gets it wrong: on some H3 cards (H3 Turbo and Two-Stage, for example) it is handed a general prompt guide instead of the H3 one, and that guide tells it to put lines in quotes. Pasting the example above into your request fixes that.

If you paste one prompt that gave you a bad clip and tell me which card you used, I'll rewrite it so you can compare.
