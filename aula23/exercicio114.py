#Criar um código que teste se o site Pudim está acessivel pelo computador usado (pudim.com.br)

import urllib
import urllib.request

print('Site que vamos testar será o https://www.youtube.com/')
try:
    test = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('\033[31mNão consegui acessar o site em questão\033[m')
else:
    print('\033[32mConsegui acessar o site em questão\033[m')