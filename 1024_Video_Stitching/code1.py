class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clips.sort()
        clips.append([float("inf"), 0])

        ans = curTime = 0
        heap = []
        
        for start, end in clips: 
            # candidate放進heap中
            if start <= curTime:
                heapq.heappush(heap, -end)
                continue
            
            # 為空代表無candidate可選
            if not heap:
                return -1
            
            # 選下一個最佳的candidate   
            curTime = -heapq.heappop(heap)
            ans += 1
            if curTime >= time:
                return ans
            
            # 選完最佳的candidate後，下一個片段仍無法超過curTime
            if start > curTime:
                return -1
            
            #加入新的candidate
            heapq.heappush(heap, -end)

        if curTime >= time:
            return ans
        else:
            return -1