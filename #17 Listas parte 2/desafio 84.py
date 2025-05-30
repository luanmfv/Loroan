dados = list()
estrutura = list()
cadastro = maispesada = maisleve = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(int(input('Peso:')))
    estrutura.append(dados[:])
    dados.clear()
    c = str(input('Quer continuar?[S/N]'))
    cadastro += 1
    if c in 'Nn':
        break
for p in estrutura:
    if p[1] >= 85:
        print(f'{p[0]} está com bastante peso')
        maispesada += 1
    else:
        print(f'{p[0]} está com pouco peso')
        maisleve +=1
print(f'O total de pessoas cadastradas foi de {cadastro}, {maispesada} com bastante peso e {maisleve} com pouco peso')
