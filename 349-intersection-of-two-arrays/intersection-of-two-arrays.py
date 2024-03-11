class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return set(nums1) & set(nums2)

        # return list(set(nums1).intersection(set(nums2)))

        nums = {}
        ans = []
        for num in nums1:
            nums[num] = nums.get(num, 0) + 1
        for num in nums2:
            if num in nums:
                ans.append(num)
                del nums[num]
        return ans