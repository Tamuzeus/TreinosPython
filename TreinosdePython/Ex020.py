import random

a = input('Digite o nome do primeiro aluno: ')
b = input('Digite o nome do segundo aluno: ')
c = input('Digite o nome do terceiro aluno: ')
d = input('Digite o nome do quarto aluno: ')

lista = [a, b, c, d]
ordem = random.shuffle(lista)  #Após o shuffle, o resultado da lista pode ser reposto que vai embaralhar sozinho

print(f'''O nome dos alunos são:
1) {a}
2) {b}
3) {c}
4) {d}''')

print(f'''A ordem dos alunos são: 
{lista}''')