class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0

        left = 0
        right = 1

        while right < len(prices):

            if prices[right] - prices[left] > maxProfit:
                maxProfit = prices[right] - prices[left]
            elif prices[left] > prices[right]:
                left = right

            right += 1

        return maxProfit