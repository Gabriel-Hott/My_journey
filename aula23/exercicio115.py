#Criar um pequeno sistema modularizado que permita  cadastrar pessoas pelo nome e idade  em um arquivo de testo simples. O programa so vai ter duas opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

import exer115
from exer115 import lib
lista = {}
arq = 'listanomes.txt'

if not lib.arqTrue(arq): #VERIFICA SE EXISTE O ARQUVIO
    lib.Newarq(arq)

while True:
    exer115.topo('MENU DE OPÇÕES') #TOPO DO INICIO DO PROGRAMA
    a = exer115.menu(['Cadastrar novo ususario', 'Mostrar usuarios', 'Sair do sistema'], 'Qual opção deseja escolher: ') #CRIA AS OPÇÕES DO PROGRAMA
    if a == 0: #CADASTRAR PESSOAS NO ARQUIVO
        lib.editarq(arq)
    elif a == 1: #LER O ARQUIVO
        lib.leraqr(arq)
    else: #ENCERAR PROGRAMA
        exer115.topo('ENCERRANDO, ATÉ LOGO')
        break