class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        actionTable = {"L": 90, "R": -90}
        
        angle = 0
        count = collections.defaultdict(int)
        start_angle = set()
        
        while angle not in start_angle:
            
            start_angle.add(angle)
        
            for action in instructions:

                if action == "G":
                    count[angle] += 1
                else:
                    angle += actionTable[action]
                    
                if angle < 0:
                    angle += 360
                elif angle >= 360:
                    angle -= 360

        return count[0] - count[180] == 0 and count[90] - count[270] == 0
