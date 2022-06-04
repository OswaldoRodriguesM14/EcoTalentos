# -- Job 3 --- #

from joblib import PrintTime


def Solution(inteiro):
    Numero = int(inteiro)
    if Numero >= 1 and Numero <= 100:
        if Numero % 2 != 0:
            print('Weird')
        else:
            print('Not Weird')
    else:
        print('Teste apenas de 1 a 100')


print(Solution(7))