# --- Job 007 --- #
class ValidadorDePalavra:

    def __init__(self,palavra):
        self.palavra = str(palavra)
    

    def VerificaCaracterInicialValido(self):
        A = 'INVÁLIDO; O nome de usuário começa com um caractere não alfabético'
        palavra = str(self.palavra)
        if palavra[0:1].isalpha():
            return True
        else:
            return False

    def VerificarTamanhoStrValido(self):
        A = 'INVÁLIDO; Comprimento do nome de usuário < 8 caracteres'
        if len(self.palavra) >= 8:
            return True
        else:
            return False

    def VerificaCaracterEspecialContem(self):
        self.CaracteresInvaldios = []
        for i in self.palavra:
            i = str(i)
            if not i.isalpha() and not i.isnumeric() and i != '_':
                self.CaracteresInvaldios.append(i)
        
        if len(self.CaracteresInvaldios) > 0:
            return True
        else:
            return False
               
       
                
        
    def VerificacaoCompleta(self):
        if self.VerificaCaracterInicialValido() is True and self.VerificarTamanhoStrValido() is True and self.VerificaCaracterEspecialContem() is False:
            A = 'Palavra atende o Requisico'
            return A
        elif self.VerificarTamanhoStrValido() is False:
            A = 'INVÁLIDO; Comprimento do nome de usuário < 8 caracteres'
            return A
        elif self.VerificaCaracterInicialValido() is False:
            A = 'INVÁLIDO; O nome de usuário começa com um caractere não alfabético'
            return A
        else:
            A = "INVÁLIDO; '%s' caractere não permitido" % self.CaracteresInvaldios[0]
            return A

  
            
Words = ['Julia', 'Samantha', 'Samantha_21', '1Samanta','Samantha?10_2A']
for i in Words:
    A = ValidadorDePalavra(i)
    print(A.VerificacaoCompleta())
    
