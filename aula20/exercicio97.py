#Criar um programa que tenha uma função chamada 'escreva()', que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(tamn):
    espaço = len(tamn) + 4
    print(espaço * '=')
    print(f'  {tamn}')
    print(espaço * '=')

#Código principal

for c in range(0, 3):
    escreva(str(input('Digite sua frase: ').strip()))