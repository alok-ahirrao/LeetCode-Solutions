class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)
        m = len(grid[0])
        nv = [2, 2, 0] # Next expected value

        @functools.cache
        def helper(x, y, turned, dir):
            # First, we do not change the direction
            res = 1
            dx, dy = dirs[dir]
            if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                res = helper(x + dirs[dir][0], y + dirs[dir][1], turned, dir) + 1
            if not turned:
                dx, dy = dirs[(dir + 1) % 4]
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                    res = max(res, helper(x + dx, y + dy, True, (dir + 1) % 4) + 1)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Optimization: we can compute the theorically longest path. If the current answer is already better than this, we do not need to make the DFS.
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > ans:
                            ans = max(ans, helper(i, j, False, d))
        return ans