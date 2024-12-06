user_input = input("Введите список значений в граммах, разделённых запятой: ")

try:
    grams_list = list(map(float, user_input.split(",")))
except ValueError:
    print("Ошибка: убедитесь, что вводите только числа, разделённые запятой.")
    grams_list = []

grams_in_pound = 453

if grams_list:
    pounds_list = [round(grams / grams_in_pound, 2) for grams in grams_list]
    print("Граммы: ", sum(grams_list))
    print("Паунды: ", sum(pounds_list))
else:
    print("Список пуст или неверно введён.")