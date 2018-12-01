def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    div = 2
    while True:
        if (n < div**2):
            return True
        if n % div == 0:
            return False
        div +=1
s = 0
for n in range(2000000):
    if isPrime(n):
        s += n
print(s)

import time

start = time.time()


def sieveOfEratosthenes(number):
    listOfPrimes = [True for i in range(number + 1)]
    primeFactor = 2
    while primeFactor**2 <= number:
        if listOfPrimes[primeFactor]:
            for j in range(primeFactor*2, number+1, primeFactor):
                listOfPrimes[j] = False
        primeFactor += 1
    sumOfPrimes = 0
    for p in range(2, number):
        if listOfPrimes[p]:
            sumOfPrimes += p
    print("Sum of prime numbers below ", number," is : ",sumOfPrimes)


sieveOfEratosthenes(2000000)
print("Time : ", time.time() - start)
