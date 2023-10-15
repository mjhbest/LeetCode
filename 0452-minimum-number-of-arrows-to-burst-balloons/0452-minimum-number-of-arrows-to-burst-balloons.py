class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: (x[1],x[0]))
        
        cnt = 1
        cur = points[0][1]
        for start, end in points[1:]:
            if cur < start:
                cnt += 1
                cur = end
        return cnt
        
        
                
            
                            