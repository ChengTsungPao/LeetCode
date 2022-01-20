class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def f(x):
            return a * x ** 2 + b * x + c
        
        if a == 0:
            ans = [f(num) for num in nums]
            return ans if b >= 0 else reversed(ans)
        
        symbol = a // abs(a)
        extreme = -b / (2 * a)
        index = bisect.bisect_left(nums, extreme)

        ans = []
        i, j = index - 1, index
        
        while i >= 0 and j < len(nums):
            num1, num2 = f(nums[i]), f(nums[j])
            if symbol * num1 < symbol * num2:
                ans.append(num1)
                i -= 1
            else:
                ans.append(num2)
                j += 1
            
        while i >= 0:
            ans.append(f(nums[i]))
            i -= 1

        while j < len(nums):
            ans.append(f(nums[j]))
            j += 1

        return ans if symbol > 0 else reversed(ans)