#Módulos e Pacotes

#modularização surgiu decada de 60 sistemas cada vez maiores, dividir um programa grande, aumentar a legibilidade, facilita a manutenção.

from uteis import numeros

num = int(input('Digite um valor:'))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')

#vantagens - organização do código; facilita manutenção; ocultar o código detalhado; reutilizar os módulos em outros projetos.

#>>>>>>>>>>>>>>>>>>>>>>>>> Pacotes <<<<<<<<<<<<<<<<<<<<<<<

#Pacotes é onde você tem uma pasta, e dentro dela varias pastas, cada um com um modulo nele, cores, datas, numeros, strings e etc aonde vc pode importar no seu programa para utilizar.
#Dentro de cada pasta precisa ter __init__.py  o pycharm faz isso sozinho, mas por exemplo em vs code você precisaria criar.



