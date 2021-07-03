class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 當超過最後的期限時，將花費時間最長之課程從課表中刪除
        
        courses.sort(key = lambda element: element[1])
        
        heap, time = [], 0
        
        for course in courses:
            
            time += course[0]
            heapq.heappush(heap, -course[0])  
            
            while time > course[1]:
                time += heapq.heappop(heap)
            
        return len(heap)