contador = 0
soma = 0
maiorvalor = 0
menorvalor = 0
média = 0
continuar = ''

while continuar != 'N':
    numero = int(input('Digite o número inteiro: '))
    soma += numero
    contador += 1

    continuar = str(input('Você quer continuar a digitar valores: [S/N]? ')).strip().upper()
    if continuar == 'S':
            numero = int(input('Digite o número inteiro: '))
            continuar = str(input('Você quer continuar a digitar valores: [S/N]? ')).strip().upper()

    elif continuar =='N':
            print('Contagem encerrada!')

#salvar valores no loop


    if contador == 1: #igualar ao numero de voltas
        maiorvalor = numero  #sempre por a posição igualada na frente
        menorvalor = numero
    else:  # não esquecer do else

        if numero > maiorvalor:
            maiorvalor = numero
        elif numero < menorvalor:
            menorvalor = numero

#salvar valores em loop

média = soma/contador #Precisa estar fora do loop

print(f'O maior valor é {maiorvalor}.')
print(f'O menor valor é {menorvalor}.')
print(f'A média de todos os valores é {média}!')