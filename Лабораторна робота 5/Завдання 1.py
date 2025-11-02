weather_data = {
    1: [5, -3],
    2: [0, 2],
    3: [4, -1],
    4: [8, 3],
    5: [2, 0],
    6: [7, -4],
    7: [6, 5],
    8: [3, -2]
}
def Print(data):
    print("\nДані про опади:")
    if not data:
        print("Словник порожній")
        return
    for day, vals in data.items():
        print(f"День {day}: {vals[0]} мм, {vals[1]}°C")
def add(data):
    try:
        day = int(input("Введіть день: "))
        rain = int(input("Введіть кількість опадів: "))
        temp = int(input("Введіть температуру: "))
        data[day] = [rain, temp]
        print("Додано")
    except ValueError:
        print("Помилка, введіть коректні числові значення.")
def delete(data):
    try:
        day = int(input("Введіть день для видалення: "))
        if day in data:
            del data[day]
            print(f"День {day} видалено")
        else:
            print(f"Помилка, дня {day} немає у словнику.")
    except ValueError:
        print("Помилка, введіть ціле число.")
def sort_dict(data):
    print("\nВідсортовані дані за днями:")
    if not data:
        print("Словник порожній")
        return
    for k in sorted(data.keys()):
        print(f"День {k}: {data[k][0]} мм, {data[k][1]}°C")
def analyze(data):
    if not data:
        print("\nСловник порожній")
        return
    snow = 0
    rain = 0
    for vals in data.values():
        if vals[1] > 0:
            rain += vals[0]
        else:
            snow += vals[0]
    print("\nСніг:", snow, "мм")
    print("Дощ:", rain, "мм")
def main():
    while True:
        print("Меню:")
        print("1 - Показати словник")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Сортування")
        print("5 - Аналіз опадів")
        print("0 - Вихід")
        ch = input("Ваш вибір: ")
        if ch == "1":
            Print(weather_data)
        elif ch == "2":
            add(weather_data)
        elif ch == "3":
            delete(weather_data)
        elif ch == "4":
            sort_dict(weather_data)
        elif ch == "5":
            analyze(weather_data)
        elif ch == "0":
            break
        else:
            print("Невірний вибір!")
main()