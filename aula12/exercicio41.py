#Criar um programa que leia o ano ano de nascimento de um atleta e mostre sua categoria, 1 - até 9 anos: MIRIM, 2 - até 14 anos:INFANTIL, 3 - até 19 anos:JUNIOR, 4 - até 20 anos:SÊNIOR, 5 - acima:MASTER
from datetime import date
print(30*'=')
print('Classificação de categoria natação')
print(10*'=', date.today().year, 10*'=')
alu = str(input('Digite o nome do atleta: '))
nas = int(input('Digite o ano de nascimento do atleta: '))
clas = date.today().year - nas
if clas <= 9:
    print('O atleta {} com a idade {} anos irá participar da categoria MIRIM'.format(alu, clas))
elif clas <= 14:
    print('O atleta {} com a idade {} anos irá participar da categoria INFANTIL'.format(alu, clas))
elif clas <=19:
    print('O atleta {} com a idade {} anos irá participar da categoria JUNIOR'.format(alu, clas))
elif clas <= 20:
    print('O atleta {} com a idade {} anos irá participar da categoria SÊNIOR'.format(alu, clas))
else:
    print('O atleta {} com a idade {} anos irá participar da categoria MASTER.'.format(alu, clas))