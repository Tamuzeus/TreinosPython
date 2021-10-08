peso = float(input('Digite o seu peso, em Kg,: '))
altura = float(input('Digite a sua altura, em metros,: '))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'Com o IMC: {imc:.2f}, você está Abaixo do Peso.')
elif imc >= 18.5 and imc <= 25:
    print(f'Com o IMC: {imc:.2f}, você está no Peso Ideal.')
elif imc > 25 and imc <= 30:
    print(f'Com o IMC: {imc:.2f}, você está com Sobrepeso.')
elif imc > 30 and imc <= 40:
    print(f'Com o IMC: {imc:.2f}, você está com Obesidade.')
elif imc > 40:
    print(f'Com o IMC: {imc:.2f}, você está Obesidade Mórbida.')
