class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        l, r = 0, k - 1

        maxAvg = - float("inf")
        currSum = 0

        for i in range(r + 1):
            currSum += nums[i]


        while r < len(nums) - 1:

            maxAvg = max(maxAvg, currSum / k)
            l += 1
            r += 1
            currSum += (nums[r] - nums[l - 1])

        return max(maxAvg, currSum / k)