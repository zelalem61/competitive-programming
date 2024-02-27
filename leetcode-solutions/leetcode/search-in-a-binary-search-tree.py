# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = None
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def preOrder(root,val):
            if root:
                if root.val == val:
                    self.ans = root
                    return 
                preOrder(root.left,val)
                preOrder(root.right,val)
        preOrder(root,val)
        return self.ans
