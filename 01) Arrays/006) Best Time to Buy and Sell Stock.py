"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""


def max_profit(prices: list[int]) -> int:
    """"""

    # 0) [TLE] Brute-force (Calculating profits for all the combinations): TC = O(n^2); SC = O(1)

    """
    n = len(prices)
    max_profit_ = 0
    for i in range(n):  # considering all the prices in the array one by one as cost price
        for j in range(i+1, n):  # for a particular cost price, all the prices in the next days will be selling prices
            profit = prices[j] - prices[i]  # selling_price - cost_price
            if profit > max_profit_:
                max_profit_ = profit
    return max_profit_
    """

    # 1) Optimal (Kadane's Algo): TC = O(n); SC = O(1)

    cost_price = float('inf')  # init
    max_profit_ = 0
    for price in prices:
        if price < cost_price:
            cost_price = price  # bought stock at a lesser price
            continue  # bought stock on this day, so doesn't make sense selling because profit will obviously be 0
        profit = price - cost_price
        if profit > max_profit_:
            max_profit_ = profit
    return max_profit_
