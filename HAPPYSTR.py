# cook your dish here
T=int(input())
for o in range(T):
    S=input()
    string="not contiguous"
    vowels=['a','e','i','o','u']
    for i in range(len(S)-3):
        if (S[i] in vowels) and (S[i+1] in vowels) and (S[i+2] in vowels):
            string="contiguous"
            print("Happy")
            break
    if string!="contiguous":
        print("Sad")