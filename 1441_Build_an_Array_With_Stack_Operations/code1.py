class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        index = 0
        target = set(target)
        for i in range(1, n + 1):
            if index == len(target):
                break
            elif i in target:
                ans += ["Push"]
                index += 1
            else:
                ans += ["Push","Pop"]
        return ans