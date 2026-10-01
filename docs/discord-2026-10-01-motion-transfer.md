**New pack: MiniMax H3 Motion Transfer**
Same moves, new everything else. Put a dance or movement clip in Reference Video 1 and describe a new shot in the prompt: who it is, what they wear, where they are, how the camera sees them. SDPose reads a whole-body skeleton (body, hands, face, feet) from every frame of your clip, and the new Fun ControlNet for H3 holds the video to it, so only the motion carries over. The person, clothes, setting and lighting all come from your prompt.

How it behaves:
- Don't describe the moves, they come from the clip. Describe the person and the place: "a man in a black leather jacket and cargo pants dances on a neon-lit rooftop at night, full body, static camera".
- The video comes out in your clip's own shape and frame rate, so a vertical 30 fps phone clip stays vertical and plays at its real speed. The aspect ratio setting is ignored.
- It keeps your clip's soundtrack, trimmed to the video, so the dancing stays on the beat. Remove the soundtrack (or use a clip with none) and H3 makes upbeat instrumental dance music instead. Left to itself, H3 kept inventing a voice (singing, laughing, made-up words), so the card asks it for instrumental music.
- 5 to 10 seconds, taken from the start of the clip. About 3.5 minutes for 5 seconds at 480p on a 12 GB card; 10 seconds takes about 16 minutes, and a 10 second 1080p phone clip used nearly all of 32 GB of system RAM, so close other heavy apps for long clips.

Tips from testing:
- Works best with one or two people whose whole body is in frame and a steady camera.
- Long dresses, coats and baggy clothes hide the legs from the pose reader, so leg moves follow more loosely. Fast spins drift more than steps and arm moves.
- In our tests the pose held on every render, and the new video never borrowed the clip's background or clothing.

Needs Faster Attention ON (Settings > Advanced) and SimpliGen engine 0.38.0 or newer. 49.8 GB if you have no H3 pack yet, about 6.5 GB on top of any H3 pack. MiniMax H3 Community License; SDPose MIT; RT-DETR Apache-2.0. Use clips of people who have agreed to it.
