# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def recursion(node):

            if node is None:
                return float("inf")

            if (node.left is None and node.right is None):
                return 1

            next = None

            return min(recursion(node.left), recursion(node.right)) + 1
        
        if root is None:
            return 0

        return recursion(root)

