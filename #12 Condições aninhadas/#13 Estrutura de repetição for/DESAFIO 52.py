#FAÇA UM PROGRAMA QUE LEIA UM NUMERO INTEIRO E DIGA SE ELE É OU NÃO UM NUMERO PRIMO.

num = int(input('Digite um número:'))
total = 0
for c in range (1, num + 1):
    if num % c ==0:
        total += 1
        print('\033[34m', end='')
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='')
print('O numero {} foi divisivel por {} vezes'.format(num,total ))
if total == 2:
         print('E por iso ele é primo')
else:
    print('E por isso ele não é primo')