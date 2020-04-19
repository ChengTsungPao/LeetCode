class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(2**(len(nums))):
            ans.append([])
            tmp = bin(i)[2:].zfill(len(nums)) 
            for j in range(len(nums)):
                if(tmp[j]=="1"):
                    ans[i].append(nums[j])
        return ans