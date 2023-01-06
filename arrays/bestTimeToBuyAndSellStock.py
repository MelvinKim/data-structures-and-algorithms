def maxProfitBruteForce(prices):
    if prices == None or len(prices) == 0:
        return 0

    current_profit = 0
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                current_profit = prices[j] - prices[i]
                max_profit = max(max_profit, current_profit)

    return max_profit


def maxProfitOptimal(prices):
    if prices == None or len(prices) == 0:
        return 0

    left_pointer = 0  # buying pointer
    right_pointer = 1  # selling pointer
    current_profit = 0
    max_profit = 0

    while right_pointer < len(prices):
        if prices[left_pointer] < prices[right_pointer]:
            current_profit = prices[right_pointer] - prices[left_pointer]
            max_profit = max(max_profit, current_profit)
            right_pointer = right_pointer + 1
        else:
            left_pointer = left_pointer + 1

        right_pointer = right_pointer + 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfitOptimal(prices))
