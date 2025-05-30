#ESCREVA UM PROGRAMA PARA APROVAR UM EMPRÉSTIMO BANCARIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA, O SALARIO
#DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
#CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODE EXCEDER 30% DO SALARIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

print('Bem vindo ao simulador de compra de imóveis 😎')

casa = float(input('Digite o valor da residência:'))
salario = float(input('Qual é o seu salário:'))
anos = int(input('Em quantos anos você vai pagar:'))
presta = casa / (anos * 12)
limite = salario * 0.3
if presta > limite:
    print('O empréstimo foi negado, o salario não pode exceder mais de 30% dele 😥')
print ('A prestação mensal será de:{:.2f}'.format(presta))