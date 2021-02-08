# We do not need to find the factorial of n because that might cause an overflow.
# formula: (n/5) + (n/25) + (n/125) + ...... until n > 0
# We only need to find the power of 5 in n, because 5 * 2 contributes a trailing zero in a number.
# lets understand with an example why we are not finding the power of 2:
# Example: Factorial(10) => 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10. Here we can see every second number
# is multiple of 2 and every fifth number is multiple of 5. so if x=power of 2's and y=power of 5's
# then x will always greater then y.


# Time: O(log(n)) to the base 5
def countTrailingZeroes(n):
    p = 5
    ans = 0
    while n // p > 0:
        ans += (n // p)
        p = p * 5
    return ans

n = int(input())
print(countTrailingZeroes(n))
