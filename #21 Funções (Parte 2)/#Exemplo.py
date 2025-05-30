#interactive help help()  que é uma função por ter ()

#help(print) #ele mostrara o que o print faz, ou então você abre o Python console na esquerda inferior, no simbolo de Python.

#print(input.__doc__) #mostra o help também, porém de outra forma comandada, porém com algumas pequenas informações diferentes.

#DOCSTRINGS uma string de documentação

#docstring começa logo depois do comando def, mostrara a instrução apos esse comando.

# esse sleep é muito legal, porque é igualmente podendo ser utilizado por exemplo para mostrar uma tabela de colocados em um jogo de corrida, primeiro lugar, segundo lugar, etc
from time import sleep

def contador(i, f, p): # abaixo é chamado de docstring
    """
    -> Faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Loroan.
    """
    c = i
    while c <=f:
        print(f'{c}', end=' ') #o end continua os parametros na mesma linha, e ainda com os pontos da uma sequencia
        c += p
        sleep(0.6)  #coloquei o sleep para que o sistema fique mais, movimentado.
    print('FIM!')


        #aqui o 2 é o inicio, 10 o fim, e o 2 a quantidade de casas para ir pulando.
contador(2, 10, 2)   #aqui o 2 vai para o i, 10 para o f e 2 para p, seria inicio, fim e passo, mas podemos fazer o que quiser com essas funções
help(contador)



print('-' *30)


#PARÂMETROS OPCIONAIS

def somar(a=0,b=0,c=0): #colocado c=0 para caso o c não receba nenhum parametro, logo ele não dá erro e segue com o 0 if nada in c
    s = a+b+c
    print(f'A soma vale {s}')

somar(3,2,5)
somar(8,4) #aqui não recebe o parametro para C, logo o c por estar c=0 o c será 0.



print ('-' * 30)


#ESCOPO DE VARIÁVEIS   #escopo é um lugar onde habita a variavel

def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

#programa principal

n = 2
print(f'No programa principal n vale {n}')
teste()
# seu colocasse aqui  print(f'No programa principal x vale {x}')  daria erro, pois x esta dito ali em cima, logo somente la podera ser executado, diferente do n que foi dito no programa principal, logo ele é dito no programa inteiro.


print('-' * 30)

def teste1(b):
    #global a     essa função dirá que o a vale 8 globalmente,  o a=5 é desconsiderado, pois aqui foi dito que o valor que importa é o a=8
    a=8 # aqui ele criara outra variavel a que recebe 8, uma variavel de escopo local, e o a=5 sera outra variavel escopo global
    b+=4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}') # essa área toda aqui se chama escopo local, por não poder interferir abaixo no programa principal


a = 5  #o A é para o programa todo, logo ela é o escopo global, o b e c apenas ali em cima não interfere em baixo.
teste1(a)
print(a)



print('-' * 30)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s  #esse return, faz com que você possa criar variaveis sobre a def somar, para formatar no final todos no mesmo print de uma vez, sem ela não funciona.


r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(4)
print(f'As somas valem {r1}, {r2} e {r3}')






















