try: 
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor: '))
    c = a/b

except (ValueError, TypeError):
    print('Desculpe mas o valor digitado não e um número inteiro.')

except ZeroDivisionError:
    print('Desculpa mas e impossivel dividir por 0.')

except Exception as erro:
    print(f'Tivemos problemas com os valores digitados, ERRO {erro}')

except KeyboardInterrupt:
    print('oi')

else:
    print(c)
finally:
    print('FIM DO PROGRAMA, VOLTE SEMPRE')