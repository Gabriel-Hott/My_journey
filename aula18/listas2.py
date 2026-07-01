teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:]) #galera.append(teste)
teste[0] = 'Maria'
teste[1] = 15
print(teste)
print(galera)