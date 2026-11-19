Shar, one more from the tutorials (app 1.84.0, engine v0.45.0): on some cards the word " high." gets added to the end of the prompt. I first saw it on FLUX 3 Klein Edit, where the Final Prompt box and the stored prompt both end "...exactly as they are. high." (jobs eef9bf73-8214-4102-aac5-403e03035b14 and 3d634f9d-59ac-4fcf-b7d7-a9334e2a55fa).

It isn't only Klein. I went through the generations table: 4,381 stored prompts end in " high.", the oldest from 2026-06-26. Since 1 Nov, every image run with the suffix has quality = "high" in its metadata, and no run without that setting has it. So it looks like the quality value is being written into the prompt as a word.

Cards where I see it on quality = high runs since 1 Nov: FLUX 3 Klein Edit, Z-Image Turbo, Qwen-Image 2.1 Edit and Edit 4 MP, MiniMax H3-Image t2i, t2i 16 MP and Edit, and several Krea 2 finetunes (Kreamania, CyberRealistic, FinalCut, Muse, GodAgo, SickOllie).

Cards where quality = high runs do not get it: Krea 2 Turbo, Krea 2 Identity Edit, the Anima and Illustrious cards, and all the H3 video cards. I haven't worked out what those have in common.

It didn't visibly hurt the pictures I checked, but it's a stray word in the prompt, and on short prompts or tag-style models it could matter. It also shows in the Final Prompt box, so users see it and think they typed it.

Expected: the quality setting changes the render settings only, and the prompt stays exactly as typed (plus the card's own template text).
