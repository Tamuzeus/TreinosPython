ano = int(input('Digite o ano de seu nascimento: '))

a = 2021-ano

if a < 18:
    print('Ainda irá chegar sua época de alistar!')
    b = 18-a
    if b > 1:
        print(f'Faltam {b} anos!')
    elif b == 1:
        print(f'Falta {b} ano!')

elif a == 18:
    print('Está na hora de você se alistar!')
    print(f'Você já tem {a} anos!')

elif a > 18:
    print('Já passou no prazo do seu alistamento!')
    b = 20*(a-18)
    c = a-18
    print(f'Você terá que pagar uma multa de R${b}, sendo R$ 20.00, por ano de atraso!')
    print(f'Pois, você está atrasado em {c} anos!')