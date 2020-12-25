# FRB Cistercian

* [Download font](https://github.com/ctrlcctrlv/FRBCistercian/raw/main/dist/FRBCistercian.otf)
* [Numberphile™ video about Cistercian numerals (“The Forgotten Number System”)](https://www.youtube.com/watch?v=9p55Qgt7Ciw)

FRB Cistercian is an OpenType font for the medeival number system known as the [Cistercian numerals](https://en.wikipedia.org/wiki/Cistercian_numerals).

This font was inspired by Kirk Miller's Unicode document [L2/20-290](https://www.unicode.org/L2/L2020/20290-cistercian-digits.pdf).

This font currently uses the Private Use Area, as these characters are not yet in Unicode. See `codepoints.tsv` and `codepoints.txt`.

![](https://raw.githubusercontent.com/ctrlcctrlv/FRBCistercian/main/dist/specimen.png)

## Building

Only FontForge is required. There's no SFD file, the source file is `make_font.py`, the entire font is made in FontForge's Python API.

Just run `make`, see `Makefile` for commands.
