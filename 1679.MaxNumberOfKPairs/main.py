class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dict = {}

        for i in nums:
            if dict.get(i, 0) == 0:
                dict[i] = 1
            else:
                dict[i] += 1
        
        operations = 0

        for i in nums:
            res = k - i
            if dict.get(res, -1) > 0:
                operations += 1
                dict[res] -= 1
        
        return operations // 2
