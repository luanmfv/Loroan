v1 = int(input('Digite o primeiro valor:'))
v2 = int(input('Digite o segundo valor:'))
v3 = int(input('Digite o terceiro valor:'))
v4 = int(input('Digite o quarto valor:'))
tupla = (v1, v2, v3, v4)
print(f'Você digitou os valores {tupla}')
print(f'O numero 9 apareceu {tupla.count(9)} vezes')
#count é usado para saber quantas vezes apareceu o numero 9
#index serve para ver em qual posição o numero está
if 3 in tupla:
    print(f'O numero 3 está na posição {tupla.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')

