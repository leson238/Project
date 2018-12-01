from math import sqrt
def t_number(n):
    tn = sum(i for i in range(n+1))
    return tn
def div_amount(n):
    div_num = 0
    for i in range(1,round(sqrt(n))):
        if n % i == 0:
            div_num += 1
    return div_num * 2
i = 1465
n = 0
while div_amount(n) <= 500:
    n = t_number(i)
    i += 1
print(n,div_amount(n))
    
