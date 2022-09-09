s = input()
c = 0
for i in range(len(s)):
    if s[i] == s[len(s)-i-1]:
        c += 1
    else:
        c = 0
print(c)        
if c == len(s):
    print("YES") 
else:
    print("NO")   
