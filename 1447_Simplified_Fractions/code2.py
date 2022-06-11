class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        
        def isVaild(a, b):
            for i in range(2, a + 1):
                if a % i == 0 and b % i == 0:
                    return False
            return True
        
        ans = []
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                if isVaild(a, b):
                    ans.append("{}/{}".format(a, b))
                    
        return ans