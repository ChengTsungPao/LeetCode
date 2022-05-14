class Solution:
    def racecar(self, target: int) -> int:
        
        que = collections.deque([(0, 1)])
        visited = set()
        step = 0

        while que:
            
            newQue = collections.deque()
            while que:
                position, speed = que.pop()

                if position == target:
                    return step

                if (position, speed) in visited:
                    continue
                visited.add((position, speed))
                    
                newQue.appendleft((position + speed, speed * 2))
                newQue.appendleft((position, 1 if speed < 0 else -1))

            que = newQue
            step += 1
            
        return -1