def fact(n):
    if n == 2 or n == 1:
        return n
    return n * fact(n-1)

print(fact(2))
print(fact(3))
