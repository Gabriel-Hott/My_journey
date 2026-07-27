def format(a = 0, b = 'R$'):
    return f'{b}{a:.2f}'.replace('.', ',')

def metade(a = 0, b = False): #DIVIDIMOS POR 2 O VALOR DE 'A'
    a /= 2
    return a if b == False else format(a)

def dobro(a = 0, b = False): #MULTIPLICAMOS POR 2 O VALOR DE 'A'
    a *= 2
    return a if b == False else format(a)

def aumentar(a = 0, b = 0, c = False): #AUMENTAMOS EM B% O VALOR DE 'A'
    a += (a/100) * b
    return a if c == False else format(a)

def diminuir(a = 0, b = 0, c = False): #DIMINUIMOS EM B% O VALOR DE 'A'
    a -= (a/100) * b
    return a if c == False else format(a)

def resumo(a = 0, b = 0, c = 0):
    print(35 * '-')
    print(f'{'RESUMO DO VALOR'}'.center(35))
    print(35 * '-')
    print(f'O valor analizado: \t{format(a)}')
    print(f'A metade do valor \t{metade(a, True)}')
    print(f'O dobro do valor: \t{dobro(a, True)}')
    print(f'Com acrescimo de {b}%: \t{aumentar(a, b, True)}')
    print(f'Com decrescimo de {c}%: \t{diminuir(a, c, True)}')
    print(35 * '-')