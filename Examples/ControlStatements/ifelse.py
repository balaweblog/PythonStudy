a = 10
b = 20

# single if
if a > b:
    print(' a is > b')
else:
    print('not a < b')

# if and elif
if a > b:
    print('a is bg b')
elif a > 2:
    print('a is elif b')
else:
    print('not b')

# if and multiple if
if a > 1:
    print('Inside')
    if a > 4:
        print('inside 1')
    else:
        print('inside outside')


# if not

if not a < 1:
    print('a is not b ')


# terinary operators
print("bigger" if a > 2 else "smaller")
