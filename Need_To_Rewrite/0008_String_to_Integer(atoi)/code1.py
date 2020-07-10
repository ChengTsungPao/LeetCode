class Solution:
    def myAtoi(self, str: str) -> int:
        try:
            try:
                ans = int(str)
            except:
                flag = True
                for i in range(len(str)):
                    if(flag and (str[i] == "-" or str[i] == "+") and (i==0 or (i > 0 and str[i-1].isdigit() == False))):
                        flag = False
                    elif(str[i].isdigit() == False and (str[i].isspace() == False or (i > 0 and str[i-1].isdigit()))):
                        break
                ans = int(str[:i])
            if(ans > 2**31-1):
                return 2**31-1
            elif(ans < -2**31):
                return -2**31
            return ans
        except:
            return 0