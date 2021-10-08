nome = str(input('Digite o nome do aluno: '))

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

if media < 5.0:
    print(f'Aluno: {nome}:')
    print(f'Você tem a média abaixo de 5.0, com: {media:.1f}, está reprovado!')
elif media >= 5.0 or media <= 6.9:
    print(f'Aluno: {nome}:')
    print(f'Você tem a média entre 5.0 e 6.9, com: {media:.1f}, você está de recuperação!')
elif media > 7.0:
    print(f'Aluno: {nome}:')
    print(f'Você tem a média acima de 7.0! Com {media:.1f}, você está aprovado!')