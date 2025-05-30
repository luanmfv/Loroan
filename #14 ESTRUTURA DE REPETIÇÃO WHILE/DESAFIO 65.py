#CRIE UM PROGRAMA QUE LEIA VARIOS NUMEROS INTEIROS PELO TECLADO. NO FINAL DA EXECUCAO, MOSTRE A MEDIA ENTRE TODOS OS VALORES E QUAL FOI O MAIOR E MENOR VALORES LIDOS. O PROGRAMA DEVE PERGUNTAR AO USUARIO SE ELE QUER OU NAO CONTINUAR A DIGITAR VALORES.
resposta = 'S'
mairo = menor = soma = quantidade = media = 0
while resposta in 'S':
    num = int(input('Digite um número:'))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar?[S/N]')).upper().strip()[0]
media = soma / quantidade
print('Você digitou {} numeros, e a media deles foi {}'.format(quantidade,media))
print('O maior numero foi {} e o menor numero foi {}'.format(maior,menor))
print('FIM')