nome = str(input('Qual é o seu nome: ')).strip()
if nome == 'Gabriel':
    print('Que nome legal')
else:
    print('Que nome feio')
print('Bom dia {}'.format(nome))