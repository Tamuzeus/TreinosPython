a = int(input('Digite a velocidade: '))
print('Você será multado por R$ 7,00 cada 1 Km, acima do limite de 80 Km')



if a > 80:
    b = (7*(a-80))
    print(f'Você será multado! Sua velocidade é de {a} Km/h, terá de pagar R${b} ')
else:
    print('Você não será multado!')

