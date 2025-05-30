#dados = []
#dados.append('Pedro')
#dados.append(25)
#print(dados[0])    (ira aparecer pedro)
#print(dados[1]) (aparece numero 25)

#pessoas = list()
#pessoas.append(dados[:]) (isso gera uma copia da lista dados completa dentro da lista pessoas, então a [0] se torna dados
# para mostrar tudo é

#pessoas[['Pedro',25], ['Maria',19], ['Joao',32]]
#print(pessoas[0][0]) ele ira printar Pedro
#print(pessoas[1]) mostrara ['Maria',19]
#teste = list()
#teste.append('Luan')
#teste.append(25)
#galera = list()
#galera.append(teste[:])
#teste[0] = 'Yansha'
#teste[1] = 24
#galera.append(teste[:])
#print(galera)

#galera =[['Luan', 25], ['Angelica', 46], ['Leticia', 13], ['Erick', 26]]
#for p in galera:
#    print(f'O nome é {p[0]} e a idade é {p[1]}')
totmaior = totmenor = 0
galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')

