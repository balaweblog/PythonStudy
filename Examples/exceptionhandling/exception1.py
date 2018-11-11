def convert(s):
    x = int(s)
    return x

print(convert("2"))
# print(convert("-"))

# this will return a value error


def convertstringtoint(s):
    try:
        x = int(s)
        print('conversion succeded')
    except ValueError:
        print('value error')
        x = -1
    except TypeError as e:
        print('type error ',e)
        x= -1
        raise
    finally:
        print('hi finallly')
    return x

print(convertstringtoint("22"))
print(convertstringtoint(""))
print(convertstringtoint([2,3,3,3]))


# raise - re raise the error method and error will coe back