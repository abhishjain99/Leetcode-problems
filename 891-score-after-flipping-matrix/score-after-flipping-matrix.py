class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] = 1 - grid[row][col]
        
        for col in range(1, n):
            cnt = 0
            for row in range(m):
                if grid[row][col] == 0:
                    cnt = cnt + 1
            if cnt > m - cnt:
                for row in range(m):
                    grid[row][col] ^= 1
        
        score = 0
        for row in range(m):
            for col in range(n):
                colScore = grid[row][col] << (n - col - 1)
                score += colScore

        return score
                