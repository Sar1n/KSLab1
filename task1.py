import math
import patoolib
import os
from array import *

#print("Будь ласка, введіть повне ім'я файлу!")
#filename = input()
filename = ""
f = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test3.txt", "r")
contents = f.read()

OverallLength = len(contents)
symbols = list(set(contents))

pairs = {}
H = 0

for i in symbols:
    pairs[i] = contents.count(i)

print("Символ           Ймовірність ")
for r in pairs:
    probability = pairs[r] / OverallLength
    if r == "\n":
        print('\\n',"                ", "{0:.9f}".format(probability), end = "\n")
    else:
        print(r,"                 ","{0:.9f}".format(probability), "          ", end = "\n")
    H -= (probability) * math.log2(probability)
    
print("\nЕнтропія:", H, " біт")
bytesInfoQuantity = H * OverallLength / 8
print("Кількість інформації в тексті:", "{0:.4f}".format(bytesInfoQuantity), "байт, що є більше за розмір файлу" if bytesInfoQuantity > OverallLength else "байт, що є менше за розмір файлу" if bytesInfoQuantity < OverallLength else "(рівне розміру файлу)")


patoolib.create_archive(filename[:len(filename) - 4]+".rar", (filename,))
patoolib.create_archive(filename[:len(filename) - 4]+".lzma", (filename,))
patoolib.create_archive(filename[:len(filename) - 4]+".bz2", (filename,))
patoolib.create_archive(filename[:len(filename) - 4]+".gz", (filename,))
patoolib.create_archive(filename[:len(filename) - 4]+".zip", (filename,))

print("Розміри оригінального файлу:")
print(os.path.getsize(filename))
print("Розміри зшакалених файлів:")
print("RAR      ", os.path.getsize(filename[:len(filename) - 4]+".rar"), "\nLZMA     ", os.path.getsize(filename[:len(filename) - 4]+".lzma"), "\nBZ2      ", os.path.getsize(filename[:len(filename) - 4]+".bz2"), "\nGZ       ", os.path.getsize(filename[:len(filename) - 4]+".gz"), "\nZIP       ", os.path.getsize(filename[:len(filename) - 4]+".zip"))