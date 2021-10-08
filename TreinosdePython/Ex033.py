
a = int(input('Digite o valor de seu salário: '))

b = a + (a * 0.10)
c = a + (a * 0.15)

if a >= 1250:
    print(f'Seu salário de \33[33m{a}\33[m, receberá aumento de 10%, ficando:{b}')
elif a < 1250:
    print(f'Seu salário de {a}, receberá aumento de 15%, ficando: {c}')
