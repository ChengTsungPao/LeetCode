class Solution:
    def grayCode(self, n: int) -> List[int]:
        if(n==0): return [0]
        ans = [0,1]
        for i in range(n-1):
            tmp = copy.copy(ans)
            tmp.reverse()
            for j in range(len(tmp)):
                tmp[j] += 2**(i+1)
            ans += tmp
        return ans