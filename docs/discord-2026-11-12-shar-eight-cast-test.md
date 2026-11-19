Tested the 8-person H3 cast in Studio 1.3.0 like you asked. It works. Official H3 R2V, 480p, 8 characters plus a location in one 6 s clip: all 9 pictures reached the engine, all eight stood in the order I wrote for the whole clip, no identity swaps, and actions landed on the right people. About 4 min per take on my 4070 Ti.

One bug, with multi-word names. If a shot says "@Coach Eli", he comes out as "[image 2]" in the prompt H3 gets, not <Subject 2>, and he's left out of the automatic "Wide shot framing ..." line. I swapped the cast order to rule out the first slot: Mama first was fine, Coach Eli second broke again. One-word names are all fine.

What I think happens in 1.82.1:
1. castSlug turns "Coach Eli" into coacheli, so his token is @coacheli.
2. rewriteCastTokens only matches the slug or an alias, so "@Coach Eli" stays as plain text, and the framing line misses him for the same reason.
3. Later, applyToPrompt sees "@Coach Eli" as a picture label and rewrites it to "[image 2]".

Possible fix: add the lowercased full name as an alias when it differs from the slug. The match is already case-insensitive and escapes the name, so "@Coach Eli" would then resolve. Typed by hand or written over MCP, the spaced form is what people will write.

Two smaller things:
- The MCP descriptions for update_clip, update_film_settings and apply_film_plan still say "At most two" cast, though update_clip accepted eight.
- A Studio take is saved under whichever project is open in the gallery when it renders, not the film's project. My first take landed in a different project from its film.
