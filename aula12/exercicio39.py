from datetime import datetime
#fazer um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 1 - se ele ainda vai se alistar ao serviço militar, 2 - se é a hora de se alistar, 3 - Sé já passou do tempo do alistamento. (O PROGRAMA DEVE MOSTRAR QUANTO TEMPO FALTA PARA ELE SE ALISTAR OU QUANTO TEMPO PASSOU PARA ELE SE ALISTAR)

print(30 * '=')
print('Vejá se esta na hora de se alistar')
nasc = int(input('Digite o ano que você nasceu [xxxx]: '))
exer = datetime.now().year - nasc
if exer < 18:
    ano = 18 - exer
    print('Você tem {} é ainda não está na idade de se alistar, pois ainda falta {} anos para seu alistamento que será em {}.'.format(exer, ano, datetime.now().year + ano))
elif exer == 18:
    print('Você tem {} anos e está na hora de se alistar em {}'.format(exer, datetime.now().year))
else:
    ano = exer - 18
    print('Voce tem {} anos e já passou da epoca de se alista em {} anos, Você deveria ter se alistado em {} procure a junta militar da sua cidade.'.format(exer, ano, datetime.now().year - ano))