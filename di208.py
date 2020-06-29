import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import glob
import sys

# FORMAT NAME -- FILE NAME DI.pdf
# W_09222_2018 1-30
# W_09227_2018 31-66
# W_09333_2018 67-99

sumber = glob.glob((r"/home/xxx/sumber/DI.pdf"))
temp = (r"/home/xxx/temp")
target = (r"/home/xxx/target")

cn = []
di = []
pages = []
page = []

# buat list

fo = open((r'/home/xxx/name.txt'), 'r')
[cn.append(line.rstrip("\n")) for line in fo]
fo.close()

for i in cn:
    j = i.split(" ")
    di.append(j[0])
    pages.append(j[1])

for p in pages:
    q = p.split("-")
    page.append(q)

a = []
b = []
j = 0
for r in page:
    a.append(int(r[0]) - 1)
    b.append(int(r[1]))

# split pdf
for r in page:
    for pdf in sumber:
        inputFile = PdfFileReader(open(pdf, "rb"))
        output = PdfFileWriter()
        for i in range((a[j]), b[j]):
            output.addPage(inputFile.getPage(i))

    j += 1
    newname = str(j) + ".pdf"

    outputStream = open((r"/home/xxx/temp/")+newname, "wb")
    output.write(outputStream)
    outputStream.close()

# rename & mkdir

for d in di:
    os.mkdir(target + '/' + d)

files = []
sortfiles = []
fileeks = ".pdf"

[files.append(file) for file in os.listdir(temp)]
[sortfiles.append(int(sortfile[:-4])) for sortfile in files]
sortfiles = sorted(sortfiles)

j = 0
for i in sortfiles:
    new_name = "{}{}".format(di[j], fileeks)
    old = temp + "/" + str(i) + fileeks
    new = target + "/" + di[j]+"/" + new_name
    j += 1
    os.rename(old, new)
