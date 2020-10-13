class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        data = collections.Counter(arr)
        for k in data.keys():
            if(data[k]==k):
                ans = max(ans, k)
        return ans