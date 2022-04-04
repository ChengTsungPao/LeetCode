class LogSystem:

    def __init__(self):
        self.calendar = {}
        self.granularityKind = {
            "Year": 0,
            "Month": 1,
            "Day": 2,
            "Hour": 3,
            "Minute": 4,
            "Second": 5
        }
        
        
    def put(self, id: int, timestamp: str) -> None:
        root = self.calendar
        timestamp = timestamp.split(":")
        
        for i in range(len(timestamp) - 1):
            time = int(timestamp[i])
            if time not in root:
                root[time] = {}
            root = root[time]
        root[int(timestamp[-1])] = str(id)
        
        
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        root = self.calendar
        start = start.split(":")
        end = end.split(":")
        timeIndex = self.granularityKind[granularity]
            
        def getID(root, index, isStartEqualBefore, isEndEqualBefore):  
            if type(root) == str:
                return [int(root)]
            
            ans = []
            lower, upper = int(start[index]), int(end[index])
            
            # 優先權大的單位比較時，時間介於lower和upper之間
            if index > timeIndex or (isStartEqualBefore == isEndEqualBefore == False):
                for time in root.keys():
                    ans.extend(getID(root[time], index + 1, False, False))
                    
            # 優先權大的單位比較時，時間剛好等於lower的時間         
            elif isStartEqualBefore == True and isEndEqualBefore == False:
                for time in range(lower + 1, max(root.keys()) + 1):
                    if time in root:
                        ans.extend(getID(root[time], index + 1, False, False))
                if lower in root:
                    ans.extend(getID(root[lower], index + 1, True, False))
                    
            # 優先權大的單位比較時，時間剛好等於upper的時間        
            elif isStartEqualBefore == False and isEndEqualBefore == True:
                for time in range(min(root.keys()), upper):
                    if time in root:
                        ans.extend(getID(root[time], index + 1, False, False))
                if upper in root:
                    ans.extend(getID(root[upper], index + 1, False, True))   
                    
            # 優先權大的單位比較時，時間剛好等於lower也等於upper的時間
            else:
                for time in range(lower + 1, upper):
                    if time in root:
                        ans.extend(getID(root[time], index + 1, False, False)) 
                if lower == upper:      
                    if lower in root:
                        ans.extend(getID(root[lower], index + 1, True, True))
                else:
                    if lower in root:
                        ans.extend(getID(root[lower], index + 1, True, False))
                    if upper in root:
                        ans.extend(getID(root[upper], index + 1, False, True))

            return ans

        return getID(root, 0, True, True)
        

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)