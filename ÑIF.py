n = input('Introduce DNI: ')
n = int(n)
print(n % 23)
a = n % 23
if a == 19:
    print('La letra del DNI es la L')
    print('')
    print('Tu NIF es: ', n, 'L')
else:
    if a == 0:
        print('La letra del DNI es la T')
        print('')
        print('Tu NIF es: ', n, 'T')
    else:
        if a == 6:
            print('La letra del DNI es la Y')
            print('')
            print('Tu NIF es: ', n, 'Y')
