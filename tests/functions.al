def fact(n):
    if n == 2 or n == 1:
        return n
    return n * fact(n-1)

def fib(n):
    if n == 2 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def four_chan():
    print(9001)

print(fact(2))
print(fact(3))
print(fact(7))
print(fib(7))
four_chan()
