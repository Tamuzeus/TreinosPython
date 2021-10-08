#numero = 0
#contador = 0
#soma = 0
#while numero != 999:

 #   numero = int(input('Digite os numeros inteiros: '))
  #  print('Ao digitar: "999", o programa vai ser finalizado.')
   # contador += 1 #a cada volta vai adicionar mais um
    #soma += numero #vai somar os numeros de cada volta

#print(f'O programa contou {contador-1} números!')
#print(f'A soma de todos esses é {soma-999}!')

#sem contagem precisar subtrair no final

numero = 0
contador = 0
soma = 0

numero = int(input('Digite os numeros inteiros: '))
print('Ao digitar: "999", o programa vai ser finalizado.') #estando aqui e repetido depois, ja desconsidera o valor digitado

while numero != 999:

    contador += 1 #a cada volta vai adicionar mais um
    soma += numero #vai somar os numeros de cada volta
    numero = int(input('Digite os numeros inteiros: '))
    print('Ao digitar: "999", o programa vai ser finalizado.') #o flag vai ser contado

print(f'O programa contou {contador} números!')
print(f'A soma de todos esses é {soma}!')
