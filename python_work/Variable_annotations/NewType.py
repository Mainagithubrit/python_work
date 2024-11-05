from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)

def get_user_name(user_id: UserId) -> str:
    ...

user_a = get_user_name(UserId(42351))
user_b = get_user_name(-1)

print(user_a)
print(user_b)