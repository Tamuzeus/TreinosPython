a = input(str('Digite o seu nome completo: '))

b = a.upper()
c = a.lower()
d = len(a.strip())-a.count(' ')
e = a.find(' ')  #Irá encontrar o primeiro espaço e ir até o primeiro após ele, começando antes do A e terminando depois do a de Ana

print(f'O nome com todas as letras maiúsculas é: {b}')
print(f'O nome com todas as letras minísculas é: {c}')
print(f'Quantas letras tem ao todo(sem espaços): {d}')
print(f'O primeiro nome é: \33[33m{e}\33[m')