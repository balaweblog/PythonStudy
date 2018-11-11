a = {1,2,3,4,2,4,5}
print(a)
print(type(a))

b = {}
print(b)
print(type(b))

c = set()
print(c)
print(type(c))

c1 = set([1,3,3,3,45,5,2])
print(c1)

if 3 in c1:
    print('3 in')

# add single element
c1.add(232)

# add multiple element
c1.update([21,22,23])

print(c1)

# remove element
c1.remove(21)
print(c1)

# if element is not there 21 then key error so better use discard

# c1.remove(21)
c1.discard(21)
print(c1)

# copy shallow
r1 = c1.copy()
print('copy value', r1)



# set union,

a = {'red','blue'}
b = {'red','green'}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
print(a.symmetric_difference(b))

print(a.issubset(b))
print(b.issubset(a))
print(b.isdisjoint(a))