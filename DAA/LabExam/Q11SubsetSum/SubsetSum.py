def subsetSum(weights, W, n):
    M = [[False] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        M[i][0] = True
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i-1] <= w:
                M[i][w] = M[i-1][w] or M[i-1][w - weights[i-1]]
            else:
                M[i][w] = M[i-1][w]
    return M

def findSubset(weights, W, n, M):
    if not M[n][W]:
        return None  # No subset with given sum
    w = W
    selected = []
    for i in range(n, 0, -1):
        if M[i][w] and not M[i - 1][w]:
            selected.append(weights[i - 1])
            w -= weights[i - 1]
    return selected

n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i+1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

M = subsetSum(weights, W, n)

if M[n][W]:
    print(f"A subset with sum {W} exists.")
    subset = findSubset(weights, W, n, M)
    print(f"Subset that sums to {W} is:",subset)
else:
    print(f"No subset with sum {W} exists.")