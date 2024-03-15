class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums,target):
            low,high=0,len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    if mid == 0 or nums[mid-1]!= target:
                        return mid
                    else:
                        high=mid-1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        
        def findLast(nums,target):
            low,high=0,len(nums)-1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    if mid == len(nums)-1 or nums[mid+1]!= target:
                        return mid
                    else:
                        low=mid+1
                elif nums[mid]<target:
                    low=mid+1
                else:
                    high=mid-1
            return -1
        ans=[-1,-1]
        ans[0]=findFirst(nums,target)
        ans[1]=findLast(nums,target)
        return ans
