idade = int(input('Digite a sua idade: '))

if idade <= 9:
    print(f'Com {idade}, você entra na categoria MIRIM')

elif idade <= 14:
    print(f'Com {idade}, você entra na categoria INFANTIL')

elif idade <= 19:
    print(f'Com {idade}, você entra na categoria JUNIOR')

elif idade == 20:
    print(f'Com {idade}, você entra na categoria SÊNIOR')

elif idade >= 21:
    print(f'Com {idade}, você entra na categoria MASTER')