# yaru-dark-ish.nvim

A dark Neovim colorscheme inspired by Ubuntu's [Yaru](https://github.com/ubuntu/yaru) theme, with some personal tweaks.

## Palette

![palette](palette.svg)

<!-- COLORS:START -->
| Name | Hex | Preview |
|------|-----|---------|
| `darker` | `#181818` | ![darker](swatches/darker.svg) |
| `darkbg` | `#1E1E1E` | ![darkbg](swatches/darkbg.svg) |
| `bg` | `#262626` | ![bg](swatches/bg.svg) |
| `surface0` | `#2A2A2A` | ![surface0](swatches/surface0.svg) |
| `surface1` | `#303030` | ![surface1](swatches/surface1.svg) |
| `surface2` | `#3D3846` | ![surface2](swatches/surface2.svg) |
| `gray` | `#504E55` | ![gray](swatches/gray.svg) |
| `black` | `#303030` | ![black](swatches/black.svg) |
| `brblack` | `#5E5C64` | ![brblack](swatches/brblack.svg) |
| `subtext0` | `#9A9996` | ![subtext0](swatches/subtext0.svg) |
| `subtext1` | `#B0AFAC` | ![subtext1](swatches/subtext1.svg) |
| `fg` | `#C0BFBC` | ![fg](swatches/fg.svg) |
| `white` | `#C0BFBC` | ![white](swatches/white.svg) |
| `brwhite` | `#FFFFFF` | ![brwhite](swatches/brwhite.svg) |
| `red` | `#EA485C` | ![red](swatches/red.svg) |
| `brred` | `#FF87AF` | ![brred](swatches/brred.svg) |
| `orange` | `#E95420` | ![orange](swatches/orange.svg) |
| `yellow` | `#FFAF87` | ![yellow](swatches/yellow.svg) |
| `bryellow` | `#FBC16A` | ![bryellow](swatches/bryellow.svg) |
| `green` | `#AFD787` | ![green](swatches/green.svg) |
| `brgreen` | `#34B948` | ![brgreen](swatches/brgreen.svg) |
| `cyan` | `#75d3f4` | ![cyan](swatches/cyan.svg) |
| `brcyan` | `#87AFFF` | ![brcyan](swatches/brcyan.svg) |
| `blue` | `#87AFFF` | ![blue](swatches/blue.svg) |
| `brblue` | `#19B6EE` | ![brblue](swatches/brblue.svg) |
| `magenta` | `#D7AFFF` | ![magenta](swatches/magenta.svg) |
| `brmag` | `#c590bf` | ![brmag](swatches/brmag.svg) |
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
