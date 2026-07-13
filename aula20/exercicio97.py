#Criar um programa que tenha uma função chamada 'escreva()', que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
def escreva(tamn):
    espaço = len(tamn) + 2
    print(espaço * '+=')
    print(f'{tamn:^espaço}')
    print(espaço * '+=')

while True:
    escreva(str(input('Digite sua frase: ').strip()))