ones_count = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4}
tens_count = {'0':0, '2':6, '3':6, '4':5, '5':5, '6':5, '7':7, '8':6, '9':6}
angsty_teens = {'0':3, '1':6, '2':6, '3':8, '4':8, '5':7, '6':7, '7':9, '8':8, '9':8}

def digits(n):
    num = str(n)
    if len(num) == 1: return ones_count[num]
    if len(num) == 2:
        if num[0] == '1':
            return angsty_teens[num[1]]
        else:
            return tens_count[num[0]]+digits(num[1])
    if len(num) == 3:
        if int(num[1:]) == 0: return ones_count[num[0]]+7
        else: return ones_count[num[0]]+10+digits(num[1:])

print(sum([digits(n) for n in range(1, 1000)])+11)
