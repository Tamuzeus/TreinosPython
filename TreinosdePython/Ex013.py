a = int(input('Digite o preço do que você deseja comprar: '))
b = int(input('Digite o valor da porcentagem(o simbolo não é nescessário): '))
c = b/100
d = a*c

print(f'A sua compra de {a}, com o desconto de {b}% é de {d}, totalizando {a-d}.')