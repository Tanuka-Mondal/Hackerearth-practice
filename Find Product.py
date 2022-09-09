n = int(input())
a = list(map(int,input().split()))
ans=1
for i in range(n):
    ans=((ans*a[i])%((10**9)+7))
print(ans)
