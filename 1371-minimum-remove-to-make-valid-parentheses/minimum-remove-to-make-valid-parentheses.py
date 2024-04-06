class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # open_cnt, close_cnt, open_flag, ans = 0, 0, 0, ""
        # for c in s:
        #     if c == "(":
        #         open_cnt += 1
        #         open_flag += 1
        #     elif c == ")" and open_flag > 0:
        #         close_cnt += 1
        #         open_flag -= 1
        
        # open_cnt, close_cnt = min(open_cnt, close_cnt), min(open_cnt, close_cnt)
        # for c in s:
        #     if c == "(" and open_cnt > 0:
        #         ans += c
        #         open_cnt -= 1
        #     elif c == ")" and close_cnt > 0 and close_cnt > open_cnt:
        #         ans += c
        #         close_cnt -= 1
        #     elif c != "(" and c != ")":
        #         ans += c
        # return ans

        stack = []
        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)
        
        ans = ""
        for i, c in enumerate(s):
            if stack and i == stack[0]:
                stack.pop(0)
                continue
            ans += c
        return ans