lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('Digite um valor:')))
    c = str(input('Quer continuar?[S/N]'))
    if c in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares foram {impares}')