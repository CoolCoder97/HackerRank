n=int(input())
arr=list(map(int,input().split(" ")))
arr.insert(0, 0)        #to start indexing from 1 
res=list()              #result list
for i in range(n+1):
    res.append(0)       #initialize result list with 0
for i in arr:
    if(i==0):
        continue
    res[arr[arr[i]]]=i  #MAIN LOGIC & store result in res
for i in res:
    if(i==0):
        continue
    print(i)            #print result
