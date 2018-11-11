from Functions.maths import mul


def add(a, b):
    c = a + b
    print('sum of two numbers', c)


add(1, 3)
add(3, 3)


# with return and without return values
def textappend(input):
    if input is None:
        print('no values')
        return
    else:
        print(input)
        return "Valid Object"


a = textappend('Bala')
b = textappend(None)

print(a)
print(b)


# importing from other class
print('imported function multiply', mul(1, 3))
