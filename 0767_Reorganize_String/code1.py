class Solution:
    def reorganizeString(self, s: str) -> str:
        
        def findMaxExcept(ch):
            maxCh = ""
            count = 0
            for c in status.keys():
                if c != ch and status[c] > count:
                    maxCh = c
                    count = status[c]
            return maxCh
        
        
        ans = preCh = ""
        status = collections.Counter(s)
        
        while len(status) > 0:            
            ch = findMaxExcept(preCh)
            preCh = ch
            ans += ch
            
            status[ch] -= 1
            if status[ch] == 0:
                del status[ch]
                
            if len(status) == 1 and sum(status.values()) > 1:
                return ""
            
        return ans