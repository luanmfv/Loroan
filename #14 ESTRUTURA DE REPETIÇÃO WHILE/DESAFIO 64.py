#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUARIO DIGITAR O VAOR 999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NUMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG).
contador = 0
quantidade = 0
soma = 0
n1 = 0
while n1 < 999:
    n1 = int(input('Digite mais um numero inteiro'))
    contador += n1
    quantidade += 1
    soma += n1
print('Você digitou {} numeros, e a soma entre eles é {}'.format(quantidade, soma))

print('Fim')