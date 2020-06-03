class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from scipy.special import comb
        ans = []
        for i in range(rowIndex + 1):
            ans.append(comb(rowIndex, i, exact=True))
        return ans