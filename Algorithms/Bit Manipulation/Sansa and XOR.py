#MAIN LOGIC - If n is even, then in contiguous subarrays all values occur even no. of times, that will lead to 0.
#If n is odd, then even indexed(0,2,4,...) values occur odd times and results in arr[0]^arr[2]^arr[4]... so on

t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if(n%2==0):
        print("0")
    else:
        result=arr[0]
        for j in range(2,n,2):
            result^=arr[j]
        print(result)
