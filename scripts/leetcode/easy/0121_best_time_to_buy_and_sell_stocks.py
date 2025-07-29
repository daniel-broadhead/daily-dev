"""
Problem: best time to buy and sell stocks (LeetCode #121)
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Approach:
- I want to iterate through the array and update the min_price if it is less than the current min_price. If not I want to calculate
the profit with that price and min_price.

Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


# Example test
if __name__ == "__main__":
    print(Solution().maxProfit([7,1,5,3,6,4], 5))
