tup = (1,'Norway', 3.3)

print(tup)

print(tup[1])

for a in tup:
    print(a)

print(len(tup))

# concatenation
print(tup + tup)

# repetation  n number of times
print(tup* 3)


# ntested tuples
tup2 = (1,3,'Nor',(1,3,'Test'))
print(tup2)
# inner eleent value wiht chain squre bracket
print(tup2[3][1])


# single element tuple this can be considred as int
# instead have trailing comma seperated
tup3 = (1)
print(type(tup3))
print(tup3)

tup4 = (1,)
print(type(tup4))
print(tup4)


# empty tuples
tup5 = ()
print(type(tup5))
print(tup5)


# create tuple from collection
coll = [1,3,'So']
tup = tuple(coll)
print(tup)

if 3 in coll:
    print('i am in ')