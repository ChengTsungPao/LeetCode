class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        count = collections.defaultdict(int)
        
        for num in sorted(arr, key = lambda x: -abs(x)):
            if count[num * 2] > 0:
                count[num * 2] -= 1
            else:
                count[num] += 1

        return sum(count.values()) == 0