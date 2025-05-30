#se a media foi 7 ele ta aprovado
dados = dict()
dados['nome'] = str(input('Digite seu nome:'))
dados['Nota'] = float(input(f'Digite a sua média:'))
if dados['Nota'] <= 6:
    print('Sua média está abaixo de 7, você reprovou.')
else:
    print('Sua média está acima de 7, parabéns você foi aprovado =)')

