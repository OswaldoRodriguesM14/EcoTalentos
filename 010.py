# --- Job 010 --- #

def hackerrankInString(s):    
    StrStrip = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k']
    StrKey = []    
    Count = 0
    for i in StrStrip:
        for x in s[Count:]:
            if i == x:
                StrKey.append(x)
                Count += 1
                break
    if StrKey == StrStrip:
        A = 'YES'
        return A
    else:
        B = 'NO'
        return B

                    



print(hackerrankInString('hereiamstackerrank'))
print(hackerrankInString('hackerworld'))



