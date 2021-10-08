pren = float(input('Digite o preço do produto: '))

cond = str(input('''Digite a condição de pagamento:
        A) Dinheiro/Cheque: Desconto de 10%.
        B) Cartão(1x): Desconto de 5%.
        C) Cartão(2x): Preço comum.
        D) Cartão (3x ou +): 20% de juros.
        Escolhe a letra correspondente a opção: ''')).strip().upper()

if cond == 'A':
    desconto = pren * (10/100)          #calcular o desconto
    print(f'O desconto será de R${desconto}!')
elif cond == 'B':
    desconto = pren * (5 / 100)
    print(f'O desconto será de R${desconto}!')
elif cond == 'C':
    print(f'O valor do produto permanecerá: R$ {pren}')
elif cond == 'D':
    juros = (pren * 20/100)              #calcular o juros
    print(f'O juros será de R${juros}!')