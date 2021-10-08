import math
angulo = int(input('Digite o angulo que deseja saber o resultado: '))

sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)

print(f'O seno é de \33[36m{sen:.2f}\33[m.')
print(f'O coseno é de \33[36m{cos:.2f}\33[m.')
print(f'A tangente é de \33[36m{tan:2f}\33[m.')