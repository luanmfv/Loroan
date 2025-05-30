#def voto(ano):
#    a = 2025 - ano
#    if a >= 18:
#        print('O voto é obrigatorio')
#    elif a <= 16:
#        print('O voto é negado')
#    else:
#        print('O voto é opcional')
#    return b


#b = int(input('Em quem ano você nasceu?'))
#voto(b)



print('-' * 30)
def voto(ano):
    from datetime import date
    atual = date.today().year #criou uma nova variavel chamada atual  e escolheu date.today().year para pegar somente o ano atual.
    idade = atual - ano #nova variavel idade para fazer o ano atual menos o ano selecionado em nasc, que é subido para a def(ano):
    if idade <16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:  # aqui ele so esta dizendo que se a idade for entre 16 e 17
        return f'Com {idade} anos: VOTO OPCINAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#programa principal
nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))
print('-' * 30)