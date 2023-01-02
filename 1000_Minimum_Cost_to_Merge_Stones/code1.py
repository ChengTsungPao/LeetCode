class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        '''
        method1 => k <= 3, Because k smaller time complexity will approach to O(nlogn)
        method2 => k >  3, Because k  bigger time complexity will approach to O(n - k)
        '''
        condition = k <= 3
        return self.method1(stones, k) if condition else self.method2(stones, k)
        
    def method1(self, stones, k):
        '''
        Divide and Conquer
        
        stones = [3,2,4,1], k = 2
        
         (3, 2, 4, 1)
         /          \
        (3, 2)   (4, 1)
        /    \   /    \
        3    2   4    1
        '''
        
        n = len(stones)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + stones[i - 1]
        
        @functools.lru_cache(None)
        def combination(i, k, n):
            if k < 0:
                return []
            elif i >= n:
                return [[n]] if k == 0 else []
            
            ans = copy.deepcopy(combination(i + 1, k, n))
            for ret in combination(i + 1, k - 1, n):
                ans.append([i] + ret)
                
            return ans

        @functools.lru_cache(None)
        def recur(i, j):
            num_of_stone = j - i + 1
            
            if num_of_stone == 1:
                return 0
            elif num_of_stone < k:
                return float("inf")

            shift = i
            ans = float("inf")
            for indices in combination(0, k - 1, num_of_stone - 1):
                cost = 0
                left = i
                for idx in indices:
                    right = idx + shift
                    cost += recur(left, right)
                    left = right + 1
                ans = min(ans, cost)
                
            return ans + (preSum[j + 1] - preSum[i])
        
        ans = recur(0, n - 1)
        return ans if ans != float("inf") else -1
    
    def method2(self, stones, k):
        '''
        Brute Force
        
        stones = [3,2,4,1], k = 2
        
           (3, 2, 4, 1)
           /          \         
          (5, 2, 4)   (3, 6, 1) ...
          /       \    /     \
        (7, 4) (5, 6)  ...... 
          |      |
         (11)   (11) 
        '''
    
        memo = {}
        def recur(stones):
            
            key = str(stones)
            num_of_stone = len(stones)
            
            if key not in memo:
                
                if num_of_stone == 1:
                    return 0
                elif num_of_stone < k:
                    return float("inf")

                ans = float("inf")
                cost = sum(stones[:k - 1])
                for i in range(num_of_stone - k + 1):
                    cost += stones[i + k - 1]
                    ans = min(ans, cost + recur(stones[:i] + [cost] + stones[i + k:]))
                    cost -= stones[i]
                    
                memo[key] = ans
                
            return memo[key]
                
        ans = recur(stones)
        return ans if ans != float("inf") else -1
  