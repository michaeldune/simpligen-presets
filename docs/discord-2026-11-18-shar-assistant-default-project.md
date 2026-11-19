Shar, a small one from making the tutorials today (app 1.84.0, engine v0.45.0): the built-in Assistant saves its pictures to the Default Project, not the project that's open.

Steps:
1. Open a project other than Default (mine is called "Claude") and go to the Gallery.
2. Open the Assistant (Claude Code) and ask it to make a picture, e.g. "the same red rowing boat at night under a full moon, Z-Image Turbo, on this PC".
3. Approve the card ("Free, runs on your GPU").

What happened: the job (8eeb2cc0-c7d2-40c9-acfc-e2de97d014f9, z-image-pack z-image-turbo-int8) has project_id "default" and the file went to F:\SimpliGen\output\z-image-packz-image-turbo-int8\ instead of output\claude\. It never showed in the open project's gallery. The Assistant even said so itself in its reply: "It was saved to the default project, not the project the original is in."

Probably related: an MCP get_status call a few minutes earlier, with "Claude" open in the sidebar, returned activeProject = Default Project. So the agent side seems to read a different "active project" than the one the UI shows. When an outside agent passes the project id to generate, it lands in the right place (same prompt, job da035190-918b-4262-98fa-a2236b6f1b65 went to output\claude\), so it looks like only runs that don't name a project are affected.

Expected: with no project named, Assistant and agent runs go to the project that's open in the app, and get_status reports that one.
