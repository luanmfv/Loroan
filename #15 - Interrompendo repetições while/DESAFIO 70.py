#CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VARIOS PRODUTOS. O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO VAI CONTINUAR. NO FINAL, MOSTRE:
#A) QUAL É O TOTAL GASTO NA COMPRA. B)QUANTOS PRODUTOS CUSTAM MAIS DE R$1000. C) QUAL É O NOME DO PRODUTO MAIS BARATO.
valor = produtos = barato = contador = 0
print('Bem vindo ao mercadinho big bom, cadastre seu produto abaixo 😋😋😋😋😋')
while True:
    nomep = str(input('Nome do produto:')).upper().strip()[0]
    preçop = float(input('Preço do produto:'))
    contador += 1
    respo = str(input('Quer continuar?[S/N]')).upper().strip()[0]
    valor += preçop
    if preçop >=1000:
        produtos+=1
    if contador ==1:
        barato = preçop
    else:
        if preçop < barato:
            barato = preçop
    if respo == 'N':
        break
print(f'O total deu R${valor}')
print(f'{produtos} produtos custam mais de R$1000')
print(f'O produto mais barato é o com valor de {barato}')
print('Obrigado por utilizar o caixa do mercadinho big bom 🥶🥶🥵🥵')