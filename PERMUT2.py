# cook your dish here
def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        a = list(map(int, input().strip().split()))
        b = [0] * n
        for i in range(n):
            b[a[i] - 1] = i + 1
        if a == b:
            print("ambiguous")
        else:
            print("not ambiguous")

if __name__ == '__main__':
    main()