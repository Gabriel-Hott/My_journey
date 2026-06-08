#faca um algritimo que leia um produto e mostre um novo preço com 5% de desconto.
#prod = float(input('Qual é o valor do produto:R$'))
#desc = (prod / 100) * 5
#total = prod - desc
#print('O produto no valor de {}R$ menos 5%'' de desconto ficara no valor de R${:.2f}'.format(prod, total))
prod = float(input('Qual o valor do Produto: R$'))
vista = prod - (prod/100 * 10)
parc = prod +  (prod/100 * 8)
print("O produto no valor de {}R$ a vista fica com o desconto de 10% que dara o valor de {}R$".format(prod, vista))
print('O produto no valor de {}R$ ficara no valor de {}R$ pois parcelado há um aumento de 8%'.format(prod, parc))
