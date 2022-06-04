# --- Job 002 --- #


from itertools import count
from operator import index


def repeatedString(s, n):
    Str = s
    Multiplo = int(n)
    StrInWord = []    
    NewStr = [] 
    for i in Str:
        if i not in StrInWord:
            StrInWord.append(i)
    if len(Str) == 1:
        A = 1 * n
        return A
    if len(s) > 0 and len(s) <= 100 and n >= 1 and n <= 10**12:
        Count = 0
        while Count < Multiplo:
            for i in Str:
                if Count == Multiplo:
                    break
                else:
                    NewStr.append(i)
                    Count += 1    
    Count = 0   
    for i in StrInWord:
        A = NewStr.count(i)
        if A > Count:
            Count = A
    return Count
       



print(repeatedString('aba',10))
print(repeatedString('a',1000000000000))