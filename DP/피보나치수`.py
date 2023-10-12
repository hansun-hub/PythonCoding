def fib(n):
    count1=0
    if n == 1 or n ==2:
        return 1
    count1+=1
    return fib(n-1)+fib(n-2)


def fibonacci(n):
    f = [0] * (n+1)
    f[1],f[2] = 1,1
    cnt2=0
    for i in range(3,n+1):
        cnt2+=1
        f[i] = f[i - 1] + f[i - 2];  # 코드2
    return cnt2

n = int(input())
print(fib(n),fibonacci(n))