def max_profit_with_requests(drama_requests):
    drama_requests.sort(key=lambda x: x[2])
    
    n = len(drama_requests)
    dp = [0] * n
    selected_requests = [[] for _ in range(n)]

    dp[0] = drama_requests[0][3]
    selected_requests[0] = [drama_requests[0]]

    for i in range(1, n):
        current_value = drama_requests[i][3]
        selected_requests[i] = [drama_requests[i]]

        for j in range(i - 1, -1, -1):
            if drama_requests[j][2] <= drama_requests[i][1]:
                current_value += dp[j]
                selected_requests[i] = [drama_requests[i]] + selected_requests[j]
                break

        dp[i] = max(dp[i - 1], current_value)

    return dp[-1], selected_requests[-1]

drama_requests = [
    (1, 1, 2, 100),
    (2, 2, 5, 200),
    (3, 3, 6, 300),
    (4, 4, 8, 400),
    (5, 5, 9, 500),
    (6, 6, 10, 100)
]

max_profit, selected_requests = max_profit_with_requests(drama_requests)
print("Maximum Profit:", max_profit)
print("Selected Requests:", selected_requests)