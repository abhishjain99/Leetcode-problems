class Solution:
    def pivotInteger(self, n: int) -> int:
        # a = sqrt(n * (n + 1) / 2)
        # if a % 1 != 0:
        #     return -1
        # return int(a)

        for i in range(1, n + 1):
            left_sum = i * (i + 1) // 2
            right_sum = n * (n + 1) // 2 - i * (i - 1) // 2
            if left_sum == right_sum:
                return i
        return -1