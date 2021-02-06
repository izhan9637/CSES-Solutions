# Technique is called the modulo exponentiation
# Time: O(log(n)) because n is divided by 2 after every iteration
n = int(input())
mod = 10**9 + 7
res = 1
a = 2
while n > 0:
    if n & 1:
        res = (res * a) % mod
    a = (a * a) % mod
    n = n >> 1
print(res)
