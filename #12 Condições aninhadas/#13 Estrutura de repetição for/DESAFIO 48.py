#FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SAO MULTIPLOS DE TRES E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500

soma = 0

for num in range(1, 501, 2):  # Pega apenas números ímpares
    if num % 3 == 0:  # Verifica se é múltiplo de 3
        soma += num  # Soma os valores

print(f'A soma de todos os números ímpares múltiplos de 3 no intervalo de 1 a 500 é {soma}')