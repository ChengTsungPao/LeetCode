class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        
        n = len(stations)
        err = 10 ** -6
        
        def condition(distance):
            count = 0
            for i in range(n - 1):
                count += math.ceil((stations[i + 1] - stations[i]) / distance) - 1
            return count <= k
                
        left = right = 0
        for i in range(n - 1):
            right = max(right, stations[i + 1] - stations[i])
        right += err
            
        while right - left >= err:
            mid = left + (right - left) / 2
            if not condition(mid):
                left = mid + err
            else:
                right = mid
                
        return left