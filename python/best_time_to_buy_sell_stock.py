from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given an array of stock prices, returns the maximum profit possible with one buy and one sell.

        Time Complexity: O(n) where n is the length of prices.
          - We traverse the array once.
        Space Complexity: O(1), constant extra space.

        :param prices: List[int] - list of stock prices
        :return: int - maximum profit achievable
        """
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate potential profit and update max_profit
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
