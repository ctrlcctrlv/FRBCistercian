import fontforge

# Constants
ONES =        0b00000001
TENS =        0b00000010
HUNDREDS =    0b00000100
THOUSANDS =   0b00001000
ALL_ANCHORS = ONES | TENS | HUNDREDS | THOUSANDS

TYPE_STRINGS = {ONES: "ones", TENS: "tens", HUNDREDS: "hundreds", THOUSANDS: "thousands"}

fontforge.loadEncodingFile("cistercian.enc", "Cistercian")
fontforge.loadNamelist("cistercian.nam")

font = fontforge.font()
font.copyright = "(c) 2020 Fredrick R. Brennan <copypaste@kittens.ph>"
font.familyname = "FRBCistercian"
font.fontname = "FRBCistercian"
font.fullname = "FRBCistercian-Regular"
font.sfntRevision = None
font.appendSFNTName("English (US)", "License URL", "http://scripts.sil.org/OFL")
with open("LICENSE") as lic:
    font.appendSFNTName("English (US)", "License", lic.read())

font.encoding = "Cistercian"
# GPOS mark
font.addLookup("mark1", "gpos_mark2base", None, (("mark",(("DFLT",("dflt")),)),))
font.addLookupSubtable("mark1", "mark1-1")
for cls in TYPE_STRINGS.values():
    font.addAnchorClass("mark1-1", cls)


def default_stroke(l):
    l.stroke("circular", 50)
    return l

def add_anchor(g, type_, base=True):
    basestr = "base" if base else "mark"
    where = (0, 0)
    # Top marks
    if type_ & ONES:
        if base: where = (400, 1000)
        g.addAnchorPoint(TYPE_STRINGS[ONES], basestr, *where)
    if type_ & TENS:
        if base: where = (400, 1000)
        g.addAnchorPoint(TYPE_STRINGS[TENS], basestr, *where)
    # Bottom marks
    if type_ & HUNDREDS:
        if base: where = (400, 0)
        g.addAnchorPoint(TYPE_STRINGS[HUNDREDS], basestr, *where)
    if type_ & THOUSANDS:
        if base: where = (400, 0)
        g.addAnchorPoint(TYPE_STRINGS[THOUSANDS], basestr, *where)

def hflip(g):
    l = fontforge.layer()
    for cc in g.foreground:
        c = fontforge.contour()
        for pp in cc:
            p = fontforge.point(-pp.x, pp.y, pp.on_curve, pp.type)
            c += p
        c.closed = cc.closed
        l += c
    g.foreground = l

def vflip(g):
    l = fontforge.layer()
    for cc in g.foreground:
        c = fontforge.contour()
        for pp in cc:
            p = fontforge.point(pp.x, -pp.y, pp.on_curve, pp.type)
            c += p
        c.closed = cc.closed
        l += c
    g.foreground = l

glyphs = dict()

# Make stick
def draw_stick():
    l = fontforge.layer()
    c = fontforge.contour()
    c += fontforge.point(400, 1000)
    c += fontforge.point(400, 0)
    l += c
    return l

font.createChar(fontforge.unicodeFromName("stick"), "stick")
font["stick"].foreground = default_stroke(draw_stick())
add_anchor(font["stick"], ALL_ANCHORS)
font["stick"].width = 800

# Make ZWSP
font.createChar(0x200b, "zwsp")
font["zwsp"].width = 0

# Draw 1
def draw_cistercian1():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   0)
    c.lineTo(300, 0)
    l += c
    return l

# Draw 2
def draw_cistercian2():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   -300)
    c.lineTo(300, -300)
    l += c
    return l

# Draw 3
def draw_cistercian3():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   0)
    c.lineTo(300, -300)
    l += c
    return l

# Draw 4
def draw_cistercian4():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   -300)
    c.lineTo(300, 0)
    l += c
    return l

# Draw 5
def draw_cistercian5():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   0)
    c.lineTo(300, 0)
    c.lineTo(0,   -300)
    l += c
    return l

# Draw 6
def draw_cistercian6():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(300, 0)
    c.lineTo(300, -300)
    l += c
    return l

# Draw 7
def draw_cistercian7():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   0)
    c.lineTo(300, 0)
    c.lineTo(300, -300)
    l += c
    return l

# Draw 8
def draw_cistercian8():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0, -300)
    c.lineTo(300, -300)
    c.lineTo(300, 0)
    l += c
    return l

# Draw 9
def draw_cistercian9():
    l = fontforge.layer()
    c = fontforge.contour()
    c.moveTo(0,   0)
    c.lineTo(300, 0)
    c.lineTo(300, -300)
    c.lineTo(0, -300)
    l += c
    return l

def add_glyphs_by_base_and_function(baseint, function):
    i = str(baseint)
    script = "cistercian"
    x = script + i
    x0 = script + i + "0"
    x00 = script + i + ("0" * 2)
    x000 = script + i + ("0" * 3)

    # Make x 
    font.createChar(fontforge.unicodeFromName(x), x)
    font[x].foreground = function()
    add_anchor(font[x], ONES, base=False)
    font[x].foreground = default_stroke(font[x].foreground)
    font[x].width = 0
    #print(x)

    # Make x0 
    font.createChar(fontforge.unicodeFromName(x0), x0)
    font[x0].foreground = function()
    add_anchor(font[x0], TENS, base=False)
    hflip(font[x0])
    font[x0].foreground = default_stroke(font[x0].foreground)
    font[x0].width = 0
    #print(x0)

    # Make x00
    font.createChar(fontforge.unicodeFromName(x00), x00)
    font[x00].foreground = function()
    add_anchor(font[x00], HUNDREDS, base=False)
    vflip(font[x00])
    font[x00].foreground = default_stroke(font[x00].foreground)
    font[x00].width = 0
    #print(x00)

    # Make x000
    font.createChar(fontforge.unicodeFromName(x000), x000)
    font[x000].foreground = function()
    add_anchor(font[x000], THOUSANDS, base=False)
    hflip(font[x000])
    vflip(font[x000])
    font[x000].foreground = default_stroke(font[x000].foreground)
    font[x000].width = 0
    #print(x000)

# Add all glyphs except stick
# Test string:
# /stick/cistercian1/stick/cistercian2/stick/cistercian3/stick/cistercian4/stick/cistercian5/stick/cistercian6/stick/cistercian7/stick/cistercian8/stick/cistercian9
add_glyphs_by_base_and_function(1, draw_cistercian1)
add_glyphs_by_base_and_function(2, draw_cistercian2)
add_glyphs_by_base_and_function(3, draw_cistercian3)
add_glyphs_by_base_and_function(4, draw_cistercian4)
add_glyphs_by_base_and_function(5, draw_cistercian5)
add_glyphs_by_base_and_function(6, draw_cistercian6)
add_glyphs_by_base_and_function(7, draw_cistercian7)
add_glyphs_by_base_and_function(8, draw_cistercian8)
add_glyphs_by_base_and_function(9, draw_cistercian9)

font.ascent = 1200
font.em = 1000

#font.save("FRBCistercian-output.sfd")
font.encoding = "UnicodeFull"
font.encoding = "compacted"
font.generate("dist/FRBCistercian.otf", flags=("opentype",))
