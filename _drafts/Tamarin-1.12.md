---
layout: post
title: Tamarin 1.12 released
date: 2026-03-09 10:00 +0100
author: cas, jannik, ralf
---

Tamarin 1.12 is now available with many quality of life features, including numerous GUI improvements for the display of dependency graphs:
  - Graphs are now in a zoomable format (SVG)
  - There are different levels of abstraction for better readability when zooming
  - The graphs can be popped out into their own window (for full screen or multi display setups)

Additional new features include:
  - Lemma editing inside the GUI
  - Files can be reloaded from the GUI without having to restart Tamarin
  - Better well-formedness messages (for fact usage, locks, etc.)
  - Improvements to the Tamarin Manual
  - Macros now also apply to lemmas and restrictions

On the more technical side, there is:
- Numerous improvements of the regression tests, including:
    - automated testing whether Tamarin can parse its own output
    - explicit testing for derivation checks which are now disabled for other tests
    - replaced oracles with tactics for regression tests
- Tamarin allows Maude up to version 3.5.1
- Lots of refactoring
- Numerous bugfixes (in particular concerning parser, pretty printing, ...)
- Using stack LTS resolver 22.44 now

## New features

TODO: Add pictures!
