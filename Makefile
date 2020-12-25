all:
	fontforge -lang=py -script make_font.py
	convert -density 300 dist/specimen.pdf dist/specimen.png
	woff2_compress dist/FRBCistercian.otf
