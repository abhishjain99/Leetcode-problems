class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = {}
        ans = []
        for num in nums1:
            nums[num] = nums.get(num, 0) + 1
        for num in nums2:
            if num in nums:
                ans.append(num)
                nums[num] -= 1
                if not nums[num]: del nums[num]
        return ans