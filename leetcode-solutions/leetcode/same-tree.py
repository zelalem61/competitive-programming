# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.bo = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preOrder(p,q):
            if p or q:
                if not p or not q:
                    print("hhh")
                    self.bo = False
                    return 
                print(p.val,q.val)
                if p.val != q.val:
                    self.bo = False
                    return 
                preOrder(p.left,q.left)
                preOrder(p.right,q.right)
        preOrder(p,q,)
        return self.bo