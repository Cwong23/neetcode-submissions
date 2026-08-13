class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0], reverse=True)
        rooms = [[0, 0] for _ in range(n)]
        while meetings:
            curr = meetings.pop()
            min_time, min_index = rooms[0][0], 0
            temp = 0
            for i, room in enumerate(rooms):
                b = False
                r = []
                if room[0] <= curr[0]:
                    room[0] = curr[1]
                    room[1]+=1
                    b = True
                if room[0] < min_time:
                    min_time = room[0]
                    min_index = i
                elif room[0] == min_time and min_index > i:
                    min_index = i
                if b:
                    break
                temp = i
            else:
                rooms[min_index][0] = rooms[min_index][0] - curr[0] + curr[1]
                rooms[min_index][1]+=1
        
        max_index, max_meetings = 0, 0
        for i in range(len(rooms)):
            if rooms[i][1] > max_meetings:
                max_index = i
                max_meetings = rooms[i][1]
        return max_index


        
        