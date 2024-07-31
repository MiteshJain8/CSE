def subsetSum(n, W, weights):
    M = [[False] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = True
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] > w:
                M[i][w] = M[i-1][w]
            else:
                M[i][w] = M[i-1][w] or M[i-1][w - weights[i-1]]
    return M[n][W]

n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i+1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

if subsetSum(n, W, weights):
    print(f"A subset with sum {W} exists.")
else:
    print(f"No subset with sum {W} exists.")