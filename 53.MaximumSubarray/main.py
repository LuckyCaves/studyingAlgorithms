class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0]
        currSum = maxSum

        l, r = 0, 1

        while r < len(nums):
            if currSum + nums[r] <  0 or nums[l] < 0:
                l = r
                currSum = nums[l]
            else:
                currSum += nums[r]
            maxSum = max(currSum, maxSum)
            r += 1

        return maxSum
