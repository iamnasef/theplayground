<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# zoxide

[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMTUuNDUiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAyMTUuNDUgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSIxMTUuMzEiIGhlaWdodD0iMzUiIGZpbGw9IiMwMDAwMDAiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSIxMTMuMzEiIHk9IjAiIHdpZHRoPSIxMDIuMTQiIGhlaWdodD0iMzUiIGZpbGw9IiM2OTY5NjkiLz48cGF0aCBjbGFzcz0ic3ZnX190ZXh0IiBkPSJNMTUuNjkgMjJMMTQuMjIgMjJMMTQuMjIgMTMuNDdMMTYuMTQgMTMuNDdMMTguNjAgMjAuMDFMMjEuMDYgMTMuNDdMMjIuOTcgMTMuNDdMMjIuOTcgMjJMMjEuNDkgMjJMMjEuNDkgMTkuMTlMMjEuNjQgMTUuNDNMMTkuMTIgMjJMMTguMDYgMjJMMTUuNTUgMTUuNDNMMTUuNjkgMTkuMTlMMTUuNjkgMjJaTTI4LjQ5IDIyTDI2Ljk1IDIyTDMwLjE3IDEzLjQ3TDMxLjUwIDEzLjQ3TDM0LjczIDIyTDMzLjE4IDIyTDMyLjQ5IDIwLjAxTDI5LjE4IDIwLjAxTDI4LjQ5IDIyWk0zMC44MyAxNS4yOEwyOS42MCAxOC44MkwzMi4wNyAxOC44MkwzMC44MyAxNS4yOFpNNDEuMTQgMjJMMzguNjkgMjJMMzguNjkgMTMuNDdMNDEuMjEgMTMuNDdRNDIuMzQgMTMuNDcgNDMuMjEgMTMuOTdRNDQuMDkgMTQuNDggNDQuNTcgMTUuNDBRNDUuMDUgMTYuMzMgNDUuMDUgMTcuNTJMNDUuMDUgMTcuNTJMNDUuMDUgMTcuOTVRNDUuMDUgMTkuMTYgNDQuNTcgMjAuMDhRNDQuMDggMjEuMDAgNDMuMTkgMjEuNTBRNDIuMzAgMjIgNDEuMTQgMjJMNDEuMTQgMjJaTTQwLjE3IDE0LjY2TDQwLjE3IDIwLjgyTDQxLjE0IDIwLjgyUTQyLjMwIDIwLjgyIDQyLjkzIDIwLjA5UTQzLjU1IDE5LjM2IDQzLjU2IDE3Ljk5TDQzLjU2IDE3Ljk5TDQzLjU2IDE3LjUyUTQzLjU2IDE2LjEzIDQyLjk2IDE1LjQwUTQyLjM1IDE0LjY2IDQxLjIxIDE0LjY2TDQxLjIxIDE0LjY2TDQwLjE3IDE0LjY2Wk01NS4wOSAyMkw0OS41MSAyMkw0OS41MSAxMy40N0w1NS4wNSAxMy40N0w1NS4wNSAxNC42Nkw1MS4wMCAxNC42Nkw1MS4wMCAxNy4wMkw1NC41MCAxNy4wMkw1NC41MCAxOC4xOUw1MS4wMCAxOC4xOUw1MS4wMCAyMC44Mkw1NS4wOSAyMC44Mkw1NS4wOSAyMlpNNjYuNjUgMjJMNjQuNjggMTMuNDdMNjYuMTUgMTMuNDdMNjcuNDcgMTkuODhMNjkuMTAgMTMuNDdMNzAuMzQgMTMuNDdMNzEuOTYgMTkuODlMNzMuMjcgMTMuNDdMNzQuNzQgMTMuNDdMNzIuNzcgMjJMNzEuMzUgMjJMNjkuNzMgMTUuNzdMNjguMDcgMjJMNjYuNjUgMjJaTTgwLjM4IDIyTDc4LjkwIDIyTDc4LjkwIDEzLjQ3TDgwLjM4IDEzLjQ3TDgwLjM4IDIyWk04Ni44NyAxNC42Nkw4NC4yMyAxNC42Nkw4NC4yMyAxMy40N0w5MS4wMCAxMy40N0w5MS4wMCAxNC42Nkw4OC4zNCAxNC42Nkw4OC4zNCAyMkw4Ni44NyAyMkw4Ni44NyAxNC42NlpNOTYuMjQgMjJMOTQuNzUgMjJMOTQuNzUgMTMuNDdMOTYuMjQgMTMuNDdMOTYuMjQgMTcuMDJMMTAwLjA1IDE3LjAyTDEwMC4wNSAxMy40N0wxMDEuNTMgMTMuNDdMMTAxLjUzIDIyTDEwMC4wNSAyMkwxMDAuMDUgMTguMjFMOTYuMjQgMTguMjFMOTYuMjQgMjJaIiBmaWxsPSIjRkZGRkZGIi8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEyOC45MiAyMkwxMjYuNDkgMjJMMTMwLjIwIDEzLjYwTDEzMi41NCAxMy42MEwxMzYuMjYgMjJMMTMzLjc5IDIyTDEzMy4xMyAyMC4zN0wxMjkuNTggMjAuMzdMMTI4LjkyIDIyWk0xMzEuMzUgMTUuOTNMMTMwLjI3IDE4LjYxTDEzMi40MyAxOC42MUwxMzEuMzUgMTUuOTNaTTE0Mi43NCAyMkwxNDAuNDEgMjJMMTQwLjQxIDEzLjYwTDE0Mi4zNyAxMy42MEwxNDYuMDggMTguMDdMMTQ2LjA4IDEzLjYwTDE0OC40MCAxMy42MEwxNDguNDAgMjJMMTQ2LjQ1IDIyTDE0Mi43NCAxNy41MkwxNDIuNzQgMjJaTTE1Mi45OCAyMS4yNEwxNTIuOTggMjEuMjRMMTUzLjc2IDE5LjQ5UTE1NC4zMiAxOS44NiAxNTUuMDcgMjAuMDlRMTU1LjgxIDIwLjMyIDE1Ni41MyAyMC4zMkwxNTYuNTMgMjAuMzJRMTU3LjkwIDIwLjMyIDE1Ny45MCAxOS42NEwxNTcuOTAgMTkuNjRRMTU3LjkwIDE5LjI4IDE1Ny41MSAxOS4xMVExNTcuMTIgMTguOTMgMTU2LjI2IDE4Ljc0TDE1Ni4yNiAxOC43NFExNTUuMzEgMTguNTMgMTU0LjY3IDE4LjMwUTE1NC4wMyAxOC4wNiAxNTMuNTggMTcuNTVRMTUzLjEzIDE3LjAzIDE1My4xMyAxNi4xNkwxNTMuMTMgMTYuMTZRMTUzLjEzIDE1LjM5IDE1My41NSAxNC43N1ExNTMuOTYgMTQuMTUgMTU0LjgwIDEzLjc5UTE1NS42MyAxMy40MyAxNTYuODQgMTMuNDNMMTU2Ljg0IDEzLjQzUTE1Ny42NyAxMy40MyAxNTguNDcgMTMuNjJRMTU5LjI4IDEzLjgwIDE1OS44OSAxNC4xN0wxNTkuODkgMTQuMTdMMTU5LjE2IDE1LjkzUTE1Ny45NiAxNS4yOCAxNTYuODMgMTUuMjhMMTU2LjgzIDE1LjI4UTE1Ni4xMiAxNS4yOCAxNTUuODAgMTUuNDlRMTU1LjQ4IDE1LjcwIDE1NS40OCAxNi4wNEwxNTUuNDggMTYuMDRRMTU1LjQ4IDE2LjM3IDE1NS44NiAxNi41NFExNTYuMjQgMTYuNzEgMTU3LjA5IDE2Ljg5TDE1Ny4wOSAxNi44OVExNTguMDUgMTcuMTAgMTU4LjY4IDE3LjMzUTE1OS4zMSAxNy41NiAxNTkuNzggMTguMDdRMTYwLjI0IDE4LjU4IDE2MC4yNCAxOS40NkwxNjAuMjQgMTkuNDZRMTYwLjI0IDIwLjIxIDE1OS44MiAyMC44M1ExNTkuNDAgMjEuNDQgMTU4LjU2IDIxLjgwUTE1Ny43MiAyMi4xNyAxNTYuNTIgMjIuMTdMMTU2LjUyIDIyLjE3UTE1NS41MCAyMi4xNyAxNTQuNTQgMjEuOTJRMTUzLjU4IDIxLjY3IDE1Mi45OCAyMS4yNFpNMTY3LjIwIDIyTDE2NC44MiAyMkwxNjQuODIgMTMuNjBMMTY3LjIwIDEzLjYwTDE2Ny4yMCAyMlpNMTc2LjkxIDIyTDE3Mi4zNyAyMkwxNzIuMzcgMTMuNjBMMTc2LjY3IDEzLjYwUTE3OC4yOCAxMy42MCAxNzkuMTIgMTQuMTlRMTc5Ljk2IDE0Ljc5IDE3OS45NiAxNS43OUwxNzkuOTYgMTUuNzlRMTc5Ljk2IDE2LjM5IDE3OS42NiAxNi44N1ExNzkuMzcgMTcuMzQgMTc4LjgzIDE3LjYyTDE3OC44MyAxNy42MlExNzkuNTUgMTcuODcgMTc5Ljk1IDE4LjQxUTE4MC4zNiAxOC45NCAxODAuMzYgMTkuNzBMMTgwLjM2IDE5LjcwUTE4MC4zNiAyMC44MCAxNzkuNDcgMjEuNDBRMTc4LjU5IDIyIDE3Ni45MSAyMkwxNzYuOTEgMjJaTTE3NC43MiAxOC41OEwxNzQuNzIgMjAuMjhMMTc2LjcyIDIwLjI4UTE3Ny45NiAyMC4yOCAxNzcuOTYgMTkuNDNMMTc3Ljk2IDE5LjQzUTE3Ny45NiAxOC41OCAxNzYuNzIgMTguNThMMTc2LjcyIDE4LjU4TDE3NC43MiAxOC41OFpNMTc0LjcyIDE1LjMxTDE3NC43MiAxNi45NEwxNzYuMzUgMTYuOTRRMTc3LjU1IDE2Ljk0IDE3Ny41NSAxNi4xMkwxNzcuNTUgMTYuMTJRMTc3LjU1IDE1LjMxIDE3Ni4zNSAxNS4zMUwxNzYuMzUgMTUuMzFMMTc0LjcyIDE1LjMxWk0xOTEuNDYgMjJMMTg1LjA4IDIyTDE4NS4wOCAxMy42MEwxODcuNDYgMTMuNjBMMTg3LjQ2IDIwLjExTDE5MS40NiAyMC4xMUwxOTEuNDYgMjJaTTIwMi42MyAyMkwxOTUuODggMjJMMTk1Ljg4IDEzLjYwTDIwMi40NyAxMy42MEwyMDIuNDcgMTUuNDRMMTk4LjI0IDE1LjQ0TDE5OC4yNCAxNi44NUwyMDEuOTcgMTYuODVMMjAxLjk3IDE4LjYzTDE5OC4yNCAxOC42M0wxOTguMjQgMjAuMTdMMjAyLjYzIDIwLjE3TDIwMi42MyAyMloiIGZpbGw9IiNGRkZGRkYiIHg9IjEyNi4zMSIvPjwvc3ZnPg==)](https://forthebadge.com)
[![Downloads][downloads-badge]][releases]
[![License][license-badge]][license]
[![Built with Nix][builtwithnix-badge]][builtwithnix]

zoxide is a **smarter cd command**, inspired by z and autojump.

It remembers which directories you use most frequently, so you can "jump" to
them in just a few keystrokes.<br />
zoxide works on all major shells.

[Getting started](#getting-started) •
[Installation](#installation) •
[Configuration](#configuration) •
[Integrations](#third-party-integrations)

</div>

## Getting started

![Tutorial][tutorial]

```sh
z foo              # cd into highest ranked directory matching foo
z foo bar          # cd into highest ranked directory matching foo and bar
z foo /            # cd into a subdirectory starting with foo

z ~/foo            # z also works like a regular cd command
z foo/             # cd into relative path
z ..               # cd one level up
z -                # cd into previous directory

zi foo             # cd with interactive selection (using fzf)

z foo<SPACE><TAB>  # show interactive completions (zoxide v0.8.0+, bash 4.4+/fish/zsh only)
```

Read more about the matching algorithm [here][algorithm-matching].

## Installation

### *Step 1: Install zoxide*

zoxide runs on most major platforms. If your platform isn't listed below,
please [open an issue][issues].

<details>
<summary>Linux</summary>

To install zoxide, run this command in your terminal:

```sh
curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash
```

Or, you can use a package manager:

| Distribution        | Repository              | Instructions                                                                                   |
| ------------------- | ----------------------- | ---------------------------------------------------------------------------------------------- |
| ***Any***           | **[crates.io]**         | `cargo install zoxide --locked`                                                                |
| *Any*               | [conda-forge]           | `conda install -c conda-forge zoxide`                                                          |
| *Any*               | [Linuxbrew]             | `brew install zoxide`                                                                          |
| Alpine Linux 3.13+  | [Alpine Linux Packages] | `apk add zoxide`                                                                               |
| Arch Linux          | [Arch Linux Community]  | `pacman -S zoxide`                                                                             |
| CentOS 7+           | [Copr]                  | `dnf copr enable atim/zoxide` <br /> `dnf install zoxide`                                      |
| Debian 11+          | [Debian Packages]       | `apt install zoxide`                                                                           |
| Devuan 4.0+         | [Devuan Packages]       | `apt install zoxide`                                                                           |
| Fedora 32+          | [Fedora Packages]       | `dnf install zoxide`                                                                           |
| Gentoo              | [GURU Overlay]          | `eselect repository enable guru` <br /> `emerge --sync guru` <br /> `emerge app-shells/zoxide` |
| Manjaro             |                         | `pacman -S zoxide`                                                                             |
| NixOS               | [nixpkgs]               | `nix-env -iA nixpkgs.zoxide`                                                                   |
| openSUSE Tumbleweed | [openSUSE Factory]      | `zypper install zoxide`                                                                        |
| Parrot OS           |                         | `apt install zoxide`                                                                           |
| Raspbian 11+        | [Raspbian Packages]     | `apt install zoxide`                                                                           |
| Ubuntu 21.04+       | [Ubuntu Packages]       | `apt install zoxide`                                                                           |
| Void Linux          | [Void Linux Packages]   | `xbps-install -S zoxide`                                                                       |

</details>

<details>
<summary>macOS</summary>

To install zoxide, use a package manager:

| Repository      | Instructions                          |
| --------------- | ------------------------------------- |
| **[crates.io]** | `cargo install zoxide --locked`       |
| [conda-forge]   | `conda install -c conda-forge zoxide` |
| [Homebrew]      | `brew install zoxide`                 |
| [MacPorts]      | `port install zoxide`                 |

Or, run this command in your terminal:

```sh
curl -sS https://raw.githubusercontent.com/ajeetdsouza/zoxide/main/install.sh | bash
```

</details>

<details>
<summary>Windows</summary>

To install zoxide, run this command in your command prompt:

```sh
curl.exe -A "MS" https://webinstall.dev/zoxide | powershell
```

Or, you can use a package manager:

| Repository      | Instructions                          |
| --------------- | ------------------------------------- |
| **[crates.io]** | `cargo install zoxide --locked`       |
| [Chocolatey]    | `choco install zoxide`                |
| [conda-forge]   | `conda install -c conda-forge zoxide` |
| [Scoop]         | `scoop install zoxide`                |

</details>

<details>
<summary>BSD</summary>

To install zoxide, use a package manager:

| Distribution  | Repository      | Instructions                    |
| ------------- | --------------- | ------------------------------- |
| ***Any***     | **[crates.io]** | `cargo install zoxide --locked` |
| DragonFly BSD | [DPorts]        | `pkg install zoxide`            |
| FreeBSD       | [FreshPorts]    | `pkg install zoxide`            |
| NetBSD        | [pkgsrc]        | `pkgin install zoxide`          |

</details>

<details>
<summary>Android</summary>

To install zoxide, use a package manager:

| Repository | Instructions         |
| ---------- | -------------------- |
| [Termux]   | `pkg install zoxide` |

</details>

### *Step 2: Add zoxide to your shell*

To start using zoxide, add it to your shell.

<details>
<summary>Bash</summary>

Add this to your configuration (usually `~/.bashrc`):

```sh
eval "$(zoxide init bash)"
```

</details>

<details>
<summary>Elvish</summary>

Add this to your configuration (usually `~/.elvish/rc.elv`):

```sh
eval (zoxide init elvish | slurp)
```

Note: zoxide only supports elvish v0.18.0 and above.

</details>

<details>
<summary>Fish</summary>

Add this to your configuration (usually `~/.config/fish/config.fish`):

```fish
zoxide init fish | source
```

Note: zoxide only supports fish v3.4.0 and above.

</details>

<details>
<summary>Nushell</summary>

Add this to your env file (find it by running `$nu.env-path` in Nushell):

```sh
zoxide init nushell --hook prompt | save ~/.zoxide.nu
```

Now, add this to the end of your config file (find it by running
`$nu.config-path` in Nushell):

```sh
source ~/.zoxide.nu
```

Note: zoxide only supports Nushell v0.61.0 and above.

</details>

<details>
<summary>PowerShell</summary>

Add this to your configuration (find it by running `echo $profile` in
PowerShell):

```powershell
# For zoxide v0.8.0+
Invoke-Expression (& {
    $hook = if ($PSVersionTable.PSVersion.Major -lt 6) { 'prompt' } else { 'pwd' }
    (zoxide init --hook $hook powershell | Out-String)
})

# For older versions of zoxide
Invoke-Expression (& {
    $hook = if ($PSVersionTable.PSVersion.Major -lt 6) { 'prompt' } else { 'pwd' }
    (zoxide init --hook $hook powershell) -join "`n"
})
```

</details>

<details>
<summary>Xonsh</summary>

Add this to your configuration (usually `~/.xonshrc`):

```python
execx($(zoxide init xonsh), 'exec', __xonsh__.ctx, filename='zoxide')
```

</details>

<details>
<summary>Zsh</summary>

Add this to your configuration (usually `~/.zshrc`):

```sh
eval "$(zoxide init zsh)"
```

For completions to work, the above line must be added *after* `compinit` is
called. You may have to rebuild your cache by running
`rm ~/.zcompdump*; compinit`.

</details>

<details>
<summary>Any POSIX shell</summary>

Add this to your configuration:

```sh
eval "$(zoxide init posix --hook prompt)"
```

</details>

### *Step 3: Install fzf (optional)*

[fzf] is a command-line fuzzy finder, used by zoxide for interactive selection.
It can be installed from [here][fzf-installation].

Note: zoxide only supports fzf v0.21.0 and above.

### *Step 4: Import your data (optional)*

If you currently use any of the following utilities, you may want to import
your data into zoxide:

<details>
<summary>autojump</summary>

```sh
zoxide import --from autojump path/to/db
```

The default path varies according to your system:

| OS      | Path                                                                                 | Example                                                |
| ------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Linux   | `$XDG_DATA_HOME/autojump/autojump.txt` or `$HOME/.local/share/autojump/autojump.txt` | `/home/alice/.local/share/autojump/autojump.txt`       |
| macOS   | `$HOME/Library/autojump/autojump.txt`                                                | `/Users/Alice/Library/autojump/autojump.txt`           |
| Windows | `%APPDATA%\autojump\autojump.txt`                                                    | `C:\Users\Alice\AppData\Roaming\autojump\autojump.txt` |

</details>

<details>
<summary>z, z.lua, or zsh-z</summary>

```sh
zoxide import --from z path/to/db
```

</details>

## Configuration

### Flags

When calling `zoxide init`, the following flags are available:

- `--cmd`
  - Changes the prefix of the `z` and `zi` commands.
  - `--cmd j` would change the commands to (`j`, `ji`).
  - `--cmd cd` would replace the `cd` command (doesn't work on Nushell / POSIX shells).
- `--hook <HOOK>`
  - Changes how often zoxide increments a directory's score:
    | Hook     | Description                       |
    | -------- | --------------------------------- |
    | `none`   | Never                             |
    | `prompt` | At every shell prompt             |
    | `pwd`    | Whenever the directory is changed |
- `--no-cmd`
  - Prevents zoxide from defining the `z` and `zi` commands.
  - These functions will still be available in your shell as `__zoxide_z` and
    `__zoxide_zi`, should you choose to redefine them.

### Environment variables

Environment variables<sup>[?][wiki-env]</sup> can be used for configuration.
They must be set before `zoxide init` is called.

- `_ZO_DATA_DIR`
  - Specifies the directory in which the database is stored.
  - The default value varies across OSes:
    | OS          | Path                                     | Example                                    |
    | ----------- | ---------------------------------------- | ------------------------------------------ |
    | Linux / BSD | `$XDG_DATA_HOME` or `$HOME/.local/share` | `/home/alice/.local/share`                 |
    | macOS       | `$HOME/Library/Application Support`      | `/Users/Alice/Library/Application Support` |
    | Windows     | `%LOCALAPPDATA%`                         | `C:\Users\Alice\AppData\Local`             |
- `_ZO_ECHO`
  - When set to 1, `z` will print the matched directory before navigating to
    it.
- `_ZO_EXCLUDE_DIRS`
  - Excludes the specified directories from the database.
  - This is provided as a list of [globs][glob], separated by OS-specific
    characters:
    | OS                  | Separator | Example                 |
    | ------------------- | --------- | ----------------------- |
    | Linux / macOS / BSD | `:`       | `$HOME:$HOME/private/*` |
    | Windows             | `;`       | `$HOME;$HOME/private/*` |
  - By default, this is set to `"$HOME"`.
- `_ZO_FZF_OPTS`
  - Custom options to pass to [fzf] during interactive selection. See
    [`man fzf`][fzf-man] for the list of options.
- `_ZO_MAXAGE`
  - Configures the [aging algorithm][algorithm-aging], which limits the maximum
    number of entries in the database.
  - By default, this is set to 10000.
- `_ZO_RESOLVE_SYMLINKS`
  - When set to 1, `z` will resolve symlinks before adding directories to the
    database.

## Third-party integrations

| Application        | Description                                  | Plugin                     |
| ------------------ | -------------------------------------------- | -------------------------- |
| [clink]            | Improved cmd.exe for Windows                 | [clink-zoxide]             |
| [emacs]            | Text editor                                  | [zoxide.el]                |
| [felix]            | File manager                                 | Natively supported         |
| [joshuto]          | File manager                                 | Natively supported         |
| [lf]               | File manager                                 | See the [wiki][lf-wiki]    |
| [nnn]              | File manager                                 | [nnn-autojump]             |
| [ranger]           | File manager                                 | [ranger-zoxide]            |
| [telescope.nvim]   | Fuzzy finder for Neovim                      | [telescope-zoxide]         |
| [vim]              | Text editor                                  | [zoxide.vim]               |
| [xplr]             | File manager                                 | [zoxide.xplr]              |
| [xxh]              | Transports shell configuration over SSH      | [xxh-plugin-prerun-zoxide] |
| [zabb]             | Finds the shortest possible query for a path | Natively supported         |
| [zsh-autocomplete] | Realtime completions for zsh                 | Natively supported         |

[algorithm-aging]: https://github.com/ajeetdsouza/zoxide/wiki/Algorithm#aging
[algorithm-matching]: https://github.com/ajeetdsouza/zoxide/wiki/Algorithm#matching
[alpine linux packages]: https://pkgs.alpinelinux.org/packages?name=zoxide
[arch linux community]: https://archlinux.org/packages/community/x86_64/zoxide/
[builtwithnix-badge]: https://img.shields.io/badge/builtwith-nix-7d81f7?style=flat-square
[builtwithnix]: https://builtwithnix.org/
[chocolatey]: https://community.chocolatey.org/packages/zoxide
[clink-zoxide]: https://github.com/shunsambongi/clink-zoxide
[clink]: https://github.com/mridgers/clink
[conda-forge]: https://anaconda.org/conda-forge/zoxide
[copr]: https://copr.fedorainfracloud.org/coprs/atim/zoxide/
[crates.io-badge]: https://img.shields.io/crates/v/zoxide?style=flat-square
[crates.io]: https://crates.io/crates/zoxide
[debian packages]: https://packages.debian.org/stable/admin/zoxide
[devuan packages]: https://pkginfo.devuan.org/cgi-bin/package-query.html?c=package&q=zoxide
[downloads-badge]: https://img.shields.io/endpoint?color=bright-green&label=downloads&style=flat-square&cacheSeconds=3600&url=https%3A%2F%2Fzoxide-dl-rlvir7rbe5ac.runkit.sh%2F
[dports]: https://github.com/DragonFlyBSD/DPorts/tree/master/sysutils/zoxide
[emacs]: https://www.gnu.org/software/emacs/
[fedora packages]: https://src.fedoraproject.org/rpms/rust-zoxide
[felix]: https://github.com/kyoheiu/felix
[freshports]: https://www.freshports.org/sysutils/zoxide/
[fzf-installation]: https://github.com/junegunn/fzf#installation
[fzf-man]: https://manpages.ubuntu.com/manpages/en/man1/fzf.1.html
[fzf]: https://github.com/junegunn/fzf
[glob]: https://man7.org/linux/man-pages/man7/glob.7.html
[guru overlay]: https://github.com/gentoo-mirror/guru
[homebrew]: https://formulae.brew.sh/formula/zoxide
[issues]: https://github.com/ajeetdsouza/zoxide/issues/new
[joshuto]: https://github.com/kamiyaa/joshuto
[lf]: https://github.com/gokcehan/lf
[lf-wiki]: https://github.com/gokcehan/lf/wiki/Integrations#zoxide
[license-badge]: https://img.shields.io/github/license/ajeetdsouza/zoxide?color=lightgray&style=flat-square
[license]: https://github.com/ajeetdsouza/zoxide/blob/main/LICENSE
[linuxbrew]: https://formulae.brew.sh/formula-linux/zoxide
[macports]: https://ports.macports.org/port/zoxide/summary
[neovim]: https://github.com/neovim/neovim
[nixpkgs]: https://github.com/NixOS/nixpkgs/blob/master/pkgs/tools/misc/zoxide/default.nix
[nnn-autojump]: https://github.com/jarun/nnn/blob/master/plugins/autojump
[nnn]: https://github.com/jarun/nnn
[opensuse factory]: https://build.opensuse.org/package/show/openSUSE:Factory/zoxide
[pkgsrc]: https://pkgsrc.se/sysutils/zoxide
[ranger-zoxide]: https://github.com/jchook/ranger-zoxide
[ranger]: https://github.com/ranger/ranger
[raspbian packages]: https://archive.raspbian.org/raspbian/pool/main/r/rust-zoxide/
[releases]: https://github.com/ajeetdsouza/zoxide/releases
[scoop]: https://github.com/ScoopInstaller/Main/tree/master/bucket/zoxide.json
[telescope-zoxide]: https://github.com/jvgrootveld/telescope-zoxide
[telescope.nvim]: https://github.com/nvim-telescope/telescope.nvim
[termux]: https://github.com/termux/termux-packages/tree/master/packages/zoxide
[tutorial]: contrib/tutorial.webp
[ubuntu packages]: https://packages.ubuntu.com/jammy/zoxide
[vim]: https://github.com/vim/vim
[void linux packages]: https://github.com/void-linux/void-packages/tree/master/srcpkgs/zoxide
[wiki-env]: https://github.com/ajeetdsouza/zoxide/wiki/HOWTO:-set-environment-variables "HOWTO: set environment variables"
[xplr]: https://github.com/sayanarijit/xplr
[xxh-plugin-prerun-zoxide]: https://github.com/xxh/xxh-plugin-prerun-zoxide
[xxh]: https://github.com/xxh/xxh
[zabb]: https://github.com/Mellbourn/zabb
[zoxide.el]: https://gitlab.com/Vonfry/zoxide.el
[zoxide.vim]: https://github.com/nanotee/zoxide.vim
[zoxide.xplr]: https://github.com/sayanarijit/zoxide.xplr
[zsh-autocomplete]: https://github.com/marlonrichert/zsh-autocomplete