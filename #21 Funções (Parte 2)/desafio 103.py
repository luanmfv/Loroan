def ficha(jog='Jogador desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input("Nome do jogador: "))
g = str(input("Numero de gols: "))  #o g foi colocado como str e as condições foram feitar para caso o usuario digite algo que não seja um numero o python não dê erro.
if g.isnumeric(): #se o g for um numero
    g = int(g) #o g passa de string para um int
else:
    g = 0  #se não digitar nada o valor será 0
if n.strip() == '': # o strip é para quebrar as linhas se houver espaço
    ficha(gol=g)
else:
    ficha(n, g)