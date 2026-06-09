#Cria um programa que calcule o valor a ser pago levando em consideração o preço normal é condição de pagamento. 1 -  a vista cheque/dinheiro: 10% desconto, 2 - a vista no cartão: 5% de desconto, 3 - em até 2x no cartão: preço normal, 4 - 3x ou mais no cartão: 20% de juros.
prod = float(input('Qual o valor das compras: R$'))
print('CODIÇÕES \n'
      '[1] DINHEIO/CHEQUE \n'
      '[2] A VISTA NO CARTÃO \n'
      '[3] ATÉ 2X NO CARTÃO \n'
      '[4] 3X OU MAIS NO CARTÃO')
cond = int(input('Qual a condição de pagamento escolhida: '))
if cond == 1:
    tot = prod/100 * 10
    print('Sua compra no valor de {}R$ ficar no total de {}R$.'.format(prod, prod - tot))
elif cond == 2:
    tot = prod / 100 * 5
    print('Sua compra no valor de {}R$ ficara {}R$'.format(prod, prod - tot))
elif cond == 3:
    print('Sua compra no valor de {}R$ será dividida em 2 parcelas de {}R$.'.format(prod, prod / 2))
elif cond == 4:
    parc = int(input('Em quantas parcelas deseja pagar sua comra: '))
    tot = prod / 100 * 20
    print('Sua compra no valor {}R$ ficar dividida em {} parcelas de {}R$ no total {}R$.'.format(prod, parc, (tot + prod) / parc, prod + tot))
else:
    print ('Erro, por favor reinicie...')