class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def longestRepeating(ch):
        
            n = len(s)
            que = collections.deque()

            ans = 1
            count = i = j = 0

            while j < n:
                if s[j] != ch:            
                    que.appendleft(j)

                    if count < k:
                        count += 1
                    else:
                        i = que.pop() + 1
                j += 1

                ans = max(ans, j - i)

            return ans      
        
        ans = 1
        for ch in set(s):
            ans = max(ans, longestRepeating(ch))
            
        return ans