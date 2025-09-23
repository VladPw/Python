n = int(input("Введіть N (1 < N < 9): "))
while n <= 1 or n >= 9:
    n = int(input("Помилка, введіть ще раз N (1 < N < 9): "))
for i in range(1, n + 1):
    for j in range(i, n + 1):
        print(j, end=" ")
    print("")
