s = input()
vowels = ['A', 'E', 'I', 'O', 'U','Y']
if s[2] in vowels:
    print("invalid")
else:
    if (int(s[0])+int(s[1])) % 2 != 0 or (int(s[3])+int(s[4])) % 2 != 0 or (int(s[4])+int(s[5])) % 2 != 0 or (int(s[7])+int(s[8])) % 2 != 0:
        print("invalid")
    else:
        print("valid")    
