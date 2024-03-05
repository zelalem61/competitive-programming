class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def helper(node, maxi, mini):
            if node is None:
                return
            if node.val < mini:
                mini = node.val
            elif node.val > maxi:
                maxi = node.val
            nonlocal ans
            ans = max(ans, abs(maxi - mini))
            helper(node.left, maxi, mini)
            helper(node.right, maxi, mini)

        helper(root, root.val, root.val)
        return ans