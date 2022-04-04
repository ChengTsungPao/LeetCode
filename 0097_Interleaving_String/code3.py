class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        length1 = len(s1)
        length2 = len(s2)
        length3 = len(s3)
        
        if length1 + length2 != length3:
            return False
        
        memo = {}
        def recur(index1, index2, index3):
            
            if (index1, index2) not in memo:
            
                if index3 >= length3:
                    return True

                ans = False
                if index1 < length1 and s1[index1] == s3[index3]:
                    ans = ans or recur(index1 + 1, index2, index3 + 1)
                if index2 < length2 and s2[index2] == s3[index3]:
                    ans = ans or recur(index1, index2 + 1, index3 + 1)

                memo[index1, index2] = ans
                
            return memo[index1, index2]
        
        return recur(0, 0, 0)