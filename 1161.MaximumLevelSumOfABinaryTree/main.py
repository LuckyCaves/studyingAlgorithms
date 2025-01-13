# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        q.append(root)

        maxSum = root.val
        level = 1
        currLevel = 1

        while q:

            currSum = 0
            for i in range(len(q)):
                curr = q.popleft()
                currSum += curr.val
    
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

            if currSum > maxSum:
                level = currLevel
                maxSum = currSum
            currLevel += 1
        
        return level