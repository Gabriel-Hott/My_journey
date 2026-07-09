#Criar um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final mostre: 1 - Quantas pessoas foram cadastradas.  2 - A média de idade do grupo. 3 - Uma lista com todas as mulheres. 4 - Uma lista com todas as pessoas com idade acima da média.
ida = 0
prov = dict()
final = list()
while True:
    prov.clear()
    prov['nome'] = str(input('Nome: '))
    prov['idade'] =  int(input('Idade: '))
    ida += prov['idade']
    while True:
        prov['sexo'] = str(input('Sexo [M/F]').upper())
        if prov['sexo'] not in 'MmFf':
            print(f'Você digitou {prov["sexo"]}, por favor digite uma opção VALIDA.')
        else:
            break
    final.append(prov.copy())
    while True:    
        esc = str(input('Quer continuar: [S/N]'))
        if esc in 'NnSs':
            break
    if esc in 'Nn':
        break
ida = ida / len(final)
print(f'Ao todo foram {len(final)} pessoas cadastradas.')
print(f'A média de idade do grupo foi {ida}.')
print(f'As mulheres do grupo digitado foram ...', end='')
for i in final:
    if i['sexo'] == 'F':
        print(f'{i["nome"]}', end='')
print()
print('As pessoas que estão com a idade acima da média foram... ', end='')
for i in final:
    if i['idade'] > ida:
        print(f'{i['nome']}',end='')
print()