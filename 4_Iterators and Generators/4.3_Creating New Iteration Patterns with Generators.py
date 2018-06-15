def frang(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment

for x in frang(1, 5, 0.5):
    print(x)

print(10 * '*')

print(list(frang(1, 6, 1.5)))

print(10 * '*')

def countdown(n):
    print("starting to count from", n)
    while n > 0:
        yield n
        n -= 1
    print('done')

c = countdown(5) # <generator object countdown at 0x10217f7d8> return a generator object
print(c)
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))
print(next(c, None))


# fib()