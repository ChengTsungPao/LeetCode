class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        '''
        nums = [..., 24,27, ...]
        1. palindromic number is in 24~27 => y = palindromic number
        2. close 24 palindromic number ? --> m, close 27 palindromic number ?
        '''
        n = len(nums)
        nums.sort()
        
        max_len = len(str(max(nums)))
        
        def findMid(sorted_nums):
            if n % 2 == 0:
                return sorted_nums[n // 2 - 1], sorted_nums[n // 2]
            else:
                return sorted_nums[n // 2], sorted_nums[n // 2]
        
        def recur(idx, num_str):
            if idx == (max_len // 2 + 1):
                return [num_str + num_str[:-1][::-1]]
            ans = []
            ans += [num_str + num_str[::-1]] if len(num_str) > 0 else []
            ans += [num_str[:-1:] + num_str[-1] + num_str[:-1:][::-1]] if len(num_str) > 0 else []
            for d in range(10):
                if idx == 0 and d == 0: continue
                for ret in recur(idx + 1, num_str + str(d)):
                    ans.append(ret)
            return ans
        
        palindromic_number = []
        for num in recur(0, ""):
            palindromic_number.append(int(num))
        palindromic_number.sort()
        
        mid1, mid2 = findMid(nums)
        idx1 = bisect.bisect_left(palindromic_number, mid1)
        idx2 = bisect.bisect_right(palindromic_number, mid2) - 1
        if idx2 >= idx1:
            y = palindromic_number[idx1]
            total_cost = sum([abs(num - y) for num in nums])
            return total_cost
        else:
            y1 = palindromic_number[idx1] if idx1 < len(palindromic_number) else palindromic_number[-1]
            total_cost1 = sum([abs(num - y1) for num in nums])
            y2 = palindromic_number[idx2]
            total_cost2 = sum([abs(num - y2) for num in nums])
            return min(total_cost1, total_cost2)