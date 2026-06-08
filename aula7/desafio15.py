# custo dia 60R$ custo Km 0,15R$
dia = int(input('Quantos dias você alugou o veículo: '))
Km = float(input('Quantos Km voce pecorreu com o veículo: '))
custoD = 60 * dia
custoKm = Km * 0.15
print('Você ira pagar o total de {}R$'.format((custoD + custoKm)))