# cook your dish here
a, b = input().split()
correct = str(int(a)-int(b))
if '0' <= correct[-1] <='8':
    print(int(a)-int(b) + 1)
else:
    print(int(a)-int(b) -1)