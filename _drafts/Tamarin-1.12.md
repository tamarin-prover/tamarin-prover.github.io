---
layout: post
title: Tamarin 1.12 released
date: 2026-03-09 10:00 +0100
author: cas, jannik, ralf
---

Tamarin 1.12 is now available with many quality of life features, including:
- GUI improvements for dependency graph display:
  - now in zoomable format (SVG)
  - different levels of abstraction for better readability
  - attack graph display can be popped out into its own window (for full screen or multi display setups)
- Lemma editing inside the GUI
- Files can be reloaded from the GUI without having to restart Tamarin
- Better well-formedness messages (for fact usage, locks, etc.)
- Improvements to the Tamarin Manual
- Macros now also apply to lemmas and restrictions

On the more technical side, there are:
- Numerous improvements of the regression tests:
  - automated testing whether Tamarin can parse its own output
  - explicit testing for derivation checks which are now disabled for other tests
  - replaced oracles with tactics for regression tests
- Allow Maude up to 3.5.1
- Lots of refactoring
- Numerous bugfixes (in particular concerning parser, pretty printing, ...)
- Using stack LTS resolver 22.44 now

## New features

TODO: Add pictures!
