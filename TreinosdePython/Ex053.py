frase = input("Qual a frase? ").upper().strip()
if frase == frase[::-1]:   #os ' :: ' servem para ativar o -1, que vai inverter a frase
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")