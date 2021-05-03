class Solution:
    def jump(self, nums: List[int]) -> int:
        
        que = collections.deque()
        que.appendleft((len(nums) - 1, 0))
        dp = set(list(range(len(nums))))
        dp.remove(len(nums) - 1)
        
        while que:
            index, step = que.pop()
            for i in list(dp):
                if index - i <= nums[i]:
                    if i == 0:
                        return step + 1
                    que.appendleft((i, step + 1))
                    dp.remove(i)
                    
        return 0