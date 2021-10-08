import math
ca = float(input('Digite o valor do comprimento do cateto oposto: '))
co = float(input('Digite o valor do comprimento do cateto adjacente: '))

h = math.hypot(ca, co)

print(f'O valor da hipotesnusa é de \33[32m{h:.2f}\33[m.')