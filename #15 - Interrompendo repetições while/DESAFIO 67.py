#FAÇA UM PROGRAM QUE MOSTRE A TABUADA DE VARIOS NUMEROS, UM DE CADA VEZ, PARA CADA VALOR DIGITADO PELO USUARIO. O PROGRAMA SERÁ INTERROMPIDO QUANDO O NUMERO SOLICITADO FOR NEGATIVO.
while True:  # Loop infinito, será interrompido se o número for negativo
    tabuada = int(input('Qual tabuada você quer? (Digite um número negativo para sair): '))

    if tabuada < 0:  # Se o número for negativo, o programa para
        break

    c = 1  # Reinicia o contador
    while c <= 10:
        resultado = tabuada * c
        print(f"{tabuada} x {c} = {resultado}")  # Exibe a tabuada formatada
        c += 1  # Incrementa o contador

    print("-" * 20)  # Linha separadora entre tabuadas

print("FIM")