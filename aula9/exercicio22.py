name = str(input('Digite seu nome completo: '))
name = name.strip()
print('Seu nome todo em maiúsculo: ', name.upper())
print('Seu nome todo em minúsculo:', name.lower())
name = name.split()
prime = name[0]
name = ''.join(name)
print('Seu nome sem considerar espaços tem: {} letras.'.format(len(name)))
print('Seu primeiro nome tem {} letras.'.format(len(prime)))
