#Aula sobre colocar cores no terminal de execução do código
print('\033[1;37;44mOlá, mundo\033[m')
nome = 'Gabriel'
print('Olá {}{}{}, como vai?'.format('\033[1;34;43m', nome, '\033[m'))
#criar variavel com cores para facilitar
p1 = 'teste'
p2 = 'teste'
p3 = 'teste'
cor = {'limpa':'\033[m',
       'azul':'\033[34m',
       'amarelo':'\033[33m',
       'pretoEbranco':'\033[7;30m'}
print('Testando cores {}{}{}'.format(cor['amarelo'], p1, cor['limpa']))