#desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a+b > c and b+c > a and c+b > a:
    print('True')

else:
    print('False')