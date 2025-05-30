palavras = ('pao', 'amendoim', 'torrada', 'feijao', 'mandioca', 'kibe', 'coxinha')
vogais = ('a', 'e' , 'i' , 'o' , 'u')
for c in palavras:
    print(f'\nNa palavra temos {c.upper()} ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')