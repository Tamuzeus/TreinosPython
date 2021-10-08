

somaidade = 0 #fara soma da idade
maioridadehomem = 0 #maior idade do homem
nomevelho = ''
cont = 0
for p in range(1, 5):           # p de pessoa
    print(f'----{p}º Pessoa ----')
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()

    somaidade += idade #fará a contagem utilizando os valores postos da idade

    if sexo == 'M' and idade > maioridadehomem:  #descobrir a maior idade do M e o nome
        maioridadehomem = idade            #assim, o maior valor vai ser guardado
        nomevelho = nome

    if sexo == 'F' and idade < 20:  #descobrir quantas F são menores de 20
        cont += 1



mediaidade = somaidade/4 #irá tirar a média da idade

print(f'A média de idade do grupo é {mediaidade}.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Existem {cont} mulheres com menos de 20 anos.')