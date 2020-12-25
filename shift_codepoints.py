f = open("codepoints3.txt", "r")
s = f.read()
print('\n'.join(['\t'.join(["U+"+hex(int(u[2:], 16)+1)[2:], n, f]) for (u, n, f) in [tuple(l.split('\t')) for l in s.splitlines()]]))
