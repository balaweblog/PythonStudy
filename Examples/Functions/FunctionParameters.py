student = []

# optional parameters
def addnames(name ='Sand'):
    student.append(name)


addnames()
addnames('Bala')

print(student)


# variable number of arguments
def add(i, j, *args):
    print(i,j, args)

add(13, 4, 4, 3, 3, 'name')


# variable number of arguments with name arguments
def enroll(name, **kwargs):
    print(name)
    print(kwargs)

enroll("balamurugan", age =10,sex="Female")

# with types for return and parameters
def add(i: object, j: object) -> object:
    print(i,j)

add(13, 4)


#Nested Function
def printa():
    print('hi')
    def printb():
        print('hi2')


printa()


# multiple return
def addsub(i: object, j: object) -> object:
    return i + j, i-j

print(addsub(3,4))