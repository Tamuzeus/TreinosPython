a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

if a > b:
    print(f'O valor {a} é maior que {b}.')

elif b > a:
    print(f'O valor {a} é menor que {b}.')

elif a == b:
    print('Os valores são iguais!')
