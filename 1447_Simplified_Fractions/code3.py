class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def getGCD(a, b):
            while b % a > 0:
                r = b % a
                a, b = r, a
            return a
        
        ans = []
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if getGCD(a, b) == 1:
                    ans.append("{}/{}".format(a, b))
                    
        return ans