a = "test"
b = """test"""
c = 'tdddd'
print(a)
print(b)
print(c)

d = "test \n recs"
print(d)

a = 10
print('int type values', type(a))
print('string type values', type(d))

# will list all the methods
print('help integer ', help(a))
print('help string ', help(d))

text = "my first value"
print(text.capitalize())
print(text.replace(' ', 'ccc'))
print(text.isdigit())
print(text.isalpha())
print('spilt', text.split('ccc'))

name = "Machine Learning"
print(f"my favourite subject is {name}")


s = 'test'
s += 'or'
print(s)


print(len(s))

# concateion
r = "test" + "test" + "or"
print(r)


# join
# used on seperator string
colors = ";".join(['a','b','c','d'])
print(colors)

print(colors.split(';'))


print("unforgettable".partition('forget'))
dep, _, arrival = "London:Ending".partition(':')
print(dep,arrival)

# format
print('current position {lat} and {lon}'.format(lat="100", lon="200"))
lat = "100"
lon = "200"
print(f'current position {lat} and {lon}')