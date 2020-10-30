class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        data = list(range(1, m + 1))
        for n in queries:
            tmp = data.index(n)
            ans.append(tmp)
            data.insert(0, data[tmp])
            del data[tmp + 1]
        return ans