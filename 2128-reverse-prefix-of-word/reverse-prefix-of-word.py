class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        left = 0
        right = 0
        word = list(word)
        for w in range(len(word)):
            if word[w] == ch:
                right = w
                break
        if w == len(word):
            return
        while right > left:
            word[left], word[right] = word[right], word[left]
            right -= 1
            left += 1
            print(word)
        return "".join(word)
