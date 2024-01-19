class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre = list(accumulate([0]+self.nums))
            
        

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right+1] - self.pre[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)