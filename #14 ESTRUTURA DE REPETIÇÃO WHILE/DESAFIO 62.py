#MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUARIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE DISSE QUE QUER MOSTRAR 0 TERMOS.
termo = int(input('Digite o termo:'))
razao = int(input('Digite a razao:'))
total = 0
contador = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print(termo, end= ' > ')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?(digite 0 para finalizar'))
print('FIM')



