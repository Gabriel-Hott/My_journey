#fazer um programa que leia um salario e mostre seu novo salario com 15% de aumento.
ini = float(input('Qual é o seu salario atual:R$'))
aume = (ini/100) * 15
salario = ini + aume
print('Atualmente seu salario é de R${} com um aumento de 15% no valor de R${:.2f}, assim seu salario passarar a ser R${:.2f}'.format(ini, aume, salario))