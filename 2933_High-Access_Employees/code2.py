class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        n = len(access_times)
        
        times = [collections.defaultdict(int) for _ in range(1441)]
        for e, t in access_times:
            h, m = int(t[:2]), int(t[2:])
            times[60 * h + m][e] += 1
        
        ans = set()
        count = collections.defaultdict(int)
        for t in range(1441):
            for e, c in times[t].items():
                count[e] += c
                
            for e, c in count.items():
                if count[e] >= 3:
                    ans.add(e)
                    
            if t >= 59:
                for e, c in times[t - 59].items():
                    count[e] -= c
                    if count[e] == 0:
                        del count[e]
                
        return list(ans)