# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            return False

        stack = []
        stack.append([root, targetSum])

        while stack:

            for i in range(len(stack)):

                curr, target = stack.pop()
                target -= curr.val
                
                if target == 0 and curr.left is None and curr.right is None:
                    return True
                
                if curr.left != None:
                    stack.append([curr.left, target])
                if curr.right != None:
                    stack.append([curr.right, target])
        
        return False