user_input = input("Введите числа через запятую: ")
numbers = list(map(int, user_input.split(",")))
product = 1

if numbers:
    print(" Сумма: ", sum(numbers))
for num in numbers:
    product *= num
print(" Произведение: ", product)
if numbers:
    print(" Максимум: ", max(numbers))
    print(" Минимум: ", min(numbers))
even_numbers = [x for x in numbers if x % 2 == 0]
print(" Чётные числа: ", even_numbers)