---
layout: post
title: Tamarin 1.12 released
date: 2026-03-08 10:00 +0100
author: cas, jannik, ralf
---

Tamarin 1.12 is now available with many quality of life features and GUI improvements, including reloading externally edited files, and new zoomable graphs, which can be popped out into a separate window, e.g., for multi-monitor use.

### Graph improvements
  - Graphs are now in a zoomable format (SVG)
  - There are different levels of abstraction for better readability when zooming
  - The graphs can be popped out into their own window, for example for full screen or multi-display setups

### Other GUI improvements
  - Lemmas can now be edited inside the GUI
  - Files can be reloaded from the GUI without having to restart Tamarin
  - Better well-formedness messages for fact usage, locks, etc.

### Additional new features
  - Improvements to the Tamarin Manual
  - Macros now also apply to lemmas and restrictions

### Backend improvements
- Numerous improvements of the regression tests, including:
    - automated testing whether Tamarin can parse its own output
    - explicit testing for derivation checks which are now disabled for other tests
    - replaced oracles with tactics for regression tests
- Tamarin now allows Maude up to version 3.5.1
- Lots of refactoring
- Numerous bugfixes, in particular concerning the parser and pretty printing.
- Updated to stack LTS resolver 22.44
