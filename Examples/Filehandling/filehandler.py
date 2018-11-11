
username = input('Enter your user name')
userid = input('Enter your user id')
password = input('Enter your password')
print(f'thanks for your inputs {username} We are saving it')


def writefile():
    try:
        file = open('testfile.txt', 'a')
        file.writelines(username + "," + userid + "," + password)
        file.writelines("\n")
        file.close()
    except:
        file.close()

def readinputfile():
    try:
        file = open('testfile.txt' ,'r')
        for line in readline(file):
            print(line)
    except:
        file.close()


def readline(f):
    for line in f:
        yield line


readinputfile()
writefile()

