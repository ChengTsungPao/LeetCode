class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        status = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums)):
                status[nums[i] + nums[j]] += [[i, j]]
        
        ans = set()
        check = set()
        for key in status.keys():
            if target - key in check or target == key * 2:
                for first in status[key]:
                    for second in status[target - key]:
                        if len(set(first + second)) == 4:
                            ans.add(tuple(sorted([nums[first[0]], nums[first[1]], nums[second[0]], nums[second[1]]])))
            else:
                check.add(key)
                
        return list(ans)