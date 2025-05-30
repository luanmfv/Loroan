listagem = ('lapis', 1.75,
            'borracha', 2,
            'caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)
#o nome do item na posição par (0) e o preço na posição impar (1)
print('-' * 40) #colocar 40 linhas de traço -
print(f'{"LISTAGEM DE PREÇOS":^40}')#entre 40 espaços  o simbolo ^ para ficar no meio
print('-' * 40)
for pos in range(0, len(listagem)):#o len foi para definir que não tem final caso você queira adicionar mais itens
    if pos % 2 == 0: #se a possição for dividido por 2, ou o mesmo que se for par
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

