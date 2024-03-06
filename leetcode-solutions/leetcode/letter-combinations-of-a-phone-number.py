class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        key_pair = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        counter = [0 for i in range(len(digits))]
        ans = []
        
        def backTracking(d,s):
            if d == len(digits):
                if s:
                    ans.append(s)
                return

            for c in range(len(key_pair[digits[d]])):    
                s += key_pair[digits[d]][c]
                backTracking(d+1,s)
                s = s[:-1]
        backTracking(0,'')
        return ans