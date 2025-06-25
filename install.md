---
title: Install Tamarin
layout: default
---

## Installation on macOS or Linux {#sec:maclinux}

The easiest way to install Tamarin on macOS or Linux is to use
[Homebrew](http://brew.sh/):

  * `brew install tamarin-prover/tap/tamarin-prover`

It's separately packaged for

  - Arch Linux: `pacman -S tamarin-prover`
  - Nixpkgs: `nix-env -i tamarin-prover`
  - NixOS: add `tamarin-prover` to your `environment.systemPackages`.

You can also [download binaries directly from GitHub](https://github.com/tamarin-prover/tamarin-prover/releases)
and [manually install dependencies yourself](#sec:dependencies), or [compile from source](#sec:LinuxSrcInstall).

## Installation on Windows 10 {#sec:windows}

You can install Tamarin (with GUI) under Windows 10 using the [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/windows/wsl/install-win10).
For performance and compatibility reasons, we recommend using WSL2 with Ubuntu.
Once you have WSL and Ubuntu installed, start the Ubuntu app and install Tamarin following the [installation instructions for Linux](#sec:maclinux) above.
You can then run Tamarin inside the the Ubuntu app using the usual command.
To use the interactive mode, start Tamarin inside the app and connect your usual Windows-run browser to [http://127.0.0.1:3001](http://127.0.0.1:3001).
Your Windows files are accessible inside the Ubuntu app via, e.g., `/mnt/c` for files on drive `C:`.

## Compiling from source {#sec:LinuxSrcInstall}

You don't need to compile Tamarin from source unless you are developing a new feature for it or you
want to use an unreleased feature. However, if you do want to install it from source:

### Manually install dependencies {#sec:dependencies}

Tamarin requires Haskell Stack to build and GraphViz and Maude (2.7.1 or newer) to run. The easiest way to
install these is

```
brew install tamarin-prover/tap/maude graphviz haskell-stack
```

Alternatively, you can install them yourself:

  - **Haskell Stack** Follow the instructions given at [Stack's install
    page](https://github.com/commercialhaskell/stack/blob/master/doc/install_and_upgrade.md). If you
    are installing `stack` with your package manager (particularly on Ubuntu), you must run `stack
    upgrade` afterwards, as that version of stack is usually out-of-date.

  - **Graphviz** Graphviz should be available using your standard package manager, or directly from
    <http://www.graphviz.org/>

  - **Maude** You can install Maude using your package manager (make sure to have version 2.7.1. or
    newer). You can also install Maude manually from the [Maude website]
    (http://maude.cs.illinois.edu/w/index.php/Maude_download_and_installation).
    In this case, you should ensure that your `PATH`
    includes the install path, so that calling `maude` runs the right version. Note that even though
    the Maude executable is movable, the `prelude.maude` file must be in the same folder that you
    start Maude from.

### Compile

Check out the source code with

```
git clone https://github.com/tamarin-prover/tamarin-prover.git
```

and you have the current development version ready for compilation. If you would prefer to use the
master version, just run `git checkout master`.

In either case, you can then run `make default` in the new directory, which will install an
appropriate GHC (the Glasgow Haskell Compiler) for your system, including all dependencies. The
`tamarin-prover` executable will be copied to `~/.local/bin/tamarin-prover`. Note that this process
will take between 30 and 60 minutes, as all dependencies (roughly 120) are compiled from scratch. If
you later pull a newer version of Tamarin (or switch to/from the `master` branch), then only the
tool itself needs to be recompiled, which takes a few minutes, at most.

Running Tamarin on a remote machine
---------------------------------

If you have access to a faster desktop or server, but prefer using
Tamarin on your laptop, you can do that. The cpu/memory intensive
reasoning part of the tool will then run on the faster machine, while you
just run the GUI locally, i.e., the web browser of your choice. To do
this, you forward your port 3001 to the port 3001 of your server
with the following command, replacing `SERVERNAME` appropriately.

```
ssh -L 3001:localhost:3001 SERVERNAME
```

If you do this, we recommend that you run your Tamarin instance on
the server in a [screen](https://www.gnu.org/software/screen/manual/screen.html) environment, which will continue
running even if the network drops your connection as you can later
reconnect to it. Otherwise, any network failure may require you to
restart Tamarin and start over on the proof.


# FAQ

#### How do I uninstall Tamarin using Homebrew?

To uninstall (and "untap" the Tamarin homebrew tap):

  * `brew uninstall tamarin-prover`
  * `brew untap tamarin-prover/tap`

#### What's with this `homebrew-science` tap?

Tamarin was previously distributed in the now-closed `homebrew-science` tap. If you have already
installed it through Homebrew, you may have to uninstall and untap that version first:

  * `brew uninstall tamarin-prover`
  * `brew untap homebrew/science`

#### After an update/pull/release Tamarin does not compile any more.

Try running `stack upgrade` and `stack update`. An out-of-date stack version can cause spurious
compilation errors.
