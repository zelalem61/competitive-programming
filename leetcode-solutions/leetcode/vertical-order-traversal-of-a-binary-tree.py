# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([(root, 0)])
        left, right = 0, 0
        levels = defaultdict(list)
        levels[0] = [root.val]
        while queue:
            nxt = []
            nxt_level = defaultdict(list)
            for curr, col in queue:
                left = min(left, col)
                right = max(right, col)
                if curr.left:
                    nxt.append((curr.left, col - 1))
                    nxt_level[col - 1].append(curr.left.val)
                if curr.right:
                    nxt.append((curr.right, col + 1))
                    nxt_level[col + 1].append(curr.right.val)

            queue = nxt
            for key, lst in nxt_level.items():
                for v in sorted(lst):
                    levels[key].append(v)  
        
        ans = []
        for i in range(left, right + 1):
            ans.append(levels[i])
        return ans