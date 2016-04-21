a = [5, 3, 1, -1, -3, 5]

b = list(a)   # list copy 
c = a         # list reference

b[0] = 0

print a
print b       # b will not update the value of a

c[0] = 4

print a
print c       # c will update the value of a
