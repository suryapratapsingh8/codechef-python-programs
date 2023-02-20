# progrm for computing a raise to the power n using recursion

def pow (a,n):
    if n==0:
        return 1 
    else:
        return a*pow(a,n-1)
a,n=map(int,input().split())
print(pow(a,n))
