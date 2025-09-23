def root(m):
    if m == 3:
        print("Помилка, m не може дорівнювати 3 (ділення на нуль)")
        return None
    if (m + 3) / (m - 3) < 0:
        print("Помилка, підкореневий вираз від’ємний")
        return None
    z = ((m + 3) / (m - 3)) ** 0.5
    return z
def parni_dobut(n):
    y = 1
    for i in range(1, n + 1):
        y *= 2 * i
    return y
m = int(input("Введіть значення m: "))
z = root(m)
if z is not None:
    print("Значення виразу z =", z)
n = int(input("Введіть натуральне число n: "))
print("Добуток парних чисел до 2n =", parni_dobut(n))
