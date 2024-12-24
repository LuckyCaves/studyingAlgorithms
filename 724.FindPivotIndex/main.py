class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)

        for i in range(1, len(nums)):
            leftSum[i] += nums[i - 1] + leftSum[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightSum[i] += nums[i + 1] + rightSum[i + 1]

        for i in range(len(nums)):
            if leftSum[i] == rightSum[i]:
                return i
        return -1