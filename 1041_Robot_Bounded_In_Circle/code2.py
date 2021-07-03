class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # 做完第一輪instructions後，不管角度是多少，做四次必回到角度為零 (最小公倍數)
        #     => 情況1:角度與一開始出發的角度相同
        #              => 若有回到原點，則為True
        #              => 若無回到原點，則為False
        #     => 情況2:角度與一開始出發的角度不同
        #              => 若有回到原點，則為True
        #              => 若無回到原點，則為True

        actionTable = {"L": 90, "R": -90}
        
        angle = 0
        count = collections.defaultdict(int)
        
        for action in instructions:

            if action == "G":
                count[angle] += 1
            else:
                angle += actionTable[action]

            if angle < 0:
                angle += 360
            elif angle >= 360:
                angle -= 360

        return angle != 0 or (count[0] - count[180] == 0 and count[90] - count[270] == 0)
