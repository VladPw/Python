def nlist():
    A = list(map(int, input('Введіть список (через пробіл): ').split()))
    print("Початковий список:", A)
    r = []
    for x in A:
        if x not in r:
            r.append(x)
    print("Список без повторів:", r)
    return r
nlist()
