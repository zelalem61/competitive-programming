# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        values = []
        def preOrder(root):
            if root:
                values.append(root.val)
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        dic = Counter(values)
        maxi = max(dic.values())
        for num in set(values):
            if dic[num] == maxi:
                ans.append(num)
        return ans
