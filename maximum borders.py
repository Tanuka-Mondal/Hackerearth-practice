t = int(input())
while(t>0):
    n,m = map(int,input().split())
    c = 0
    s = ""
    for i in range(n):
        s = input()
        if s.count("#") > c:
            c = s.count("#")
        s = " " 
    print(c)
    t -= 1       
