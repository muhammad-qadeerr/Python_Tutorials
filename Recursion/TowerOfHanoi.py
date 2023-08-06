# Tower of Hanoi

def TowerOfHanoi(n, A, B, C):
    if (n > 0):
        TowerOfHanoi(n-1, A, C, B)
        print("Move disk ", n, " from ", A, " to ", C)
        TowerOfHanoi(n-1, B, A, C)


# main()

N = int(input("Enter the no of discs: "))
TowerOfHanoi(N, 'A', 'B', 'C')
