class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        left = 0
        res = 0
        counter = defaultdict(int)
        
        for i in range(len(answerKey)):
            
            counter[answerKey[i]] += 1
            
            
            while (i - left + 1) - max(counter.values()) > k:
                counter[answerKey[left]] -= 1
                left += 1
                    
            res = max(res, i - left + 1)
        
        return res
        