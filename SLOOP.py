# cook your dish here
for i in range(int(input())):
    trip, song = map(int, input().split(" "))
    print(trip//song)