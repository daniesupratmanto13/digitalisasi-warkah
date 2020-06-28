import os
import glob
from PyPDF2 import PdfFileReader, PdfFileWriter

# FORMAT NAME --- FILE NAME BT.pdf
# 80980
# 79869#3
# 97970#6
# 87090A#5

bt = "BT_160106071"
sumber = glob.glob((r"/home/xxx/sumber/BT.pdf"))
temp = (r"/home/xxx/temp")
target = (r"/home/xxx/target")

cna = []
cn = []
pages = []

# buat list

fo = open((r'/home/xxx/name.txt'), 'r')
[cna.append(line.rstrip("\n")) for line in fo]
fo.close()


for i in cna:
    if len(i) > 6:
        j = i.split("#")
        cn.append(j[0])
        pages.append(int(j[1]))
    else:
        cn.append(i)
        pages.append(4)


names = []

for n in range(len(cn)):
    names.append(bt + cn[n] + ".pdf")


# split data

a = 0
b = 0
q = 0

for p in pages:
    a = b
    b += p
    for pdf in sumber:
        inputFile = PdfFileReader(open(pdf, "rb"))
        output = PdfFileWriter()
        for _ in range(a, b):
            output.addPage(inputFile.getPage(_))

    q += 1
    newName = str(q) + ".pdf"

    outputStream = open((r"/home/xxx/temp/")+newName, "wb")
    output.write(outputStream)
    outputStream.close()

files = []
sortFiles = []

[files.append(file) for file in os.listdir(temp)]
[sortFiles.append(int(sortfile[:-4])) for sortfile in files]
sortFiles = sorted(sortFiles)


# # rename

j = 0
for s in sortFiles:
    old = temp + "/" + str(s) + ".pdf"
    new = target + "/" + names[j]
    j += 1
    os.rename(old, new)
