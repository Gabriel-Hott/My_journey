from math import hypot
Co = float(input('Qual o comprimento do cateto oposto: '))
Ca = float(input('Qual o comprimento do cateto adjacente: '))
Hi = hypot(Co, Ca)
print('A hipotenusa vai medir {:.2f}'.format(Hi))