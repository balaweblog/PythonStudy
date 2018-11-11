iterable = ['Spring','Autumn','Summer','Winter']

itertor = iter(iterable)

print(next(itertor))
print(next(itertor))
print(next(itertor))
print(next(itertor))



def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(['hi','second']))