countrytocapiatl = {'UK': 'London', 'Tamilandu': 'Chennai', 'US': 'Washington', 'Australia': 'sydney'}

print(countrytocapiatl)

capitaltocountry = {capital: country for country, capital in countrytocapiatl.items()}
print(capitaltocountry)