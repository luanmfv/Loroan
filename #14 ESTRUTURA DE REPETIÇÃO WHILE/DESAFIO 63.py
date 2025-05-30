#ESCREVA UM PROGRAMA QUE LEIA UM NUMERO N INTEIRO QUALQUER E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUENCIA DE FIBONACCI.
#EX: 0 > 1 > 1 > 2 > 3 > 5 > 8

n1 = int(input('Vamos verificar a sequência de Fibonacci, digite um número para verificar:'))
t1 = 0
t2 = 1
print(' {} > {}'.format(t1, t2), end='')
cont = 3
while cont <= n1:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('> FIM')







