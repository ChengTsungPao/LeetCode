class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # 把走過的index利用nums紀錄成"#"，若第二次在走到"#"的位置代表重複
        
        index = nums[0]
        
        while True:
            num = nums[index]
            
            if num == "#":
                return index
            else:
                nums[index] = "#"
                index = num
