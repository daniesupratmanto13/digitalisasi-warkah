import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
import sys

# FORMAT NAME ---- SPLIT PER 3 HALAMAN ---HALAMANN KE 3 TIDAK DIIKUTKAN -- file name SU.pdf
# 09999_SAMBUTAN
# 08821_LOA JANAN
# 09822_TANI AMAN

temp = (r"/home/xxx/temp")
target = (r"/home/xxx/target")
sumber = glob.glob((r"/home/xxx/sumber/SU.pdf"))
os.chdir(target)
tahun = "1990"
cna = []

for pdf in sumber:
    inputFile = PdfFileReader(open(pdf, "rb"))
    for i in range(inputFile.numPages // 4):
        output = PdfFileWriter()
        output.addPage(inputFile.getPage(i * 4))

        if i * 3 + 1 < inputFile.numPages:
            output.addPage(inputFile.getPage(i * 4 + 1))

            if i * 3 + 2 < inputFile.numPages:
                output.addPage(inputFile.getPage(i * 4 + 3))

        newName = str(i+1) + ".pdf"

        outputStream = open(
            (r"//home/xxx/temp/")+newName, "wb")
        output.write(outputStream)
        outputStream.close()

outputStream.close()

a = {"SUNGAI KELEDANG": "16010201", "BAQA": "16010202", "MESJID": "16010203", "GUNUNG PANJANG": "16010210", "MANGKUPALAS": "16010211",
     "TENUN": "16010212", "LOA JANAN": "16010204",
     "SELILI": "16010401", "SUNGAI DAMA": "16010402", "SIDOMULYO": "16010403", "SIDODAMAI": "16010404", "PELITA": "16010405",
     "TELUK LERONG ILIR": "16010301", "JAWA": "16010302", "AIR PUTIH": "16010304", "SIDODADI": "16010305", "AIR HITAM": "16010306",
     "DADIMULYA": "16010307", "GUNUNG KELUA": "16010308", "BUKIT PINANG": "16010309",
     "SEMPAJA UTARA": "16010502", "LEMPAKE": "16010503", "SUNGAI SIRING": "16010504", "SEMPAJA SELATAN": "16010510", "TANAH MERAH": "16010511",
     "SEMPAJA BARAT": "16010513", "SEMPAJA TIMUR": "16010514", "BUDAYA PAMPANG": "16010515", "SEMPAJA": "16010512",
     "RAWA MAKMUR": "16010101", "BUKUAN": "16010102", "HANDIL BAKTI": "16010103", "SIMPANG PASIR": "16010104", "BANTUAS": "16010105",
     "LOA BAKUNG": "16010601", "LOA BUAH": "16010602", "KARANG ASAM ULU": "16010603", "LOK BAHU": "16010604", "TELUK LERONG ULU": "16010605",
     "KARANG ASAM ILIR": "16010606", "KARANG ANYAR": "16010607", "KARANG ASAM": "16010608",
     "SUNGAI KAPIH": "16010701", "SAMBUTAN": "16010702", "MAKROMAN": "16010703", "SINDANG SARI": "16010704", "PULAU ATAS": "16010705",
     "KARANG MUMUS": "16010901", "PELABUHAN": "16010902", "PASAR PAGI": "16010903", "BUGIS": "16010904", "SUNGAI PINANG LUAR": "16010905",
     "TEMINDUNG PERMAI": "16010801", "SUNGAI PINANG DALAM": "16010802", "GUNUNG LINGAI": "16010803", "MIGIREJO": "16010804", "BANDARA": "16010805",
     "SIMPANG TIGA": "16011001", "TANI AMAN": "16011002", "SENGKOTEK": "16011003", "HARAPAN BARU": "16011004", "RAPAK DALAM": "16011005"
     }

cn = []
files = []
sortfiles = []
wil = []
fileeks = ".pdf"
same = []
cnt = []
cnf = []

fo = open((r'/home/xxx/name.txt'), 'r')
[cn.append(line.rstrip("\n")) for line in fo]
fo.close()


for c in cn:
    if c in cnt:
        d = c
        same.append(d)
        c = c[:5] + "B" + c[5:]
        if c in cnt:
            c = c[:5] + "C" + c[6:]
            if c in cnt:
                c = c[:5] + "D" + c[6:]
    cnt.append(c)

for i in cnt:
    if i in same:
        i = i[:5] + "A" + i[5:]
    cnf.append(i)

for c in cnf:
    b = c.split('_')
    c = b[0]
    cna.append(c)


for w in cn:
    v = w.split('_')
    w = v[1]
    w = w.upper()
    wil.append(w)

b = set(wil)


for i in b:
    os.mkdir(target+"/"+i)


[files.append(file) for file in os.listdir(temp)]
[sortfiles.append(int(sortfile[:-4])) for sortfile in files]
sortfiles = sorted(sortfiles)

j = 0
for i in sortfiles:
    new_name = "SU_{}_{}_{}{}".format(a[wil[j]], cna[j], tahun, fileeks)
    old = temp + "/" + str(i) + fileeks
    new = target + "/" + wil[j]+"/" + new_name
    j += 1
    os.rename(old, new)
