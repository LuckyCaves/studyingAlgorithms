# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        stack = []
        stack.append([root, 0, 0])
        maxZigZag = 0

        while stack:

            for i in range(len(stack)):

                curr, direction, zigZag = stack.pop()

                if curr is None:
                    continue
                
                maxZigZag = max(maxZigZag, zigZag)

                if direction == 1:
                    stack.append([curr.left, -1, zigZag + 1])
                    stack.append([curr.right, 1, 1])
                elif direction == -1:
                    stack.append([curr.left, -1, 1])
                    stack.append([curr.right, 1, zigZag + 1])
                elif direction == 0:
                    stack.append([curr.left, -1, zigZag + 1])
                    stack.append([curr.right, 1, zigZag + 1])
                    

        return maxZigZag