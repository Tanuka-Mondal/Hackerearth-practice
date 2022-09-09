def sumall(x):
    result = 0
    while(x>0):
        result += x%10
        x = x//10
    return result
    
t = int(input())
while(t>0):
    a = int(input())
    while(True):
        if sumall(a)%4 == 0:
            print(a)
            break
        else:
            a = a+1
    t -= 1        
