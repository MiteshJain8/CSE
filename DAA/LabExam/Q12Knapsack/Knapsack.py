def knapsack(items, W, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    w = W
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(items[i-1])
            w -= items[i-1][1]
    selected.reverse()
    return dp[n][W], selected

n = int(input("Enter number of items: "))
items = []

print("Enter weight and value (space separated):")
for i in range(n):
    weight, value = map(int, input(f"Item {i+1}: ").split())
    items.append((i+1, weight, value))

W = int(input("Enter maximum weight: "))

maxValue, selected = knapsack(items, W, n)
print("Maximum Value:", maxValue)
print("Selected Items:", selected)