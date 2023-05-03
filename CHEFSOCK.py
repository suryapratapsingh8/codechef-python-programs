import sys
j,s,m=map(int,sys.stdin.readline().split())
sys.stdout.write('Lucky Chef\n' if ((m-j)//s)%2==0 else 'Unlucky Chef\n')