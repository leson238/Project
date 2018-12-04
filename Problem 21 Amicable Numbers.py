def sum_of_div(n):
    sums = 0
    for i in range(1,n//2 + 1):
        if n % i == 0:
            sums = sums + i
    return sums
sumss = 0
for i in range(10000):
    if (sum_of_div(sum_of_div(i)) == i) and (sum_of_div(i) != i):
        sumss += sum_of_div(i)
print(sumss)
