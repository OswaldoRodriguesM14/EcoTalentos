def CalcularBytes(Dado):
    tamanho = len(bin(Dado)[2:])
    if(tamanho < 9):
        print(' O número pode ser armazenado em um byte (8-bit)')
    
    if(tamanho < 17):
        print('O número pode ser armazenado em uma variável SHORT (16-bit)')
    
    if(tamanho < 33):
        print('O número pode ser armazenado em uma variável INT (32-bit)')
    
    if(tamanho < 65):
        print('O número pode ser armazenado em uma varíavel LONG (64-bit)')
    
    if(tamanho > 64):
        print('O número é muito grande e não pode ser armazenado')

CalcularBytes(5)
print()
CalcularBytes(-150)
print()
CalcularBytes(150000)
print()
CalcularBytes(1500000000)
print()
CalcularBytes(213333333333333333333333333333333333)






