a = float(input('Digite a largura da parede: '))
b = float(input('Digite a altura da parede: '))
area = a*b

print(f'Se a cada 1 litro de tinta pinta uma área de 2m^2, para pintar uma parede com a largura {a}m^2 e altura {b}m^2, formando a área de {area:.2f} m^2, é nescessário {area/2:.2f} litros de tinta')