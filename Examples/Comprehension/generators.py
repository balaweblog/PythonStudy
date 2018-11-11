def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g) # generator object
print(next(g))
print(next(g))
print(next(g))


def gen2357():
    print('am in 2')
    yield 2
    print('am in 3')
    yield 3
    print('am in 5')
    yield 5
    print('am in 7')
    yield 7

r = gen2357()

print(next(r))
print(next(r))
print(next(r))
print(next(r))