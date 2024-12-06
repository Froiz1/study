user_num = 5

if user_num < 0:
    print("Error")
else:
    factorial = 1
    for i in range(1, user_num + 1):
        factorial *= i
    print(f"Your factorial num for {user_num} = {factorial}")