def is_ap_free(seq):
    # Check if the sequence is AP-free
    n = len(seq)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if seq[j] - seq[i] == seq[k] - seq[j]:
                    return False
    return True

# Main function to read input and output results
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        seq = list(map(int, input().split()))
        if is_ap_free(seq):
            print("YES")
        else:
            print("No")