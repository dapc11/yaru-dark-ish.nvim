# yaru-dark-ish.nvim

A dark Neovim colorscheme inspired by Ubuntu's [Yaru](https://github.com/ubuntu/yaru) theme, with some personal tweaks.

## Palette

![palette](palette.svg)

<!-- COLORS:START -->
| Name | Hex | Preview |
|------|-----|---------|
| `darker` | `#181818` | ![darker](https://via.placeholder.com/16/181818/181818.png) |
| `darkbg` | `#1E1E1E` | ![darkbg](https://via.placeholder.com/16/1E1E1E/1E1E1E.png) |
| `bg` | `#262626` | ![bg](https://via.placeholder.com/16/262626/262626.png) |
| `surface0` | `#2A2A2A` | ![surface0](https://via.placeholder.com/16/2A2A2A/2A2A2A.png) |
| `surface1` | `#303030` | ![surface1](https://via.placeholder.com/16/303030/303030.png) |
| `surface2` | `#3D3846` | ![surface2](https://via.placeholder.com/16/3D3846/3D3846.png) |
| `gray` | `#504E55` | ![gray](https://via.placeholder.com/16/504E55/504E55.png) |
| `black` | `#303030` | ![black](https://via.placeholder.com/16/303030/303030.png) |
| `brblack` | `#5E5C64` | ![brblack](https://via.placeholder.com/16/5E5C64/5E5C64.png) |
| `subtext0` | `#9A9996` | ![subtext0](https://via.placeholder.com/16/9A9996/9A9996.png) |
| `subtext1` | `#B0AFAC` | ![subtext1](https://via.placeholder.com/16/B0AFAC/B0AFAC.png) |
| `fg` | `#C0BFBC` | ![fg](https://via.placeholder.com/16/C0BFBC/C0BFBC.png) |
| `white` | `#C0BFBC` | ![white](https://via.placeholder.com/16/C0BFBC/C0BFBC.png) |
| `brwhite` | `#FFFFFF` | ![brwhite](https://via.placeholder.com/16/FFFFFF/FFFFFF.png) |
| `red` | `#EA485C` | ![red](https://via.placeholder.com/16/EA485C/EA485C.png) |
| `brred` | `#FF87AF` | ![brred](https://via.placeholder.com/16/FF87AF/FF87AF.png) |
| `orange` | `#E95420` | ![orange](https://via.placeholder.com/16/E95420/E95420.png) |
| `yellow` | `#FFAF87` | ![yellow](https://via.placeholder.com/16/FFAF87/FFAF87.png) |
| `bryellow` | `#FBC16A` | ![bryellow](https://via.placeholder.com/16/FBC16A/FBC16A.png) |
| `green` | `#AFD787` | ![green](https://via.placeholder.com/16/AFD787/AFD787.png) |
| `brgreen` | `#34B948` | ![brgreen](https://via.placeholder.com/16/34B948/34B948.png) |
| `cyan` | `#75d3f4` | ![cyan](https://via.placeholder.com/16/75d3f4/75d3f4.png) |
| `brcyan` | `#87AFFF` | ![brcyan](https://via.placeholder.com/16/87AFFF/87AFFF.png) |
| `blue` | `#87AFFF` | ![blue](https://via.placeholder.com/16/87AFFF/87AFFF.png) |
| `brblue` | `#19B6EE` | ![brblue](https://via.placeholder.com/16/19B6EE/19B6EE.png) |
| `magenta` | `#D7AFFF` | ![magenta](https://via.placeholder.com/16/D7AFFF/D7AFFF.png) |
| `brmag` | `#c590bf` | ![brmag](https://via.placeholder.com/16/c590bf/c590bf.png) |
<!-- COLORS:END -->

## Installation

Using [lazy.nvim](https://github.com/folke/lazy.nvim):

```lua
{
  "dapc11/yaru-dark-ish.nvim",
  lazy = false,
  priority = 1000,
  config = function()
    vim.cmd.colorscheme("yaru-dark-ish")
  end,
}
```

## Features

- Single-file colorscheme — no dependencies, no build step
- Treesitter, LSP, and diagnostic highlight groups
- Support for popular plugins (Telescope, Gitsigns, Cmp, Mini, Snacks, and more)
- Terminal colors included
