class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        n = len(access_times)
        
        def getTime(t1, t2):
            h1, m1 = int(t1[:2]), int(t1[2:])
            h2, m2 = int(t2[:2]), int(t2[2:])
            return (h2 - h1) * 60 + (m2 - m1)
        
        access_times.sort()
        
        ans = set()
        for i in range(n - 2):
            e1, e2 = access_times[i][0], access_times[i + 2][0]
            t1, t2 = access_times[i][1], access_times[i + 2][1]
            if e1 == e2 and getTime(t1, t2) < 60:
                ans.add(e1)
                
        return list(ans)