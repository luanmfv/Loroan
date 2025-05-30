#FAÇA UM PROGRAMA QUE JOGUE PAR OU IMPAR COM O COMPUTADOR. O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, MOSTRANDO O TOTAL DE VITORIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.
from random import randint
v = 0
while True:
     jogador = int(input('Digite um valor:'))
     computador = randint(0 , 10)
     total = jogador + computador
     tipo = ' '
     while tipo not in 'PI':
         tipo = str(input('Par ou impar?[P/I]')).upper().strip()[0]
     print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
     if tipo == 'P':
        if total % 2 == 0:
            print('Parabéns,você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
     elif tipo == 'I':
            if total % 2 == 1:
                print('Parabéns, você venceu')
                v += 1
            else:
                    print('Voce perdeu')
            break
     print('Vamos jogar novamente...')
print(f'GAME OVER! Você ganhou {v} vezes.')





