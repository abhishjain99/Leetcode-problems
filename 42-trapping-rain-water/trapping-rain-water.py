class Solution:
    def trap(self, height: List[int]) -> int:
        n, max_height, max_h = len(height), 0, [0] * len(height)
        for i in range(n - 1, -1, -1):
            max_height = max(max_height, height[i])
            max_h[i] = max_height
        
        max_height, ans = 0, 0
        for i in range(n):
            max_height = max(max_height, height[i])
            ans += min(max_height, max_h[i]) - height[i]

        return ans