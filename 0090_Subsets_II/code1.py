class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = collections.defaultdict(list)
        for i in range(2**(len(nums))):
            temp = []
            binary = bin(i)[2:].zfill(len(nums)) 
            for j in range(len(nums)):
                if(binary[j]=="1"):
                    temp.append(nums[j])
            temp.sort()
            ans[str(temp)] = temp
        return list(ans.values())