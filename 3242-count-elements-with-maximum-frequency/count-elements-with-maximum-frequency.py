class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # freq = {}
        # max_freq = -99
        # for n in nums:
        #     freq[n] = freq.get(n, 0) + 1
        #     max_freq = max(max_freq, freq[n])
        # return sum(freq[f] for f in freq if freq[f] == max_freq)

        freq = {}
        max_freq = -99
        ans = 0
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
            max_freq = max(max_freq, freq[i])
        for f in freq:
            if freq[f] == max_freq:
                ans += max_freq
        return ans
