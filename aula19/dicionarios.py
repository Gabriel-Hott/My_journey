#dados = {'nome':'Gabriel','idade':'25','sexo':'M'}
#print(dados)
#print(f'O {dados["nome"]} tem {dados["idade"]} anos e é do sexo {dados["sexo"]}')
#print(dados.values())
#print(dados.keys())
#print(dados.items())
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
for e in brasil:
    for k, v in e.items():
        print(f'{k} = SIGLA {v}')