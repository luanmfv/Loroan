#Tuplas são imutaveis
#Se existe a varivel lanche = hamburguer, suco, pizza e pudim. e vc quiser alterar o pudim para sorvete não consegue.
#lanche = () tuplas [] lista {} dicionario
#é possivel também criar tuplas sem parenteses: lanche = 'hamburguer', 'Suco', 'Pizza', 'Pudim'

#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
#for comida in lanche:
#    print(f'Eu comi {comida}')
#for cont in range (0, len(lanche)):
 #   print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#for pos,  comida in enumerate(lanche):
 #  print(f'Eu comi {comida} na posição {pos}')
#print('Comi demaiszi')
#print(sorted(lanche))
#print(lanche)

#-=---------------------------------------------------------------------------------------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(4))
print(c.count(5))

#=======================================================================================================================
#pessoa = ('Gustavo', 39, 'M', 99.88)
#del(pessoa)
#(pessoa)