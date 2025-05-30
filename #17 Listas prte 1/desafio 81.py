lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    c = str(input('Quer continuar?[S/N]')).upper()
    if c in 'N':
        break
print('=-' *30)
print(f'A quantidade de numeros digitados foram de {len(lista)}')
print('=-' *30)
lista.sort(reverse=True)
print(f'os numeros digitados na forma decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
