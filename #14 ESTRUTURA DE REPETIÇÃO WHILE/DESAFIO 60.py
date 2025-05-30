#FAÇA UM PROGRAMA QUE LEIA UM NUMERO QUALQUER E MOSTRE O SEU FATORIAL.
#EX: 5! = 5X4X3X2X1 = 120
fatorial = 1
n = int(input('Digite um número:'))
for c in range (n , 0 , -1):
    fatorial *= c
print(' O fatorial desse número é {}'.format(fatorial))

