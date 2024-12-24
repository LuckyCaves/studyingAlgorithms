# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def getLeafValues(root):

            stack = []
            stack.append(root)
            res = []

            while stack:

                for i in range(len(stack)):

                    curr = stack.pop()
                    if curr.left is None and curr.right is None:
                        res.append(curr.val)
                        continue
                    if curr.left != None:
                        stack.append(curr.left)
                    if curr.right != None:
                        stack.append(curr.right)
            return res

        return getLeafValues(root1) == getLeafValues(root2)
