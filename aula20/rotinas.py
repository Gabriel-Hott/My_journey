def top(msg):
    print(12 * '+=')
    print(msg)
    print(12* '+=')

print('MENSAGEM')    
top('geral')
top('inferior')
top('final') 
print('FIM MENSAGEM')

def soma(a, b):
    s = a + b
    print(s)

print('SOMA')
soma(1, 5)
soma(10, 15)
soma(135, 71)
print('FIM SOMA')

def contador(*num):
    print(num)

print('contador')
contador(1, 2, 5, 6, 7)
contador(1, 4, 5, 0) 
print('FIM CONTADOR')


print('LISTA')
lista = [1, 2, 8 , 5, 12, 62]
print(lista)
def dobra(lss):
    pos = 0
    print('A lista dobrada sera >', end=' ')
    while pos < len(lss):
         lss[pos]*= 2 
         pos += 1
    print(lss)
dobra(lista)
print('FIM LISTA')