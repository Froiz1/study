user_num = 5

print("\nMultiplication table:\n")

for a in range(1, 11):
    for b in range(user_num, user_num + 1):
        print(f'{b} * {a} = {b * a}')
        break
else:
    print("\nWell Done!")