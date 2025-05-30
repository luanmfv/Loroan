#DESENVOLVA UMA LOGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO: ABAIXO DE 18.5: ABAIXO DO PESO ; ENTRE 18.5 E 25: PESO IDEAL ; 25 ATÉ 30 SOBREPESO ; ACIMA DE 40: OBESIDADE MORBIDA.

peso = float(input('Olá, vamos calcular o seu IMC. Digite seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso / (altura * altura)
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc <= 25:
    print('Você está com o peso ideal, parabéns =)')
elif 25.1 <= imc <= 39:
    print('Você está com sobrepeso')
else:
    print('Você está com obesidade morbida, tome cuidado com sua saúde')