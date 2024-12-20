class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandies = max(candies)
        
        res = []

        for i in candies:
            res.append(i + extraCandies >= maxCandies)

        return res