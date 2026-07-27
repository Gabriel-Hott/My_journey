#Dentro do pacote utilidadesCeV, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com validação de dados para aceitar apenas valores que sejam monetários.(tem que aceitar números monetarios com virgula EX: R$ 120,45)

from utilidadesCeV import dados, moeda

r = dados.isdinheiro('Digite um valor: R$')
moeda.resumo(r, 20, 40)