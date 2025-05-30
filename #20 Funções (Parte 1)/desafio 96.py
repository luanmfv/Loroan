def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terro {largura} x {comprimento} é de {a}m²')


#programa principal
print(' Controle de terrenos')
print('-' * 20)
l = float(input('LARGURA (m):'))
c = float(input('COMPRIMENTO (m):'))
area(l, c)
