for i in range(1,11):
    print(i)

for i in range(10):
    print(i)

ls = list(range(2))
print(ls)

ls1 = list(range(5,10))
print(ls1)

ls2 = list(range(5,10,2))
print(ls2)

# enumerate to return the index and value of the list over iteration
t = [1,2,3,4,5,6]
for p,v in enumerate(t):
    print(p,v)