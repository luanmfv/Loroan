def aumentar(preço=0, taxa=0, formato=False):
    '''

    :param preço: recebe o valor informado
    :param taxa: % aplicada
    :param formato: R$ e , inserio para exemplo R$150,00
    :return: none
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)
#pode-se utilizar também
#   return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')  #replace parece ser um comando de trocar um pelo outro, ai parace trocar . por ,

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30)) #esse center parece deixar a palavra dita no centro entre 30 caracteres
    print('-' * 30)
    print(f'Preço analisado: {moeda(preço)}')
    print('-' * 30)
