casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Digite em quantos anos você deseja pagar: '))

prestm = casa/(12*anos) #prestação, da casa
minimo = salario * 30/100 #assim, tira 30% do salario dele. A casa só passa se a prestação não passar os 30%.

if minimo > prestm:
    print(f'Seu empréstimo foi aprovado. Pagou o {minimo} de {prestm:.2f}', end='') # ,end='' isso fará a linha debaixo subir
    print(f'a prestação será de {prestm:.2f}.')

elif minimo < prestm:
    print('Seu empréstimo foi rejeitado.')
    print(f'Tem que pagar {prestm}, e você só tem: {minimo}.')