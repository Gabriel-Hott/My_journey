#Criar um tupla preenchida com 20 primeiros colocados da tabela do Campeonato brasileiro de futebol, na ordem de colocação. Depois mostre: 1 - Apenas os 5 primeiros colocados, 2 - Os últimos 4 colocados, 3 - Uma lista em ordem alfabética, 4 - Em que posição na tabela está o time Chapecoense.
brasi = 'Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba', 'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional', 'Santos', 'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense' 
print(40 *'+=')
print(f'Os times do brasileirão são: {brasi}')
print(40 *'+=')
print(f'Os 5 primeiros colocados são {brasi[:5]}')
print(40 *'+=')
print(f'Os 4 últimos colocados são {brasi[16:]}')
print(40 *'+=')
print(f'A lista em ordem alfabética {sorted(brasi)}')
print(40 *'+=')
print(f'Atualmente o time Chapecoense se encontra na {brasi.index('Chapecoense') + 1}º posição no Brasileirão')
print('FIM PROGRAMA')