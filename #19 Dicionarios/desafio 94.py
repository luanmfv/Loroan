pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('erro, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade:'))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('erro, responda apenas S ou N.')
    if resp == 'N':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.') # o len de galera mostra quantas pessoas foram cadastradas
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram', end=' ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print('        ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('encerrado')

