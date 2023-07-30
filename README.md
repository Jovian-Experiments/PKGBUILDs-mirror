PKGBUILDs
=========

This repository hosts PKGBUILDs and image manifests as published by the vendor.
The PKGBUILDs are in per-package branches, and tagged for every version.

This repository also hosts a manifest history for the shipped images.

 - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/manifest/release
 - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/manifest/main

FAQ
---

### How do I link to a package or manifest?

If you want a link to the latest, use the branch name.

If you want a permalink, use the tag name.

**Never** link to a direct commit, ***this repository will be force-pushed to fix mistakes***, and to add new data.

Examples:

 - Branches:
    - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/jupiter-main/gamescope
    - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/manifest/main
 - Tags:
    - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/jupiter-main/gamescope-3.12.0-1.1
    - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/tree/manifest/main/20230727.1000


### How do I link to diffs?

Use the form `$tag^1...$tag` (using the same tag name here) in the compare URL.

 - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/compare/

This way, if a missed revision appears, it will be updated accordingly.

Example:

 - https://github.com/Jovian-Experiments/PKGBUILDs-mirror/compare/manifest/main/20230727.1000%5E...manifest/main/20230727.1000


NOT FAQ
-------

### How?

Through a yet to be published tool.


### But why?

To ensure we don't miss changes that happens only through packaging changes.


### license?

¯\\\_(ツ)\_/¯
