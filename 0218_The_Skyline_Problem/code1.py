class Solution:
    def getSkyline(self, buildings):
        
        points = []
        for index, (left, right, height) in enumerate(buildings):
            points += [(right, height, index, 1)] + [(left, height, index, -1)]
            
        points.sort(key = lambda x: (x[0], x[1] * x[3]))
        heap, left_point_start, ans = [(0,-1)], set([-1]), []
        
        for posx, height, index, left_or_right in points:
            if left_or_right == -1:
                left_point_start.add(index)
                if height > -heap[0][0]: 
                    ans.append([posx, height])
                heappush(heap, (-height, index))
            else:
                left_point_start.remove(index)
                if height == -heap[0][0]:   
                    while heap and heap[0][1] not in left_point_start: 
                        heappop(heap)
                if -heap[0][0] != ans[-1][1]: 
                    ans.append([posx, -heap[0][0]])
                    
        return ans