
# Return Type  sum_of_bst,Min(BST),Max(BST),isBST

class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max1=0
        def recur(root):
            if root is None:
                return 0,inf,-inf,True

            left= recur(root.left)
            right=recur(root.right)
            # print(left,right,root.val)

            if (left[3] and right[3]) and (left[2]<root.val and root.val<right[1]):
                sum1=root.val+left[0]+right[0]
                nonlocal max1
                max1=max(max1,sum1)
            else:
                return 0,0,0,False
            
            return sum1,min(root.val,left[1]),max(root.val,right[2]),True

        recur(root)
        return max1