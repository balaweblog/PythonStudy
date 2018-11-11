class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self._name = name  # instance variable unique to each instance


d = Dog('Sona')
print(d.kind)
print(d._name)


class Planet:

    def __init__(self, name):
        self.name = name
        self.obj = "SOna Iyer"
        self.age = 10

    def getage(self):
        return self.age


r = Planet('arch arch')
print(r.name)
print(r.obj)
print(r.getage())