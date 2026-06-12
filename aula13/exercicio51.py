#fazer um programa que leia a primeiro termo e a razão de uma PROGRESÂO ARITIMETICA, No final mostre os 10 primeiros termos desta progressão.(pula a partir do número da razão)
P1 = int(input('Digite da onde deseja começar: '))
R1 = int(input('Digite a razão que você deseja: '))
dec = P1 + (10-1) * R1
for c in range (P1, dec + R1, R1):
    print(c)