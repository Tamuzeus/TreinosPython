opção = 0
primeironumero = int(input('Digite o 1º número: '))
segundonumero = int(input('Digite o 2º número: '))

while not opção == 5:

    opção = int(input('''Digite o número de uma das seguintes opções:
    
    [1] Somar os números.
    [2] Multiplicar os números.
    [3] Ver qual é o maior número.
    [4] Escolher novos números.
    [5] Encerrar o programa
    
    Número: '''))      #escolha do número

    if opção == 1:  #soma
        soma = primeironumero+segundonumero
        print(f'A soma de {primeironumero}+{segundonumero} = {soma}!')

    elif opção == 2: #multiplicação
        multiplicaçao = primeironumero*segundonumero
        print(f'A multiplicação de {primeironumero}+{segundonumero} = {multiplicaçao}!')

    elif opção == 3:  #maior número
        if primeironumero > segundonumero:
            print(f'O maior número é: {primeironumero}!')
        else:
            print(f'O maior número é: {segundonumero}!')

    elif opção == 4: #escolher novos números
        primeironumero = int(input('Digite o 1º número: '))
        segundonumero = int(input('Digite o 2º número: '))


    elif opção == 5:          #encerrar o programa
        print('Fim do programa!')

    else:  #opção inválida
        print(f'Opção "{opção}" inválida! Tente novamente! ')

print('Obrigado por usar nossa calculadora!')
