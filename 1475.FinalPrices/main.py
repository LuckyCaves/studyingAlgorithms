class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        res = []

        price = 0
        discount = 1

        while(price < len(prices)):

            if(discount >= len(prices)):
                res.append(prices[price])
                price += 1
                discount = price + 1
            elif(prices[price] >= prices[discount]):
                res.append(prices[price] - prices[discount])
                price += 1
                discount = price + 1
            else:
                discount += 1

        return res

            