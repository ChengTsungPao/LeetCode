class Binary_Indexed_Tree():
    def __init__(self, n):
        self.tree = [0] * (n + 1)
        
    def lowbit(self, x):
        return x & -x
    
    def update(self, index, delta):
        while index < len(self.tree):
            self.tree[index] += delta
            index += self.lowbit(index)
            
    def quary(self, index):
        ans = 0
        while index > 0:
            ans += self.tree[index]
            index -= self.lowbit(index)
        return ans


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        # time complexity: O(nlogn)
        # space complexity: O(maxNum - minNum + 1)
        
        # 概念: 將Binary_Indexed_Tree的delta都設為1，來統計數量
        # 方法: 由右而左update，在quary的時候只會有該index右邊的數字參與，且只有較小的數字會被加起來 (非rank直接用數值大小)
        # 注意: 但須注意不能quary與自己大小相同的數字 (nums[i] - 1)
        
        # 比起另一個方法少了一個sort，速度會較快，但較耗空間，且無法處理有小數點的情況
        
        _max = -float("inf")
        _min = float("inf")
        for num in nums:
            _max = max(_max, num)
            _min = min(_min, num)
        
        BIT = Binary_Indexed_Tree(_max - _min + 1)
        
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i] - _min + 1
            ans.append(BIT.quary(num - 1))
            BIT.update(num, 1)
            
        return ans[::-1]