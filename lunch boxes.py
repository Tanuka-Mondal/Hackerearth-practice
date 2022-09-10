t = int(input())
while(t>0):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    result = 0
    x = 0
    for i in range(m):
        if result < n:
            x += a[i]
            if x <= n:
                result += 1
            else:
                break
    print(result)
    t-=1
        
