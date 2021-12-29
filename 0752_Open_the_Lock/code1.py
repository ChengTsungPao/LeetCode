class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        que = collections.deque()
        found = set()
        deadends = set(deadends)
        
        if "0000" in deadends:
            return -1
        
        que.append([[0, 0, 0, 0], 0])
        found.add((0, 0, 0, 0))
        
        while que:
            action, step = que.pop()

            if "".join([str(element) for element in action]) == target:
                return step
            
            for i in range(4):
                
                action[i] = (action[i] + 1) % 10
                if tuple(action) not in found and "".join([str(element) for element in action]) not in deadends:
                    que.appendleft([action.copy(), step + 1])
                    found.add(tuple(action))
                action[i] = (action[i] - 1) % 10
                
                action[i] = (action[i] - 1) % 10
                if tuple(action) not in found and "".join([str(element) for element in action]) not in deadends:
                    que.appendleft([action.copy(), step + 1])
                    found.add(tuple(action))
                action[i] = (action[i] + 1) % 10
            
        return -1
