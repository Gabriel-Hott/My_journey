#aula de condições alinhadas
name = str(input('Digite seu nome: ')).strip()
if name == 'Gabriel':
    print('Que nome lindo,')
elif name == 'Maria' or name == 'Pedro' or name =='João':
    print('Seu nome e bem comum, ')
else:
    print('Seu nome e bem normal, ')
print('Tenha um bom dia {}!'.format(name))
