class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        ans = ""
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for o in order:
            if o in freq:
                ans += o * freq[o]
                del freq[o]

        for o in freq:
            ans += o * freq[o]
        return ans