class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        l, r = 0, 0
        k = 1

        while r < len(nums):

            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            r += 1
        
        return r - l - 1