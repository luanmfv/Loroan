from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
ano = int(input('Ano de nascimento:'))
dados['idade'] = datetime.now().year - ano
dados['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salario'] = float(input('Salário:'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')