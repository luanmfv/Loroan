#REFAÇA O DESAFIO 35 DOS TRANGULOS ACRESCENTANDO O RECURSO DE MOSTRAR QUE TIPO DE TRIANGULO SERÁ FORMADO: EQUILATERO: TODOS OS LADOS IGUAIS ; ISOSCELES: DOIS LADOS IGUAIS; ESCALENO: TODOS OS LADOS DIFERENTES.
#OLHAR A RESPOSTA

print('Analisador de Triângulo')
t1 = float(input('Vamos tentar fazer um triângulo, digite a distância da primeira reta: '))
t2 = float(input('Segunda reta: '))
t3 = float(input('Terceira reta: '))

# Verifica se as três retas formam um triângulo
if t1 + t2 > t3 and t1 + t3 > t2 and t2 + t3 > t1:
    print('Isso é um triângulo', end=' ')
    # Verifica o tipo de triângulo
    if t1 == t2 == t3:
        print('Equilátero (todos os lados iguais)')
    elif t1 == t2 or t2 == t3 or t1 == t3:
        print('Isósceles (dois lados iguais)')
    else:
        print('Escaleno (todos os lados diferentes)')
else:
    print('Isso não é um triângulo')