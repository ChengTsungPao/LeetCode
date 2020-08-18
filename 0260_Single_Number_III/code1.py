class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        tmp = collections.Counter(nums)
        for i in tmp.keys():
            if(tmp[i]==1):
                ans.append(i)
                if(len(ans)==2):
                    return ans