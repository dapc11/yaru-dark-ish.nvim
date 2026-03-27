# yaru-dark-ish.nvim

A dark Neovim colorscheme inspired by Ubuntu's [Yaru](https://github.com/ubuntu/yaru) theme, with some personal tweaks.

## Palette

![palette](palette.svg)

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
