n = int(input())
a = list(map(int,input().split()))
if a[n-1]%10 == 0:
    print('Yes')
else:
    print('No')    
