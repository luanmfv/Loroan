#ESTRUTURAS DE CONTROLE   (ESTRUTURA CONDICIONAL ANINHADA)
#IF, ELSE E ELIF
import emoji

nome = str(input('Qual é seu nome?'))
if nome == 'Luan':
    print ('Que nome bonito, Luan =)')
elif nome == 'Taina':
    print ('Seu nome é maravilhoso, e o Luan te ama demais 💜')
elif nome == 'Yansha':
    print ('Belo nome em? Você é especial demais! 🤩')
else:
    print ('Muito prazer, {} 😎'.format(nome))