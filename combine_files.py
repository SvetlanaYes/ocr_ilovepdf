import os
import sys


file_name = sys.argv[1]
files = os.listdir(file_name)

str_to_int = []
for f in files:
    str_to_int.append(int(f))
str_to_int.sort()
print(str_to_int)

cmd = "pdftk"
for i in str_to_int:
    cmd += " " + file_name + "/" +str(i) + "/" + str(i) + "_ocr.pdf"
cmd += " cat output " + file_name + ".pdf"

os.system(cmd)


