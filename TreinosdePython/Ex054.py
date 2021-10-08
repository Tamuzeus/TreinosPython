atual = 2021   #ano atual
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input(f'Em que ano a {1}° pessoa nasceu?'))
    idade = atual - nasc   #tirar a idade.
    if idade >= 18:
        print('Essa pessoa é maior.')
        totmaior += 1
    elif idade < 18:
        print('Essa pessoa é menor.')
        totmenor += 1

print(f'Ao todo tivemos {totmaior} de maior.')
print(f'Ao todo tivemos {totmenor} de menor.')