a = input(str('Digite o seu nome: '))
a = a.title()

if 'Silva' in a:
    print(f'O nome {a}, possui o nome "Silva".')

if not 'Silva' in a:
    print(f'O nome {a}, não possui o nome "Silva".')
