class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(num):
            if len(path) == k:
                ans.append(path.copy())
                return

            for cand in range(num+1,n+1):
                path.append(cand)
                backtrack(cand)
                path.pop()
        backtrack(0)
        return ans
        