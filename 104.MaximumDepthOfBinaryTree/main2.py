# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = []
        stack.append(root)

        counter = 0

        while len(stack) > 0:

            for i in range(len(stack)):
                curr = stack.pop()
                if curr.left != None:
                    stack.append(curr.left)
                if curr.right != None:
                    stack.append(curr.right)
            counter += 1

        print(counter)

def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        stack = []
        stack.append([root, 1])

        depth = 1

        while len(stack) > 0:

            curr, level = stack.pop()

            if curr.right:
                stack.append([curr.right, level + 1])
            if curr.left:
                stack.append([curr.left, level + 1])

            depth = max(depth, level)

        return depth