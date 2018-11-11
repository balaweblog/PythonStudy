class Flight:
    def __init__(self,number, aircraft):
        self._number = number
        self._airline = "CCCCC"
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._airline

    def aircraft(self):
        return self._aircraft

    def model(self):
        return self._aircraft.model()


class Aircraft:
    def __init__(self):
        self._model = "3333"
        self._registration ="3c"

    def model(self):
        return self._model

    def registration(self):
        return self._registration


f = Flight('Bala', Aircraft())
print(f.number())
print(f.airline())
print(f.model())
c = f.aircraft()
print(c.model())
print(c.registration())