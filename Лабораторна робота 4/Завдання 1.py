n = int(input("Введіть розмір масиву n = "))
print(f"Введіть {n} елементів масиву (має бути ціле число):")
arr = [int(input()) for _ in range(n)]
print("Початковий масив:", arr)
print("Додатні елементи масиву:")
for x in arr:
    if x > 0:
        print(x)
