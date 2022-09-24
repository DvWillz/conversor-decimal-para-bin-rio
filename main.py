import math
from random import choice

converter = int(input("Digite o número para ser convertido em bínario: "))
oldnumber = converter
conversor = ''

while True:
    oldvalue = converter
    if converter != 0 and converter != 1:
        converter /= 2
        converter = math.floor(converter)
        if converter * 2 == oldvalue:
            conversor += '0'
        else:
            conversor += '1'
    else:
        if converter == 0:
            conversor += '0'
        else:
            conversor += '1'
        break
conversor = conversor[::-1]
print(f"o número {oldnumber} em binário é {conversor}")