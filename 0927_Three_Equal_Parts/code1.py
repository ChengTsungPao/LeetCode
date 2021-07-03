class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
        # 讓當前數值較小的那一邊的數值增大(增加一個bit)
        # 若兩邊數值一樣，選擇右邊，以下來探討原因
        # 情況1  ０和１相間 => 選左造成最小位的部分會不同 (這是我選右邊的最初動機)
        # 情況2  全部皆為０ => 選左邊新增1造成最小位的部分會不同，新增0之後右邊還是得新增(新增到最後必會碰到1)
        # 情況3  全部皆為１ => 選左邊新增0造成最小位的部分會不同，新增1之後右邊還是得新增
        # 結論   當左右相等時，選左邊存在風險，且就算選了沒事，右邊還是得新增bit，那不如選右邊

        length = len(arr)
        
        number = 0
        for i in range(length):
            number = 2 * number + arr[i]
        
        left, right = 0, len(arr) - 1
        leftValue, rightValue = arr[0], arr[-1]
        
        rightVar = 2 ** 1
        
        while left + 1 < right:

            if leftValue > rightValue:
                right -= 1
                rightValue += rightVar * arr[right]
                rightVar *= 2
                
            elif leftValue < rightValue:
                left += 1
                leftValue = 2 * leftValue + arr[left]
                
            else:
                midValue = (number - rightValue - (leftValue << (length - left - 1))) >> (length - right)
                if leftValue == midValue and midValue == rightValue:
                    return [left, right]
                right -= 1
                rightValue += rightVar * arr[right]
                rightVar *= 2
                
        return [-1, -1]