# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        parents = []
        parents.append(root)
        i = root

        if root is None:
            return res

        while len(parents) != 0:

            if i.right == None and i.left == None:
                i = parents.pop()
                if i == root:
                    break

            if i.left != None:
                parents.append(i)
                i = i.left
                parents[len(parents) - 1].left = None
            else:
                res.append(i.val)

            if i.right != None:
                parents.append(i)
                i = i.right
                parents[len(parents) - 1].right = None
            else:
                res.append(i.val)

        return res
        