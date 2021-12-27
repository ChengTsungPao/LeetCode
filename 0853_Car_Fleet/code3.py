class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        count = 0
        nextPos, nextVel = float("inf"), 1
        
        for pos, vel in sorted(zip(position, speed), reverse = True):
            if (target - pos) / vel > (target - nextPos) / nextVel:
                nextPos, nextVel = pos, vel
                count += 1
        
        return count