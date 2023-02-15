# cook your dish here
for _ in range(int(input())): 
    n = int(input()) 
    new_list = []
    
    for i in range(n): 
        s = input().split() 
        new_list.append(s) 
    dict_a = {} 
    for char in new_list: 
        if char[0] in dict_a: 
            dict_a[char[0]] += char[1] 
        else: 
            dict_a[char[0]] = char[1] 
    result = []
    for key,value in dict_a.items(): 
        result.append(value[-1]) 
    r = 0 
    for char in result: 
        if char == "+": 
            r += 1 
        elif char == "-": 
            r-=1 
    print(r)
            
        