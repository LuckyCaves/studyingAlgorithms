class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        p1, p2 = 0, len(height) - 1
        maxArea = 0

        while p1 != p2:

            x = p2 - p1
            y = min(height[p1], height[p2])

            maxArea = max(maxArea, x * y)

            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1
        
        return maxArea