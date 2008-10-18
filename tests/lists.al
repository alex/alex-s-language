x = []
print(x)
x += [2,3]
for i in x:
    print(i)
x += [[]]
for i in x:
    print(i)
print(x[1])
x[1] = 4
print(x[1])
