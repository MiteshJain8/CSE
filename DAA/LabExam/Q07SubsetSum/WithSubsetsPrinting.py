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
    return M

def findSubsets(M, weights, n, W):
    def backtrack(i, w, currentSet):
        if i == 0 and w == 0:
            allSubsets.append(currentSet)
            return
        if i == 0:
            return
        if M[i-1][w]:
            backtrack(i-1, w, currentSet[:])
        if w >= weights[i-1] and M[i-1][w-weights[i-1]]:
            backtrack(i-1, w-weights[i-1], currentSet + [weights[i-1]])

    allSubsets = []
    backtrack(n, W, [])
    return allSubsets

n = int(input("Enter the number of elements: "))
weights = [int(input(f"Enter weight {i+1}: ")) for i in range(n)]
W = int(input("Enter the target sum: "))

M = subsetSum(n, W, weights)

if M[n][W]:
    print(f"A subset with sum {W} exists.")
    subsets = findSubsets(M, weights, n, W)
    print("Subsets that sum to", W, "are:")
    for subset in subsets:
        print(subset)
else:
    print(f"No subset with sum {W} exists.")