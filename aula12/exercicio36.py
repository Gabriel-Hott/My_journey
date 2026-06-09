#Fazer um programa que irar ver a aprovação de empréstimo bancario, o programa deve pergunta o salário da pessoa, o valor da casa e em quantos anos ele ira pagar a casa. calcular a prestação mensal, sabendo que ela não deve eceder 30% do salário do usuario ou então o emprestimo será negado. 
print(30 *'=')
print('Banco Saldita')
print(30 *'=')
print('Emprestimos:')
nome = str(input('Qual é o seu nome: '))#username
sal = float(input('Qual o valor do seu salário atualmente: R$'))#user salay
casa = float(input('qual o valor da residência/emprestimo: R$'))#value of the residence
ano = int(input('Quantos anos deseja paga: '))#how many installments
ano = ano * 12 #turning years into months
prest = casa / ano #loan amount per month
print('A prestação do eu emprestimo sera R${:.2f}, que sera paga em {} meses'.format(prest, ano), end='')
if prest >= (sal/100 * 30):#if greater than 30%
    print('Descupe {}, Seu emprestimo foi NEGADO pois o valor da parcela do seu empréstimo supera em 30% valor do seu salário'.format(nome))
else: #if less than 30%
    print('Parabens {}, Seu empréstimo foi APROVADO.'.format(nome))
print('Você será direcionado ao setor responsavel')
print(30 * "=")
print('Fim emprestimo...')