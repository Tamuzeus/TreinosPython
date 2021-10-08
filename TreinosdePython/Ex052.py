num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num+1): #+1 para chegar até o ultimo número, pois o python corta o último.
    if num % c == 0:    #Aqui verá se o número é divisivel por ele mesmo na passagem! E, caso seja, será marcado!

        print('\033[33m',end=' ')
        tot += 1 #somará a quantidade de voltas que passou por aqui!

    else:
        print('\033[31m',end=' ')
    print(f'{c}',end=' ') #ele tem que ficar dentro para fazer a aplicação de todos os loops.
                         #o ,end = ' ', serve para por os espaços dos lados/não pular de linha

if tot == 2:       #iguala a quantidade de vezes que tot contou as voltas. Para ser primo precisa de duas(2).
    print(f'\33[m - {num} é divisivel apenas por {tot} números, por isso é primo.')
else:
    print(f'\33[m - {num} é divisivel por {tot} números, logo ele não é primo!')