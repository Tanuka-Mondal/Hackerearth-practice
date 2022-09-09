t = int(input())
while(t>0):
    g,p = map(int,input().split())
    gs = 0
    ps = 0
    a = 0
    b = 0
    value = 0
    n = int(input())
    while(n>0):
        a,b = map(int,input().split())
        gs = gs+a
        ps = ps+b
        n -= 1
    value = (max(gs,ps) * min(g,p)) +  (min(gs,ps) * max(g,p))   
    print(value) 
    t -= 1
