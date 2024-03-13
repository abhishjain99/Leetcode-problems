class Solution:
    def maximum69Number (self, num: int) -> int:
        i = -1
        num = str(num)
        for index, c in enumerate(num):
            if c == "6":
                i = index
                break

        if i == -1:
            return int(num)
        else:
            return int(num[:i] + "9" + num[i+1:])