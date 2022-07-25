class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        def countCh(s):
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            return count
        
        cache = set()
        def recur(s1, s2):
            if s1 == s2:
                return True
            
            if (s1, s2) in cache:
                return False
            
            cache.add((s1, s2))
            
            n = len(s1)
            leftcount1 = [0] * 26
            leftcount2 = [0] * 26
            rightcount2 = [0] * 26
            
            for k in range(len(s1) - 1):
                ch1, ch2, ch3 = s1[k], s2[k], s2[~k]
                
                leftcount1[ord(ch1) - ord("a")] += 1
                leftcount2[ord(ch2) - ord("a")] += 1
                rightcount2[ord(ch3) - ord("a")] += 1
                
                if leftcount1 == leftcount2 and recur(s1[:k + 1], s2[:k + 1]) and recur(s1[k + 1:], s2[k + 1:]):
                    return True

                if leftcount1 == rightcount2 and recur(s1[k + 1:], s2[:n - k - 1]) and recur(s1[:k + 1], s2[n - k - 1:]):
                    return True       
                
            return False

        return countCh(s1) == countCh(s2) and recur(s1, s2)