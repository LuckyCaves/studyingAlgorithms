# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def recursion(node):

            if node is None:
                return 0

            if (node.left is None and node.right is None):
                return 1

            next = None

            return max(recursion(node.left), recursion(node.right)) + 1
        
        if root is None:
            return 0

        return recursion(root)

