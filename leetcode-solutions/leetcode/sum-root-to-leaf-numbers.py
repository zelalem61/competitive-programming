class Solution:
    def __init__(self):
        self.stri = ""
        self.arr = []

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root:
            self.stri += str(root.val)
            if root.left is None and root.right is None:  # it's a leaf node
                self.arr.append(self.stri)
            else:
                if root.left is not None:
                    self.sumNumbers(root.left)
                if root.right is not None:
                    self.sumNumbers(root.right)
            self.stri = self.stri[:-1]  

        return sum(int(s) for s in self.arr)