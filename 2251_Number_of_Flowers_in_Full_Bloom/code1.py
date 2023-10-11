class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        START = 0 # first
        GET = 1   # second
        END = 2   # third
        
        record = []
        for s, e in flowers:
            record.append((s, START))
            record.append((e, END))
            
        for t in set(people):
            record.append((t, GET))
        
        ans = {}
        count = 0
        for t, m in sorted(record):
            if m == START:
                count += 1
            elif m == GET:
                ans[t] = count
            else:
                count -= 1
                
        return [ans[t] for t in people]
                