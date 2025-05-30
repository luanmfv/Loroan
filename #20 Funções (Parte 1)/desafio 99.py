from time import sleep

def maior(* núm): #o * é para dizer que vai receber varios parametros
    cont = maior = 0
    print('=-' *30)
    print('Analisando os valores passados...')  #parece que o \n faz com o que seja printado em cima de tudo, e depois os valores em for sao mostrados em baixo
    for valor in núm: #o for para pegar cada valor de num  e mostrar
        print(f'{valor} ', end='', flush=True) #o end é para continuar na mesma linha o próximo codigo
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram inforamdos {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}.')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()