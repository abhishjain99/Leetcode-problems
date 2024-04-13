class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if k == len(num): return "0"
        # i, ans, stack = 0, "", []
        # stack.append(num[0])
        # while i < len(num) and k != 0:
        #     if num[i] < stack[-1]:
        #         stack.pop()
        #         stack.append(num[i])
        #     k -= 1
        #     i += 1

        # while stack:
        #     res = stack.pop()
        #     if res != "0":
        #         ans += res
        # while i < len(num):
        #     ans += num[i]
        #     i += 1
        # return ans
        ans, stack = "", []
        if k >= len(num): return "0"
        for n in num:
            while stack and k != 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1
        ans = "".join(stack).lstrip("0")
        if ans == "": return "0"
        else: return ans
