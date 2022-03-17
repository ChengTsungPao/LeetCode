class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:
            if asteroid <= 0:
                # 當前隕石比較大破壞碰撞隕石
                while stack and stack[-1] > 0 and stack[-1] < -asteroid:
                    stack.pop()
                    
                # 相等隕石抵銷
                if stack and stack[-1] >= 0 and stack[-1] == -asteroid:
                    stack.pop()
                # 當前隕石比較小因此消失
                elif stack and stack[-1] >= 0 and stack[-1] > -asteroid:
                    continue
                # 當前隕石和碰撞到的隕石都是負的
                else:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
                
        return stack