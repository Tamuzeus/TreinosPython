a = input(str('Digite o nome: ')).strip()

lista = a.split()
b = lista[0]
c = lista[len(lista)-1] #Com isso, vai contar o ultimo nome, sempre subtraindo com o menos 1

print(f'O primeiro nome é: {b}')
print(f'O último nome é: {c}')