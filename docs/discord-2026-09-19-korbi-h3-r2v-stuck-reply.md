# SENT by Michael (confirmed 2026-09-21) — reply: H3 Reference-to-Video stuck on "Preparing the model on your Graphics card" (user "korbi", RTX 4080 SUPER 16 GB, 64 GB RAM, 2026-09-19)

_Not our preset (official MiniMax H3 GGUF pack). Michael to decide whether to post or hand to Sharmystic._

Thanks for the logs. Your PC isn't the problem; it's the size of the job.

Every Reference-to-Video run in your logs used the **low-VRAM (GGUF) preset at 1664×928, 15 seconds, 20 steps**.
928p sits above H3's native 768p, and at 15 s that's a very large video for 16 GB. The engine works out that the frames
themselves need nearly all of the card's memory, so it keeps **none** of the model on the GPU (the log says
`0.00 MB loaded, 13711 MB offloaded`). Every step then has to pull about 14 GB of model across from system RAM. Your
first run sat on step 0 of 20 for 39 minutes before you cancelled it, and the last one was still on step 0 when you
exported the logs.

That's also why the PC is quiet while Task Manager shows the GPU busy: the card is mostly waiting for data to arrive
from RAM, not doing heavy maths, so it draws little power and the fans stay low.

What should fix it:
1. **Resolution: 768p or lower.** 768p is H3's native size, and the tiers above it are flagged in the picker for a
   reason. Dropping from 928p to 768p cuts the pixels by about a third, which is often enough for the model to stay
   on the card.
2. **Duration: try 5-10 s first.** Longer clips cost more than their length suggests, because the model looks at all
   the frames together. Once a 768p 10 s run completes, you'll know what your card handles.
3. **Turn on Settings > Advanced > Faster attention.** It's off on your machine. It needs a one-time download of about
   20 MB and speeds up long clips noticeably on RTX cards.
4. **Worth trying: turn off Settings > Advanced > Reduce system RAM usage.** SimpliGen switches it on automatically
   for 16 GB cards, and your log shows it's active. It stops the engine reserving system RAM to stream models faster.
   With 64 GB of RAM you can afford that reservation, and streaming is exactly what these runs are stuck on. If other
   generations start running out of RAM, switch it back on.
5. **Let a cancelled run finish cancelling** before you start the next one. Your second run began with only 1.4 GB of
   VRAM free because the cancelled one was still holding it.

Image-to-Video taking about an hour for 15 s is most likely the same issue: a large resolution at 15 s. The same
settings should bring it down a lot.
