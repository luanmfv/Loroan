#ELABORE UM PROGRAMA QUE CALCULE UM VALOR A SER PAGO PELO PRODUTO, CONSIDERANDO SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO: A VISTA DINHEIRO/CHQUE: 10% DE DESCONTO  ;  A VISTA NO CARTÃO: 5% DE DESCONTO  ;  EM ATÉ 2X NO CARTÃO: PREÇO NORMAL  ;  3X OU MAIS NO CARTÃO: 20% DE JUROS.

print('Você quer comprar nossa lava louças, ela custa R$1300')
print('Qual será a forma de pagamento? (Digite o número correspondente')
print('1 A vista dinheiro/cheque')
print('2 A vista no cartão')
print('3 Em até 2x no cartão')
print('4 3x ou mais no cartão?')
pagamento = int(input(':'))

preco = 1300

if pagamento == 1:
    desconto = preco * 0.90
    print('O valor com desconto é {}'.format(desconto))
elif pagamento == 2:
    desconto = preco * 0.95
    print('O valor com desconto é {}'.format(desconto))
elif pagamento == 3:
    print('O valor normal é 1300')
elif pagamento == 4:
    juros = preco * 1.20
    print('O valor com juros é {}'.format(juros))