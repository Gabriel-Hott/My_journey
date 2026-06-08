#criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostra quantos dolares ela pode comprar. considerar US$1.00 = R$3.27
real = float(input('Quantos R$ você tem:R$'))
dolar= real / 3.27
print('Com R${} você consegue comprar US${:.2f} .'.format(real,dolar))