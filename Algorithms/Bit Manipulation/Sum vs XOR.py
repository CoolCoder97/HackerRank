'''MAIN LOGIC - corresponding to every '1' in 'n' there must be '0' in our required 'x',
and corresponding to every '0' in 'n' there will be 2 possibilities, either 0 or 1 in 'x'.
So total possible count of 'x' = 2**no. of '0' in 'n'.
'''


def solve(n):
    if(n==0):
        return 1
    return pow(2,format(n,'b').count('0'))

n = int(input().strip())
result = solve(n)
print(result)
