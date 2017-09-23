''' MAIN LOGIC - if you see closely we can have all the possible values greater than 'x' (upto next power of 2),
when 'x' is XORed with values less than 'x'.
For example: x=25 (11001) 5 bits
x^3=26
x^2=27
x^5=28
x^4=29
x^7=30
x^6=31
So total possible 'a' = 31(max value using 5 bits)-25(x)=6
'''

def theGreatXor(x):
    return (2 ** x.bit_length() - x - 1)

q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    print(result)
