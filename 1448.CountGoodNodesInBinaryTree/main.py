# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        stack = []
        goodNodes = 0
        stack.append([root, root.val])

        while stack:

            for i in range(len(stack)):

                curr, parentValue = stack.pop()

                if curr is None:
                    continue

                if curr.val >= parentValue:
                    goodNodes += 1
                
                nextVal = max(curr.val, parentValue)

                stack.append([curr.left, nextVal])
                stack.append([curr.right, nextVal])
        
        return goodNodes