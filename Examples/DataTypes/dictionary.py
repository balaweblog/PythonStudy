d = {'a': 1, 'b': 2}
print(d)
print(type(d))

e = {}
print(e)

r = d.values()
s = d.keys()
print(r)
print(s)

student = {
    "name": "balamurugan",
    "id": 19939,
    "feedback": None
}
print(student)


# group the dictionary
studentarr = [
    {"name":"bala", "age": 20},
    {"name": "bala", "age": 20}
]
print(studentarr)


print(student["name"])
student["name"] = "test"
print(student)


# update
student['name'] = 'rose'
print(student)

# delete
del student['feedback']
print(student)

# modify
student.update({
'sample': 'dfdfdf'
})
print(student)

# constructor dict
name = dict({'a': 'sona'})
print(name)

name1 = dict(a ='alpha',b='beta',c='gamma')
print(name1)

# copy idctoronary
name2 = name1.copy()
print(name2)

# update dictonry either add new or modify existing
name1.update(c='test',d='ra')
print(name1)

dollars = dict(US='usd',IN='inr',EUR='EURO')

if 'US' in dollars:
    print('yes')


dex = [{'name': [1,2,3]}]
print(dex)
dex[0]['name'] += [3,2,3,4]
print(dex)