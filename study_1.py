print()
user_1 = {
    "name": "admin",
    "password": "password123",
    "age": 26,
    "status": True
}
user_2 = {
    "name": "user",
    "password": "hello123",
    "age": 17,
    "status": True
}
user_3 = {
    "name": "player",
    "password": "player123",
    "age": 33,
    "status": False
}

user_name_list = ["admin", "user", "player"]
user_password_list = ["password123", "hello123", "player123"]

if user_1["status"]:
    if not user_1["name"] in user_name_list:
        print("Неправильне ім'я")
    elif not user_1["password"] in user_password_list:
        print("Неправильний пароль")
    elif user_1["age"] < 18:
        print("Тобі має бути 18 років")
    else:
        print(f"Вітаю вас {user_1["name"]} !!!")
else:
    print("Error")