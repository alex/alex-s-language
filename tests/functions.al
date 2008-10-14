def fact(n):
    if n == 2 or n == 1:
        return n
    return n * fact(n)

print(fact(3))
