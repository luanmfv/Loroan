#todas as funções no python são identificadas por () no nome
#agora você aprendeu o que é def

#def soma(a,b):
#    print(f'A = {a} e B = {b}')
#    s = a + b
#    print(f'A soma A + B = {s}')


#soma(b=5, a=4)
#soma(7,2)

#o end='' é para não quebrar a linha e continuar na mesma
#def contador(* num):
#    print(num)


#contador(2, 1, 7)
#contador(8, 0)
#contador(4, 4, 7, 6, 2)

#def contador(* num):
#    for valor in num:
#       print(f'{valor} ', end='')
#    print('FIM') #aqui ele mostra 2, 1, 7 FIM. dps 8,0 FIM

def contador(* num):  # esse *num significa que recebera parametros infinitos
    tam = len(num)# len informa quantos elementos tem exemplo,(1, 2 , 3, 5) o len informa que existem 4 elementos
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

print()
print()

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores) #esses comandos foram feitos para dobrar os valores da lista valores

print()
print()

def soma(*valores):
    s = 0
    for n in valores:
        s+= n
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)#essas funções foram feitas para somas todos os valores registrados