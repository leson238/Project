def sum_days(start,end):
    sums = 0
    for i in range(start,end+1):
        if (i % 4 == 0) or (i % 400 == 0):
            sums += 366
        elif i % 4 == 0 and i % 400 !=0:
            sums += 365
        else:
            sums += 365
    return sums

def sunday(t):
    sunday = []
    for i in range(t):
        if i % 7 == 6:
            sunday.append(i)
    return sunday

def first_month(t):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    first_month = [0]
    i = 0
    count = 0
    while i <= t:
        for day in month:
            i += day
            first_month.append(i)
            if count % (365*4) == 0:
                i += 1
            count += day
    return first_month
print(len(set(sunday(sum_days(1900,2000))).intersection(first_month(sum_days(1900,2000))))-len(set(sunday(365)).intersection(first_month(365)))
)

        
        
