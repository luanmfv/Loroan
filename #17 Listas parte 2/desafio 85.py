
estrutura = [[], []]
valor = 0
for c in range (1,8):
    valor = (int(input(f'Digite o {c} valor:')))
    if c % 2 == 0:
       estrutura[0].append(valor)
    else:
        estrutura[1].append(valor)
print('-=' * 30)
print(f'os valores pares foram {estrutura[0]}, e os impares foram {estrutura[1]}')

