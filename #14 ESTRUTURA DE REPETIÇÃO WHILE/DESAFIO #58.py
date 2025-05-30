#MELORES O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI ''PENSAR'' EM UM NUMERO ENTRE 0 E 10. SO QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.

from random import randint
computador = randint (0 , 10)
palpite = int(input('Desafio == Advinhe o numero que estou pensando de 0 a 10:'))
while palpite != computador:
    palpite = int(input('Você errou, tente novamente:'))
else:
    print('Parabéns, você acertou!')