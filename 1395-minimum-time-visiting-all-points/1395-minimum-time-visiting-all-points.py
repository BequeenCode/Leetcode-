class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(len(points)-1):
            current_point = points[i]
            next_point = points[i+1]

            xd = abs(next_point[0] - current_point[0])
            yd = abs(next_point[1] - current_point[1])

            time += max(xd,yd)
        return time

        