
<div align="center">

<p align="center">
  <img src="img/cover.png" />
</p>

<img src="img/badge1.svg"/>
<img src="img/badge2.svg"/>
<br />
<br />
Docker Installer is an ansible playbook, built to install docker across multiple numbers of virtual machine in the cloud.

I wanted to deploy a docker swarm. My only problem was that all the available virtual machines doesn't have docker

**This is why I created this project**.

[Key Features](#key-features) •
[Installation](#installation) •
[Technologies Used](#technologies-used) •
[Contact Me](#contact-me) 
</div>

## Key Features

- Ability to execute command on hundreds of machine instances.
- It can work with both on-prem and in the cloud (AWS, Azure, GCP...etc) 
- It has the ability to install docker which is the most popular containerization and orchestration software

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


## Technologies Used

| Application                                         | Description                                  
| --------------------------------------------------- |--------------------------------------------- 
| [YAML](https://yaml.org/)                           | A Human-readable data-serialization language                 
| [Ansible](https://www.ansible.com/)                 | A software provisioning, configuration management, and application deployment tool                                  
| [Markdown Guide](https://www.markdownguide.org/)    | A reference guide that explains how to use markdown                                 

## Contact Me