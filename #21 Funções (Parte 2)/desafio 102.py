def fatorial(n, beterraba=False): # o beterraba é a variavel nova criada, e o False é para manter desativado, porém se colocar True no programa ele ativa a função
    f = 1
    for c in range(n, 0, -1):
        if beterraba:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, beterraba=True))