class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []
        data = collections.Counter(nums)        
        for key in data.keys():
            if(data[key] >= 2):
                ans.append(key)
            ans.append(key)
        nums[:] = ans[:]
        return len(nums)