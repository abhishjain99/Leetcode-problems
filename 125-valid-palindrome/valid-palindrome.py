class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.compile('[^a-zA-Z0-9]').sub('', s).lower()
        print(s)
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True