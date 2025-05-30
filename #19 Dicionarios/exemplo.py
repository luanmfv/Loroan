#VARIAVEIS COMPOSTAS (DICIONARIOS)
# Tuplas ()    Listas []     Dicionarios {}

#dados = dict()     ou dados = {} para criar um dicionario
dados = dict()
dados = {'nome':'Pedro', 'idade':25}
dados['sexo'] = 'M'
print(dados['nome'])
print(dados['idade'])
print(dados['sexo'])

#temos deldados['idade']     iria excluir a coluna idade

filme = {}
filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George Lucas'
         }
print(filme['titulo'])
print(filme['ano'])
print(filme['diretor'])
#se usar print(filme.values())    ele ira mostrar todos os valores de uma vez
#se quiser somente as chaves (titulo, ano e diretor) o comando é print(filme.keys())
#se quiser todo os itens, chaves e valores o comando é print(filme.items())

for k,v in filme.items():
    print(f'O {k} é {v}')

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
for k, v in pessoas.items():
    print(f'{k} = {v}')

#del pessoas['sexo'] apagaria a coluna sexo que tem o m dentro
#pessoas['nome'] = 'Leandro'   o nome gustavo passaria a ser leandro
#para adicionar um novo elemento é pessoas['peso'] = 98.5

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil[1]['sigla']) #mostrara SP

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
    brasil.append(estado.copy())  # para copiar a lista no dicionario ao inves de [:]
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.') # para mostrar o campo uf tem valor sp e o campo sigla tem valor sp







