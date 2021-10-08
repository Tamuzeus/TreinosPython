
sexo = ''
while sexo != 'M' and sexo != 'F' and sexo != 'O': #enquanto sexo for diferente de M ''e'' sexo for diferente de F ''e'' sexo for diferente de o
    sexo = str(input('''Escolha a opção do seu gênero [M/F/O]: 
                    M = Masculino
                    F = Feminino
                    O = Outros
                    
                    Opção: ''')).strip().upper()

    if sexo == 'M':
        print('Você é do gênero masculino!')
                     #interrupção que corta direto para fora do bloco.
    elif sexo == 'F':
        print('Você é do gênero feminino!')

    elif sexo == 'O':
        print('Você se considera "outros".')
        outrogenero = str(input('Digite o gênero que você se considera: ')).strip().lower()
        print(f'Seu gênero é {outrogenero}.')

    else:
        print('Escolha uma opção viável, tente novamente!') #sem interrupção, para que o bloco volte.

print('Obrigado pela participação!')