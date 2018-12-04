def factorial(n):
    m = 1
    for i in range(1,n+1):
        m = m*i
    return m
print(sum([int(i) for i in str(factorial(100))]))
