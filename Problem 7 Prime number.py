def isPrime(integer):
    if integer <= 1:
        return False
    elif integer == 2:
        return True
    divisor = 2
    while True:
        if divisor * divisor > integer:
            return True
        if integer % divisor == 0:
            return False
        divisor += 1

count = 0
i = 1
while count < 10001:
    if isPrime(i):
        count += 1
    i += 1
print(i-1)
