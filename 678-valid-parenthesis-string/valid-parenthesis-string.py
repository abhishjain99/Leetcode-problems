class Solution:
    def checkValidString(self, s: str) -> bool:
        para, star, ans = [], [], False
        opens, closes, stars = 0, 0, 0
        for i, c in enumerate(s):
            if c == "(":
                para.append(i)
            elif c == ")":
                if para:
                    para.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(i)

        while para:
            if len(star) == 0:
                return False
            if para[-1] > star[-1]:
                return False
            para.pop()
            star.pop()
        return True