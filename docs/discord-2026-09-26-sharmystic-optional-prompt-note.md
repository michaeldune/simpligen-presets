# Note draft — let a preset make the prompt optional (to Sharmystic, 2026-09-26)

SENT by Michael to Sharmystic, 2026-09-26 ~18:06. Reply ~18:14: likes the idea; no commitment to a flag name or release yet.

---

Small request. Generate always wants a prompt ("Please enter a prompt first"; the MCP returns `needs_prompt`), even on a card whose instruction is already built into its workflow. We have several like that now: Qwen Image 2.1 Cutout, Character Sheet, Enhance to 4MP, and the new Head Swap and Outfit Swap cards. Each one bakes in the brief and appends `{{prompt}}` only as extra notes, so the user has nothing to say and types "head swap" just to get past the check.

Could a preset declare the prompt optional? Something like `"promptOptional": true` in the media block, which would skip the empty-prompt check and send `{{prompt}}` as an empty string. The cards already handle an empty value; we tested them that way by direct submission.
