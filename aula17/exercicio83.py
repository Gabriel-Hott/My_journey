#Criar um programa aonde o usuário crie uma expressão qualquer que use parênteses(). Seu aplicativo deverá analisar se a expresão passada está em abertos e fechados na ordem correta(seria como ((A+b)83) temos que conferir se a expresão está corretamente fechada com os parênteses).
expr = str(input('Digite sua expressão: '))
pilha = list()
for c in expr:
    if c == '(':
        pilha.append('(')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')