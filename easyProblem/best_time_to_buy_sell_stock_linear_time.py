class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        # Check for current element with minimum value in list
        # if current price is less than minimum then we will not sell stock instead update minimum
        for i in prices:
            if (i < min_price):
                min_price = i
            else:
                max_profit = max(max_profit, i-min_price)
            
        return max_profit
