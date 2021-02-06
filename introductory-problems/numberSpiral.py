n = int(input())
ls = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    x, y = ls[i]
    if x > y:
        if x % 2 == 0:
            print(x * x - y + 1)
        else:
            print((x-1) * (x-1) + y)
    else:
        if y % 2 == 0:
            print((y-1) * (y-1) + x)
        else:
            print(y * y - x + 1)
