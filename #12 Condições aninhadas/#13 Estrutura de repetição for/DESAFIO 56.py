#DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DO PROGRAMA, MOSTRE: A MEDIA DE IDADE DO GRUPO ; QUAL É O NOME DO HOMEM MAIS VELHO ; QUANTAS MULHERES TEM MENOS DE 20 ANOS.
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1,5):
    print('{}ª pessoa'.format(c))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade
    if c ==1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
        if sexo in 'Mm' and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        if sexo in 'Ff' an idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiordadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))
