class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Monotonic Queue
        #   1. 每個element都有自己在window內的有效時間，先進到window內的element會先被剔除，因此有Queue的概念
        #   2. 比較晚近到window的new element之有效時間相對較較長，因此在此問題中可以剔除較小的數字，因為在這段時間內該element不會比new element大
        
        ans = []
        que = collections.deque()

        for i in range(len(nums)):
            
            # 剔除超出window之element (que[0]在window內之時間最長)
            if que and i - que[0] >= k:
                que.popleft()
            
            # 剔除比新element小的element
            while que and nums[i] >= nums[que[-1]]:
                que.pop()
                
            # 加入新的element
            que.append(i)

            # 紀錄當前window內最大的element
            if i >= k - 1:
                ans.append(nums[que[0]])
            
        return ans