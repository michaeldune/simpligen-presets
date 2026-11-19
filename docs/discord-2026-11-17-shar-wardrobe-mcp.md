Shar, on Christopher's "MCP cannot access wardrobe" thread: it's a missing API surface, not his setup. His diagnostics show app 1.84.0, engine v0.44.0, agent API up on 48199, no errors (the control API doesn't log requests, so the failed ask itself isn't in there).

What I found in 1.84.0 and @simpligen/mcp 0.9.1:
- agentApi has routes for /characters, /locations, /products, /films, /subjects, but nothing for wardrobe. wardrobeService only has IPC handlers (wardrobeHandlers.js).
- 0.9.1's tools.js has no wardrobe or outfit tool.
- open_screen's enum (generate, gallery, characters, character, video-studio, prompt-library, settings) has no wardrobe screen either.
- GET /subjects DOES return wardrobe rows (type "wardrobe"), since wardrobeService upserts into the subjects spine. But the list_subjects description says "characters and products", so an agent sees outfit names and ids it can't use.

A matching set like locations/products would cover it: list_wardrobe, create_wardrobe_item (name, description, optional garment image via upload handle), maybe remove. It would also help if update_clip / apply_film_plan could take an outfit for a cast member, if the Studio supports that in the UI. Until then I've told him to add outfits by hand and let Claude write the descriptions.
