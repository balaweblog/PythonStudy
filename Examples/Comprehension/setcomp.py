words = 'Hello balamurugan how are you how is the weather and time now hope you are doing good and had breafast Have a nice day'


wordslist = words.split(' ')

newrod = {len(word) for word in words}
print(newrod)


from math import factorial

f = {len(str(factorial(x))) for x in range(1,20)}
print(f)

print(type(f))