#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print ('O maior número é {} e o menor é {}'.format(maior,menor))