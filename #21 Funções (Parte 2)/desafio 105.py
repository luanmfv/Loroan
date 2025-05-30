def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n) #max é para pegar o maior valor
    r['menor'] = min(n) #min pegar o menor valor da lista
    r['media'] = sum(n)/len(n) #soma de todos os valores dividio pela quantidade de valores, 2 + 5 + 4 + 3 / 4
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Razoável'
        else:
            r['situação'] = 'Ruim'
    return r # o return é necessário, pois caso não exista não haverá retorno de uma função que recebe os parametros (resp = notas(2,5,4,3) caso fosse uma lista direta como notas(2,5,5 não haveria necessidade do return)


#Programa principal
resp = notas(2, 5, 4, 3, sit=True)
print(resp)
