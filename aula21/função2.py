#help()

def soma(a, b):
    global somar
    global c
    c = 10
    somar = a + b
    print(f'Somar no DEF vale {somar}')

somar = 0 
print(f'Somar vale {somar}')
soma(1, 5)
print(f'Depois do DEF somar vale {somar}')
print(c)