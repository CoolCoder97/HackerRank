# table[i] will be storing the number of ways for n=i. We need n+1 rows as the table is constructed
# in bottom up manner using the base case (n = 0)

def count(S, m, n):
    table = [0 for k in range(n+1)]        # Initialize all table values as 0
    table[0] = 1                           # If n=0, then only 1 way is possible
    for i in range(0,m):
        for j in range(S[i],n+1):          # j starts from S[i] bcoz previous values of j are less than S[i] & wont be affected 
            table[j] += table[j-S[i]]
    return table[n]
 
# Driver program to test above function

n,m=map(int,input().split())
c=list(map(int,input().split()))
print (count(c, m, n))
