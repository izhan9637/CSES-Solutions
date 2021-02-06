n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if arr[i] > arr[i+1]:
        diff = arr[i] - arr[i+1]
        ans += diff
        arr[i+1] += diff
print(ans)
