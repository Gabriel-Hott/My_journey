#Criar um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário reberá também o ano de contratação e o salario. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos de contribuição)
from datetime import datetime
from time import sleep
prov = dict()
final = dict()
while True:
    prov['nome'] = str(input('Nome: '))
    prov['idade'] = datetime.now().year - int(input('Ano nascimento: '))
    cart = str(input('Tem CTPS: [S/N]'))
    if cart in 'Ss':
        prov['contrato'] = int(input('Ano de contratação: '))
        prov['salario'] = float(input('Qual o salario: R$'))
    esc = str(input('Deseja continuar? [S/N] '))
    final = prov.copy()
    if esc in 'Nn':
        print('Você escolheu sair, indo para a proxima página')
        break
    elif esc not in 'Ss':
        print(f'Opção {esc} Invalida')
print(final)