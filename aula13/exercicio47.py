#criar um programa que mostre todos os números pares na contagem de 1 a 50.
import time
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        time.sleep(0.5)