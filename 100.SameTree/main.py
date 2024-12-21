# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = []
        stack.append([p, q])
            
        while len(stack) > 0:

            curr1, curr2 = stack.pop()

            if curr1 and curr2:
                if curr1.val != curr2.val:
                    return False
                stack.append([curr1.left, curr2.left])
                stack.append([curr1.right, curr2.right])
            elif curr1 != curr2:
                return False

        return True

