class Solution:
    def solve(self, x1, y1, x2, y2):
        if x1 == x2:
            return f"x={x1}"
        if y1 == y2:
            return f"y={y1}"
        m = (y2 - y1) / (x2 - x1)
        c = y1 - (m * x1)

        return f"y={m}x+{c}"

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            lines = defaultdict(int)
            x1, y1 = points[i]
            # print(x1, y1)
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                eq = self.solve(x1, y1, x2, y2)
                lines[eq] += 1
                ans = max(ans, lines[eq])
            # print(lines)
        return ans + 1