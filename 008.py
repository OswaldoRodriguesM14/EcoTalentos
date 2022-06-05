# --- Job 007 --- #

def camelcase(s):
    if len(s) >= 1 and len(s) <= 10**5:
        Count = 1
        for i in s:
            i = str(i)
            if i.isupper():
                Count += 1
    else:
        A = 'ERROR4'
        return A
    return Count


print(camelcase('saveChangesInTheEditor'))


