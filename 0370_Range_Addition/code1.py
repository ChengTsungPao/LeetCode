class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        
        record = collections.defaultdict(int)
        for start, end, value in updates:
            record[start] += value
            record[end + 1] -= value
        record[length] = 0

        ans = []
        total = 0
        preTime = 0
        for time, value in sorted(record.items()):
            ans.extend([total] * (time - preTime))
            total += value
            preTime = time
            
        return ans