class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dict = {}
        degree = 1
        maxDistance = 1

        for i, j in enumerate(nums):
            if dict.get(j, 0):
                dict[j][1] += 1

                if degree < dict[j][1] or (degree == dict[j][1] and maxDistance > i - dict[j][0] + 1):
                    maxDistance = i - dict[j][0] + 1
                    degree = dict[j][1]

            else:
                dict[j] = [i, 1]
    
        return maxDistance
