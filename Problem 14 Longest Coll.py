def coll(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n + 1
        count += 1
    return count
def longest(n):
    longest = 0
    count = 0
    for i in range(1,n+1):
        if coll(i) > count:
            count = coll(i)
            longest = i
    return longest
print(longest(999999))
        
        
