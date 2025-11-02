def new_list():
    A = list(map(int, input('Введіть список (через пробіл): ').split()))
    print("Початковий список:", A)
    start = int(input("Введіть елемент, який потрібно додати на початок списку: "))
    end = int(input("Введіть елемент, який потрібно додати в кінець списку: "))
    A.insert(0, start)
    A.append(end)
    print("Оновлений список:", A)
    return A
new_list()
