a = int(input('Digite o valor do seu salário: '))
b = int(input('Digite o valor da porcentagem(o simbolo não é nescessário): '))
c = b/100
d = a*c

print(f'O seu salário de {a}, com o acréscimo de {b}% é de {d}, totalizando {a+d}.')