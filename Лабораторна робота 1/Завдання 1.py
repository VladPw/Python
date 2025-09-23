a = int(input("Введіть a: "))
while a < 0:
    a = int(input("Число повинно бути додатнім, введіть ще раз a: "))
b = int(input("Введіть b: "))
while b < 0:
    b = int(input("Число повинно бути додатнім, введіть ще раз b: "))
if a < b:
    X= 5*a+b
elif a == b:
    X=-125
else:
    X=(a-5)/b
print("Результат X = ", X)
