class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        answer = []
        path = []
        
        def dp(idx, total):
            if len(path) > k:
                return
            if total > n:
                return
            if total == n and len(path) == k:
                answer.append(path.copy())
                return 
                
            for i in range(idx, 10):
                path.append(i)
                dp(i+1, total + i)
                path.pop()
        
        dp(1, 0)
        return  answer