class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in map_dict:
                map_dict[nums[i]] = i
            else:
                return [map_dict[complement], i]