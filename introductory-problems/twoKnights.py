n = int(input())
for k in range(1, n + 1):
    # Total ways in which we can place two knights on k*k chessboard
    total = ((k*k) * (k*k - 1)) // 2
    # Now we have to subtract the total ways in which two knights
    # will attack each other.
    # Steps:
    # 1. Find the 2*3 and 3*2 regions on a k*k chessboard.
    # 2*3 regions => (n-1)(n-2) ....Horizontally
    # 3*2 regions => (n-2)(n-1) ....Vertically
    # so total regions => 2(n-1)(n-2)
    # Now in one region there are 2 ways in which knights can attack each other.
    # Therefore, total number of ways in which knights can attack each other
    # on k*k chessboard = 2*2(n-1)(n-2) => 4(n-1)(n-2)
    totalWaysOfAttack = 4*(k-1)*(k-2)
    print(total - totalWaysOfAttack)
