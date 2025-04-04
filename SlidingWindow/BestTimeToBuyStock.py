
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


def maxProfit(prices):
    # max_profit = 0
    # n = len(prices)
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         profit = prices[j] - prices[i]
    #         max_profit = max(max_profit, profit)
    # return max_profit

         min_price = float('inf')            #O(n),0(1)
         max_profit = 0

         for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(max_profit,profit)

         return max_profit



