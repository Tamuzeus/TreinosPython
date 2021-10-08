a = int(input('Digite o número a ser convertido: '))
b = str(input('''Escolha a letra de uma dessas opções:'
              A) Binário
              B) Octal
              C) Hexadecimal
              Digite a letra da opção: ''')).strip().upper()

if b == 'A':
    c = bin(a)
    print(f'{a}, em binário é {c}')
elif b == 'B':
    c = oct(a)
    print(f'{a}, em Octal é {c}')
elif b == 'C':
    c = hex(a)
    print(f'{a}, em Hexadecimal é {c}')