class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for start in nums:
            if start - 1 not in hash_set:
                end = start + 1
                while end in hash_set:
                    end += 1
                ans = max(end - start, ans)
        return ans