class MyUser:
    def __init__(self):
        self.user_name = 'Admin'
        self.password = 'qwerty'
        self.is_banned = False
        self.friends = []

    def __str__(self):
        return f'User: {self.user_name}, Banned: {self.is_banned}'

    def print_info(self):
        print('Name: {}\nPassword: {}\nBan status: {}\nFriends: {}'.format(
            self.user_name,
            self.password,
            self.is_banned,
            ', '.join(str(friend) for friend in self.friends)
        ))

    def add_friend(self, friend):
        self.friends.append(friend)

# Тест
user_1 = MyUser()
user_2 = MyUser()
user_2.user_name = 'All'

user_1.add_friend('Bob')
user_1.add_friend(user_2)

user_1.print_info()
print(user_1.friends)
