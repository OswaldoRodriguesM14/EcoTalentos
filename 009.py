# --- Job 09 --- #


def gameOfThrones(s):
    Str = str(s)
    Letters = []
    for i in s:
        if i not in Letters:
            Letters.append(i)
    Count = 0
    for i in Letters:        
        if Str.count(i) > 1:
            Count = Count + 1            

    if Count >= 1:
        A = 'YES'
        return A
    else:
        B = 'NO'
        return B
    
    
print(gameOfThrones('aaabbbb'))        
print(gameOfThrones('cdefghmnopqrstuvw'))
