for a in range(2, 50 + 1):
    count = 0
    for b in range(1, a + 1):
        if a % b == 0 and a != b and b != 1:
         count += 1
    if count == 0:
        print(a)