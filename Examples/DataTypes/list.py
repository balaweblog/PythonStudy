from typing import List

a = [1, 2, 4, 5]
print(a)
print(type(a))

b = [1, 'Balamurugan', 2, 2.2]
print(b)
print(type(b))

c = []
print(c)
c.append(1)
print(c)
c.append(1.1)
print(c)

students = []
print('emtpy students')

students1 = [1]
students1[0] = 1
print('one student', students1)

# 0 starts from left and -1 from right
student_names = ['Mark', 'Antony', 'Sona']
print(student_names)
print(student_names[0])
print(student_names[1])
print(student_names[2])
print(student_names[-1])
print(student_names[-2])
print(student_names[-3])

# length
print(len(student_names))

# delete
del student_names[1]
print(student_names)
student_names.remove('Mark')

# slicing
print(student_names[1:2])

print(student_names[:])

s = student_names[:]

if student_names is s:
    print('hi')
if student_names == s:
    print('hi1')

# list repeation
a = [1, 2]
print(a * 3)

b = [2]
print(b * 2)

c = [[1, 2]] * 3
print(c)

# repeation is shallow ie all outer list is modified wiht 2
c[1].append(2)
print(c)

# unlike here see the code only the second list is changed compared to previous one
d = [[2, 2], [2, 3]]
print(d)
d[1].append(1)
print(d)

'index of element or find an eleent '
student_names1: List[str] = ['Mark', 'Antony', 'Sona']

print(student_names1.index('Sona'))
print(student_names1.index('Mark'))
print(student_names1.index('Antony'))
# value error
# print(student_names1.index('s'))

student_names1.insert(3,'add')
print(student_names1)


# concatenate list

st = student_names + student_names1
print(st)

st += [11,2]
print(st)
st.extend([1,1,1,1,1,1])
print(st)


a = [1,2,4,63,2,4,5,6]
a.sort()
print(a)
b = reversed(a)
print(b)
print(list(b))


d = sorted(a)
print(list((d)))