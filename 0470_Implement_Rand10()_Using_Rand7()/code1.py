# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        
        while True:
            status = collections.defaultdict(int)

            countMax = -float("inf")
            for start in range(10):
                result = (start + rand7() - 1) % 10
                status[result] += 1
                if status[result] > countMax:
                    countMax = status[result]
                    ans = [result]
                elif status[result] == countMax:
                    ans.append(result)
                    
            if len(ans) == 1:
                return ans[0] + 1
        