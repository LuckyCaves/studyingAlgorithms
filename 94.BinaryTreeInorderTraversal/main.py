# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def recursion(node):

            if node == None:
                return

            if node.left != None:
                recursion(node.left)
            res.append(node.val)
            if node.right != None:
                recursion(node.right)
            
        recursion(root)

        return res
        