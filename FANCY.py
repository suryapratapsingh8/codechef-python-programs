
for i in range(int(input())):
    s=input()
    if len(s)>=4:
        if s[:4]=="not "  or  s[len(s)-4:len(s)]==" not":
            print("Real Fancy")
        else:        
            if " not " in s:
                print("Real Fancy")
            else:
                print("regularly fancy")
    else:
        if s=="not":
            print("Real Fancy")
        else:
            print("regularly fancy")
