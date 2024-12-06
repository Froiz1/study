week_days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday",
}

user_day = 5

if user_day < 1 or user_day > 7:
    print("Error")
else:
    print(week_days[user_day])