class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def partition(i, j):
            index = random.randrange(i, j + 1)
            nums[index], nums[j] = nums[j], nums[index]
            pivot = nums[j]
            
            index = i
            for k in range(i, j):
                if count[nums[k]] > count[pivot]:
                    nums[k], nums[index] = nums[index], nums[k]
                    index += 1
            nums[j], nums[index] = nums[index], nums[j]      

            return index
        
        
        def quickSelect(i, j):
            index = partition(i, j)
            
            if index == k - 1:
                return nums[:index + 1]
            
            if index > k - 1:
                return quickSelect(i, index - 1)
            else:
                return quickSelect(index + 1, j)
            

        count = collections.Counter(nums)
        nums = list(count.keys())
        
        return quickSelect(0, len(nums) - 1)