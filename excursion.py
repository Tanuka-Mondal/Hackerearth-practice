import math
t = int(input())
while (t>0):
    n,m,k = map(int,input().split())
    result = 0
    result = math.ceil(n/k) + math.ceil(m/k)
    print(result)
    t-=1
