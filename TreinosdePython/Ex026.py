a = input(str('Digite uma frase: ')).upper()
b = a.count('A')
c = a.find('A')
d = a.rfind('A')

print(f'A letra \33[36m"A"\33[m aparece {b} vezes.')
print(f'A letra \33[36m"A"\33[m começa em {c+1}.')
print(f'A letra \33[36m"A"\33[m termina em {d+1}.')

#a soma é devido a contagem iniciar sempre no 0
