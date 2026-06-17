#Melhore o exercicio 28, aonde o computador "pensa" de um número de 0 até 10. So que o jogador vai tentar adivinhar até acertar. mostrando no final o resultado de quantos palpites foram necessarios até o jogador acertar. 
import random
import time
PC = random.randint(0, 10)
User = 11 
C = 0
print('O computado escolheu um número de 0 a 10, tente descobrir qual foi...')
print('3...', time.sleep(1))
print('2...', time.sleep(1))
print('1...', time.sleep(1))
print('GO', time.sleep(1))
while User != PC:
    User = int(input('Digite um número: '))
    C += 1
    if User != PC:
        print('Você ERROU', end=', ')
    if User > PC:
        print('(Talvez um número menor),', end=' ')
    elif User < PC and User != PC: 
        print('(Talvez um número maior)', end=' ')
print('Parabêns você ACERTOU, teve um total de {} tentativas para encontrar o N°{}'.format(C, PC))