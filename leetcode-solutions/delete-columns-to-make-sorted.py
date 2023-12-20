class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        arr = [list(t) for t in strs]
        i = 0 
        n = len(arr[0])
        count = 0
        while i < n:
            new_arr = []
            for k in range(len(arr)):
                new_arr.append(arr[k][i])
            if new_arr != sorted(new_arr):
                count+=1    
            i+=1
        return count