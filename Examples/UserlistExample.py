__author__ = 'mkv-aql'

# List of usernames and passwords will be stored here as objects (saved only when running, deletes when program ends)
class UserDict:
    username = {

    }

class UserInput:

    def insertuser(x,y):
        print(x)
        UserDict.username["user1"] = "pass1"
        UserDict.username["user2"] = "pass2"
        UserDict.username[x] = y
        UserDict.username["user4"] = 45

x = 'userX'
y = 'passX'
UserInput.insertuser(x,y)
print(UserDict.username)
print(UserDict.username.get('user2'))
