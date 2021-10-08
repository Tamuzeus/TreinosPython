import random

print('''A DW quer saber, qual é o membro mais gay.
''')

a = input('Digite o nome da primeiro otário: ')
b = input('Digite o nome do segundo otário: ')
c = input('Digite o nome do terceiro otário: ')
d = input('Digite o nome do quarto otário: ')

lista = [a, b, c, d]
sorteio = random.choice(lista)

print(f'O mais gay é o \33[36m{sorteio}\33[m')
