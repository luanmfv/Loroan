#FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
# SE ELE AINDA VAI SE ALISTAR NO SERVIÇO MILITAR; SE É A HORA DE SE ALISTAR; SE JÁ PASSOU DO TEMPO DE ALISTAMENTO.
# SEU PROGRAMA DEVE MOSTRAR O TEMPO QUE FALTOU, OU PASSOU DO PRAZO.


idade = int(input('Olá, bem vindo a consulta da junta militar. Por favor digite a sua idade ☠️:'))
if idade < 18:
    print('Ainda não é a hora de você se alistar, ainda faltam {} anos'.format(18-idade))
elif idade == 18:
    print('Já está na hora de se alistar ☠️')
elif idade > 18:
    print('Já até passou do tempo de se alistar safado, já passaram {} anos ☠️'.format(idade-18))
