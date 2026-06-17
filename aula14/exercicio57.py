#criar um programa que leia o sexo de uma pessoa, mas so pode M e F. Caso sejá difente ele tera que pedi para a pessoa digite novamente até o resutado desejado.
test = 0
print('Olá, essa é uma pesquisa sobre a identidade de genêro de pessoas, Você se identifica como?')
while test == 0:
    res = str(input('[M] \n' \
    '[F]\n' \
    '')).upper()
    if res == 'M' or res == 'F':
        test = 1
    else: 
        print('Opção INVALIDA, por favor digite novamente.')
if res == 'M':
    print('Sua escolha foi {} (MASCULINO)'.format(res))
else:
    print('Sua escolha foi {} (FEMININO)'.format(res))
print('Obrigado por participar da nossa pesquisa')