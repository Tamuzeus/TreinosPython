s = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:         #achará o multiplo de 3
        s += c             #contagem da soma
        contador += 1      #faz a contagem de cada rodada
print(s)

print(contador)


