#DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR DIGITADO FOR IMPAR, DESCONSIDERE-O.
soma = 0
conta = 0

for c in range(1,7):
    numero = int(input('Digite o {}° numero:'.format(c)))
    if numero % 2 == 0:
        soma += numero
        conta += 1
print ('Você informou {} números  pares e a soma foi {}'.format(conta,soma))
