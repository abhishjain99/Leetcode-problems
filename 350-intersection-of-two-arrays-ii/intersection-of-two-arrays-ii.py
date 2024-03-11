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

        # ans = []
        # counter1 = Counter(nums1)
        # counter2 = Counter(nums2)

        # for key in counter1.keys():
        #     if key in counter2:
        #         ans.extend([key] * min(counter1[key], counter2[key]))

        # return ans