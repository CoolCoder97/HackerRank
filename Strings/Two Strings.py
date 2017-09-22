#MAIN LOGIC - if any alphabet of 'a' occurs in 'b' also, then the two strings share a common substring
def twoStrings(s1, s2):
    for i in s1:            #for each alphabet in 'a'
        if(i in s2):            #if it occurs in 'b' also
            return "YES"            #return "YES"
    return "NO"             #return "NO"

p = int(input())
for a0 in range(p):
    a = input()
    b = input()
    print(twoStrings(a, b))
