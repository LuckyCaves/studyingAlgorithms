class Node:

    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.val = value

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        root = Node(nums[0])

        pos = root

        def recursion(root, val):

            if val > root.val and root.right != None:
                recursion(root.right, val)
                return
            elif val < root.val and root.left != None:
                recursion(root.left, val)
                return

            n = Node(val)
            if val > root.val:
                root.right = n
            elif val < root.vale:
                root.left = n

        def recursion2(node):

            if node == None:
                return

            if node.left != None:
                recursion(node.left)
            print(node.val)
            if node.right != None:
                recursion(node.right)

        for i in nums:
            recursion(root, i)

        recursion2(root)
        
