#MAIN LOGIC - in a palindrome all alphabets occur even no. of times(only one alphabet can occur odd no. of times)
def gameOfThrones(s):
    frequency=dict()                        #initialize dict
    for i in s:
        frequency[i]=frequency.get(i,0)+1   #calculating frequency of each alphabet
    res=list(frequency.values())
    count=0                                 #'count' stores total no. of odd alphabets
    for i in res:
        if(i%2!=0):
            count+=1
    if(count>1):
        return "NO"                         #if count>1: return NO
    else:
        return "YES"                        #else: return YES

s = input().strip()
result = gameOfThrones(s)
print(result)
