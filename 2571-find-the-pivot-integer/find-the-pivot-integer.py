class Solution:
    def pivotInteger(self, n: int) -> int:
        a = sqrt(n * (n + 1) / 2)
        if a % 1 != 0:
            return -1
        return int(a)