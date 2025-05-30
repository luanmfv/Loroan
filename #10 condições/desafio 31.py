#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Quantos kms deram a sua viagem?'))
if distancia <= 200:
    total = distancia * 0.50
else:
    total = distancia * 0.45
print ('Sua viagem deu o total de R${:.2f}'.format(total))