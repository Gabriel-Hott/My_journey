from exer115 import topo
from time import sleep

def arqTrue(name): #VERIFICA SE EXISTE UM ARQUIVO DE TEXTO E RETORNA TRUE OU FALSE
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def Newarq(name):#CASO NÃO TENHA UM ARQUIVO ELE IRÁ CRIAR UM
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('\033[31mNão foi possivel Criar o arquivo\033[m')
    else:
        print(f'\033[32mO arquivo {name} foi criado com sucesso!!!\033[m')

def leraqr(name):#MOSTRA A LISTA DE USUARIOS
    try:
        a = open(name, 'rt')
    except:
        print('\033[31mNão foi possivel ler o arquivo\033[m')
    else:
        topo('MOSTRANDO USUARIOS')
        for i in a:
            dado = i.split(';')
            dado[1] = dado[1].replace('\n', '')
            sleep(0.5)
            print(f'{dado[0]:<25}{dado[1]:>3} anos')
    finally:
        a.close()

def editarq(name): #CADASTRO DE PESSOAS
    topo('NOVO CADASTRO')
    while True:
        try:
            nome = input('Nome: ')
            idade = int(input('Idade: '))
            a = open(name, 'at')
        except (ValueError, TypeError):
            print('\033[31mPor favor, no campo "Idade" digite um número inteiro.\033[m')
        except FileNotFoundError:
            print('\033[31mNão foi possivel abrir o arquivo!!!\033[m')
            break
        else:
            try:
                a.write(f'{nome};{idade}\n')
            except:
                print('\033[31mDESCULPE, ouve algum erro ao editar o arquivo.\033[m')
            else:
                print(f'\033[32mO cadastro de {nome} foi criado com sucesso\033[m')
                print(35 * '-')
                break
