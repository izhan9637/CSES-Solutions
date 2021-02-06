def makeTwoSets(n):
    # Base case
    if n <= 2:
        print("NO")
        return
    total = n*(n+1) // 2

    # If sum of first n natural numbers is odd then we can't make 2 sets having equal sum
    if total % 2 == 1:
        print("NO")
        return
    set1 = set()
    set2 = set()

    # When n is even
    if not(n & 1):
        first = 1
        last = n
        turnFlag = True
        while first < last:
            if turnFlag:
                set1.add(first)
                set1.add(last)
                turnFlag = False
            else:
                 set2.add(first)
                 set2.add(last)
                 turnFlag = True
            first += 1
            last -= 1
    else:
        # When n is odd
        halfTotal = total // 2
        visited = [False] * (n+1)
        visited[0] = True
        for i in range(n, 0, -1):
            if i < halfTotal:
                set1.add(i)
                visited[i] = True
                halfTotal -= i
            else:
                set1.add(halfTotal)
                visited[halfTotal] = True
                break
        # Add remaining elements in set2
        for i in range(1, n+1):
            if not visited[i]:
                set2.add(i)
    print("YES")
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)

N = int(input())
makeTwoSets(N)
