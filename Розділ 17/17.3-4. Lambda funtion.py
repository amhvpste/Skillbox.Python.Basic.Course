from typing import Callable, List
import functools

users: List[str] = ['user1', 'user2', 'user3  ', 'user4', 'user100']

sorted_users = sorted(users, key=lambda x: x.strip().lower())

print(sorted_users)
