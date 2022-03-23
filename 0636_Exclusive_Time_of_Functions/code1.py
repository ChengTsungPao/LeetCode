class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        def get_ID_Time(log):
            str_ = log.split(":")
            return int(str_[0]), int(str_[-1]), str_[-2]
        
        ans = [0] * n
        stack = [(-1, -1, -1, -1)]
        total_time = 0
        
        for i in range(len(logs)):
            ID, time, state = get_ID_Time(logs[i])
            preID, preTime, preState, pre_total_time = stack[-1]
            
            if state == "end" and preState == "start" and preID == ID:
                curTime = (time - preTime + 1) - (total_time - pre_total_time)
                ans[ID] += curTime
                stack.pop()
                total_time += curTime
            else:
                stack.append((ID, time, state, total_time))
                
        return ans