s = str(input())
ans = 1
n = len(s)
i = 0
while i < n - 1:
    print("i ", i)
    character = s[i]
    count = 1
    for j in range(i+1, n):
        print("j ", j)
        if character == s[j]:
            count += 1
        else:
            break
    if count >= ans:
        ans = count
    i += count
print(ans)
