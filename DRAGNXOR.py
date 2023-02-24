# cook your dish here
def decimalToBinary(n):
    return bin(n).replace("0b","")

for _ in range(int(input())):
    n, a, b = map(int, input().split()) 
    a, b = decimalToBinary(a).count('1'), decimalToBinary(b).count('1')
    l = min([a+b,2*n-a-b])
    print(int(l*"1"+(n-l)*"0", 2))
    
    
