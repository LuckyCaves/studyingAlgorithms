class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        

        l = r = float('inf')

        for num in nums:

            if num <= l:
                l = num
            elif num <= r:
                r = num
            
            if num > r:
                return True

        return False
