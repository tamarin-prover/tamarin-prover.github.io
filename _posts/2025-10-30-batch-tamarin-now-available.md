---
layout: post
title: <code>batch-tamarin</code> is now available
date: 2025-10-30 10:00 +0100
author: lmandrelli
---

`batch-tamarin` is a Python wrapper for Tamarin Prover that enables batch execution of protocol verification tasks with reproducibility features. Available now on [PyPI](https://pypi.org/project/batch-tamarin/). Blog post below!

## Context

If you've ever worked with Tamarin Prover, you know the pain of running large experiments. Whether you're comparing different prover versions, testing multiple models, or trying to reproduce someone else's results, you've probably ended up writing custom shell scripts that are hard to maintain and even harder to share.

Researchers have tried to solve this problem in different ways. Some tools like UT-Tamarin help with individual model development, while others like ANSSI's parser focus on specific analysis workflows. Many research groups even built their own Python wrappers for their papers. But these solutions are usually limited in scope—you might get good lemma-level testing, or nice parsing, or basic orchestration, but rarely all together in a way that works across different experiments.

That's exactly why `batch-tamarin` has been built. After observing researchers struggle with the same reproducibility issues over and over, it became clear that a unified solution was needed that could handle real-world research workflows: multiple models, different Tamarin versions, proper resource management, and results that are actually comparable. Instead of yet another paper-specific script, `batch-tamarin` aims to be the tool that works for any Tamarin experiment, making it easier to focus on the protocol analysis.

## Features

`batch-tamarin` provides a comprehensive solution for reproducible Tamarin workflow orchestration with the following key features:

- **Declarative Configuration**: Define experiments using JSON "recipes" that specify models, Tamarin versions, resources, and options with inheritance support for clean, maintainable configurations
- **Multi-Version Management**: Seamlessly work with multiple Tamarin Prover versions (1.4.0 through 1.10.0)
- **Intelligent Scheduling**: Choose from three scheduling policies (FIFO, SJF, LJF) to optimize resource usage and execution time based on your experimental needs
- **Per-Lemma Analysis**: Automatic parsing of SPTHY models enables fine-grained execution and reporting at the lemma level, with detailed telemetry for each proof attempt
- **Interactive Setup**: Use the `init` command to generate configuration files through guided prompts, making it easy to get started without manual JSON editing
- **Semantic Caching**: Avoid redundant computations with intelligent caching that considers model content, prover version, and execution parameters
- **Comprehensive Reporting**: Generate detailed reports in HTML, Markdown, LaTeX, or Typst formats with execution timelines, resource usage charts, and automatically rendered attack traces
- **Validation Tools**: Quickly verify model well-formedness and configuration correctness using the `check` command before launching long-running experiments
- **Rerun Support**: Automatically generate rerun recipes for failed lemmas, allowing easy parameter adjustment without reconfiguring the entire experiment
- **Cross-Platform Support**: Works on macOS and Linux

## Technical Details

A full report of the first version of `batch-tamarin`, including its architecture, design decisions, and implementation details is available in the GitHub repository [report](https://github.com/tamarin-prover/batch-tamarin/blob/f5350720bcde2d6e79a6e1b6200a2b88f3faa483/assets/internship-report.pdf), in addition to the documentation markdown in the root of the repository: [ARCHITECTURE.md](https://github.com/tamarin-prover/batch-tamarin/blob/main/ARCHITECTURE.md).

## Reproducibility ?

Yes, reproducibility was one of the main design goals for `batch-tamarin`. The tool provides Dockerfiles that can be used to build Docker images with all dependencies needed to run `batch-tamarin` with a preconfigured environment containing Tamarin Prover. Currently, version 1.10.0 and the latest development version are available with `batch-tamarin`. These Dockerfiles are available in the GitHub repository [here](https://github.com/tamarin-prover/batch-tamarin/tree/main/examples/__dockerfiles__/with-batch-tamarin).

Docker images are also available on DockerHub: [lmandrelli/tamarin-prover](https://hub.docker.com/r/lmandrelli/tamarin-prover) providing Tamarin Prover from version 1.4.0 up to 1.10.0, both for amd64 and arm64 architectures. The Dockerfiles used to build these images are available in the GitHub repository [here](https://github.com/tamarin-prover/batch-tamarin/tree/main/examples/__dockerfiles__/tamarin-only).

## Installation

Prerequisites:
- Python 3.10 or higher
- Tamarin Prover installed, preferably accessible in your system PATH

You can install `batch-tamarin` using pip:
```bash
pip install batch-tamarin
```
It will then automatically be available as a command line tool `batch-tamarin`.