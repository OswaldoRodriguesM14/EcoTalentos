# --- Job 001 -- #

Lista001 = [1,2,3]
Lista002 = [1, 2, 3, 4, 10, 11]
Lista003 = [1,3,5,'a',2,2.5]
Lista004 = []
Lista005 = [100000,1000000000]
Lista006 = [1.5,1.2,1.5,6.5]


def simpleArraySum(ar):
    if len(ar) > 0:
        try:
            FirstLine = len(ar)
            SecondLine = []
            Sum = 0
            while len(SecondLine) < FirstLine:
                for i in ar:
                    if i < 1000:
                        int(i)
                        SecondLine.append(i)
                        Sum = Sum + i
                    else:
                        A = 'Array witch value greater than 1000'
                        return A  
         
        except:
            A = 'Is not possible sum the String'
            return A
     
        return int(Sum)
        
    else:
        A = 'Is not possible sum the array Null'
        return A

print(simpleArraySum(Lista001))
print(simpleArraySum(Lista002))
print(simpleArraySum(Lista003))
print(simpleArraySum(Lista004))
print(simpleArraySum(Lista005))
print(simpleArraySum(Lista006))



