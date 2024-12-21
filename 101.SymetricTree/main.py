# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        d = deque()
        d.append(root.left)
        d.append(root.right)

        while d:

            for i in range(len(d)):
                curr1 = d.popleft()
                curr2 = d.pop()

                if not(curr1 and curr2):
                    return False

                if curr1.val != curr2.val:
                    return False
                d.appendleft(curr1.left)
                d.append(curr2.right)
                d.appendleft(curr2.left)
                d.append(curr1.right)
        
        return True
