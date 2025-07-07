class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda e: e[1])

        mx = events[-1][1]
        fa = list(range(mx + 2))

        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        ans = 0
        for start_day, end_day in events:
            x = find(start_day)
            if x <= end_day:
                ans += 1
                fa[x] = x + 1
        return ans