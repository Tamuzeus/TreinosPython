a = int(input('Digite a distância da viagem em Km: '))

b = 0.50*a
c = 0.45*a

if a<=200:
    print(f'A distância de sua viagem é de {a} Km, logo deve pagar R$ \33[36m{b}\33[m!')

elif a>200:
    print(f'A distância de sua viagem é de {a} Km, logo deve pagar R$ \33[33m{c}\33[m!')