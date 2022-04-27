class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        m = len(p)

        countp = collections.Counter(p)
        counts = collections.Counter(s[:m])
        
        ans = [0] if countp == counts else []
        
        for i in range(n - m):
            counts[s[i]] -= 1
            counts[s[i + m]] += 1
            if counts[s[i]] == 0:
                del counts[s[i]]

            if countp == counts:
                ans.append(i + 1)
                
        return ans