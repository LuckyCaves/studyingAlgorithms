# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []

        q = deque()
        q.append(root)

        result = []

        while q:

            curr = None
            for i in range(len(q)):
                curr = q.popleft()
    
                if curr.left != None:
                    q.append(curr.left)
                if curr.right != None:
                    q.append(curr.right)

            result.append(curr.val)
        
        return result