#ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTERIOS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# O PRIMEIRO VALOR É MAIOR; O SEGUNDO VALOR É MAIOR; NAO EXISTE VALOR MAIOR, OS DOIS SAO IGUAIS.

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
if n1 > n2:
    print('O maior numero é {} e o menor {}'.format(n1,n2))
else:
    print('O maior número é {} e o menor {}'.format(n2,n1))