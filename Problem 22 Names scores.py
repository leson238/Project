from string import ascii_uppercase
def score(w):
    return sum(ascii_uppercase.index(char) + 1 for char in w.strip('"'))
with open('C:\\Users\\lk300\\Project\\p022_names.txt') as f:
  names = f.read().split(',')
  names.sort()
print(sum((i+1)*score(name) for i, name in enumerate(names)))
