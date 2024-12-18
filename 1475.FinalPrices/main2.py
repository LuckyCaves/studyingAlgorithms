class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        stack = []
        pos = -1

        for i in range(len(prices)):

            while(pos >= 0 and prices[i] <= prices[stack[pos]]):
                ind = stack.pop()
                pos -= 1
                prices[ind] -= prices[i]

            stack.append(i)
            pos += 1

        return prices