from random import randint
from time import sleep


def sorteia(lista): #criou uma nova variavel chamada lista
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)     # lista -> sorteia -> números
        print(f' {n} ', end='')
        sleep(0.3)
    print('PRONTO')

def somaPar(lista):
    soma  = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores totais da lista são {lista} e a soma dos pares é de {soma}')

números = list()
sorteia(números)
somaPar(números)
