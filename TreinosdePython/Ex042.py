plado = int(input('Digite o primeiro lado: '))
slado = int(input('Digite o segundo lado: '))
tlado = int(input('Digite o terceiro lado: '))

if plado + slado > tlado and slado + tlado > plado and tlado + plado > slado:
    if plado != slado and plado != tlado and tlado != slado:
        print(f'''O triangulo é escaleno, com todos os lados diferentes!
        Primeiro lado: {plado}
        Segundo lado: {slado}
        Terceiro lado: {tlado}''')
    elif plado == slado and plado == tlado and slado == tlado:
        print(f'''O triangulo é equilátero, com todos os lados iguais!
        Primeiro lado: {plado}
        Segundo lado: {slado}
        Terceiro lado: {tlado}''')
    else:
        print(f'''O triangulo é isóceles, com dois lados iguais!
               Primeiro lado: {plado}
               Segundo lado: {slado}
               Terceiro lado: {tlado}''')

else:
    print('Não é possivel formar um triangulo!')