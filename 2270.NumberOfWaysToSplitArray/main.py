class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        prefixSum = 0


        for i in range(n - 1, -1, -1):

            prefixSum += nums[i]
        
        count = 0
        i = 1
        totalSum = 0

        while i < n:
            totalSum += nums[i - 1]
            prefixSum -= nums[i - 1]
            if totalSum >= prefixSum:
                count += 1
            i += 1

        return count