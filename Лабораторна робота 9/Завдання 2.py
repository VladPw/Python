import json
def load():
    try:
        with open("weather.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл 'weather.json' не знайдено")
        return {}
def save(data):
    with open("weather.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def Print(data):
    print("\nДані про опади:")
    if not data:
        print("Словник порожній")
        return
    for day, vals in data.items():
        print(f"День {day}: {vals[0]} мм, {vals[1]}°C")
def sort(data):
    print("\nСортування даних")
    try:
        sorted_keys = sorted(data.keys(), key=int)
        sorted_data = {key: data[key] for key in sorted_keys}
        save(sorted_data)
        print("Дані відсортовано та збережено у 'weather.json'")
        print("Відсортовані дані за днями:")
        for k, v in sorted_data.items():
            print(f"День {k}: {v[0]} мм, {v[1]}°C")
        return sorted_data
    except ValueError:
        print("Помилка сортування")
        return data
def add(data):
    try:
        day = int(input("Введіть день (1–31): "))
        if not (1 <= day <= 31):
            print("Помилка, день повинен бути від 1 до 31.")
            return
        rain = int(input("Введіть кількість опадів (мм): "))
        temp = int(input("Введіть температуру (°C): "))
        data[str(day)] = [rain, temp]
        save(data)
        print("Дані успішно додано")
    except ValueError:
        print("Помилка, введіть числові значення")
def delete(data):
    try:
        day = int(input("Введіть день для видалення: "))
        day_str = str(day)
        if day_str in data:
            del data[day_str]
            save(data)
            print(f"День {day} видалено")
        else:
            print(f"Помилка, дня {day} немає у словнику")
    except ValueError:
        print("Помилка, введіть ціле число")
def search(data):
    if not data:
        print("Словник порожній")
        return
    print("\nПошук:")
    print("1 - за днем")
    print("2 - за температурою")
    print("3 - за кількістю опадів")
    choice = input("Ваш вибір: ").strip()
    found = False
    if choice == "1":
        d = input("Введіть день: ")
        if d in data:
            print(f"День {d}: {data[d][0]} мм, {data[d][1]}°C")
            found = True
    elif choice == "2":
        try:
            t = int(input("Введіть температуру: "))
            for k, v in data.items():
                if v[1] == t:
                    print(f"День {k}: {v[0]} мм, {v[1]}°C")
                    found = True
        except ValueError:
            print("Помилка вводу")
    elif choice == "3":
        try:
            r = int(input("Введіть кількість опадів: "))
            for k, v in data.items():
                if v[0] == r:
                    print(f"День {k}: {v[0]} мм, {v[1]}°C")
                    found = True
        except ValueError:
            print("Помилка вводу")
    if not found:
        print("Нічого не знайдено")

def analyze(data):
    if not data:
        print("\nСловник порожній")
        return
    snow = 0
    rain = 0
    for vals in data.values():
        if vals[1] >= 0:
            rain += vals[0]
        else:
            snow += vals[0]
    print("Аналіз опадів")
    print("\nСніг:", snow, "мм")
    print("Дощ:", rain, "мм")
    result = {"Сніг (мм)": snow, "Дощ (мм)": rain}
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
    print("Результат аналізу записано у 'result.json'")
def main():
    weather_data = {
        "1": [5, -3],
        "2": [0, 2],
        "3": [4, -1],
        "4": [8, 3],
        "5": [2, 0],
        "6": [7, -4],
        "7": [6, 5],
        "8": [3, -2]
    }
    try:
        with open("weather.json", "x", encoding="utf-8") as f:
            json.dump(weather_data, f, indent=4, ensure_ascii=False)
    except FileExistsError:
        pass
    data = load()
    while True:
        print(" МЕНЮ ")
        print("1 - Вивести вміст JSON файлу")
        print("2 - Додати запис")
        print("3 - Видалити запис")
        print("4 - Пошук запису")
        print("5 - Аналіз (сніг / дощ)")
        print("6 - Відсортувати та зберегти у файл")
        print("0 - Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            Print(data)
        elif choice == "2":
            add(data)
        elif choice == "3":
            delete(data)
        elif choice == "4":
            search(data)
        elif choice == "5":
            analyze(data)
        elif choice == "6":
            data = sort(data)
        elif choice == "0":
            print("Вихід із програми")
            break
        else:
            print("Помилка, спробуйте ще раз")
main()