class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        height = [0] * n

        for r in range(m):
            for c in range(n):
                height[c] = height[c] + 1 if mat[r][c] == 1 else 0

            stack = []
            count = [0] * n
            for i in range(n):
                while stack and height[stack[-1]] >= height[i]:
                    stack.pop()
                if stack:
                    prev_index = stack[-1]
                    count[i] = count[prev_index] + height[i] * (i - prev_index)
                else:
                    count[i] = height[i] * (i + 1)
                stack.append(i)
                ans += count[i]

        return ans