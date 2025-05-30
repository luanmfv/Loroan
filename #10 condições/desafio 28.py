#Escreva um programa que faça o computador ''pensar'' em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint (0,5) #aqui o sistema entrega para o código o número de 0 a 5
print ('Vou pensar em um número entre 0 e 5, tente advinhar')
jogador = int(input('Em que número eu pensei?'))
if jogador == computador:
    print('Parabéns, você conseguiu advinhar')
else:
    print('Parabéns viu, seu coco, eu pensei no {} e não no {}'.format(computador,jogador))

