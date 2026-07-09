#Criar um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de ZERO, o dicionário reberá também o ano de contratação e o salario. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. (35 anos de contribuição)
from datetime import datetime
prov = dict()
prov['nome'] = str(input('Nome: '))
prov['idade'] = datetime.now().year - int(input('Ano nascimento: '))
cart = int(input('Nº CTPS (digite 0 se não tiver):'))
if cart > 0:
    prov['contrato'] = int(input('Ano de contratação: '))
    prov['salario'] = float(input('Qual o salario: R$'))
for k, v in prov.items():
    print(f'{k} recebe {v}')
if 'contrato' in prov:
    aposentar = 35 - (datetime.now().year - prov['contrato'])
    if aposentar > 0:
        print(f'Você tera que trabalhar mais {aposentar} anos, e poderar aposentar no ano {aposentar + datetime.now().year}')
    else:
        print(f'Você ja pode se aposentar')