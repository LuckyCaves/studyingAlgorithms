class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        curr = 1
        left = False

        while curr < len(nums):

            if nums[curr - 1] < nums[curr]:
                left = True
            elif nums[curr - 1] > nums[curr] and left:
                return curr - 1
            else:
                left = False
            curr += 1
        
        if left:
            return curr - 1
        else:
            return 0