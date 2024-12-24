class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recursion(n):

            if n <= 2:
                return n

            return recursion(n - 1) + recursion(n - 2) 