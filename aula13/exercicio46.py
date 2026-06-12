#Criar um programa que faça uma contagem regressiva para estouro de fogos no fim, a contagem deve ter uma pause de 1s entre os números. A contagem é de 10 até 0.
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print('kabum kabum kabum')