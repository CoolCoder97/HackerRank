n=input()
arr=list(map(int, input().split()))
freq=dict()
for i in arr:
    freq[i]=freq.get(i,0)+1
size=len(freq)
keys=list()
values=list()
for k,v in freq.items():
    keys.append(k)
    values.append(v)
max=0
for i in range(size-1):
    if(keys[i+1]-keys[i]<=1):
        temp=values[i+1]+values[i]
        if(temp>max):
            max=temp
for v in values:
    if(v>max):
        max=v
print(max)
