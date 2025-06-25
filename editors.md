---
title: Editor integrations
layout: default
---


Tamarin is supported through plugins, extensions, and syntax definitions for several editors. Below you can find extensions for Visual Studio Code, VIM, Emacs, [Sublime Text 3](#sublime-text-3), Notepad++, and Atom.

The source code of some of these extensions can be found Uunder the [etc](https://github.com/tamarin-prover/tamarin-prover/tree/develop/etc) folder contained
in the Tamarin Prover project.


## VSCode

Tamarin has an official plugin for [Visual Studio Code](https://code.visualstudio.com/) providing
syntax highlighting, detection of syntax errors, and numerous wellformedness checks. It is available from the
[VSCode marketplace](https://marketplace.visualstudio.com/items?itemName=tamarin-prover.tamarin-prover)
or from [Open VSX](https://open-vsx.org/extension/tamarin-prover/tamarin-prover).
Its source code can be found in [vscode-tamarin](https://github.com/tamarin-prover/vscode-tamarin) repository.


## VIM

#### Using Vim plugin managers

This example will use [Vundle](https://github.com/VundleVim/Vundle.vim) to install the plugin directly
from this repository. The instructions below should be translatable to other plugin managers.

1. Make sure you installed Vundle (or your favorite plugin manager)
2. Put the below, or equivalent instructions, into your `.vimrc`:

```vimrc
Plugin 'tamarin-prover/editors'
```
3. Restart Vim or reload the configuration
4. Run the Vim command `:PluginInstall` (or equivalent)

You can install updates through `:PluginUpdate`.

#### Manual installation (not recommended)

If you install the Vim support files using this method, you will need to keep the files up-to-date yourself.

1. Create `~/.vim/` directory if not already existing, which is the typical location for `$VIMRUNTIME`
2. Copy the contents of `etc/vim` to `~/.vim/`, including the folders.

## Sublime Text 3

[editor-sublime](https://github.com/tamarin-prover/editor-sublime) is a plug-in developed for the Sublime Text 3 editor. The plug-in has the following functionality:
- Basic Syntaxes
- Snippets for Theories, Rules, Restrictions and Lemmas

editor-sublime can be installed in two ways:

The first and preferred method is with [PackageControl.io](https://packagecontrol.io/). editor-sublime can now be installed via the sublime package manager. See the [install](https://packagecontrol.io/installation) and [usage](https://packagecontrol.io/docs/usage) documentation, then search and install Tamarin​Prover.

Alternatively it can be installed from source. For Linux / macOS this process can be followed. We assume you have
the `git` tool installed.

1. Change Directory to Sublime Text packages directory:
    + macOS: `cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/`
    + Linux: `cd ~/.config/sublime-text-3/Packages/`

2. Clone the directory into the Packages folder.
    + SSH: `git clone git@github.com:tamarin-prover/editor-sublime.git`
    + HTTPS: `git clone https://github.com/tamarin-prover/editor-sublime.git`

3. Close and re-open Sublime, and in the bottom right list of syntaxes 'Tamarin' should now be in the list.

*Please be aware that this plugin is under active development and as such, several of the features are still implemented in a prototypical manner. If you experience any problems or have any questions on running any parts of the plug-in please [visit the project GitHub page](https://github.com/tamarin-prover/editor-sublime).*

## Notepad++

Follow steps from the [Notepad++ Wiki](http://docs.notepad-plus-plus.org/index.php/User_Defined_Language_Files#How_to_install_user_defined_language_files) using the [notepad_plus_plus_spthy.xml](https://github.com/tamarin-prover/tamarin-prover/blob/develop/etc/notepad_plus_plus_spthy.xml) file.

## Emacs

The [spthy.el](https://github.com/tamarin-prover/tamarin-prover/blob/develop/etc/spthy-mode.el)
implements a SPTHY major mode. You can load it with `M-x load-file`, or add it to your `.emacs` in
your favourite way.

## Atom

The [language-tamarin](https://atom.io/packages/language-tamarin) package provides Tamarin syntax
highlighting for Atom. To install it, run `apm install language-tamarin`.

