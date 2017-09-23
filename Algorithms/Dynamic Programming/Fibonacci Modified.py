def fibonacci(n):
    if n<=len(Fib):
        return Fib[n-1]
    else:
        temp_fib = fibonacci(n-1)**2+fibonacci(n-2)
        Fib.append(temp_fib)
        return temp_fib
 
# Main Program
a,b,n=map(int,input().split())
Fib = [a,b]
print(fibonacci(n))
