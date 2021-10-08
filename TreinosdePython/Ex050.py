s = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número inteiro: '))
    s += num  #usou o num, pois ele recebeu a quantidade para somar!
    cont += 1
print(f'Foram usados {cont} números!')
print(f'A soma é de {s}!')

