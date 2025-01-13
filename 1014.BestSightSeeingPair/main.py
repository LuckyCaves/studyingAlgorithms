class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        l, r = 0, 1
        maxScore = 0
        currScore = 0

        while r < len(values):

            currScore = values[l] + values[r] + (l - r)
            maxScore = max(currScore, maxScore)
            
            if values[l] + (l - r) <= values[r]:
                l = r
            r += 1
        
        return maxScore