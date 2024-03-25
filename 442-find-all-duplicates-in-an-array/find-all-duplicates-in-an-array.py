class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return []
        ans = []
        for num in nums:
            num = abs(num)
            if nums[num - 1] < 0:
                ans.append(num)
            nums[num - 1] *= -1
        return ans
