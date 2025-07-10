fmax = lambda a, b: a if a > b else b

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        head = 0
        space = []

        for s, e in zip(startTime, endTime):
            space.append([0, s - head])
            space.append([1, e - s])
            head = e

        space.append([0, eventTime - endTime[-1]])

        func = lambda total, x: fmax(total, x[1] if x[0] == 0 else -1)
        pre_max = list(accumulate(space, func, initial=-1))
        suf_max = list(accumulate(space[::-1], func, initial=-1))[::-1]
        
        ans = -inf
        for i, (t, v) in enumerate(space):
            if t == 0:
                continue
            
            if pre_max[i - 1] >= v or suf_max[i + 2] >= v:
                ans = fmax(ans, space[i - 1][1] + space[i + 1][1] + v)
            else:
                ans = fmax(ans, space[i - 1][1] + space[i + 1][1])

        return ans


    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:

        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        size = len(startTime)
        suf_max = [-1] * size
        suf_max[-1] = eventTime - endTime[-1]

        for i in range(size - 2, -1, -1):
            suf_max[i] = fmax(suf_max[i + 1], startTime[i + 1] - endTime[i])

        ans = pre_max = -1
        for i in range(1, size - 1):
            s, e = startTime[i], endTime[i]
            
            space = (s - endTime[i - 1]) + (startTime[i + 1] - e)
            duration = e - s

            if duration <= pre_max or duration <= suf_max[i + 1]:
                ans = fmax(ans, space + duration)
            else:
                ans = fmax(ans, space)
            pre_max = fmax(pre_max, s - endTime[i - 1])

        return ans


class Solution1:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        def get(i: int) -> int:
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[n - 1]
            return startTime[i] - endTime[i - 1]

        a, b, c = 0, -1, -1
        for i in range(1, n + 1):
            sz = get(i)
            if sz > get(a):
                a, b, c = i, a, b
            elif b < 0 or sz > get(b):
                b, c = i, b
            elif c < 0 or sz > get(c):
                c = i

        ans = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s
            if i != a and i + 1 != a and sz <= get(a) or \
               i != b and i + 1 != b and sz <= get(b) or \
               sz <= get(c):
                ans = fmax(ans, get(i) + sz + get(i + 1))
            else:
                ans = fmax(ans, get(i) + get(i + 1))
        return ans