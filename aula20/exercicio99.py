#Criar um programa que tenha uma função chamada 'maior()', que receba vários valores inteiros. O programa tem que analisar todos os valores e dizer qual deles é o maior.  
lista = list()
def maior(*num):
    mai = 0 
    print(f'Ao total foram {len(num[0])} números digitados, sendo eles ', end='')
    for c in num[0]:
        if c == 0:
            mai = c
        elif c > mai:
            mai = c
        print(f'{c}', end=', ')
    print(f'diante disso o maior número digitado foi o {mai}')

#Código
while True:
    lista.append(int(input('Digite um número: ')))
    esc = str(input('Deseja continuar: [S/N] ').strip())
    if esc in 'Nn':
        break
    elif esc not in 'Ss':
        print(f'Opção {esc} e uma opção invalida! Por favor escolha entre S ou N')
maior(lista)