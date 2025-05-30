#FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, MAS SO ACEITE OS VALORES 'M' OU 'F'. CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.


sexo = str(input('QUAL É O SEU SEXO? [M] , [F]?')).strip().upper()[0]
print(sexo)
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor, digite seu sexo[M/F]:')).strip().upper(0)
print('Sexo {} registrado com sucesso'.format(sexo))
