class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        insertStart, insertEnd = newInterval
        
        isMapping = False
        isInsert = False
        preEnd = 0
        for start, end in intervals:
            if isInsert == False and isMapping == False and insertStart <= end:
                ans.append([min(start, insertStart)])
                isMapping = True
            if isInsert == False and isMapping and insertEnd < start:
                ans[-1].append(max(preEnd, insertEnd))
                isMapping = False
                isInsert = True
            
            preEnd = end
            if isMapping == False:
                ans.append([start, end])
                
        if isMapping:
            ans[-1].append(max(preEnd, insertEnd))  
        elif isInsert == False:
            ans.append([insertStart, insertEnd])
                
        return ans