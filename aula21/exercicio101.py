#Criar um programa que tenha um função voto() que recebe como parâmetro o ano de nascimento de uma pessoa, retornando um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. (opcional 16 aos 17 e depois de 65, obrigatorio de 18 aos 64)
from datetime import datetime
def voto(nasc):
    global data
    data = datetime.now().year - nasc
    if data > 18 and data <= 64:
        return 'OBRIGATORIO'
    elif  data == 16 or data == 17 or data >= 65:
        return 'OPCIONAL'
    else:
        return 'NEGADO'

#Código principal

R1 = voto(int(input('Ano: ')))
print(f'Com a idade {data} anos, votar se torna {R1}')