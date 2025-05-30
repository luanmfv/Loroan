#CRIE UM POGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRONICO. NO INICIO, PERGUNTE AO USUARIO QUAL SERÁ O VALOR A SER SACADO (NUMERO INTEIRO) E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1.

print('Bem vindo ao caixa eletronico do banco Loroan =D')
print('CÉDULAS DE R$50, R$20, R$10 E R$1.')
valor = int(input('Digite o valor para saque:'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
        print(f'total de {totced} de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break


