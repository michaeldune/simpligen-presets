Hi Christopher, I looked through your logs and the connector. Your connection is fine, so disconnecting and reconnecting won't change anything.

The cause: the SimpliGen MCP has no Wardrobe tools yet. I checked the current app (1.84.0, the same version as yours) and the current connector (@simpligen/mcp 0.9.1, the one Claude Desktop runs). An agent can create and list characters, locations and products, but it has nothing that adds or edits a Wardrobe outfit. So Claude is telling you the truth: that part of the app is not exposed to agents. The upgrade didn't remove it; agents never had Wardrobe access.

Your logs agree. App and engine started normally, the agent API came up on its usual port, and there are no errors.

What works today:
- Add the outfit yourself in the Wardrobe. Claude can still help by writing the outfit's name and a detailed description for you to paste in.
- Claude can see your existing outfits by name (they show up in its list of subjects), but it can't open, change or create them.

@Sharmystic this is the gap, nothing wrong on Christopher's side. I'll send you the details.
