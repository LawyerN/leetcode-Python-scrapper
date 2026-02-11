result = m
# n + 1 as the problem statement is inclusive of n
for x in range(m + 1, n + 1):
    result &= x
return x