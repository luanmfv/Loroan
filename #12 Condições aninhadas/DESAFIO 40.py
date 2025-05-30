#CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA.
#MEDIA ABAIXO DE 5.0 REPROVADO; ENTRE 5.0 E 6.9 RECUPERAÇÃO; 7.0 OU SUPERIOR APROVADO.

n1 = float(input('Digite sua primeira nota:'))
n2 = float(input('Digite sua segunda nota:'))
r1 = (n1 + n2) / 2
if r1 < 5.0:
    print('Sua média é {} Você foi reprovado :('.format(r1))
elif 5.0 <= r1 <= 6.9:
    print('Sua média é {}, você está de recuperação :/'.format(r1))
else:
    print('Parabéns, sua média é {}, você foi aprovad =D'.format(r1))





