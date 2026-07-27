#Criar um programa que faça um mini-sistema que utilize o Interactive Help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. USAR CORES

from time import sleep
c = ['\033[m',        #0 - sem cor
     '\033[0;30;41m', #1 - vermelho
     '\033[0;30;42m', #2 - verde
     '\033[0;30;43m', #3 - amarelo
     '\033[0;30;44m', #4 - azul
     '\033[0;30;45m', #5 - vermelho
     ]

def cabe(men, cor=0):
    tam = len(men) + 2
    sleep(0.5)
    print(c[cor], end='')
    print(tam* '=',flush=True)
    sleep(0.5)
    print(f' {men}')
    sleep(0.5)
    print(tam* '=')
    print(c[0], end='')

def userHelp(a):
    print(f'Mostrando o manual da função {a}', flush=True)
    sleep(1)
    help(a)
            
#Código principal

while True:
    cabe('AJUDA INTERATIVA', cor=2)
    duv = (str(input('Qual a sua duvida? '))).strip()
    if duv == 'exit':
        sleep(1)
        cabe('OBRIGADO POR USAR A AJUDA INTERATIVA', cor=1)
        break
    else:
        userHelp(duv)