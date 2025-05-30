#lanche.append('cookie')  append vc adiciona um item ao final da lista
#lanche.insert(0, 'cachorroquente') #o insert ira adicionar um item na lista e o 0 é a posição da lista onde você quer colocar
# ao inves do insert substituir o item 0 ele vai colocar uma posição 0 nova em cima e o 0 anterior passa a ser o 1

#lista é
#lanche = [hamburguer, suco, pao, farofa]


#del lanche [3]   (3 seria o espaço que você escolheu para deletar
# ou então usa-se lanche.pop(3) que faz a mesma coisa (caso nao coloque nada no (3) ele elimina diretamente o ultimo elemento
# ou lanche.remove('pizza')     (pizza seria o conteudo que vc quer eliminar, temos essas tres formas de eliminar um item na lista
# apos a eliminação dele os elementos são reposicionados

#if 'pizza' in lanche:
#    lanche.remove('pizza')


#valores = list(range(4,11))

#ele iria mostrar abaixo

#valores = 4,5,6,7,8,9,10
#nas posições 0,1,2,3,4,5,6
#len(valores) == 7

#caso vc queira uma lista organizada vc faz valores.sort()  que ele organiza os numeros por ordem ou por letra alfabetica

#caso vc queira organizar de forma ao contrario utiliza-se:  valores.sort(reverse=True)

#valores = []
#valores.append(5)
#valores.append(9)
#valores.append(4)
#for c, v in enumerate(valores):  #enumerate pega a posição e o valor e mostre, sendo assim, c posição e v valor
#    print(f'na posição {c} encontrei o valor {v}!')
#print('cheguei ao final da lista')

#valores = []
#for cont in range (0,5):
#   valores.append(int(input('Digite um valor')))
#for c, v in enumerate(valores):  #enumerate pega a posição e o valor e mostre, sendo assim, c posição e v valor
#    print(f'na posição {c} encontrei o valor {v}!')
#print('cheguei ao final da lista')



a = [1,2,3,4,5]
b = a    #aqui caso fosse b = a[:] ele alteraria somente o b, pois o a seria apenas uma copia dele e não o proprio a em si
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#alterar um dado da lista altera ele todo





