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
            for i in range(len(d) // 2):
                curr1 = d.popleft()
                curr2 = d.pop()

                if curr1 is None and curr2 is None:
                    continue
                elif curr1 is None or curr2 is None:
                    return False
                elif curr1.val != curr2.val:
                    return False
                
                d.appendleft(curr1.left)
                d.append(curr2.right)
                d.appendleft(curr2.left)
                d.append(curr1.right)
        
        return True
