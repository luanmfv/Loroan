#REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZAO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.
termo = int(input('Digite o termo:'))
razao = int(input('Digite a razao:'))

contador = 0

while contador <10:
    print(termo, end= ' > ')
    termo += razao
    contador += 1
print('FIM')


