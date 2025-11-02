def squares():
    n = int(input("Введіть кількість елементів: "))
    while n > 1000 or n < 1:
        print("Число повинно бути в діапазоні від 0 до 1000")
        n = int(input("Введіть кількість елементів ще раз: "))
    sqset = set(i * i for i in range(1, n + 1))
    sorted_sq = sorted(list(sqset))
    print("Результат відсортовані квадратів чисел:")
    print(*sorted_sq)
    return sqset
squares()
