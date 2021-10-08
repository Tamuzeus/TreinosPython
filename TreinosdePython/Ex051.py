pa = int(input('Digite o número para a conta da P.A: '))
razao = int(input('Digite a razão: '))
décimo = pa + ((11-1) * razao)  #calcular até aonde a pa vai
for c in range(pa, décimo, razao):
    print(c, end = ' > ')  #o end sobe os caracteres e os alinha, também define o que tem entre os espaços
print('Fim')