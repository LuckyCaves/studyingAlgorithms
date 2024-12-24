class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        currAlt = 0
        maxAlt = 0

        for i in gain:
            currAlt += i
            maxAlt = max(maxAlt, currAlt)
        
        return maxAlt