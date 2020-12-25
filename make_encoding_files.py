import csv
import datetime

f = open("codepoints.tsv")
encoding_file = open("cistercian.enc", "w+")
name_file = open("cistercian.nam", "w+")
reader = csv.DictReader(f, delimiter='\t')
now = datetime.datetime.utcnow().astimezone(datetime.timezone.utc)
with open("cistercian.enc.header") as header:
    encoding_file.write(header.read().format(now.strftime("%Y-%m-%d %H:%M:%S %Z"), now.strftime("%Y %B %d")))
for row in reader:
    i = int(row["unicode"][2:], 16)
    encoding_file.write("0x{:02x}\t0x{:02x}\t#\t{}\n".format(i - 0x100000, i, row["name"]))
    name_file.write("0x{:02x} {}\n".format(i, row["glyphname"]))
f.close()
encoding_file.close()
name_file.close()
