class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # first, we will create array of tuples which will contain (newnum, index) mapping
        # while we are not at the end of nums:
          # we iterate through each num and create newnum
          # once we reach end of num, we store it in hashmap with its index
        # we sort the hashmap
        # we go through nums and store answer wrt index
        hash_map = [] # (number, i)
        for i, num in enumerate(nums):
            mapped_num = 0
            base = 1
            if num == 0:
                mapped_num = mapping[num]
            while num > 0:
                digit = num % 10
                num = num // 10
                mapped_num += base * mapping[digit]
                base *= 10
            hash_map.append((mapped_num, i))
        hash_map.sort()
        return [nums[num[1]] for num in hash_map]