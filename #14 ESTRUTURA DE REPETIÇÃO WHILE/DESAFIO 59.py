#CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
#[1] SOMAR
#[2] MULTIPLICAR
#[3] MAIOR
#[4] NOVOS NUMEROS
#[5] SAIR DO PROGRAMA
#SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

v1 = int(input('Digite um valor:'))
v2 = int(input('Digite mais um valor:'))
opcao = 0
while opcao != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    opcao = int(input('Qual é a sua opção?'))
    if opcao == 1:
        print('A soma dos valores é {}'.format(v1+v2))
    elif opcao ==2:
        print('A multiplicação dos valores é {}'.format(v1 * v2))
    elif opcao ==3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('O maior número é {}'.format(maior))
    elif opcao ==4:
        print('Informe os numeros novamente:')
        v1 = int(input('Primeiro valor:'))
        v2 = int(input('Segundo valor'))
    elif opcao ==5:
        print('Finalizando...')

    else:
        print('Opção invalida, tente novamente.')
    print('==' *10)
print('Fim do programa')




