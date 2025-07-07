class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])
        
        minHeap = []
        d = events[0][0]
        i = 0
        res = 0

        while minHeap or i < len(events):
            while i < len(events) and events[i][0] <= d:
                _, e = events[i]
                heapq.heappush(minHeap, e)
                i += 1

            if minHeap:
                e = heapq.heappop(minHeap)
                if d > e:
                    continue
                d += 1
                res += 1
            else:
                d = events[i][0]
        return res