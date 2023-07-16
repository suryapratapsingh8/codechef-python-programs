# cook your dish here
t = int(input())
for i in range(t):
    n,x,y,a,b = map(int,input().split())
    petrol = (n/a)*x 
    diesel = (n/b)*y 
    print("PETROL") if  petrol < diesel else print("DIESEL") if diesel < petrol else print("ANY")