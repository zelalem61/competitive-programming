class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)

        inter = nums1.intersection(nums2)
        if len(inter) == 0:
            return -1
        return min(inter)