class MyUser:
    def __init__(self):
        self.user_name = 'Admin'
        self.password = 'qwerty'
        self.is_banned = False

    def __str__(self):
        return f'User: {self.user_name}, Banned: {self.is_banned}'

user_1 = MyUser()  # екземпляр класу MyUser
user_2 = MyUser() 
user_1.user_name = 'Tom'
print(user_2.user_name,user_1.user_name)
user_1.user_name = 'Noname'
print(user_2.user_name,user_1.user_name)