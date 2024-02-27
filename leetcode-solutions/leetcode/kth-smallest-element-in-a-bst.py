# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def preOrder(root):
            if root:
                self.arr.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        self.arr.sort()
        return self.arr[k-1]