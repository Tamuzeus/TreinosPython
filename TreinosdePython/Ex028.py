from random import randint

print('Estou pensando em um número... de 0 a 5.')
random = (randint(0,5))

num = int(input('Digite um número de 0 a 5, se você estiver certo, vencerá: '))

if num == random:
    print(f'Você venceu! O número era: {random}')

else:
    print(f'Você perdeu! O número era: {random}')