class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        bo = True
        maxi = sorted(arr)[-1]
        index = arr.index(maxi)
        if len(arr) < 3 or index == 0 or index == len(arr)-1:
            return False
        else:
            i = 1
            while i <= index:
                if arr[i] <= arr[i-1]:
                    bo = False
                i+=1
            j = index+1
            while j < len(arr):
                if arr[j] >= arr[j-1]:
                    bo = False
                j+=1
        return bo
            