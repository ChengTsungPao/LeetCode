class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        status = set()
        for i in range(1, n + 1):
            for j in range(1, i):
                if round(j / i, 8) not in status:
                    ans.append("{}/{}".format(j, i))
                    status.add(round(j / i, 8))
        return ans