# -*- coding: UTF-8 -*-

import zipfile

import io

f1 = None
f2 = None
f3 = None

try:
    f1 = io.open("./tmp1.txt", 'w+')
    f1.flush()
finally:
    f1.close()

try:
    f1 = io.open("./tmp2.txt", 'w+')
    f1.flush()
finally:
    f1.close()

try:
    f1 = io.open("./tmp3.txt", 'w+')
    f1.flush()
finally:
    f1.close()

zip = zipfile.ZipFile("tmp.zip", 'w')
zipfile.ZipFile.write(zip, "./tmp1.txt")
zipfile.ZipFile.write(zip, "./tmp2.txt")
zipfile.ZipFile.write(zip, "./tmp3.txt")



