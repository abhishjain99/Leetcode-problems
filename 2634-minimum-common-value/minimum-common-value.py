class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        while len(nums1) > p1 and len(nums2) > p2:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            elif nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
        return -1