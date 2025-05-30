#CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VARIAS PESSOAS. A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUARIO QUER OU N~ÇAO CONTINUAR. NO FINAL, MOSTRE:
#A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS. B) QUANTOS HOMENS FORAM CADASTRADOS. C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.
maior = homem = mulher20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F]')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'M' and idade <= 20:
        mulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {maior}')
print(f'Total de homens cadastrdos{homem}')
print(f'Total de mulheres com menos de 20 anos {mulher20}')
print('Acabou')
