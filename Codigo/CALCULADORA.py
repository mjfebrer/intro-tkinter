number_1 = input('Escribe un número: ')
number_1 = number_1.replace('.', '')+
number_1 = int(number_1)

number_2 = input('Escribe otro número: ')
number_2 = int(number_2)

operator = ''
valid_operators = ['+', '-', '*', '/']

while operator not in valid_operators:
    operator = input('que operación quieres hacer (* , - , + , /): ')
    if operator in valid_operators:
        if operator == '*':
            print(number_1 * number_2)

        if operator == '-':
            print(number_1 - number_2)

        if operator == '+':
            print(number_1 + number_2)

        if operator == '/':
            print(number_1 / number_2)
    else:
        print('Has elegido un operador incorrecto')
