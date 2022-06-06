# --- Job 006 --- #

LISTA_DE_IP = ['000.12.12.034','121.234.12.12','23.45.12.56','00.12.123.123123.123','122.23','Hello.IP']

def VerificaIpValido(ip):
    Contem4 = []
    ip = str(ip).split(sep='.')    
    for i in ip:
        if len(i) <= 3 and i.isnumeric():
            Contem4.append(i)
        else:
            break    
    if len(Contem4) == 4:
        return True
    else:
        return False


for i in LISTA_DE_IP:
    print(VerificaIpValido(i))


 
