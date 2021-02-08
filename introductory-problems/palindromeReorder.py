from collections import Counter as ct


s = str(input())
count = ct(s)
oddCharCount = 0
oddChar = ""

for char in count:
    if count[char] % 2 != 0:
        oddCharCount += 1
        oddChar = char

if oddCharCount > 1 or oddCharCount == 1 and len(s) % 2 == 0:
    print("NO SOLUTION")
else:
    firstHalf, secondHalf = "", ""
    temp = ""

    for char in count:
        temp = char * (count[char] // 2)
        firstHalf = firstHalf + temp
        secondHalf = temp + secondHalf
    if oddCharCount == 1:
        print(firstHalf + oddChar + secondHalf)
    else:
        print(firstHalf + secondHalf)
