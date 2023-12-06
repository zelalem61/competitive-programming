class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        count = 0
        smallest = []
        largest = []
        
        for i in nums:
            if i < pivot:
                smallest.append(i)
            elif i > pivot :
                largest.append(i)
            else:
                count += 1
        for j in range(count):
            smallest.append(pivot)
        return smallest + largest
        