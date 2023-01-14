# cook your dish here
tescase = int(input());

while(tescase):
    tescase -= 1;
    
    N,Y = map(int,input().split());
    
    a = list(map(int,input().split()));
    
    s = 0;
    for i in a:
        s = s|i;
    
    if(s > Y):
        print('-1');
    elif(Y%2 == 0 and s%2 == 1):
        print('-1');
    else:
        print(Y-s);