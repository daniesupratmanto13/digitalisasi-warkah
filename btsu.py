import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import sys

# FORMAT NAME -- FILE NAME BTSU.pdf
# 09999 80980_1990
# 08821#4 84809_2000#9
# 09822 77070_1990
# 09992 80980_1990

bt = "BT_160908071"
su = "SU_16090807_"
# tahun_su = "_2000"
sumber = glob.glob((r"/home/xxx/sumber/BTSU.pdf"))
temp = (r"/home/xxx/temp")
target = (r"/home/xxx/target")

cna = []
cnb = []
cns = []
cnbt = []
cnsu = []
pages = []
pagebt = []
pagesu = []


# buat list

fo = open((r'/home/xxx/name.txt'), 'r')
[cna.append(line.rstrip("\n")) for line in fo]
fo.close()

for i in cna:
    j = i.split(" ")
    cnb.append(j[0])
    cns.append(j[1])

for b in cnb:
    if len(b) > 6:
        t = b.split("#")
        cnbt.append(t[0])
        pagebt.append(int(t[1]))
    else:
        cnbt.append(b)
        pagebt.append(4)


for s in cns:
    if len(s) > 11:
        u = s.split("#")
        cnsu.append(u[0])
        pagesu.append(int(u[1]))
    else:
        cnsu.append(s)
        pagesu.append(3)

for p in range(len(pagebt)):
    pages.append(pagebt[p])
    pages.append(pagesu[p])

folder = []
names = []

for c in range(len(cnbt)):
    folder.append(bt + cnbt[c])
    folder.append(bt + cnbt[c])
    names.append(bt + cnbt[c] + ".pdf")
    names.append(su + cnsu[c] + ".pdf")


# split data

a = 0
b = 0
j = 0
for r in pages:
    a = b
    b += r
    for pdf in sumber:
        inputFile = PdfFileReader(open(pdf, "rb"))
        output = PdfFileWriter()
        for i in range(a, b):
            output.addPage(inputFile.getPage(i))

    j += 1
    newname = str(j) + ".pdf"

    outputStream = open((r"/home/xxx/temp/")+newname, "wb")
    output.write(outputStream)
    outputStream.close()

# mkdir
m_dir = set(folder)

for m in m_dir:
    os.mkdir(target+"/"+m)

# rename

files = []
sortfiles = []

[files.append(file) for file in os.listdir(temp)]
[sortfiles.append(int(sortfile[:-4])) for sortfile in files]
sortfiles = sorted(sortfiles)

j = 0
eks = ".pdf"
for i in sortfiles:
    old = temp + "/" + str(i) + eks
    new = target + "/" + folder[j] + "/" + names[j]
    j += 1
    os.rename(old, new)
