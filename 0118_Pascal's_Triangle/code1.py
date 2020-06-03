class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] for _ in range(numRows)]
        for i in range(1, len(ans)):
            for j in range(i - 1):
                ans[i].append(ans[i - 1][j] + ans[i - 1][j + 1])
            ans[i].append(1)
        return ans