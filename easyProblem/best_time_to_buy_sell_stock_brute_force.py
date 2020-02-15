class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        N = len(prices)
        
        for i in range(N):
            for j in range(i+1, N):
                max_profit = max(max_profit, prices[j] - prices[i])
        
        return max_profit
