numeros = list()
while True:
    n = (int(input(f'Digite um valor:')))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado, não será possível adicionar.')
    r = (str(input('Quer continuar?[S/N]')))
    if r in 'Nn':
        break
numeros.sort()
print(f'O valores digitado em ordem crescente são {numeros}')


