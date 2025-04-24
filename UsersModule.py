class User:
    activeUsersCount = 0
    allowedUsers = ['Ava', 'milad', 'sara', 'iman']
    loggedInUsers = []

    def __init__(self, userName, userFamily):
        if userName not in User.allowedUsers:
            raise ValueError(f"{userName} can not login !!")

        self.name = userName
        self.family = userFamily
        User.activeUsersCount += 1
        User.loggedInUsers.append(userName)
        # print(f"{self.name} logged in")

    def logOut(self):
        # print(f"{self.name} has logged out")
        User.activeUsersCount -= 1
        User.loggedInUsers.remove(self.name)


Ava = User('Ava', 'ordookhani')

sara = User('sara', 'moradi')

print(User.allowedUsers)
User.allowedUsers = ['sara', 'mostafa']

print(Ava.allowedUsers)
# Ava.allowedUsers = ['Ava', 'asghar']
# print(Ava.allowedUsers)
# print(User.allowedUsers)

# print(User.loggedInUsers)
# print(User.activeUsersCount)
# print(Ava.activeUsersCount)
#
#
# print(Ava.allowedUsers == User.allowedUsers)
# print(Ava.allowedUsers is User.allowedUsers)

# print(id(Ava.allowedUsers))
# print(id(sara.allowedUsers))
# print(id(User.allowedUsers))

# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
#
# Ava = User('Ava', 'ordookhani')
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
#
# sara = User('sara', 'moradi')
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
# sara.logOut()
# Ava.logOut()
#
# print(f"active users : {User.activeUsersCount}")
# print(User.loggedInUsers)
