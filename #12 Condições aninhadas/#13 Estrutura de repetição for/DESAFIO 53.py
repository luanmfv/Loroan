#CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS.#EX: APOS A SOPA
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]

#'''for letra in range(len(junto) - 1, - 1, - 1):
#    inverso += junto[letra]'''

print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos uma palíndromo')
else:
    print('A frase não é um palíndromo')
