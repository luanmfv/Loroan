#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Quanto é o seu salário?'))
if salario <= 1250:
   novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print ('Seu salario era {:.2f} e agora é {:.2f}'.format(salario,novo))

