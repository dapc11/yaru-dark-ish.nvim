#!/usr/bin/env python3
"""Generate palette.svg and update README.md color table from the colorscheme."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COLORS_FILE = ROOT / "colors" / "yaru-dark-ish.lua"
SVG_FILE = ROOT / "palette.svg"
README_FILE = ROOT / "README.md"
SWATCH_DIR = ROOT / "swatches"

ROWS = [
    ("Backgrounds & Surfaces", ["darker", "darkbg", "bg", "surface0", "surface1", "surface2", "gray"]),
    ("Text", ["black", "brblack", "subtext0", "subtext1", "fg", "white", "brwhite"]),
    ("Warm", ["red", "brred", "orange", "yellow", "bryellow", "green", "brgreen"]),
    ("Cool", ["cyan", "brcyan", "blue", "brblue", "magenta", "brmag"]),
]

SWATCH_W, SWATCH_H, GAP, PAD, ROW_H = 80, 40, 10, 20, 70


def parse_colors():
    text = COLORS_FILE.read_text()
    return dict(re.findall(r'(\w+)\s*=\s*"(#[0-9A-Fa-f]{6})"', text))


def needs_light_text(hex_color):
    r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
    return (0.299 * r + 0.587 * g + 0.114 * b) < 140


def generate_svg(colors):
    max_cols = max(len(r[1]) for r in ROWS)
    w = PAD * 2 + max_cols * (SWATCH_W + GAP) - GAP
    h = PAD + 30 + len(ROWS) * ROW_H + 20

    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}">',
        "  <style>text { font-family: monospace; font-size: 11px; }</style>",
        f'  <rect width="{w}" height="{h}" rx="8" fill="#1E1E1E"/>',
        f'  <text x="{PAD}" y="28" fill="#C0BFBC" font-size="14" font-weight="bold">yaru-dark-ish palette</text>',
    ]

    for row_i, (_, names) in enumerate(ROWS):
        y = 50 + row_i * ROW_H
        for col_i, name in enumerate(names):
            hex_val = colors.get(name, "#000000")
            x = PAD + col_i * (SWATCH_W + GAP)
            txt_fill = "#C0BFBC" if needs_light_text(hex_val) else "#1E1E1E"
            stroke = ' stroke="#3D3846" stroke-width="1"' if hex_val.upper() in ("#1E1E1E", "#181818") else ""
            lines.append(f'  <rect x="{x}" y="{y}" width="{SWATCH_W}" height="{SWATCH_H}" rx="4" fill="{hex_val}"{stroke}/>')
            lines.append(f'  <text x="{x+4}" y="{y+15}" fill="{txt_fill}">{name}</text>')
            lines.append(f'  <text x="{x+4}" y="{y+30}" fill="{txt_fill}" opacity="0.7">{hex_val}</text>')

    lines.append("</svg>")
    return "\n".join(lines) + "\n"


def generate_color_table(colors):
    all_names = []
    for _, names in ROWS:
        all_names.extend(names)
    seen = set()
    unique = [n for n in all_names if n not in seen and not seen.add(n)]

    SWATCH_DIR.mkdir(exist_ok=True)
    for name in unique:
        hex_val = colors.get(name, "#000000")
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><rect width="16" height="16" rx="3" fill="{hex_val}"/></svg>\n'
        (SWATCH_DIR / f"{name}.svg").write_text(svg)

    lines = ["| Name | Hex | Preview |", "|------|-----|---------|"]
    for name in unique:
        hex_val = colors.get(name, "#000000")
        preview = f"![{name}](swatches/{name}.svg)"
        lines.append(f"| `{name}` | `{hex_val}` | {preview} |")
    return "\n".join(lines)


def update_readme(color_table):
    text = README_FILE.read_text()
    marker_start = "<!-- COLORS:START -->"
    marker_end = "<!-- COLORS:END -->"
    block = f"{marker_start}\n{color_table}\n{marker_end}"

    if marker_start in text:
        text = re.sub(
            rf"{re.escape(marker_start)}.*?{re.escape(marker_end)}",
            block, text, flags=re.DOTALL,
        )
    else:
        text = text.replace("## Installation", f"{block}\n\n## Installation")

    README_FILE.write_text(text)


def main():
    colors = parse_colors()
    SVG_FILE.write_text(generate_svg(colors))
    update_readme(generate_color_table(colors))
    print(f"Updated {SVG_FILE.name} and {README_FILE.name}")


if __name__ == "__main__":
    main()
