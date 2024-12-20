class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        size = 1
        count = 0
        maximum = nums[0]

        for i in nums:
            if i > maximum:
                count += 1
            

        
