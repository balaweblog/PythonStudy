input = ['1', '2', '3']


def change(input):
    input[2] = '111'


def nochange(input):
    input1 = input
    input1[2] = '1121'


print(input)
change(input)
print(input)

print(input)
nochange(input)
print(input)
