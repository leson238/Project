def pyt_trip_2(x):
    for m in range(1, int(x/2)):
        for n in range(1, m):
            if m * (m + n) == x / 2:
                a = 2 * m * n
                b = m * m - n * n
                c = m * m + n * n
                return a * b * c, a, b, c

e = pyt_trip_2(1000)
print(e)
