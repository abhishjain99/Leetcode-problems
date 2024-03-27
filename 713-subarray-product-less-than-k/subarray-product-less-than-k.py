class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = []
        left, right, ans = 0, 0, 0
        product = 1
        n = len(nums)
        if k <= 1: return 0
        while right < n:
            product *= nums[right]
            while product >= k:
                product /= nums[left]
                left += 1
            ans += right - left + 1
            right += 1
        return ans