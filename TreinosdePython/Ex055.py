#totp = 0
#lista = []   #abre a lista vázia
#for c in range(1, 4):
 #   lista.append(float(input(f'Digite o número do peso da {c}° pessoa: ')))
      #lista.append faz a leitura direto para dentro da lista.
#print(f'O maior valor é: {max(lista)} Kg')    #faz a leitura do valor máximo da lista
#print(f'O menor valor é: {min(lista)} Kg')    #faz a leitura do valor mínimo da lista

kgmaior = 0
kgmenor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}° pessoa: '))

    if c == 1:  # vai fazer a contagem da primeira rodada e salvar os primeiros valores.
        kgmenor = peso
        kgmaior = peso
    else:
        if peso > kgmaior:  # caso o peso seja maior que o valor, vai salvar o maior
            kgmaior = peso

        elif peso < kgmenor:  # caso peso seja menor que o valor, vai salvar o menor
            kgmenor = peso

print(f'Maior peso é: {kgmaior} kg.')
print(f'Menor peso é: {kgmenor} kg.')