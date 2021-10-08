from random import randint

#variáveis
player = 0
pc = randint(1, 10)
palpites = 0

print('-*'*10)
print(' Jogo de adivinhação')
print('-*'*10)

print('Eu, o computador, pensei em um número de 1 a 10. Consegue adivinhar qual?')
player = int(input('''
     > Digite um número(1 a 10): '''))

while player != pc: #enquanto player for diferente de pc
    player = int(input('''ERROU! Tente mais uma vez!
    > Digite um número(1 a 10): '''))
    palpites += 1   #contar os palpites


    if player == pc:
        print('Wow! Acertou!')

print(f'O número era {pc}!')
print(f'Foram nescessários {palpites} palpites!')
