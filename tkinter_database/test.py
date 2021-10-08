from functools import reduce
L1 = ['adam', 'LISA', 'barT']

def normalize(s):
    return str.upper(s[0])+str.lower(s[1:])
L2 = list(map(normalize,L1))

print(L2)