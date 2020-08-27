class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        num, opr, temp = [], [], ""
        for ch in input:
            if ch.isdigit():
                temp += ch
            else:
                num.append(temp)
                opr.append(ch)
                temp = ""
        num.append(temp)
        
        ans = []
        def dfs(num, opr, index):
            if opr == []:
                ans.append(int(num[0]))
            for i in range(index, len(opr)):
                dfs(num[: i] + [str(eval(num[i] + opr[i] + num[i + 1]))] + num[i + 2:], opr[: i] + opr[i + 1 :], (i - 1) * (i != 0))
        dfs(num, opr, 0)

        return ans