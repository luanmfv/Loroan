#DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZAO DE UMA PA. NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO (PROGRESSÃO ARITMETICA)
termo = int(input('Digite um numero para ser o termo:'))
razao = int(input('Digite um numero para ser a razao:'))
decimo = termo + ( 10-1 ) * razao
for c in range (termo, decimo + razao, razao):
    print('{}'.format(c), end=' > ')
print('🙄 FIM 🙄')

