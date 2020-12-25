import csv
import random

ri = random.randint(0, 9999)

f = open("codepoints.tsv")
reader = csv.DictReader(f, delimiter='\t')
codepoints = dict()
for row in reader:
    codepoints[row["glyphname"]] = int(row["unicode"][2:], 16)
f.close()

todo = list(str(ri))
todo = ['']*(4-len(todo))+todo
todo = list(zip(["thousands", "hundreds", "tens", "ones"], todo))

zeroes = {"thousands": "000", "hundreds": "00", "tens": "0", "ones": str()}
encoded = chr(codepoints["stick"]).encode('ascii', 'xmlcharrefreplace').decode('utf-8')

for (t, c) in todo:
    if not len(c) or c == '0': continue
    encoded += chr(codepoints["cistercian{}{}".format(c,zeroes[t])]).encode('ascii', 'xmlcharrefreplace').decode('utf-8')

print("    <!-- {} -->\n    {}".format(ri, encoded))
