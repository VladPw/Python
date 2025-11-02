n = 7
a = [[n - i for j in range(n)] for i in range(n)]
for r in a:
    print(*r)
