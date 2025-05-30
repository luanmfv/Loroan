from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Roberto': randint(1,6),
         'Silvana': randint(1,6),
         'Jailson': randint(1,6),
         'Pedrinho Matador': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' *30)
print('RANK DOS JOGADORES')
for i, v in enumerate(ranking): #indice e valor
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)