n = int(input())
arr = list(map(int, input().split()))

# optimal approach
a = 1
b = arr[0]

for i in range(2, n+1):
    a ^= i

for i in range(1, n-1):
    b ^= arr[i]
print(a ^ b)

# First Approach
# keep = {}
# for num in arr:
#     keep[num] = True
# missingNumber = 1
# for i in range(1, n+1):
#     if i not in keep:
#         missingNumber = i
#         break
# print(missingNumber)
