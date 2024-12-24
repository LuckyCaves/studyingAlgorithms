class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        dict = {}
        zeros = 0

        for i, j in enumerate(nums):
            if j == 0:
                zeros += 1
                nums.remove(i)

        for i in range(zeros):
            nums.append(0)

