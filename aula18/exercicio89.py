#Criar um programa que leia um nome e duas notas de vários alunos e guarde em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente. 
temp = list()
final = list()
print(4*'+=', 'NOTAS ALUNOS', 4* '+=')
while True:
    temp.append(str(input('Digite o nome do aluno: ')))
    temp.append(float(input('NOTA 1: ')))
    temp.append(float(input('NOTA 2: ')))
    temp.append((temp[1] + temp[2]) / 2)
    final.append(temp[:])
    temp.clear()
    res = str(input('Deseja continuar: [S/N] '))
    if res in 'Nn':
        break
print(f'{'Nº':<4} | {'ALUNO':<10} | {'MEDIA':>7}')
for a, c in enumerate(final):
    print(f'{a:<4} | {c[0]:<10} | {c[3]:>7.1f}')
while True:
    print(20* '-')
    esc = int(input('Qual aluno dejesa ver: (DIGITE 999 PARA sair) '))
    if esc <= len(final) - 1:
        print(f'Notas de {final[esc][0]} são {final[esc][1:3]}')
    elif esc == 999:
        break