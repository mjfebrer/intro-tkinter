x = input("Introduzca el número del DNI: ")

x = x.replace(' ', '')

x = x.replace('.', '')
x = int(x)

lista = [
    'T',
    'R',
    'W',
    'A',
    'G',
    'M',
    'Y',
    'F',
    'P',
    'D',
    'X',
    'B',
    'N',
    'J',
    'Z',
    'S',
    'Q',
    'V',
    'H',
    'L',
    'C',
    'K',
    'E'
]
print(x)

cociente = x % 23
print('tu cociente es: ', cociente)
print('La letra del DNI es: ', lista[cociente])
