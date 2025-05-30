#A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE. 9 ANOS MIRIM; 14 ANOS INFANTIL; 19 ANOS JUNIOR; 20 ANOS SENIOR; ACIMA MASTER.

id = int(input('Olá nadador, bem vindo a Confederação nacional de natação, digite sua idade:'))
if id <= 9:
    print('Sua classe de nadador é MIRIM')
elif 10 <= id <= 14:
    print('Sua classe de nadador é INFANTIL')
elif 15 <= id <= 19:
    print('Sua classe de nadador é JUNIOR')
elif id == 20:
    print('Sua classe de nadador é SENIOR')
else:
    print('Sua classe de nadador é MASTER')