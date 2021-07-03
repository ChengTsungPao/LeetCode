# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):   
        
        # 測試
        # total = 0
        # testing = 10000
        # for _ in range(testing):
        #     count = 0
        #     for _ in range(8):
        #         if rand7() <= 6:
        #             count += 1
        #     total += count == 8
        # print("Probability = {}%".format(total * 100 / testing))
        
        # 模擬 30% 約等於 (6 / 7) ** 8
        count = 0
        for _ in range(8):
            if rand7() <= 6:
                count += 1
                
        select_1_to_3 = count == 8
        
        if select_1_to_3:
            rand = rand7()
            while rand == 7:
                rand = rand7()
            return rand % 3 + 1
        else:
            return rand7() + 3
