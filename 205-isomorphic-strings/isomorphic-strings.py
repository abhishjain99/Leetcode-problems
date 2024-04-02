class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # map_s, map_t, ans = {}, {}, True
        # for i in range(len(s)):
        #     if s[i] in map_s:
        #         if map_s[s[i]] == t[i]:
        #             ans = True
        #         else: return False
        #     else:
        #         if t[i] not in map_t:
        #             map_s[s[i]] = t[i]
        #             map_t[t[i]] = s[i]
        #             ans = True
        #         else:
        #             return False
        # return ans

        map_s, map_t = {}, {}
        for i in range(len(s)):
            if s[i] not in map_s and t[i] not in map_t:
                map_s[s[i]] = t[i]
                map_t[t[i]] = s[i]
            elif map_s.get(s[i]) != t[i] or map_t.get(t[i]) != s[i]:
                return False
        return True