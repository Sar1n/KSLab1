import base64
import math
f = open(r"C:\data\knu\6 semestr\KompSys\Laba1\alice.txt", "r")
content = f.read()

def ToBase64(content):
    base64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    asciibinary = ""
    for c in content:
        #print ("SSSSSSSSSSSSSSSSSSSSSSSSSSSSS               ",c)
        asciibinary += '0' * (8 - len(bin(ord(c)).replace('b',''))) + bin(ord(c)).replace('b','')
    if (len(asciibinary) % 6 != 0):
        asciibinary += '0' * (6 - (len(asciibinary) % 6))
    base64string = ""
    for x in range(0, len(asciibinary), 6):
        base64string += base64chars[int(asciibinary[x:x+6], 2)]
    if len(content) % 3 != 0:
        base64string += '=' * (3 - len(content) % 3)
    if base64string == base64.b64encode(content.encode()).decode():
       # print ("String to encode:")
       # print (content)
        #print ("My function:")
        #print (base64string)
        #print ("Lib function:")
        #print (base64.b64encode(content.encode()).decode())
        #print ("Base56 encoding matches with library function.")
        print ("True")
    else:
        print ("False")
    return base64string

def Quantity(base64string):
    symbols = list(set(base64string))
    pairs = {}
    Entropy = 0
    OverallLength = len(base64string)
    for i in symbols:
        pairs[i] = base64string.count(i)
    for r in pairs:
        Entropy -= (pairs[r] / OverallLength) * math.log2(pairs[r] / OverallLength)
    InfoQuantity = Entropy * OverallLength / 8
    return InfoQuantity

def InfoQuanitity(contents):
    #f = open(filename)
    #contents = f.read()
    OverallLength = len(contents)
    symbols = list(set(contents))
    pairs = {}
    H = 0
    for i in symbols:
        pairs[i] = contents.count(i)
    for r in pairs:
        probability = pairs[r] / OverallLength
        H -= (probability) * math.log2(probability)
    bytesInfoQuantity = H * OverallLength / 8
    #f.close()
    return bytesInfoQuantity

base64string = ToBase64(content)
#print (base64string)

f.close()

h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test1.txt", "r")
file1 = h.read()
file11 = base64.b64encode(file1.encode()).decode()
print ("Input File ", InfoQuanitity(file1), "Byte")
print ("Base64 ", InfoQuanitity(file11), "Byte")
h.close()

h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test2.txt", "r")
file2 = h.read()
file22 = base64.b64encode(file2.encode()).decode()
print ("Input File ", InfoQuanitity(file2), "Byte")
print ("Base64 ", InfoQuanitity(file22), "Byte")
h.close()

h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test3.txt", "r")
file3 = h.read()
file33 = base64.b64encode(file3.encode()).decode()
print ("Input File ", InfoQuanitity(file3), "Byte")
print ("Base64 ", InfoQuanitity(file33), "Byte")
h.close()


print ("-----------------------------------")

print ("Input File ", InfoQuanitity(file1), "Byte")
h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test1.bz2", "rb")
arch1 = h.read()
arch11 = base64.b64encode(arch1)
print ("text1.bz2 to Base64 ", InfoQuanitity(arch11), "Byte")
h.close()


print ("Input File ", InfoQuanitity(file2), "Byte")
h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test2.bz2", "rb")
arch2 = h.read()
arch22 = base64.b64encode(arch2)
print ("text2.bz2 to Base64 ", InfoQuanitity(arch22), "Byte")
h.close()


print ("Input File ", InfoQuanitity(file3), "Byte")
h = open(r"C:\data\knu\6 semestr\KompSys\Laba1\task1test3.bz2", "rb")
arch3 = h.read()
arch33 = base64.b64encode(arch3)
print ("text3.bz2 to Base64 ", InfoQuanitity(arch33), "Byte")
h.close()


#print ("ASCII ", Quantity(content), "Byte")
#print ("Base64 ", Quantity(base64string), "Byte")

archive = open(r"C:\data\knu\6 semestr\KompSys\Laba1\alice.lzma", "rb")
archivecontent = archive.read()
#print (archivecontent)
print ("Archive ASCII ", Quantity(archivecontent), "Byte")


#pidr = ToBase64(archivecontent)

#print ("--------------------", base64.b64encode(content.encode()).decode())
print ("Archive ASCII to Base64", Quantity(base64.b64encode(content.encode()).decode()), "Byte")