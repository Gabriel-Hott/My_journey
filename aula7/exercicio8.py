#fazer um programa que leia um valor em metros e converta em centímetros e milímetros.
L = int(input('Digite o valor que deseja converte em Centimetros e Milimetros: '))
KM = L / 1000
C = L * 100
M = L * 1000
print('O valor {}M em kilometros {}Km centimetros seria {}Cm e milimetros {}Mm'.format(L,KM, C, M))