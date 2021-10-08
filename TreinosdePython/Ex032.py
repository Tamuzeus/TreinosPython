#nome = str(input('Digite o seu nome: ')).strip().title()
#sexo = str(input('Digite o seu sexo [M/F]: ')).strip().title()
#EstadoCivil = str(input('Digite o seu estado civil[S/C]: ')).strip().title()

#if sexo == 'M' and EstadoCivil == 'C':
 #   anos = int(input('Digite a quanto tempo, em anos, estão casados: '))
  #  print(f'Parabéns pelos seus {anos} anos de casados!')

#else:
 #   print('Fim do programa')

a = int(input('Digite o ano, assim verificarei se ele é bissexto: '))

b = a%4

if b == 0:
    print(f'{a}, é um ano bissexto')
else:
    print(f'{a}, não é um ano bissexto')