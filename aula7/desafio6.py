# fazer um algoritimo que leia um numero e mostre seu dobro, triplo e a raiz quadrada
n1 = int(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
r = n1 ** (1/2)
print('O dobro de {} é {}, o triplo é de {} e a raiz é {:.2f}.'.format(n1, d, t, r))