class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        
        for i in range(len(boxes)):
            count = 0 
            for j in range(len(boxes)):
                if i == j:
                    continue
                elif boxes[j] == "0":
                    continue
                else:
                    count += abs(i-j)
            ans.append(count)
        return ans