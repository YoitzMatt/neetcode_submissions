class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = profit = 0
        
        l = 0 
        for r in range(len(prices)):
            while l < len(prices) and prices[r] - prices[l] < 0:
                l += 1
            curr_profit = prices[r] - prices[l]
            profit = max(profit, curr_profit) 
        return profit