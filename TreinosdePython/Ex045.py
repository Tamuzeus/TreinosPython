from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
pc = itens[computador]  #isso substiuirá os números por nomes!

jogador = int(input('''Escolha um número de uma das seguintes opções:
    0) Pedra
    1) Papel
    2) Tesoura
    Digite o número da opção: '''))

print(f'Jogador jogou: {itens[jogador]}')
print(f'Computador jogou: {itens[computador]}')

pj = itens[jogador]

#Tudo certo até aqui


if jogador == 0:  #pedra

    if jogador == computador:
        print('Empate!')
        print(f'{pc} empata com {pj}')

    elif computador == 1:
        print('Você perdeu!')
        print(f'{pc} vence de {pj}')

    elif computador == 2:
        print('Você venceu!')
        print(f'{pc} perde de {pj}')

elif jogador == 1: #papel

    if jogador == computador:
        print('Empate!')
        print(f'{pc} empata com {pj}')

    elif computador == 0:
        print('Você venceu!')
        print(f'{pc} perde de {pj}')

    elif computador == 2:
        print('Você perdeu!')
        print(f'{pc} vence de {pj}')

elif jogador == 2: #tesoura

    if jogador == computador:
        print('Empate!')
        print(f'{pc} empata com {pj}')

    elif computador == 1:
        print('Você venceu!')
        print(f'{pc} perde de {pj}')

    elif computador == 0:
        print('Você perdeu!')
        print(f'{pc} vence de {pj}')

else:
    print('Jogada inválida!')