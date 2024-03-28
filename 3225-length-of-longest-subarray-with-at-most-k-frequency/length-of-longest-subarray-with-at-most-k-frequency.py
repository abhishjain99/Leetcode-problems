class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, right, max_size = 0, 0, 0
        cnt = {}
        while right < len(nums):
            j = nums[right]
            cnt[j] = cnt.get(j, 0) + 1
            while cnt[j] > k:
                cnt[nums[left]] -= 1
                left += 1
            max_size = max(max_size, right-left+1)
            right += 1
        return max_size