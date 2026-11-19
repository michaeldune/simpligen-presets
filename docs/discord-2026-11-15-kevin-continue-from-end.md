@KevinLewis checked it, and you found a real gap on our side.

The two options in the clip's "How it starts":
- **Continue from the end of** starts the new clip on the exact last frame of the clip before. Any H3 card.
- **Continue the movement of** also carries the camera and action across the cut. LTX 2.5 only, on both clips, with no cast. It is greyed out on every H3 card, the official one too.

**Without a cast**, Continue from the end works on our community cards (Pika Flex, PRISM-PIKA, GXS v5, DMAD PDMD...). The clip goes through the pack's image-to-video card and starts on that last frame.

**With a cast** (shot with your cast), the clip always goes through the pack's reference card, and the app only hands it the last frame if that card says it can pin a frame. The official H3 cards and Midnight say so. None of our community packs did, so the app quietly dropped the last frame and the clip started fresh from the cast pictures. That's what you saw.

Fixed today. These now declare it: Pika Flex 1.0.8, PRISM-PIKA 1.0.8, GXS v5 1.0.4, DMAD PDMD 1.0.4, Turbo Accelerated 1.7.8, Heptagram v2 1.0.7, 10Eros beta7 fix1 1.0.6. They're in the store: click Update on the pack, then re-render the continuing clip. I filmed it on Pika Flex 1.0.8: before, the cast clip opened on a different shot; now it opens on the exact last frame. 8+2 can't do it (its second, full-size pass rejects the pinned frame).

Midnight already did this and runs at 8 steps, so it is a fast option too.

Either way, the last frame sets how the clip opens, not where it goes: describe the same camera move and outfit in the prompt.
