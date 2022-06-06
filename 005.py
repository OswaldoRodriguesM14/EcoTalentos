# --- Job 005 --- #


def Soluction(strA,strB):
    A = ''
    StrA = str.capitalize(strA)
    StrB = str.capitalize(strB)
    StrAB = StrA + StrB
    LenA = len(str(strA))
    LenB = len(str(strB))
    Sum = LenA + LenB
    if LenA > LenB:
        A = 'Yes'        
    else:
        A = 'No'
    Str_Out =   '''
                %s
                %s
                %s
                ''' % (Sum,A,StrAB )
    return Str_Out


print(Soluction('ola','mundo'))
    