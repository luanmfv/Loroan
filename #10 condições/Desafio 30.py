#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
numero = int(input('Me diga um número:'))
resultado = numero % 2
if resultado ==0:
    print('{} é par'.format(numero))
else:
    print('{} é impar'.format(numero))