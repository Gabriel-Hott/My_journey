def isdinheiro(a):
    ok = False
    while not ok:
        msg = str(input(a)).strip().replace(',','.')
        if msg.isalpha() or msg == '':
            print(f'\033[0;31mO valor "{msg}" não e um valor valido!!!\033[m')
        else:
            ok = True
            return float(msg)