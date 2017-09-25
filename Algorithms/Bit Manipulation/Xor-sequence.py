#MAIN LOGIC - XORing (L to R) is same as XORing (0 to L-1) and (0 to R). For example cumulative XORing of first 16 elements
#are as under
''' 0 1 2 2 6   7  0 0
    8 9 2 2 14  15 0 0'''

def findXOR(n):
    mod=n%8
    if(mod==0 or mod==1):
        return n
    elif(mod==2 or mod==3):
        return 2
    elif(mod==4 or mod==5):
        return n+2
    else:
        return 0

t=int(input())
for i in range(t):
    L,R=map(int,input().split())
    print(findXOR(L-1)^findXOR(R))
