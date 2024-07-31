def knapsack(items, maxWeight, n):
    dp = [[0] * (maxWeight + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(maxWeight + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    w = maxWeight
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(items[i-1])
            w -= items[i-1][1]
    selected.reverse()
    return dp[n][maxWeight], selected

n = 6
#items=[tuples(No., weight, value)]
items = [(1, 5, 100),(2, 7, 300),(3, 8, 200),(4, 10, 100),(5, 5, 200),(6, 2, 100)]
maxWeight = 20
maxValue, selected = knapsack(items, maxWeight, n)
print("Maximum Value:", maxValue)
print("Selected Items:", selected)