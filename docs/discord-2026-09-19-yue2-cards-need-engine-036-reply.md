# SENT by Michael (confirmed 2026-09-21) — reply: Song + Album Art YuE2 cards fail on engine v0.34.2 (user "delav", RTX 3060, 2026-09-19)

Thanks for the logs, they made this quick.

**The YuE2 cards need a newer SimpliGen engine than the one you're on.** Song, Cover Song and Faithful Cover use the
YuE2 and SheetSage2 nodes, and those are part of ComfyUI itself from engine **v0.36.0**. You're on the **stable**
channel, where the newest engine is **v0.34.2**, which doesn't have them. That's why each run stops before it starts
with "Node 'Melody + chords score' not found" / "Node 'Transcribe the source melody' not found". Reinstalling the pack
won't change it. That's my fault: the pack should have said so up front.

What you can do:
- **Switch SimpliGen's engine updates to the beta channel** (Settings), update the engine to v0.36.0, then restart.
  The three YuE2 cards will run after that.
- Or **wait for v0.36 to reach stable**. The cards will start working then with no change on your side.

**The other two cards work on your current engine.** Your second Swap run finished fine at 12:51. The Swap run that
"failed" at 12:40 was stopped by the cancel button (the log shows the interrupt), so it wasn't a fault. The MiniMax
Music 3 card also works on v0.34.
