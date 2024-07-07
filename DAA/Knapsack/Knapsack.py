def knapsack(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(max_weight + 1):
            if items[i-1][1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - items[i-1][1]] + items[i-1][2])
            else:
                dp[i][w] = dp[i-1][w]
    
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(items[i-1])
            w -= items[i-1][1]
    
    selected_items.reverse()
    return dp[n][max_weight], selected_items

items = [
    (1, 5, 100),
    (2, 7, 300),
    (3, 8, 200),
    (4, 10, 100),
    (5, 5, 200),
    (6, 2, 100)
]

max_weight = 20

max_value, selected_items = knapsack(items, max_weight)
print("Maximum Value:", max_value)
print("Selected Items:", selected_items)