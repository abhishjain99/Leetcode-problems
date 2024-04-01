class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        return sorted(hash_map, key = lambda n: hash_map[n], reverse=True)[:k]