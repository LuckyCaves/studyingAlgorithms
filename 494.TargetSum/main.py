class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        def recursion(index, total):
            if index > len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            return recursion(index + 1, total + nums[index]) + recursion(index + 1, total - nums[index])
        
        return recursion(0, 0)