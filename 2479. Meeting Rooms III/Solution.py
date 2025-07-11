class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts, rooms, t = [0]*n, list(range(n)), 0
        meetings, ongoingMeetings = sorted(meetings, key = lambda x: x[0]), []
        heapq.heapify(rooms)

        for start, end in meetings:
            while ongoingMeetings and ongoingMeetings[0][0]<=start:
                heapq.heappush(rooms, heapq.heappop(ongoingMeetings)[1])
            if rooms:
                room = heapq.heappop(rooms)
            else:
                t, room = heapq.heappop(ongoingMeetings)
                end += t-start

            counts[room] += 1
            heapq.heappush(ongoingMeetings, (end, room))
            
        return max(range(n), key = lambda x: (counts[x], -x))