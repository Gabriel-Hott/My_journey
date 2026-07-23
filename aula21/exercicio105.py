#Criar um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retonar um dicionário com as seguintes informações: - Quantidade de notas - A maior nota - A menor nota - A média da turma - A situação (opcional)-  ADCIONAR A DOCSTRINGS da função

def notas(*n, sit=False):
    """notas

    Args:
        sit (n, optional): '*n' retorna as notas do aluno, e sit=True retorna se a situação do aluno o APROVA ou REPROVA

    Returns:
        r:Retorna em um dicionario varias informações das notas do aluno
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] >= 7:
            r['Situação'] = 'Passou'
        elif r['Média'] >= 5:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'REPROVADO'
    return r


#Código principal

final = notas(10, 4.5, 3.9, 10, sit=True)
print(final)
help(notas)