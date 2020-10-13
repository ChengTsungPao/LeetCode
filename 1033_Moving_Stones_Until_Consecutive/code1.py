class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        data = sorted([a, b, c])
        AnsMax = data[1] - data[0] - 1 + data[2] - data[1] - 1
        if data[1] - data[0] == 1 and data[2] - data[1] == 1:
            AnsMin = 0
        elif data[1] - data[0] > 2 and data[2] - data[1] > 2:
            AnsMin = 2
        else:
            AnsMin = 1
        return [AnsMin, AnsMax]