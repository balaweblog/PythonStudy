count = 0


def showcount():
    print('count = ', count)


def setcount(c):
    global count
    count = c


setcount(1)
showcount()
