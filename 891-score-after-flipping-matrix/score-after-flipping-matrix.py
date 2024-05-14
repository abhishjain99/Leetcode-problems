class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]

        cnt = {}
        for c in range(1, cols):
            cnt[c] = cnt.get(c, 0)
            for r in range(rows):
                if grid[r][c] == 0:
                    cnt[c] += 1

        ans = rows * (2 ** (cols - 1))
        for c in range(1, cols):
            ans += max(cnt[c], rows - cnt[c]) * 2 ** (cols - c - 1)

        return ans