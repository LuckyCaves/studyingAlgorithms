# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getDepth(root):

            if not root:
                return 0

            stack = []
            stack.append([root, 0])
            maxDepth = 0

            while stack:

                for i in range(len(stack)):

                    curr, level = stack.pop()
                    level += 1

                    if curr.left != None:
                        stack.append([curr.left, level])
                    if curr.right != None:
                        stack.append([curr.right, level])
                    maxDepth = max(maxDepth, level)
            return maxDepth

        if root is None:
            return True

        s = []
        s.append(root)

        while s:
            for i in range(len(s)):
                curr = s.pop()

                if curr.left != None:
                    s.append(curr.left)
                if curr.right != None:
                    s.append(curr.right)

                if abs(getDepth(curr.left) - getDepth(curr.right)) > 1:
                    return False
        
        return True