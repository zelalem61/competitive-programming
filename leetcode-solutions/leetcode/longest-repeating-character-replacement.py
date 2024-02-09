class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        res = 0
        counter = defaultdict(int)
        
        for i in range(len(s)):
            
            counter[s[i]] += 1
            
            
            while (i - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
                    
            res = max(res, i - left + 1)
        
        return res