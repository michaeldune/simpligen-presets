# Reply draft — eGPU disconnects mid-load (NUC8i7BEK + Thunderbolt 3 + RTX 3060 in an Orara enclosure, 2026-09-22) (SENT by Michael, confirmed 2026-09-23)

_Not our preset (official H3 Unlocked I2V). Hardware/link-level, not preset size._

Your logs say this isn't the preset and isn't a memory problem. The card leaves the bus while the model is being
loaded, and SimpliGen dies with it.

**What the logs show**

- At 19:23:11 you started H3 Unlocked I2V at 576x736, 5 s, 8 steps: small, as you said.
- At 19:23:15 the engine staged the H3 text encoder, 14956 MB, into a 12 GB card. That part is normal: SimpliGen
  streams the overflow from system RAM across the PCIe link for as long as the model is in use.
- From 19:23:18 the app's routine GPU status check slows from 0.5 s to 1.6 s and stays there. Something is already
  struggling to answer.
- At 19:23:59 the engine log simply stops. No CUDA error, no out-of-memory, no crash message. A software fault leaves
  an exception behind; a GPU that leaves the bus leaves silence.
- When you restarted, SimpliGen's own startup check said: `verdict=block reason=gpu-disappeared
  gpu="Intel(R) Iris(R) Plus Graphics 655"`. At that moment Windows only had the NUC's built-in graphics; your 3060
  was gone.
- The clincher: Windows' internal id for the GPU changed between the two runs (`03c6da42` then `0413c42e`). That only
  happens when the device is removed and re-added, not when a driver hiccups.

So: the enclosure link is dropping under sustained traffic. Your PSU wattage isn't the issue, and neither is the
preset, which is why LTX 2.3 failed the same way. H3 streams about 15 GB of model over Thunderbolt continuously, which
is a much harsher, longer test of that link than gaming or short bursts.

**What to check, in order**

1. **Confirm it in Event Viewer.** Windows Logs > System, at the minute it drops. Look for *Kernel-PnP* "was surprise
   removed", *nvlddmkm* errors, or *WHEA-Logger* PCI Express entries. Repeated WHEA PCIe entries mean the link itself
   is throwing errors, which points at the enclosure, port or controller rather than anything in software.
2. **Turn OFF Settings > Advanced > "Reduce system RAM usage".** It's on for you. It stops the engine reserving a
   block of system RAM for transfers, which makes the streaming use many small transfers instead of fewer large ones.
   On an internal card that's a fair trade; over Thunderbolt it's the harder pattern for the link. You have a large
   pagefile, so try it off.
3. **Stop the link from powering down.** Control Panel > Power Options > your plan > Change advanced settings > PCI
   Express > Link State Power Management = **Off**, and USB selective suspend off. In NVIDIA Control Panel set Power
   management mode to **Prefer maximum performance**. Link-state power saving is a common cause of eGPU drops.
4. **Thunderbolt firmware and settings.** In Thunderbolt Control Center set the enclosure to "Always Connect", and
   check Intel's NUC8i7BEK page for a Thunderbolt NVM/firmware update. TB3 firmware updates on that NUC generation
   fixed exactly this kind of drop.
5. **Isolate streaming from plain GPU load.** Run something that fits inside 12 GB (an image preset) for ten minutes.
   If that's rock solid and every model bigger than your VRAM drops, the trigger is sustained streaming across the
   link, which lines up with everything above.

One smaller thing: ten seconds before the GPU vanished, the app logged the machine losing internet
(`ERR_INTERNET_DISCONNECTED`). That may be unrelated, but if your network also runs through anything Thunderbolt or
USB, it hints at a controller-wide reset rather than the graphics card alone.

I can't fix this from the preset side: at 576x736 and 5 s you're already asking for very little. Anything that uses
H3 will stream that 15 GB encoder across the link.
