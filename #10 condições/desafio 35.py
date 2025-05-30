#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print ('Analisador de triangulo')
t1 = float(input('Vamos tentar fazer um triangulo, digite a distancia da primeira reta:'))
t2 = float(input('Segunda reta'))
t3 = float(input('Terceira reta'))

nt = t1 + t2 < t3 and t1 + t3 < t2
if t2 + t3 < t1 or t2 + t1 < t3 or nt:
    print('Isso não é um triangulo')
else:
    print('Isso é um triangulo')


