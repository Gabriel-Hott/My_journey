#Criar um programa que tenha um função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(a='', b=0):
    if a in '':
        a = '<INDEFINIDO>'
    if b in '':
        b = 0
    print(f'O jogador {a} marcou {b} gol(s)')

#Código principal

r1 = str(input('Nome: ')) 
r2 = str(input('gols: '))
ficha(r1, r2)